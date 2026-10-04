"""Plan placement of short SFX hits on a list of visual events (banners, pops, clicks, notifications).

- start = event - onset_in_clip, rounded to the sequence frame (Premiere places audio on frame boundaries)
- variants rotate in a random order with no identical neighbours and no A-B-A-B / A-B-C-A-B-C patterns
- a small random gain jitter (default +/-0.8 dB) so repeats don't sound machine-made
- lanes: clips that would overlap go to the next free audio track (overwrite on the same track cuts the
  earlier clip's tail), using only the tracks you pass (pick tracks that are empty in that time range)

usage: plan_hits.py plan.json out.json
plan.json:
{
  "fps": 30,
  "events": [30.083, 30.2, ...],                   # timeline seconds (from contact sheets / burst_times.py)
  "variants": {"A": {"item": "<premiere node id>", "onset": 0.057, "len": 0.2667, "gain": -14.8}, ...},
       # onset/len are within the item as placed (after subclip trimming); gain = base clip volume in dB
  "tracks": [9, 16, 17, 18],
  "jitter_db": 0.8, "seed": 3,
  "order": "BDABADBDADBABD"                        # optional: fixed order instead of the random one
}
Then for each entry: overwrite_clip(item_id=item, start_seconds=start, audio_track_index=track) and
set_clip_volume on the new clip's nodeId (read them back with get_track_info).
"""
import json, random, sys


def score(s):
    if any(a == b for a, b in zip(s, s[1:])):
        return 1e9
    abab = sum(1 for i in range(len(s) - 3) if s[i] == s[i + 2] and s[i + 1] == s[i + 3])        # A-B-A-B
    abcabc = sum(1 for i in range(len(s) - 5) if s[i:i + 3] == s[i + 3:i + 6])                   # A-B-C-A-B-C
    p2 = sum(1 for i in range(len(s) - 2) if s[i] == s[i + 2])
    p3 = sum(1 for i in range(len(s) - 3) if s[i] == s[i + 3])
    cnt = [s.count(k) for k in set(s)]
    return abab * 3 + abcabc * 3 + (p2 + p3) * 0.3 + (max(cnt) - min(cnt))


def order_for(n, names, rnd):
    if len(names) == 1:
        return names[0] * n
    best = None
    for _ in range(30000):
        s = "".join(rnd.choice(names) for _ in range(n))
        sc = score(s)
        if best is None or sc < best[0]:
            best = (sc, s)
    return best[1]


def main():
    cfg = json.load(open(sys.argv[1]))
    fps = cfg.get("fps", 30)
    rnd = random.Random(cfg.get("seed", 1))
    V = cfg["variants"]
    names = "".join(sorted(V.keys()))
    seq = cfg.get("order") or order_for(len(cfg["events"]), names, rnd)
    lanes = {t: -1.0 for t in cfg["tracks"]}
    out = []
    for e, k in zip(cfg["events"], seq):
        v = V[k]
        st = round(round((e - v["onset"]) * fps) / fps, 4)
        free = [t for t in cfg["tracks"] if lanes[t] <= st + 1e-6]
        if not free:
            raise SystemExit(f"no free track at {st}: pass more tracks")
        tr = free[0]
        lanes[tr] = st + v["len"]
        g = round(v.get("gain", 0) + rnd.uniform(-cfg.get("jitter_db", 0.8), cfg.get("jitter_db", 0.8)), 1)
        out.append({"event": e, "variant": k, "item": v["item"], "track": tr, "start": st, "gain_db": g})
        print(f"{e:8.3f}  {k}  A{tr:<3d} start {st:8.4f}  {g:+.1f} dB")
    print("order:", seq)
    json.dump(out, open(sys.argv[2], "w"), indent=1)


if __name__ == "__main__":
    main()
