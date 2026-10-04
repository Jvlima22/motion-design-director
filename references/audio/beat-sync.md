\# BEAT SYNC



Beat sync is the coordination of musical structure, editorial rhythm, motion timing, and visual emphasis.



It does not mean making every animation happen on every beat.



Professional synchronization uses music as a temporal architecture.



The objective is to understand:



```text

WHERE THE MUSIC IS

WHERE THE PHRASE IS GOING

WHERE ENERGY CHANGES

WHICH VISUAL EVENTS DESERVE ACCENTS

AND WHICH EVENTS SHOULD FLOW BETWEEN THEM

```



A strong beat-synced sequence should feel musical without feeling mechanical.



\---



\# CORE PRINCIPLE



Do not ask:



```text

"Which animation happens on every beat?"

```



Ask:



```text

"What musical event should this visual event relate to?"

```



The relationship may be:



```text

BEFORE THE BEAT

ON THE BEAT

AFTER THE BEAT

BETWEEN BEATS

ACROSS MULTIPLE BEATS

ON A DOWNBEAT

ON A PHRASE CHANGE

ON A DROP

ON A MUSICAL ATTACK

```



Beat synchronization is about relationships, not repetition.



\---



\# BEAT SYNC DECISION CHAIN



Use:



```text

MUSIC

→ TEMPO

→ BEAT-1

→ BEAT GRID

→ BARS

→ PHRASES

→ MUSICAL STRUCTURE

→ ENERGY CURVE

→ SHOT RHYTHM

→ VISUAL EVENT

→ MUSICAL TARGET

→ FRAME

→ MOTION TIMING

→ SOUND RELATIONSHIP

→ RENDER VALIDATION

```



Never start by randomly placing cuts on waveform peaks.



Understand the musical structure first.



\---



\# 1. MUSIC FIRST



When music is central to the piece, choose or understand the track before finalizing detailed timing.



Music can influence:



```text

shot duration

edit rhythm

motion speed

transition timing

impact timing

camera movement

typography rhythm

energy curve

climax

CTA timing

```



However, product communication remains the priority.



Do not distort the product story merely to satisfy a beat grid.



\---



\# 2. BPM



BPM means:



```text

BEATS PER MINUTE

```



It describes tempo.



Example:



```text

120 BPM

```



means:



```text

120 beats / 60 seconds

= 2 beats per second

```



Therefore:



```text

1 beat = 0.5 seconds

```



\---



\# 3. SECONDS PER BEAT



Formula:



```text

secondsPerBeat = 60 / BPM

```



Example:



```text

BPM = 120



60 / 120

= 0.5 seconds per beat

```



At 128 BPM:



```text

60 / 128

= 0.46875 seconds

```



\---



\# 4. FRAMES PER BEAT



For frame-based production:



```text

framesPerBeat = fps × 60 / BPM

```



Example:



```text

FPS = 30

BPM = 120



framesPerBeat

= 30 × 60 / 120

= 15 frames

```



At 128 BPM and 30 fps:



```text

framesPerBeat

= 30 × 60 / 128

= 14.0625 frames

```



This fractional result matters.



Do not blindly round every beat interval to 14 frames.



That creates drift.



\---



\# 5. BEAT-1 OFFSET



The musical beat grid does not necessarily begin at:



```text

00:00

```



A track may contain:



```text

silence

pickup

intro

breath

ambient lead-in

pre-roll

partial measure

```



before the first meaningful downbeat.



Therefore identify:



```text

BEAT 1

```



or the chosen musical reference point.



\---



\# 6. SOURCE\_BEAT0



Represent the musical reference explicitly.



Concept:



```text

SOURCE\_BEAT0

```



This means:



```text

the source-time position of the beat chosen as grid origin

```



Example:



```text

SOURCE\_BEAT0 = 0.42 seconds

```



Then beat calculations are relative to that point.



Do not assume:



```text

SOURCE\_BEAT0 = 0

```



unless verified.



\---



\# 7. BUILDING THE BEAT GRID



Conceptually:



```text

beatTime(n)

=

SOURCE\_BEAT0

\+

n × secondsPerBeat

```



Then:



```text

beatFrame(n)

=

round(

&#x20; beatTime(n) × fps

)

```



This generates frame positions from cumulative musical time.



\---



\# 8. GRID VALIDATION



Never trust BPM alone.



Validate the grid against:



```text

kick

snare

clap

percussion

bass attack

chord attack

known downbeats

section changes

```



Check:



```text

early section

middle section

late section

```



If the grid begins correctly but drifts later:



```text

BPM may be inaccurate

tempo may vary

beat-1 may be wrong

rounding may be wrong

```



\---



\# 9. HALF-TIME / DOUBLE-TIME



Tempo detection can return musically equivalent interpretations.



Example:



```text

70 BPM

140 BPM

```



may describe the same pulse at different levels.



Do not automatically trust the detected number.



Ask:



```text

Which pulse matches the editorial rhythm?

```



A fast track may be edited at half-time.



A slower track may use subdivisions.



\---



\# 10. BARS



A beat is not the same as a bar.



In common 4/4 music:



```text

BAR

├── beat 1

├── beat 2

├── beat 3

└── beat 4

```



Beat 1 is often the strongest structural point.



Use bars to organize larger visual events.



\---



\# 11. PHRASES



Music often groups bars into phrases.



Common editorial structures may span:



```text

2 beats

4 beats

8 beats

multiple bars

```



Phrase boundaries are often stronger edit points than arbitrary individual beats.



Think:



```text

BEAT

→ local pulse



BAR

→ rhythmic unit



PHRASE

→ musical thought

```



Important scene changes often belong to phrase changes.



\---



\# 12. SUBDIVISIONS



A beat can be subdivided.



Common subdivisions:



```text

1/2 beat

1/4 beat

1/8-note relationships

```



Use subdivisions for:



```text

fast UI interactions

micro accents

typing

rapid assembly

short transitions

```



Do not use subdivisions merely to make the video busier.



\---



\# 13. EIGHTH-GRID



An eighth-note grid can provide higher temporal resolution than full beats.



Conceptually:



```text

eighthDuration

=

secondsPerBeat / 2

```



At 120 BPM:



```text

beat = 0.5 s

eighth = 0.25 s

```



Use this grid for smaller rhythmic events while preserving the larger beat hierarchy.



\---



\# 14. DOWNBEATS



Downbeats are strong structural anchors.



Good candidates for downbeats:



```text

hero reveal

major scene change

product landing

headline emphasis

metric reveal

logo arrival

drop

major transition

```



Do not waste every downbeat on minor decoration.



\---



\# 15. MUSICAL ATTACKS



Not every useful synchronization point belongs to a mathematical beat grid.



Music may contain meaningful attacks:



```text

kick

snare

bass

vocal onset

chord stab

percussion

FX hit

```



Sparse accents should often follow the actual attack rather than an abstract grid point.



\---



\# 16. ENERGY CURVE



Map the track's energy.



Possible sections:



```text

INTRO

BUILD

RISE

DROP

GROOVE

BREAKDOWN

CLIMAX

RELEASE

OUTRO

```



Then map visual intensity to musical intensity.



\---



\# 17. STRUCTURE TABLE



For important videos, build a structure table.



Example:



```text

TIME / FRAME

MUSIC SECTION

ENERGY

VISUAL SECTION

PRIMARY EVENT

```



Example:



```text

0–2s

Intro

Low

Brand setup

Logo atmosphere



2–6s

Build

Medium

Problem / context

UI fragments



6–12s

Groove

Medium-high

Feature demonstration

Product interactions



12–16s

Rise

High

Assembly

Increasing motion



16s

Drop

Peak

Hero reveal

Main product landing



16–24s

Groove

High

Proof

Features / metrics



24–28s

Release

Medium

Resolution

Product overview



28–30s

Outro

Controlled

CTA

Brand lock

```



The exact structure depends on the track.



\---



\# 18. DROPS



A drop is a high-value synchronization point.



Possible visual events:



```text

hero product reveal

UI explosion resolving

major transformation

full composition arrival

metric reveal

brand moment

```



Do not automatically place the biggest visual event on every musical drop.



Choose the drop that serves the narrative.



\---



\# 19. SHOT RHYTHM



Shot duration should relate to:



```text

information density

music

motion complexity

reading time

product comprehension

energy

```



Music is one input.



Not the only input.



\---



\# 20. MOTION PERSONALITY → RHYTHM



Art direction should influence rhythmic behavior.



\## PREMIUM



```text

longer phrases

fewer accents

controlled impacts

smooth continuity

```



\## ENERGETIC



```text

shorter shots

more subdivisions

stronger accents

faster transitions

```



\## TECHNICAL



```text

precise rhythm

structured events

controlled repetition

```



\## PLAYFUL



```text

syncopation

spring

unexpected accents

rhythmic variation

```



\## CINEMATIC



```text

build

anticipation

large phrase changes

strong contrast

```



Do not derive personality from BPM alone.



\---



\# 21. CUTTING ON PHRASES



A useful default:



```text

CUT MAJOR IDEAS

ON MUSICAL PHRASE BOUNDARIES

```



rather than:



```text

CUT EVERY BEAT

```



Possible hierarchy:



```text

PHRASE

→ scene



BAR

→ shot



BEAT

→ major motion event



SUBDIVISION

→ micro interaction

```



This is a model, not a rigid rule.



\---



\# 22. CUTTING ON ACTION



When possible:



```text

CUT DURING MEANINGFUL MOTION

```



Examples:



```text

camera whip

object crossing frame

card expanding

device rotating

cursor action

panel opening

```



Action can hide the seam.



Music determines timing context.



Motion determines the visual seam.



\---



\# 23. MATCH CUTS



Match cuts connect visual structures across shots.



Possible matches:



```text

shape

position

direction

scale

color

movement

UI geometry

```



A musical accent can strengthen the match.



But the match should work visually even without the sound.



\---



\# 24. IMPACT EVENTS



Define important events explicitly.



Examples:



```text

HERO\_LAND

FEATURE\_OPEN

METRIC\_HIT

LOGO\_LOCK

DROP\_REVEAL

```



Then map those events to musical targets.



Avoid scattered magic-frame numbers.



\---



\# 25. BEAT-SYNCED MOTION



Beat-synced motion should usually affect the element that logically responds.



Example:



```text

CARD

→ small scale pulse



NODE

→ activation



WORD

→ emphasis



DEVICE

→ landing



PARTICLE

→ burst

```



Avoid making the entire camera or full frame pump continuously with the beat unless that is the intended style.



\---



\# 26. STRUCTURAL MOTION VS IMPACT MOTION



Distinguish:



```text

STRUCTURAL MOTION

```



from:



```text

IMPACT EVENT

```



Structural motion:



```text

continuous camera

parallax

float

slow rotation

ambient motion

```



Impact event:



```text

landing

pulse

flash

burst

scale hit

```



A useful system is:



```text

STRUCTURAL MOTION

runs continuously



IMPACT EVENTS

activate at selected musical moments

```



This prevents robotic beat pumping.



\---



\# 27. SPEED RAMPS



Speed ramps can align a visual climax with a musical target.



Concept:



```text

accelerate

→ target moment

→ land on beat / downbeat / attack

→ decelerate

```



The important visual moment should meet the musical target.



Do not create a speed ramp merely because the music is energetic.



\---



\# 28. BUILD → CLIMAX → RELEASE



Motion can mirror musical structure.



Example:



```text

BUILD

increasing motion

shorter intervals

more layers



CLIMAX

hero event



RELEASE

slower motion

fewer elements

longer hold

```



This creates audiovisual structure.



\---



\# 29. PACING CURVES



A video does not need constant pacing.



Possible curve:



```text

SLOW

→ MEDIUM

→ FAST

→ PEAK

→ RELEASE

```



Or:



```text

FAST HOOK

→ BREATH

→ BUILD

→ HERO

→ CTA

```



Use contrast.



Constant speed becomes monotonous.



\---



\# 30. CUMULATIVE ROUNDING



When frames-per-beat is fractional, calculate each beat from cumulative musical time.



Correct:



```text

beatFrame(n)

=

round(

&#x20; SOURCE\_BEAT0\_FRAME

&#x20; +

&#x20; n × framesPerBeat

)

```



Do not do:



```text

roundedInterval = round(framesPerBeat)



beatFrame(n)

=

SOURCE\_BEAT0\_FRAME

\+

n × roundedInterval

```



The second approach accumulates timing error.



\---



\# 31. DRIFT PREVENTION



Example:



```text

framesPerBeat = 14.0625

```



If every interval becomes:



```text

14 frames

```



then after many beats the grid drifts.



Instead the generated frame intervals naturally vary:



```text

14

14

14

14

15

14

...

```



according to cumulative rounding.



The long-term grid remains aligned.



\---



\# 32. REMOTION IMPLEMENTATION



Use explicit musical timing helpers.



Concept:



```tsx

const secondsPerBeat = 60 / bpm;

const framesPerBeat = fps \* secondsPerBeat;



const beatFrame = (beat: number) =>

&#x20; Math.round(

&#x20;   sourceBeat0Frame +

&#x20;   beat \* framesPerBeat

&#x20; );

```



Then:



```tsx

const HERO\_LAND = beatFrame(16);

```



Prefer:



```text

semantic event names

```



over unexplained numbers.



\---



\# BEAT PROGRESS



For continuous beat-aware motion:



```text

beatT

```



can represent position within the beat.



Concept:



```tsx

const beatT =

&#x20; ((frame - sourceBeat0Frame) / framesPerBeat) % 1;

```



Use carefully.



Continuous full-frame beat pulsing often becomes repetitive.



\---



\# EVENT SET



A stronger pattern:



```tsx

const IMPACT\_BEATS = \[4, 8, 16, 24];

```



or semantic mapping:



```tsx

const EVENTS = {

&#x20; heroReveal: beatFrame(16),

&#x20; featureHit: beatFrame(24),

&#x20; logoLock: beatFrame(32),

};

```



This keeps synchronization intentional.



\---



\# 33. AFTER EFFECTS IMPLEMENTATION



In After Effects:



```text

identify BPM

identify beat-1

create markers

mark phrase boundaries

mark important attacks

map major visual events

animate between markers

```



Do not add markers for every beat unless needed.



Too many markers can obscure the important structure.



\---



\# 34. DAVINCI / NLE IMPLEMENTATION



In an editing timeline:



```text

mark beat-1

mark phrase changes

mark drops

mark important attacks

mark hero moments

```



Then edit around:



```text

story

action

music

```



together.



Waveform peaks can help locate events but should not replace musical interpretation.



\---



\# 35. SOURCE TIMING VS OUTPUT OFFSET



Keep two concepts separate:



```text

SOURCE MUSICAL TIMING

```



and:



```text

FINAL OUTPUT COMPENSATION

```



Example:



```text

SOURCE\_BEAT0

```



belongs to music analysis.



An encoding shift belongs to delivery correction.



Do not alter the musical grid to compensate for an output-container offset.



\---



\# 36. RENDER VALIDATION



A timeline can be mathematically correct while the exported file feels wrong.



Validate:



```text

early beat

middle beat

late beat

major drop

hero impact

logo

```



Check both:



```text

visual sync

audio sync

```



If all events share the same final-file offset:



```text

investigate output compensation

```



If drift increases over time:



```text

investigate BPM / grid / rounding

```



These are different problems.



\---



\# 37. VARIABLE-TEMPO MUSIC



Not every track has constant BPM.



Possible causes:



```text

live performance

tempo automation

rubato

intentional tempo change

imperfect recording

```



Do not force one constant grid onto variable-tempo material.



Use:



```text

manual markers

section-specific grids

detected attacks

phrase landmarks

```



when required.



\---



\# 38. PRODUCT / SAAS RHYTHM



Product videos must balance:



```text

MUSIC

\+

COMPREHENSION

```



Do not cut away from a feature before the viewer understands it merely because the next beat arrived.



Use musical structure to support product understanding.



\---



\# 39. UI RHYTHM



UI interactions may happen:



```text

on beat

between beats

as a short rhythmic series

across a phrase

```



Example:



```text

beat

→ card enters



between beats

→ cursor travels



next beat

→ click



next phrase

→ result

```



This often feels more natural than:



```text

beat = card

beat = cursor

beat = click

beat = result

```



with identical spacing.



\---



\# 40. TYPOGRAPHY + BEAT



Typography can relate to music through:



```text

headline entrance

word emphasis

line reveal

highlight

hero word

exit

```



Do not land every word on consecutive beats by default.



Use semantic hierarchy.



Example:



```text

phrase begins

→ headline enters



important word

→ musical accent



hero word

→ downbeat



supporting copy

→ settles between accents

```



Use:



```text

references/typography.md

```



for typography hierarchy.



\---



\# 41. CAMERA + BEAT



Camera movement can span multiple beats.



Example:



```text

BEAT 1

push begins



BEATS 1–4

continuous acceleration



BEAT 5

hero landing

```



This is often more cinematic than:



```text

camera pulse

camera pulse

camera pulse

camera pulse

```



Camera should follow shot purpose first.



\---



\# 42. TRANSITIONS + BEAT



Transitions can target:



```text

beat

downbeat

phrase boundary

musical attack

drop

```



But a transition may begin before the target.



Example:



```text

BEAT - 0.5

transition begins



BEAT

transition peak / cut



BEAT + tail

settle

```



The target is often the peak, not the animation start.



\---



\# 43. SOUND DESIGN + BEAT



Music provides temporal structure.



Sound design provides event reinforcement.



Possible relationship:



```text

MUSICAL BUILD

\+

RISER



DOWNBEAT

\+

VISUAL LANDING

\+

IMPACT



AFTERBEAT

\+

SPARKLE / TAIL

```



Do not automatically stack SFX on every musical transient.



Use:



```text

references/audio/sound-design.md

```



for sonic hierarchy.



\---



\# 44. ANTI-PATTERNS



Avoid:



```text

CUTTING ON EVERY BEAT



DISSOLVE ON EVERY BEAT



PULSING THE ENTIRE FRAME CONTINUOUSLY



ASSUMING BEAT 1 = TIME ZERO



ROUNDING FRAMES-PER-BEAT ONCE



IGNORING LONG-TERM DRIFT



USING BPM WITHOUT VALIDATING THE TRACK



CONFUSING HALF-TIME AND DOUBLE-TIME



TREATING EVERY WAVEFORM PEAK AS A BEAT



IGNORING PHRASES



IGNORING READING TIME



CUTTING UI BEFORE IT CAN BE UNDERSTOOD



USING SPEED RAMPS WITHOUT A VISUAL PURPOSE



MAKING EVERY CAMERA MOVE REACT TO MUSIC



PUTTING EVERY WORD ON A BEAT



USING THE DROP FOR A MINOR EVENT



CORRECTING OUTPUT OFFSET BY CORRUPTING SOURCE\_BEAT0



TRUSTING TIMELINE SYNC WITHOUT CHECKING THE RENDER

```



\---



\# 45. BEAT-SYNC AUDIT



Before approving:



\## MUSIC



```text

Is BPM correct?

Is beat-1 correct?

Is half-time/double-time interpretation correct?

```



\## GRID



```text

Does the grid align early?

Does it align in the middle?

Does it align late?

```



\## STRUCTURE



```text

Where are the bars?

Where are the phrases?

Where are the energy changes?

Where is the drop?

```



\## EDIT



```text

Are cuts serving both story and music?

Are we cutting too frequently?

```



\## MOTION



```text

Which motion is structural?

Which motion is an impact event?

```



\## PRODUCT



```text

Can the viewer understand the UI?

Are we sacrificing comprehension for rhythm?

```



\## TYPOGRAPHY



```text

Does text have enough reading time?

Are only meaningful words receiving accents?

```



\## CAMERA



```text

Does camera movement span musical structure naturally?

```



\## DRIFT



```text

Are fractional beat intervals handled cumulatively?

```



\## OUTPUT



```text

Was the final exported file checked?

```



\---



\# 46. PRODUCT TRUTH



Beat synchronization must not distort product truth.



Do not:



```text

fake interactions

accelerate real workflows until they become misleading

invent success states

hide important product steps solely to hit beats

```



Music serves the product story.



The product story does not become false to serve the music.



\---



\# 47. BEAT-SYNC OUTPUT CONTRACT



For important rhythmic sequences define:



```text

TRACK:

BPM:

FPS:

SOURCE\_BEAT0:

SECONDS\_PER\_BEAT:

FRAMES\_PER\_BEAT:

TIME SIGNATURE:

GRID LEVEL:

PHRASE LENGTH:

ENERGY SECTION:

SHOT:

VISUAL EVENT:

MUSICAL TARGET:

TARGET FRAME:

EVENT TYPE:

MOTION START:

MOTION PEAK:

MOTION END:

CUT:

SFX RELATIONSHIP:

OUTPUT OFFSET:

VALIDATION:

```



Example:



```text

TRACK:

Product Launch Main



BPM:

128



FPS:

30



SOURCE\_BEAT0:

verified first downbeat



FRAMES\_PER\_BEAT:

14.0625



ENERGY SECTION:

Drop



VISUAL EVENT:

Hero dashboard lands



MUSICAL TARGET:

Downbeat



EVENT TYPE:

Impact



MOTION START:

before target



MOTION PEAK:

target frame



MOTION END:

after target



SFX RELATIONSHIP:

impact reinforces landing



VALIDATION:

early/middle/late grid + final render

```



\---



\# 48. ROUTING



Use this module for:



```text

BPM

beat grids

downbeats

bars

phrases

music structure

rhythmic cuts

speed ramps

drops

musical accents

motion rhythm

frame conversion

drift

```



For sonic hierarchy:



```text

references/audio/sound-design.md

```



For detailed SFX selection:



```text

references/audio/sfx-language.md

```



For precise audiovisual event synchronization:



```text

references/audio/audio-motion-sync.md

```



For typography:



```text

references/typography.md

```



For motion principles:



```text

references/animation-principles.md

```



For transitions:



```text

references/transitions.md

```



For camera:



```text

references/creative/camera-language.md

```



\---



\# 49. FINAL BEAT-SYNC DECISION LOOP



Before implementing:



```text

WHAT IS THE PRODUCT MESSAGE?

&#x20;       ↓

WHAT ROLE DOES MUSIC HAVE?

&#x20;       ↓

WHAT IS THE BPM?

&#x20;       ↓

WHERE IS THE TRUE BEAT-1?

&#x20;       ↓

IS THE TEMPO CONSTANT?

&#x20;       ↓

WHAT IS THE BEAT GRID?

&#x20;       ↓

WHERE ARE THE BARS?

&#x20;       ↓

WHERE ARE THE PHRASES?

&#x20;       ↓

WHERE DOES ENERGY CHANGE?

&#x20;       ↓

WHAT ARE THE IMPORTANT VISUAL EVENTS?

&#x20;       ↓

WHICH EVENTS DESERVE MUSICAL ACCENTS?

&#x20;       ↓

SHOULD EACH EVENT LEAD, LAND, OR FLOW BETWEEN BEATS?

&#x20;       ↓

WHAT MOTION IS STRUCTURAL?

&#x20;       ↓

WHAT MOTION IS AN IMPACT?

&#x20;       ↓

DOES THE VIEWER HAVE ENOUGH TIME TO UNDERSTAND THE PRODUCT?

&#x20;       ↓

ARE FRACTIONAL FRAME INTERVALS HANDLED WITHOUT DRIFT?

&#x20;       ↓

IS SOURCE TIMING SEPARATE FROM OUTPUT COMPENSATION?

&#x20;       ↓

HAS THE FINAL RENDER BEEN VERIFIED?

```



\---



\# GOLDEN RULE



Synchronize meaning, not everything.



The beat grid is a map, not a prison.



Use beats for accents.



Use bars for rhythm.



Use phrases for structure.



Use musical energy for pacing.



Let motion flow between musical events.



Let important events own the strongest accents.



Protect product comprehension.



Prevent mathematical drift.



And always validate synchronization in the final render.

