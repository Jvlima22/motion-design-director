\# AUDIO MOTION SYNC



Audio-motion sync defines how sound and visual motion become one perceptual event.



This module is not primarily about:



```text

WHICH SOUND TO CHOOSE

```



That belongs to:



```text

references/audio/sfx-language.md

```



It is not primarily about:



```text

WHERE THE MUSIC BEAT IS

```



That belongs to:



```text

references/audio/beat-sync.md

```



It is not primarily about:



```text

OVERALL SOUND HIERARCHY

```



That belongs to:



```text

references/audio/sound-design.md

```



This module answers:



```text

WHERE SHOULD THE SOUND BEGIN?



WHERE SHOULD ITS IMPORTANT TRANSIENT LAND?



WHAT VISUAL MOMENT SHOULD IT REINFORCE?



SHOULD SOUND LEAD, LAND WITH, OR TRAIL THE VISUAL?



HOW SHOULD SOUND FOLLOW MOTION VELOCITY?



HOW DO WE VERIFY THAT THE FINAL RENDER STILL FEELS SYNCHRONIZED?

```



\---



\# CORE PRINCIPLE



Do not synchronize:



```text

AUDIO FILE START

```



to:



```text

ANIMATION START

```



blindly.



Synchronize:



```text

PERCEPTUAL AUDIO EVENT

```



to:



```text

PERCEPTUAL VISUAL EVENT

```



The important moment may be:



```text

motion start

maximum acceleration

maximum velocity

contact

landing

state change

reveal

completion

release

```



The sound file may contain:



```text

pre-roll

anticipation

attack

body

peak

tail

reverb

```



Therefore:



```text

FILE START

≠

SOUND EVENT

```



and:



```text

ANIMATION START

≠

VISUAL EVENT

```



\---



\# AUDIO-MOTION SYNC DECISION CHAIN



```text

VISUAL EVENT

&#x20;       ↓

EVENT PURPOSE

&#x20;       ↓

MOTION PHASE

&#x20;       ↓

PERCEPTUAL VISUAL TARGET

&#x20;       ↓

SOUND FUNCTION

&#x20;       ↓

SOUND ANATOMY

&#x20;       ↓

PERCEPTUAL AUDIO TARGET

&#x20;       ↓

LEAD / LAND / TRAIL

&#x20;       ↓

FRAME ALIGNMENT

&#x20;       ↓

MUSIC RELATIONSHIP

&#x20;       ↓

MIX CONTEXT

&#x20;       ↓

FINAL RENDER

&#x20;       ↓

PERCEPTUAL VALIDATION

```



\---



\# 1. SYNCHRONIZE EVENTS, NOT CLIPS



The basic unit is not:



```text

audio clip

```



The basic unit is:



```text

audiovisual event

```



Example:



```text

CARD LANDS

\+

IMPACT PEAK

```



Together they form:



```text

CARD\_LAND\_EVENT

```



Think in events first.



Assets come later.



\---



\# 2. VISUAL EVENT ANATOMY



A visual motion can contain:



```text

ANTICIPATION

START

ACCELERATION

MAX VELOCITY

DECELERATION

CONTACT

SETTLE

HOLD

```



Different sounds belong to different phases.



\---



\# 3. AUDIO EVENT ANATOMY



A sound can contain:



```text

PRE-ROLL

ONSET

ATTACK

PEAK

BODY

DECAY

TAIL

```



Do not assume the first non-silent sample is the perceptually important moment.



\---



\# 4. PERCEPTUAL TARGET



Define the exact visual target.



Examples:



```text

BUTTON PRESSED STATE

CARD CONTACT

DEVICE LANDING

LOGO LOCK

TRANSITION MIDPOINT

MAXIMUM SWIPE VELOCITY

DATA ARRIVAL

SUCCESS STATE

```



Then identify the audio feature that should correspond to it.



\---



\# 5. ONSET



Onset is when a sound becomes perceptually present.



Useful for:



```text

movement begins

interaction begins

anticipation begins

mechanism activates

```



The onset may occur before the main transient.



\---



\# 6. ATTACK



Attack describes how quickly sound reaches meaningful energy.



Sharp visual events usually benefit from:



```text

fast attack

```



Soft visual events may benefit from:



```text

slower attack

```



Match sonic attack to visual acceleration.



\---



\# 7. PEAK



The audio peak or dominant transient is often more important than clip start.



For an impact:



```text

IMPACT PEAK

→ VISUAL CONTACT

```



may matter more than:



```text

IMPACT FILE START

→ VISUAL CONTACT

```



because the sample may contain pre-impact material.



\---



\# 8. BODY



The sound body communicates:



```text

weight

mass

duration

presence

```



It often belongs around the visual object's:



```text

contact

settle

hold

```



phase.



\---



\# 9. TAIL



The tail communicates aftermath.



Examples:



```text

reverb

air

sparkle

ring

decay

texture

```



The visual event may already be complete while the tail continues.



That is normal.



\---



\# 10. LEAD / LAND / TRAIL



Three fundamental relationships:



```text

LEAD

LAND

TRAIL

```



\---



\# 11. LEAD



Sound begins or becomes meaningful before the visual target.



Useful for:



```text

anticipation

riser

approaching motion

incoming object

transition preparation

```



Concept:



```text

AUDIO

\----->



&#x20;     VISUAL TARGET

&#x20;         |

```



Sound prepares the eye.



\---



\# 12. LAND



The important sonic transient and visual event coincide.



Useful for:



```text

click

impact

snap

landing

confirmation

cut

logo lock

```



Concept:



```text

AUDIO PEAK

&#x20;    |

&#x20;    V

\-----X-----



VISUAL EVENT

&#x20;    |

&#x20;    V

\-----X-----

```



This creates strong perceived synchronization.



\---



\# 13. TRAIL



Sound follows the primary visual event.



Useful for:



```text

reverb

sparkle

resonance

echo

release

after-effect

```



Concept:



```text

VISUAL EVENT

&#x20;    X



AUDIO

&#x20;    X-------->

```



The tail extends perception after the visual action.



\---



\# 14. LEAD + LAND + TRAIL



Many professional events contain all three.



Example:



```text

RISER

→ IMPACT

→ SPARKLE

```



maps to:



```text

LEAD

→ LAND

→ TRAIL

```



This creates a complete audiovisual phrase.



\---



\# 15. DO NOT UNIVERSALIZE FRAME OFFSETS



There is no universal rule such as:



```text

SFX MUST ALWAYS BE 2 FRAMES EARLY

```



or:



```text

AUDIO MUST ALWAYS PRECEDE VIDEO

```



Correct timing depends on:



```text

sound transient

visual event

motion speed

sample pre-roll

fps

music

editorial intention

perception

```



Small offsets may be useful.



They are techniques, not laws.



\---



\# 16. PERCEPTUAL SYNC



Mathematical equality does not always guarantee perceived equality.



Two events can occur on the same timestamp but feel unsynchronized because:



```text

sound attack is slow

visual contact is ambiguous

sample transient occurs later

motion blur hides contact

reverb masks attack

music masks the transient

```



Judge the perceptual event.



\---



\# 17. FRAME-LEVEL THINKING



At 30 fps:



```text

1 frame ≈ 33.33 ms

```



At 60 fps:



```text

1 frame ≈ 16.67 ms

```



A shift of a few frames can materially change perceived synchronization.



Therefore inspect critical events frame by frame when necessary.



\---



\# 18. AUDIO TIME VS VIDEO FRAME



Video is commonly reasoned about in frames.



Audio exists continuously in time.



Convert deliberately:



```text

timeSeconds = frame / fps

```



and:



```text

frame = round(timeSeconds × fps)

```



Do not confuse audio sample precision with video-frame precision.



\---



\# 19. MOTION START



The beginning of motion does not always need a strong sound.



For example:



```text

CARD STARTS MOVING

→ subtle onset



CARD REACHES TARGET

→ impact

```



This creates direction and payoff.



\---



\# 20. ACCELERATION



Increasing acceleration can be reinforced with:



```text

rising pitch

increasing noise

riser

increasing intensity

```



when appropriate.



Do not mechanically map every acceleration curve to pitch.



Use perceptual correspondence.



\---



\# 21. VELOCITY



Fast movement often supports:



```text

whoosh

air

pass-by

sweep

```



The sound's energy should often relate to perceived velocity.



Slow motion should not automatically receive a fast sharp whoosh.



\---



\# 22. MAXIMUM VELOCITY



For a whoosh, the strongest sonic region may align near:



```text

maximum perceived velocity

```



rather than:



```text

motion start

```



This makes movement feel physically connected.



\---



\# 23. DECELERATION



As movement slows:



```text

sound intensity may decrease

pitch may settle

noise may soften

```



Then a landing event may occur separately.



Think:



```text

MOVEMENT SOUND

→ DECELERATION

→ IMPACT

```



\---



\# 24. CONTACT



Contact is one of the strongest synchronization points.



Examples:



```text

card lands

device reaches surface

panel locks

object hits boundary

```



Usually align the relevant transient with perceived contact.



\---



\# 25. SETTLE



Spring or overshoot motion may continue after contact.



Possible structure:



```text

CONTACT

→ impact



OVERSHOOT

→ subtle secondary detail



SETTLE

→ tail / silence

```



Do not add a full impact for every spring oscillation.



\---



\# 26. CLICK EVENTS



For a button:



```text

CURSOR APPROACH

→ usually silent



PRESS

→ click



STATE CHANGE

→ optional confirmation

```



Sound should correspond to interaction semantics.



\---



\# 27. PRESS VS RELEASE



A UI sound may correspond to:



```text

PRESS

```



or:



```text

RELEASE

```



depending on interaction design.



Be consistent within the product.



\---



\# 28. CURSOR MOTION



Cursor travel generally does not need continuous audio.



Use sound for:



```text

meaningful hover

press

drag start

drop

important selection

```



not every movement.



\---



\# 29. DRAG AND DROP



Possible audiovisual structure:



```text

PICKUP

→ small activation



DRAG

→ subtle movement if needed



DROP

→ confirmation / landing

```



The strongest cue normally belongs to the semantic event.



\---



\# 30. UI REVEAL



Possible structure:



```text

anticipation

→ movement onset



panel enters

→ movement sound



panel reaches final position

→ subtle landing



content activates

→ optional detail

```



Do not stack every layer loudly.



\---



\# 31. UI EXPLOSION



When UI separates into multiple pieces:



```text

GLOBAL MOVEMENT

→ broad movement layer



IMPORTANT OBJECTS

→ selective accents



FINAL COMPOSITION

→ hero landing

```



Avoid one loud SFX per fragment.



\---



\# 32. FLOATING UI



Ambient floating motion generally requires restraint.



Possible sound:



```text

soft ambience

air texture

occasional movement cue

```



Constant synchronization destroys the feeling of effortless motion.



\---



\# 33. DEVICE MOTION



For device movement:



```text

ROTATION

→ spatial movement



APPROACH

→ increasing movement energy



LAND

→ controlled impact



SCREEN ACTIVATION

→ digital detail

```



Separate physical motion from interface activation.



\---



\# 34. CAMERA MOVEMENT



Camera motion may receive sound when it is:



```text

fast

intentional

transition-like

dramatic

```



Examples:



```text

whip

push

pull

orbit acceleration

pass-through

```



Do not sound every slow camera drift.



\---



\# 35. CAMERA PUSH



A push may use:



```text

soft rising air

subtle spatial movement

```



with the strongest moment near:



```text

arrival

feature reveal

```



not necessarily at camera start.



\---



\# 36. CAMERA WHIP



A whip often maps:



```text

movement onset

→ whoosh begins



maximum velocity

→ whoosh peak



cut / arrival

→ impact or transition resolution

```



This creates one coherent event.



\---



\# 37. ZOOM



Zoom sound should reflect perceived spatial acceleration.



Possible:



```text

suction

whoosh

tonal movement

air

```



Avoid generic whooshes that contradict direction or scale.



\---



\# 38. TRANSITIONS



A transition has:



```text

ENTRY

MIDPOINT

EXIT

```



The main sonic target may be:



```text

transition peak

cut point

new-scene arrival

```



Do not automatically align the sound peak to transition start.



\---



\# 39. WIPE



For a directional wipe:



```text

visual edge movement

↔ directional sound movement

```



The audio should follow the perceived travel.



\---



\# 40. SCALE TRANSITION



For:



```text

small object

→ full scene

```



sound can grow in:



```text

width

energy

frequency body

```



to support the scale change.



\---



\# 41. MATCH CUT



A match cut may use one sonic event bridging two visual states.



Example:



```text

SHOT A MOTION

→ sonic movement



CUT

→ transient



SHOT B CONTINUES DIRECTION

→ tail

```



Sound can hide or strengthen the seam.



\---



\# 42. SPEED RAMPS



A speed ramp may map:



```text

slow

→ build



acceleration

→ rising sound



target frame

→ impact / beat



release

→ tail

```



The important visual frame should be defined before designing the sound.



\---



\# 43. RAMP TARGET



Ask:



```text

WHAT EXACT FRAME IS THE RAMP TRYING TO EMPHASIZE?

```



Possible target:



```text

contact

cut

reveal

drop

hero frame

```



Then design sound around that target.



\---



\# 44. LOGO REVEAL



Possible structure:



```text

APPROACH

→ subtle build



LOGO APPEARS

→ tonal/visual reveal



LOGO LOCKS

→ confirmation



FINAL HOLD

→ tail

```



The strongest sound may belong to lock rather than first visibility.



\---



\# 45. TYPOGRAPHY



Text animation may synchronize:



```text

word entrance

line completion

highlight

hero word

punctuation

```



Sound important semantic events.



Do not sound every character unless the concept specifically requires it.



\---



\# 46. KINETIC TYPOGRAPHY



For kinetic typography:



```text

MOTION RHYTHM

\+

SPEECH/MUSIC RHYTHM

\+

SEMANTIC EMPHASIS

```



should work together.



Avoid mechanical word-per-beat behavior unless stylistically intentional.



\---



\# 47. DATA FLOW



A useful structure:



```text

SOURCE ACTIVATES

→ activation cue



DATA MOVES

→ motion cue



DATA ARRIVES

→ confirmation cue

```



This creates causal audiovisual logic.



\---



\# 48. CONNECTION EVENT



For connecting two nodes:



```text

NODE A

→ source cue



PATH

→ travel cue



NODE B

→ arrival cue

```



The sound teaches the visual relationship.



\---



\# 49. CHARTS AND METRICS



Do not sound every number change.



Use sound for:



```text

important threshold

final metric

major comparison

key proof point

```



The sonic hierarchy should mirror information hierarchy.



\---



\# 50. NOTIFICATION



A notification sound should coincide with the meaningful notification state.



Not necessarily the first frame of the notification's entrance animation.



Possible:



```text

panel begins

→ silent



notification becomes readable

→ cue

```



depending on design.



\---



\# 51. SUCCESS STATE



Possible structure:



```text

ACTION

→ click



PROCESS

→ subtle activity



SUCCESS

→ confirmation tone

```



This communicates causality.



\---



\# 52. ERROR STATE



Possible structure:



```text

ACTION

→ input cue



REJECTION

→ error cue



ERROR UI

→ visible state

```



Avoid aggressive timing that feels unrelated to the UI state.



\---



\# 53. SOUND CAN ANTICIPATE VISION



Sound may intentionally arrive first.



Useful for:



```text

incoming object

off-screen movement

scene transition

dramatic reveal

attention direction

```



Audio can prepare the viewer.



\---



\# 54. VISION CAN ANTICIPATE SOUND



Visual movement may begin before the sound's main transient.



Example:



```text

object falls

→ visual anticipation



contact

→ sound impact

```



This is physically intuitive.



\---



\# 55. EXACT SYNC



Exact perceptual synchronization works well for:



```text

click

contact

snap

impact

cut

lock

```



But not every event needs exact sync.



\---



\# 56. LOOSE SYNC



Ambient motion can use looser relationships.



Examples:



```text

floating UI

background particles

slow camera drift

atmospheric light

```



Trying to frame-sync every ambient element makes motion artificial.



\---



\# 57. RHYTHMIC SYNC



Rhythmic sync means events belong to the same musical structure without necessarily sharing exact timestamps.



Example:



```text

beat 1

→ panel enters



between beats

→ cursor moves



beat 3

→ click



next downbeat

→ result

```



This often feels more musical than identical beat hits.



\---



\# 58. SEMANTIC SYNC



The most important synchronization can be semantic.



Example:



```text

CLICK SOUND

```



should correspond to:



```text

ACTUAL ACTIVATION

```



not merely:



```text

CURSOR TOUCHING BUTTON

```



Meaning has priority.



\---



\# 59. MOTION ENERGY → SOUND ENERGY



Visual energy can guide sound energy.



Consider:



```text

velocity

acceleration

scale

distance

weight

direction

complexity

```



Then design sound intensity accordingly.



\---



\# 60. SCALE → SOUND SCALE



Small visual:



```text

short

light

precise

```



Large visual:



```text

broader

heavier

longer

```



But art direction can intentionally break physical realism.



\---



\# 61. DISTANCE



Perceived distance may influence:



```text

level

high-frequency detail

reverb

stereo width

```



Use only when spatial realism supports the design.



\---



\# 62. DEPTH



Elements moving toward the viewer may gain:



```text

presence

body

width

```



Elements moving away may lose:



```text

presence

high-frequency detail

```



when appropriate.



\---



\# 63. DIRECTION



Large directional movement can be reinforced spatially.



But stereo movement should support the picture, not distract from it.



\---



\# 64. MOTION BLUR AND AUDIO



Heavy motion blur can make exact visual contact less obvious.



In these cases:



```text

sound

```



can help define the perceptual event.



But do not use sound to hide fundamentally unclear animation.



\---



\# 65. SPRING MOTION



Spring animation contains:



```text

approach

overshoot

return

settle

```



Possible sound design:



```text

main landing

→ primary sound



overshoot

→ subtle detail if necessary



settle

→ tail

```



Avoid machine-gun impacts.



\---



\# 66. BOUNCE



A stylized bounce may use multiple sounds if each contact is visually meaningful.



Scale later contacts down.



Example:



```text

CONTACT 1

100%



CONTACT 2

40%



CONTACT 3

15%

```



Conceptually, sonic energy should decay with visual energy.



\---



\# 67. REPEATED EVENTS



Repeated visual events may need:



```text

sample variation

level variation

pitch variation

selective omission

```



Keep them in the same sonic family.



\---



\# 68. AUDIO-MOTION PHRASE



Do not think only in individual effects.



Think:



```text

ANTICIPATION

→ MOTION

→ CONTACT

→ RELEASE

```



Then map:



```text

RISER

→ WHOOSH

→ IMPACT

→ TAIL

```



when appropriate.



This creates a complete audiovisual sentence.



\---



\# 69. MUSIC + SFX + MOTION



Three systems may converge:



```text

MUSIC

MOTION

SFX

```



Example:



```text

MUSIC

downbeat



MOTION

hero landing



SFX

impact peak

```



This creates a strong triple lock.



Reserve it for meaningful events.



\---



\# 70. DO NOT TRIPLE-LOCK EVERYTHING



If every event has:



```text

beat

\+

visual hit

\+

impact

```



nothing feels important.



Use contrast.



Some events should:



```text

flow

anticipate

trail

remain silent

```



\---



\# 71. AUDIO TRUTH VS TIMELINE TRUTH



A timeline may show perfect numerical alignment while playback feels late or early.



Potential causes:



```text

sample pre-roll

slow attack

codec delay

output offset

playback environment

motion ambiguity

```



Therefore final judgment must include actual playback.



\---



\# 72. SOURCE OFFSET



The source audio may contain timing before the perceptual event.



Example:



```text

sample starts

→ 40 ms pre-roll

→ transient

```



Do not move the visual event merely to match sample start.



Trim or offset the sample appropriately.



\---



\# 73. OUTPUT OFFSET



Export or playback can introduce an apparent systematic offset.



Keep this separate from creative synchronization.



Conceptually:



```text

CREATIVE SYNC

```



and:



```text

DELIVERY COMPENSATION

```



are different layers.



\---



\# 74. DO NOT CORRUPT SOURCE TIMING



If final output requires compensation, do not rewrite:



```text

SOURCE\_BEAT0

```



or semantic event timing to hide the problem.



Keep source truth and output correction separate.



\---



\# 75. FRAME QUANTIZATION



An audio event may occur between video frames.



The visual target must ultimately resolve to a frame.



Choose the closest perceptually correct frame.



For repeated musical events, use the cumulative timing logic defined in:



```text

references/audio/beat-sync.md

```



\---



\# 76. REMOTION EVENT MODEL



Represent audiovisual events semantically.



Example:



```tsx

const EVENTS = {

&#x20; heroLand: {

&#x20;   frame: 240,

&#x20;   sound: "hero-impact",

&#x20; },

&#x20; featureClick: {

&#x20;   frame: 310,

&#x20;   sound: "ui-click",

&#x20; },

};

```



Do not scatter unexplained frame numbers throughout the composition.



\---



\# 77. REMOTION SOUND OFFSET



A sound may need to begin before its target frame so that its transient lands correctly.



Concept:



```text

TARGET\_FRAME

=

perceptual visual event



SOUND\_START

=

TARGET\_FRAME

\-

sample pre-roll

```



Use measured or auditioned timing.



Do not assume a universal offset.



\---



\# 78. REMOTION LONG SAMPLES



Long effects may need controlled sequencing.



Examples:



```text

riser

ambience

transition sweep

```



Use timeline boundaries deliberately.



Do not accidentally restart or truncate important tails.



\---



\# 79. DECLARATIVE AUDIO EVENTS



Prefer:



```text

event registry

```



over:



```text

random Audio components

```



Concept:



```text

EVENT

VISUAL TARGET

SFX

START

PEAK

END

PRIORITY

```



This makes sync auditable.



\---



\# 80. EVENT CONTRACT



For important audiovisual events define:



```text

EVENT:

VISUAL PURPOSE:

VISUAL START:

VISUAL TARGET:

VISUAL END:

MOTION TYPE:

MOTION VELOCITY:

SOUND FUNCTION:

SFX FAMILY:

SOUND START:

SOUND PEAK:

SOUND END:

SYNC MODE:

MUSIC RELATIONSHIP:

VALIDATION:

```



\---



\# 81. SYNC MODE



Possible values:



```text

LEAD

EXACT

TRAIL

RHYTHMIC

LOOSE

```



This forces an intentional synchronization decision.



\---



\# 82. AFTER EFFECTS WORKFLOW



For critical events:



```text

identify visual target frame

↓

place marker

↓

inspect audio transient

↓

align perceptual peak

↓

play in context

↓

adjust

↓

render test

```



Use waveform as evidence.



Not as the sole judge.



\---



\# 83. DAVINCI / NLE WORKFLOW



Use markers for:



```text

visual contact

musical accents

SFX transient

scene arrival

```



Then inspect:



```text

waveform

picture

playback

```



together.



Do not judge synchronization from waveform alone.



\---



\# 84. AUDIO LAYERING AND SYNC



When multiple SFX form one event:



```text

attack layer

body layer

tail layer

```



they do not necessarily start at the same frame.



Their important perceptual moments should combine into one event.



\---



\# 85. LAYER OFFSETS



Example:



```text

AIR / RISER

starts before



TRANSIENT

lands on event



LOW BODY

lands on or immediately around event



SPARKLE

follows event

```



This creates depth.



\---



\# 86. MUSIC MASKING



Music can hide:



```text

clicks

small transients

high-frequency details

```



A synchronized sound that cannot be perceived contributes little.



Check the actual mix.



\---



\# 87. SFX MASKING



Large SFX can hide:



```text

music accents

voice

UI detail

```



Do not solve sync by simply increasing volume.



Use hierarchy and frequency space.



\---



\# 88. SILENCE AS SYNC



Silence can make the next synchronized event stronger.



Example:



```text

BUILD

→ short reduction

→ HERO IMPACT

```



Absence of sound is part of timing.



\---



\# 89. PRE-IMPACT SPACE



Before a major landing, reducing competing sound can increase perceived impact.



Use intentionally.



Do not mechanically mute before every hit.



\---



\# 90. POST-IMPACT SPACE



After a major event, allow:



```text

tail

hold

breath

```



when the narrative permits.



Immediate clutter can destroy the landing.



\---



\# 91. PRODUCT COMPREHENSION



Never synchronize so aggressively that:



```text

UI becomes unreadable

states disappear too quickly

cursor becomes confusing

feature causality breaks

```



Product truth and comprehension outrank rhythmic novelty.



\---



\# 92. CAUSALITY



Audio should reinforce causal order.



Example:



```text

CLICK

→ PROCESS

→ RESULT

```



not:



```text

SUCCESS SOUND

→ CLICK

→ RESULT

```



unless anticipation is intentionally part of the concept.



\---



\# 93. EVENT PRIORITY



Classify:



```text

PRIMARY

SECONDARY

AMBIENT

```



\## PRIMARY



Hero events.



\## SECONDARY



Supporting interactions.



\## AMBIENT



Atmospheric movement.



Synchronization precision and sonic prominence should reflect priority.



\---



\# 94. HERO EVENTS



Hero events deserve:



```text

clear target

intentional timing

strong hierarchy

render validation

```



Examples:



```text

product reveal

main transformation

critical metric

logo lock

CTA arrival

```



\---



\# 95. SECONDARY EVENTS



Secondary events can use lighter synchronization.



Examples:



```text

supporting cards

small UI actions

secondary labels

minor transitions

```



Do not give them the same weight as hero events.



\---



\# 96. AMBIENT EVENTS



Ambient motion often should not have exact transient sync.



Examples:



```text

particles

floating cards

background glow

slow parallax

```



Use texture rather than repeated event sounds.



\---



\# 97. SYNC AUDIT — VISUAL



Ask:



```text

What exact visual frame is important?



Is that frame visually readable?



Is contact clear?



Is the event semantic or merely decorative?

```



\---



\# 98. SYNC AUDIT — AUDIO



Ask:



```text

Where is the perceptual onset?



Where is the important transient?



Where is the peak?



Does the sample have pre-roll?



Does the tail need preservation?

```



\---



\# 99. SYNC AUDIT — RELATIONSHIP



Ask:



```text

Should sound lead?



Should it land exactly?



Should it trail?



Should it only share rhythm?



Should it remain loose?

```



\---



\# 100. SYNC AUDIT — MOTION



Ask:



```text

What is the velocity profile?



Where is maximum velocity?



Where is contact?



Where is settle?



Does sound follow the correct phase?

```



\---



\# 101. SYNC AUDIT — MUSIC



Ask:



```text

Is there a beat relationship?



Downbeat?



Phrase?



Drop?



Attack?



Or should this event ignore the grid?

```



Use:



```text

references/audio/beat-sync.md

```



when necessary.



\---



\# 102. SYNC AUDIT — MIX



Ask:



```text

Can the synchronized event actually be heard?



Is music masking it?



Is it masking music?



Does it need less volume or better spectral space?

```



\---



\# 103. SYNC AUDIT — FINAL RENDER



Check:



```text

early event

middle event

late event

hero event

fast transition

UI click

final logo

```



Watch the exported file.



Not only the editor preview.



\---



\# 104. DESYNC DIAGNOSIS



If one event feels wrong:



```text

inspect sample

inspect target frame

inspect attack

inspect peak

adjust local event

```



If every event feels equally shifted:



```text

investigate global output offset

```



If sync becomes progressively worse:



```text

investigate timing drift

BPM

frame conversion

rounding

```



Different symptoms imply different causes.



\---



\# 105. EARLY/LATE TEST



For ambiguous events, compare small offsets.



Example:



```text

VERSION A

1 frame early



VERSION B

exact



VERSION C

1 frame late

```



Judge in motion.



Do not rely only on timeline appearance.



\---



\# 106. HIGH-FPS REVIEW



When available, inspect high-frame-rate playback or frame-by-frame views for:



```text

fast clicks

contacts

speed ramps

transitions

```



Then validate again at normal playback speed.



\---



\# 107. HEADPHONES + SPEAKERS



Critical audiovisual sync may feel different depending on playback environment.



At minimum validate with a reliable monitoring setup.



Do not optimize to a visibly laggy playback device.



\---



\# 108. EXPORT VALIDATION



After export:



```text

play from beginning

check representative events

check climax

check ending

```



Do not assume export preserves perceived synchronization perfectly.



\---



\# 109. PRODUCT TRUTH



Audio must not imply an event that the interface does not perform.



Examples to avoid:



```text

confirmation sound before confirmation

success sound without success state

connection sound before connection exists

notification sound without notification

```



Sound reinforces product truth.



It does not invent it.



\---



\# 110. AUDIO-MOTION OUTPUT CONTRACT



For every major synchronized event:



```text

EVENT:

PURPOSE:

PRIORITY:



VISUAL\_START:

VISUAL\_TARGET:

VISUAL\_END:



MOTION\_TYPE:

MOTION\_DIRECTION:

MOTION\_VELOCITY:

MOTION\_ACCELERATION:



SOUND\_FUNCTION:

SFX\_FAMILY:

SOUND\_START:

SOUND\_TRANSIENT:

SOUND\_PEAK:

SOUND\_END:



SYNC\_MODE:

LEAD\_OFFSET:

TRAIL:



MUSIC\_TARGET:

TARGET\_FRAME:



MIX\_PRIORITY:

VALIDATION\_STATUS:

```



\---



\# 111. ROUTING



For overall audio strategy:



```text

references/audio/sound-design.md

```



For SFX vocabulary:



```text

references/audio/sfx-language.md

```



For musical timing:



```text

references/audio/beat-sync.md

```



For animation behavior:



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



For typography:



```text

references/typography.md

```



\---



\# 112. FINAL AUDIO-MOTION DECISION LOOP



```text

WHAT IS THE VISUAL EVENT?

&#x20;       ↓

WHY DOES IT MATTER?

&#x20;       ↓

WHAT EXACT VISUAL MOMENT IS PERCEPTUALLY IMPORTANT?

&#x20;       ↓

WHAT IS THE MOTION PHASE?

&#x20;       ↓

DOES THIS EVENT NEED SOUND?

&#x20;       ↓

WHAT FUNCTION SHOULD THE SOUND PERFORM?

&#x20;       ↓

WHAT SFX FAMILY REPRESENTS IT?

&#x20;       ↓

WHERE IS THE SAMPLE'S ONSET?

&#x20;       ↓

WHERE IS ITS IMPORTANT TRANSIENT?

&#x20;       ↓

WHERE IS ITS PEAK?

&#x20;       ↓

SHOULD SOUND LEAD, LAND, OR TRAIL?

&#x20;       ↓

HOW DOES VISUAL VELOCITY AFFECT THE SOUND?

&#x20;       ↓

IS THERE A MUSICAL TARGET?

&#x20;       ↓

WHAT EXACT FRAME IS THE VISUAL TARGET?

&#x20;       ↓

DO WE NEED SAMPLE PRE-ROLL COMPENSATION?

&#x20;       ↓

CAN THE EVENT BE HEARD IN THE MIX?

&#x20;       ↓

DOES IT PRESERVE PRODUCT CAUSALITY?

&#x20;       ↓

DOES IT FEEL SYNCHRONIZED IN PLAYBACK?

&#x20;       ↓

DOES IT STILL FEEL SYNCHRONIZED AFTER EXPORT?

```



\---



\# GOLDEN RULE



Synchronize perception, not file boundaries.



Find the visual event.



Find the sonic event.



Understand the motion between them.



Let sound lead when anticipation helps.



Let sound land when contact matters.



Let sound trail when aftermath matters.



Match sonic energy to motion energy.



Protect hierarchy.



Protect causality.



Protect product truth.



And validate the relationship in the final rendered video.

