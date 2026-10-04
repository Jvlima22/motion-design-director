# Audio Analysis and Verification



\## Purpose



This reference defines how Motion Design Director analyzes audio when direct

perceptual listening is unavailable or cannot be established.



The goal is not to simulate hearing.



The goal is to extract measurable evidence from the audio signal and use that

evidence without overstating what has actually been verified.



\---



# Core Epistemic Rules



MEASUREMENT != LISTENING



GRID STABILITY != MUSICAL CORRECTNESS



RHYTHMIC PROXIMITY != MUSICAL INTENTION



SECONDS ARE THE SOURCE OF TRUTH



FRAMES ARE EDITING COORDINATES DERIVED FROM TIME



Never describe a measured property as something that was heard.



\---



# Evidence States



Every important audio claim should belong to one of these states.



\## MEASURED



Produced directly by metadata or signal analysis.



Examples:



\- duration

\- sample rate

\- channel count

\- integrated LUFS

\- loudness range

\- true peak

\- sample peak

\- RMS

\- silence regions

\- detected onset timestamps

\- estimated BPM

\- detected beat timestamps

\- fitted beat period

\- fitted grid offset

\- beat-grid residuals

\- rhythmic-grid distance

\- time-to-frame mapping



\## OBSERVED



Directly perceived by a human or model that actually has perceptual access to

the media.



Do not use OBSERVED merely because an audio file exists.



\## INFERRED



Interpretation supported by measured or observed evidence.



Examples:



\- the signal is consistent with a stable approximately 120 BPM pulse

\- an onset is consistent with a half-beat subdivision

\- several strong transients follow a repeated rhythmic pattern



Inference must remain distinguishable from measurement.



\## NOT\_VERIFIED



Claims that cannot be established by the available analysis.



Examples:



\- whether an SFX sounds premium

\- whether a sound feels powerful

\- whether a sound is pleasant

\- whether timbre matches the visual motion

\- whether the mix feels balanced

\- emotional appropriateness

\- musical taste

\- whether the detected pulse is the musically perceived beat

\- whether synchronization feels correct



\---



# Analysis Pipeline



Use:



tools/audio-analysis/analyze\_motion\_audio.py



The pipeline is:



MEDIA INPUT

\-> FFPROBE

\-> FFMPEG NORMALIZATION

\-> SIGNAL ANALYSIS

\-> RHYTHM ANALYSIS

\-> RHYTHMIC GRID ANALYSIS

\-> TIME / FRAME MAPPING

\-> STRUCTURED REPORT

\-> HUMAN OR MODEL INTERPRETATION



The rhythm worker is:



tools/audio-analysis/rhythm\_analyzer.py



Librosa rhythm analysis is intentionally isolated from the main analysis

process.



\---



# Media Normalization



Do not rely on Librosa to decode arbitrary video containers directly.



Normalize media through FFmpeg first.



Preferred analysis representation:



\- PCM WAV

\- 48 kHz

\- mono or controlled channel conversion for rhythm analysis



Architecture:



MP4 / MOV / WEBM / AUDIO

\-> FFMPEG

\-> PCM WAV

\-> RHYTHM ANALYSIS



This avoids container and codec decoding inconsistencies.



\---



# Loudness Analysis



The analysis may measure:



\- integrated LUFS

\- loudness range

\- true peak

\- sample peak

\- global RMS



These are signal measurements.



They do not establish subjective mix quality.



Correct:



"The integrated loudness measures -18.5 LUFS."



Incorrect:



"The mix sounds perfectly balanced at -18.5 LUFS."



\---



# Silence and Low-Level Regions



Silence detection identifies regions below the configured signal threshold for

the configured duration.



Treat these as measured low-level regions.



Do not automatically interpret them as:



\- intentional silence

\- dramatic pause

\- bad edit

\- missing audio



Those interpretations require context.



\---



# Onset Detection



An onset candidate is a detected increase in signal energy.



The onset detector can provide:



\- timestamp

\- frame

\- relative signal jump



The reported dB jump is detector-envelope change.



It is not equivalent to:



\- perceived loudness

\- impact

\- quality

\- importance

\- emotional strength



A large detector jump does not automatically mean that an event sounds strong.



\---



# Rhythm Analysis



Rhythm analysis may provide:



\- raw BPM estimate

\- detected beat timestamps

\- fitted BPM

\- beat period T

\- grid offset t0

\- beat count

\- residual statistics

\- grid stability classification



The fitted model is:



t\_i = t0 + i \* T



where:



\- t0 = fitted beat-grid offset

\- T = fitted beat period

\- i = beat index



Fitted BPM:



BPM = 60 / T



Keep time values as floating-point seconds.



Do not repeatedly accumulate rounded frame intervals.



\---



# Beat Grid Stability



Grid stability describes mathematical consistency between detected beat events

and the fitted linear beat grid.



Current classification:



HIGH



median absolute residual <= 10 ms

AND

mean absolute residual <= 15 ms



MEDIUM



median absolute residual <= 25 ms

AND

mean absolute residual <= 30 ms



LOW



anything above those thresholds



Also report when available:



\- maximum absolute residual

\- residual standard deviation



Maximum residual alone must not determine the classification.



Important:



GRID STABILITY != MUSICAL CORRECTNESS



A mathematically stable grid does not prove that the detector selected the

musically intended pulse.



\---



# Rhythmic Subdivision Analysis



Do not compare visual or audio events only to the nearest full beat.



An event may intentionally occur on a subdivision.



The current analysis tests these positions inside each fitted beat:



0.00 = BEAT



0.25 = QUARTER\_PHASE



0.50 = HALF\_BEAT



0.75 = THREE\_QUARTER\_PHASE



For every onset candidate, calculate the nearest mathematical rhythmic

position.



Report:



\- onset time

\- onset frame

\- rhythmic position

\- reference beat

\- rhythmic target time

\- signed delta

\- absolute grid distance

\- derived frame distance



Example:



18.490 s onset



nearest fitted rhythmic position:

HALF\_BEAT



target:

18.516 s



signed delta:

\-26.40 ms



rhythmic grid distance:

26.40 ms



This means:



MEASURED:

The detected onset is 26.40 ms from the fitted half-beat position.



Possible INFERENCE:

The event is consistent with a half-beat rhythmic placement.



It does NOT mean:



\- the event was intentionally placed on the offbeat

\- the event sounds synchronized

\- the music feels correct

\- the detected beat is perceptually correct



\---



# Why Nearest Beat Alone Is Insufficient



At approximately 120 BPM:



one beat \~= 500 ms



half beat \~= 250 ms



quarter phase \~= 125 ms



An onset approximately 230 ms after a detected beat could look like a large

timing error if compared only against that beat.



But it may be only approximately 20 ms from the mathematical half-beat.



Therefore:



DO NOT LABEL LARGE BEAT DELTAS AS SYNC ERRORS BEFORE CHECKING SUBDIVISIONS.



\---



# Time and Frame Mapping



Seconds are the canonical timing representation.



Use:



frame = round(seconds \* fps)



Frames are derived editing coordinates.



Never construct long rhythmic grids by repeatedly adding rounded frame

intervals.



Wrong:



next\_frame = previous\_frame + rounded\_frames\_per\_beat



Preferred:



beat\_time = t0 + n \* T



beat\_frame = round(beat\_time \* fps)



This prevents cumulative frame drift.



\---



# Audiovisual Review



When reviewing motion against audio:



1\. identify the visual event timestamp

2\. identify relevant measured audio events

3\. compare their timestamps

4\. compare against the fitted rhythmic grid when appropriate

5\. inspect beat subdivisions

6\. report delta in milliseconds

7\. optionally report derived frame delta

8\. distinguish measurement from inference

9\. do not claim perceptual quality without actual perceptual access



Example:



VISUAL EVENT



20.570 s

frame 617



AUDIO EVENT \[MEASURED]



20.740 s

frame 622



DELTA \[MEASURED]



+170 ms

approximately +5 frames at 30 fps



PERCEPTUAL JUDGMENT



NOT\_VERIFIED unless the audio was actually perceived.



\---



# Relationship to Other Audio References



Use this reference for:



WHAT CAN ACTUALLY BE MEASURED OR VERIFIED?



Use:



references/audio/sound-design.md



for:



WHY and WHERE should sound exist?



Use:



references/audio/beat-sync.md



for:



WHEN should motion relate to music?



Use:



references/audio/sfx-language.md



for:



WHAT TYPE OF SOUND should represent the event?



Use:



references/audio/audio-motion-sync.md



for:



HOW should sound and motion behave together?



Do not load every audio reference by default.



Use the smallest useful set.



\---



# Recommended Review Language



Prefer:



"\[MEASURED] Integrated loudness is -18.5 LUFS."



"\[MEASURED] The fitted rhythm is approximately 120 BPM."



"\[MEASURED] Beat-grid stability is HIGH under the current residual thresholds."



"\[MEASURED] This onset is 26 ms from the fitted half-beat."



"\[INFERRED] The event is consistent with a half-beat placement."



"\[NOT\_VERIFIED] Whether the synchronization feels correct cannot be established

from signal measurements alone."



Avoid:



"I can hear that the impact is weak."



"The SFX sounds premium."



"The beat definitely lands here."



"The music feels energetic."



"The sync is perfect."



unless actual perceptual access exists and supports that statement.



\---



# Failure Modes



\## Pretending measurement is hearing



Never do this.



\## Calling every onset a beat



Onsets and beats are different signal events.



\## Comparing only against full beats



Always consider relevant subdivisions before diagnosing timing error.



\## Treating detector strength as perceived impact



Detector-envelope change is not subjective impact.



\## Treating BPM as certain musical truth



BPM is an estimate produced by the current detector.



\## Treating HIGH grid stability as musical correctness



HIGH means mathematically stable under the current fitted model.



\## Rounding too early



Keep seconds as source-of-truth values until frame mapping is required.



\## Using Librosa directly on arbitrary video containers



Normalize through FFmpeg first.



\---



# Quality Gate



Before making an audio-related claim, ask:



1\. Was this actually perceived?

2\. Was this measured?

3\. Is this an inference?

4\. Is this not verifiable with current capabilities?



Then label or phrase the claim accordingly.



If uncertain:



prefer NOT\_VERIFIED over fabricated certainty.



\---



# Golden Rule



MEASURE WHAT CAN BE MEASURED.



INFER ONLY WHAT THE EVIDENCE SUPPORTS.



NEVER CALL MEASUREMENT LISTENING.

