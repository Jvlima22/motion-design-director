# Visual Motion Router



## Purpose



This file is the decision router for the visual motion system.



Do not load every reference or component by default.



Use progressive disclosure:



REQUEST

→ INTENT

→ CREATIVE DECISION

→ REQUIRED MODULES

→ SHOT DESIGN

→ IMPLEMENTATION



Load only the knowledge required for the current decision.



---



# 1. Core Routing Principle



Before choosing effects, transitions or software, determine:



1\. What must the viewer understand?

2\. What is the hero?

3\. What changes during the shot?

4\. What should the viewer look at first?

5\. What should happen next?



Then route to the appropriate module.



Never begin with:



"Which effect should I use?"



Begin with:



"What visual problem must be solved?"



---



# 2. Primary Decision Chain

Use this hierarchy:

MESSAGE

-> PRODUCT GOAL

-> ART DIRECTION

-> COMPOSITION

-> SHOT VOCABULARY

-> COMPONENT PATTERN

-> CAMERA LANGUAGE

-> TYPOGRAPHY, WHEN REQUIRED

-> TRANSITION

-> EFFECTS

-> SOUND STRATEGY, WHEN REQUIRED

-> MUSIC / BEAT RELATIONSHIP, WHEN REQUIRED

-> SFX LANGUAGE, WHEN REQUIRED

-> AUDIO-MOTION SYNC, WHEN REQUIRED

-> IMPLEMENTATION ENGINE

-> FINAL VALIDATION

This order expresses decision priority, not a requirement to load every module.

Not every shot requires typography.

Not every shot requires sound.

Not every sound decision requires all audio modules.

Use progressive disclosure.

Do not choose effects before shot logic.

Do not choose audio assets before understanding the audiovisual event.

Do not choose software before visual intent.

Product truth and communication remain above spectacle.

---

# 3. Foundation Layer



For overall motion behavior consult:



references/animation-principles.md



Use when deciding:



- timing

- easing

- anticipation

- follow-through

- stagger

- rhythm

- motion hierarchy

- motion restraint

- springs

- pacing



This is foundational knowledge.



It may inform almost every motion sequence,

but does not need to be reread completely for every small task.



---



# 4. Art Direction Layer



For overall creative direction consult:



references/art-direction.md



Use when deciding:



- tone

- energy

- motion personality

- visual hierarchy

- signature moments

- pacing architecture

- overall product-film language

- consistency



Art direction comes before individual shots.



---



# 5. Composition



For frame construction consult:



references/creative/composition.md



Use when deciding:



- focal point

- grid

- negative space

- visual weight

- depth hierarchy

- cropping

- safe areas

- multi-aspect layouts

- UI placement



---



# 6. Camera



For camera behavior consult:



references/creative/camera-language.md



Use when deciding:



- push

- pull

- orbit

- follow

- macro

- parallax

- camera continuity

- camera transitions

- depth travel

- shot progression



Do not use camera movement merely to make a shot cinematic.



Camera must support information hierarchy.



---



# 7. Visual Treatment



For visual design rules consult:



references/visual/design-rules.md



Use when deciding:



- color

- gradients

- glow

- shadows

- glass

- lighting

- surface hierarchy

- backgrounds

- visual density

- premium/futuristic treatment

- finishing



---



# 8. Shot Selection



When the question is:



"What kind of shot should communicate this?"



Consult:



references/shot-vocabulary.md



Examples:



- product establishing shot

- hero shot

- feature shot

- macro UI shot

- workflow shot

- ecosystem shot

- transformation shot

- result shot

- logo resolve



SHOT VOCABULARY selects the cinematic grammar.



It does not automatically define implementation.



---



# 9. Cinematic Interface Treatment



When the shot contains product UI and the question is:



"How should this interface behave cinematically?"



Consult:



references/cinematic-ui.md



Use for:



- UI depth

- spatial interfaces

- card hierarchy

- UI lighting

- focus

- decomposition

- floating interface

- interface transitions

- product fidelity

- readable cinematic UI



---



# 10. Component Selection



After selecting the shot,

determine whether a reusable visual pattern applies.



Available components:



components/ui-reveal.md



components/ui-explosion.md



components/floating-ui.md



components/feature-focus.md



components/device-mockup.md



components/data-flow.md



components/cursor-animation.md



components/logo-reveal.md



Do not load all components.



Select only the ones required by the shot.



---



# 11. UI Reveal Routing



Load:



components/ui-reveal.md



when the problem is:



- introduce interface

- reveal dashboard

- introduce application

- transition from abstract visual into product

- progressively expose UI

- establish product for first time



Typical intents:



SHOW THE PRODUCT



INTRODUCE THE INTERFACE



ENTER THE PRODUCT WORLD



---



# 12. UI Explosion Routing



Load:



components/ui-explosion.md



when the problem is:



- explain product structure

- separate functional layers

- visualize architecture

- expose interface hierarchy

- transition from whole product to one subsystem



Typical intents:



EXPLAIN STRUCTURE



DECOMPOSE PRODUCT



SHOW HOW PARTS RELATE



Do not use simply because separated cards look impressive.



---



# 13. Floating UI Routing



Load:



components/floating-ui.md



when the problem is:



- represent product ecosystem

- create spatial UI world

- show related features simultaneously

- show integrations around a hero

- build cinematic product environment



Typical intents:



SHOW ECOSYSTEM



SHOW RELATIONSHIPS



CREATE SPATIAL PRODUCT WORLD



---



# 14. Feature Focus Routing



Load:



components/feature-focus.md



when the problem is:



- explain one feature

- isolate functionality

- demonstrate action → result

- communicate feature value



Typical intents:



SHOW WHAT THIS FEATURE DOES



DIRECT ATTENTION



PROVE PRODUCT VALUE



Default logic:



CONTEXT

→ ISOLATION

→ ACTION

→ CONSEQUENCE

→ RESULT

→ VALUE



---



# 15. Device Mockup Routing



Load:



components/device-mockup.md



when:



- platform context matters

- mobile device is part of story

- wearable is important

- device provides physical scale

- device creates transition into UI

- multi-device ecosystem matters



Typical intents:



SHOW WHERE PRODUCT LIVES



CONNECT PHYSICAL DEVICE TO DIGITAL PRODUCT



Do not keep device frame after it stops helping communication.



---



# 16. Data Flow Routing



Load:



components/data-flow.md



when the problem involves:



- automation

- integrations

- APIs

- agents

- AI processing

- synchronization

- data pipelines

- CRM flow

- payments

- messaging

- event systems



Default logic:



SOURCE

→ TRANSPORT

→ PROCESS

→ DESTINATION

→ RESULT



Every signal must have semantic meaning.



---



# 17. Cursor Routing



Load:



components/cursor-animation.md



when user interaction needs to establish causality.



Examples:



- click

- hover

- drag

- select

- scroll

- connect

- search

- edit



Default logic:



INTENT

→ MOVEMENT

→ LANDING

→ ACTION

→ PRODUCT RESPONSE



The cursor is not the hero.



The result is the hero.



---



# 18. Logo Reveal Routing



Load:



components/logo-reveal.md



when:



- introducing brand

- resolving product film

- transforming product into identity

- creating end card

- transitioning logo → product

- transitioning product → logo



Default logic:



SOURCE VISUAL

→ BRAND CONSTRUCTION

→ RECOGNITION

→ SETTLE

→ HOLD



Avoid generic logo templates.



---



# 19. Transition Routing



When two shots already exist and the question is:



"How should Shot A become Shot B?"



Consult:



references/transitions.md



Determine relationship first:



SPATIAL



SEMANTIC



GRAPHIC



CAMERA



UI



TEMPORAL



BRAND



Then select transition.



Do not choose transition because it looks impressive.



---



# 20. Effects Routing



When shot logic already exists and needs enhancement consult:



references/effects-library.md



Use for:



- attention

- depth

- light

- energy

- atmosphere

- material

- distortion

- UI-native enhancement

- finishing



Effects come after:



MESSAGE



SHOT



COMPONENT



CAMERA



TRANSITION.



---



# 21. Effect Budget



Default:



1 PRIMARY EFFECT



+



0–2 SUPPORTING EFFECTS



+



OPTIONAL AMBIENT TREATMENT



Do not stack effects without purpose.



---



# 22. Product Introduction Request



If user asks:



"Introduce this SaaS/product/app."



Load:



art-direction



shot-vocabulary



ui-reveal



cinematic-ui



Then optionally:



device-mockup



if platform context matters.



---



# 23. Feature Demonstration Request



If user asks:



"Show this feature."



Load:



shot-vocabulary



feature-focus



cursor-animation



if user action matters.



Then:



transitions



if connecting to another feature.



---



# 24. AI Feature Request



If user asks:



"Show how the AI works."



Determine whether actual story is:



INPUT → OUTPUT



or:



INPUT → PROCESS → TOOLS → OUTPUT



Load:



feature-focus



data-flow



cinematic-ui



effects-library only after structure exists.



Do not default to particles.



---



# 25. Automation Request



If user asks:



"Show this automation."



Load:



data-flow



shot-vocabulary



camera-language



Optionally:



cursor-animation

if user builds workflow.



Optionally:



floating-ui

if ecosystem/integrations matter.



---



# 26. Integration Request



If user asks:



"Show integrations."



Determine whether message is:



QUANTITY



RELATIONSHIP



FLOW



ECOSYSTEM



If relationship/ecosystem:



floating-ui



If actual information movement:



data-flow



Do not automatically connect every logo with glowing lines.



---



# 27. Mobile App Request



Load:



device-mockup



feature-focus



cinematic-ui



cursor-animation should normally NOT be used.



Use touch interaction instead.



---



# 28. Dashboard Request



Load:



cinematic-ui



feature-focus



composition



Use:



data-flow

only when movement of information matters.



---



# 29. Product Architecture Request



Load:



ui-explosion



data-flow



camera-language



shot-vocabulary



Use conceptual abstraction when actual architecture is unknown.



Never fabricate technical architecture.



---



# 30. Product Ecosystem Request



Load:



floating-ui



data-flow if relationships transmit information



composition



camera-language



Maintain one hero.



Avoid card soup.



---



# 31. Product Hero Request



Load:



art-direction



shot-vocabulary



cinematic-ui



composition



effects-library



Possibly:



device-mockup.



Hero shots require restraint.



---



# 32. Product Film Opening



Possible routing:



art-direction



→ shot-vocabulary



→ logo-reveal OR ui-reveal



→ cinematic-ui



→ transitions



Choose logo-first only when branding should precede product.



---



# 33. Product Film Closing



Possible routing:



final result



→ logo-reveal



→ CTA



Load:



logo-reveal



transitions



sound-design when the closing requires a deliberate sonic resolution.



The closing should resolve the visual story.



---



# 34. Before / After Request



Load:



shot-vocabulary



feature-focus



transitions



Potential structure:



PROBLEM



→ TRANSFORMATION



→ RESULT.



---



# 35. Complex Request



For a full product film,

do not load everything simultaneously.



Process scene by scene.



Example:



SCENE 01

art direction + hero shot



SCENE 02

UI reveal



SCENE 03

feature focus + cursor



SCENE 04

data flow



SCENE 05

floating UI



SCENE 06

logo reveal



This is progressive disclosure.



---



# 36. Multi-Module Limit

As a default, for each decision load only:

1 FOUNDATION MODULE

+

1-2 PRIMARY VISUAL MODULES

+

0-1 TYPOGRAPHY MODULE

+

0-2 AUDIO MODULES

+

1 SUPPORT MODULE

when required.

These are routing defaults, not rigid quotas.

Do not load typography when text is incidental.

Do not load audio modules when sound is irrelevant to the current decision.

For ordinary audiovisual decisions, prefer the smallest useful audio set.

Examples:

GENERAL SONIC STRATEGY
-> sound-design

MUSIC TIMING
-> beat-sync

SFX SELECTION
-> sfx-language

PRECISE AUDIOVISUAL ALIGNMENT
-> audio-motion-sync

A hero audiovisual event may justify multiple audio modules when each solves a different decision.

Expand only when necessary.

Progressive disclosure is more important than module count.

---

# 37. Module Priority

When modules conflict, use this priority:

1. PRODUCT TRUTH
2. COMMUNICATION
3. ART DIRECTION
4. SHOT LOGIC
5. INFORMATION HIERARCHY
6. READABILITY
7. MOTION PRINCIPLES
8. AUDIOVISUAL CAUSALITY
9. RHYTHMIC COHERENCE
10. EFFECTS
11. SONIC SPECTACLE
12. TECHNICAL NOVELTY

Typography must not reduce comprehension for visual novelty.

Music synchronization must not damage product comprehension.

SFX must not imply events that do not occur.

Audio-motion synchronization must preserve causal order.

Never sacrifice product truth for visual, rhythmic or sonic spectacle.

---

# 38. Product Truth



Do not invent:



features



metrics



architecture



integrations



AI behavior



data



device behavior



interaction



unless clearly presented as conceptual.



---



# 39. Creative Abstraction



It is acceptable to visually abstract:



data movement



AI processing



automation



system relationships



when literal representation would be unclear.



But abstraction must remain semantically honest.



---



# 40. Decision Before Implementation



Never route directly:



USER REQUEST

→ REMOTION



or:



USER REQUEST

→ AFTER EFFECTS.



First:



USER REQUEST

→ VISUAL SOLUTION



Then select engine.



---



# TYPOGRAPHY + AUDIO ROUTING



Typography and audio are not finishing decorations.



They are communication systems.



Route them intentionally after the core visual logic is understood and before final implementation decisions are locked.



---



## Typography Routing



When the shot contains meaningful text and the question involves:



- hierarchy

- headline treatment

- kinetic typography

- text reveal

- word emphasis

- readability

- measuring text

- text timing

- typography as motion

- product copy hierarchy

- hero words

- text composition



consult:



```text id="8znq5p"

references/typography.md

```



Typography must follow:



```text id="6bcax5"

MESSAGE

→ INFORMATION HIERARCHY

→ COMPOSITION

→ READING TIME

→ MOTION

→ EMPHASIS

```



Do not animate text merely because text exists.



Use typography as part of the communication architecture.



---



## Typography Loading Rule



Load `references/typography.md` when typography is:



- the hero

- a major communication layer

- animated

- synchronized with music

- structurally important to composition

- part of a product feature explanation



Do not load the full typography reference for incidental static labels unless needed.



---



# AUDIO ROUTING



Do not treat:



```text id="rj8nt8"

SOUND

```



as one undifferentiated decision.



Route audio according to the actual problem.



Use:



```text id="a0pf4r"

AUDIO QUESTION

        ↓

WHY / WHERE?

→ sound-design.md



WHEN RELATIVE TO MUSIC?

→ beat-sync.md



WHAT SOUND?

→ sfx-language.md



HOW DOES SOUND BIND TO MOTION?

→ audio-motion-sync.md

```



---



## Sound Design Routing



When the question involves:



- whether an event needs sound

- sonic hierarchy

- density

- silence

- music vs SFX balance

- audio layers

- narrative function

- sound importance

- overall sonic strategy



consult:



```text id="z4svmy"

references/audio/sound-design.md

```



Sound design determines the role of audio.



It does not primarily choose the exact SFX asset.



---



## Beat Sync Routing



When the question involves:



- BPM

- beat grid

- beat 1

- SOURCE_BEAT0

- downbeats

- bars

- phrases

- drops

- musical structure

- edit rhythm

- rhythmic cuts

- speed ramps related to music

- frame conversion

- musical timing drift



consult:



```text id="r52z7i"

references/audio/beat-sync.md

```



Use beat sync to determine:



```text id="et2h9w"

WHEN

```



an audiovisual event should relate to music.



Do not interpret beat sync as:



```text id="w1r3dm"

EVERY BEAT

=

ANIMATION

```



---



## SFX Language Routing



When the question involves:



- whoosh

- impact

- click

- snap

- pop

- riser

- sparkle

- transition sound

- digital sound

- mechanical sound

- material

- sonic scale

- SFX family

- SFX search terms

- sample variants



consult:



```text id="b9druv"

references/audio/sfx-language.md

```



Use SFX language to determine:



```text id="6tpc31"

WHAT SOUND

```



best represents the visual event.



---



## Audio-Motion Sync Routing



When the question involves:



- exact audiovisual timing

- onset

- attack

- transient

- sound peak

- visual contact

- velocity

- landing

- lead

- exact sync

- trail

- perceptual sync

- sample pre-roll

- desynchronization

- render offset



consult:



```text id="fy5sgx"

references/audio/audio-motion-sync.md

```



Use audio-motion sync to determine:



```text id="8np38g"

HOW SOUND

AND MOTION

BECOME ONE EVENT

```



---



# AUDIO DECISION CHAIN



For important audiovisual events use:



```text id="id09js"

VISUAL EVENT

→ EVENT PURPOSE

→ SOUND NECESSITY

→ SOUND FUNCTION

→ MUSICAL RELATIONSHIP

→ SFX FAMILY

→ AUDIO-MOTION RELATIONSHIP

→ MIX PRIORITY

→ FINAL RENDER VALIDATION

```



---



# AUDIO PROGRESSIVE DISCLOSURE



Do not load all four audio references by default.



Load according to the problem.



### General sound strategy



Load:



```text id="g21ckm"

sound-design.md

```



### Music-driven editing



Load:



```text id="5lnzpc"

beat-sync.md

```



and add:



```text id="1bqu1j"

audio-motion-sync.md

```



only when precise audiovisual alignment matters.



### Choosing an effect



Load:



```text id="i85hwj"

sfx-language.md

```



Add:



```text id="8sru1r"

audio-motion-sync.md

```



if placement must be frame-accurate.



### Hero audiovisual event



Load:



```text id="wckql6"

sound-design.md

+

sfx-language.md

+

audio-motion-sync.md

```



Add:



```text id="l3ul0q"

beat-sync.md

```



when music provides the target.



---



# TYPOGRAPHY + AUDIO INTERACTION



When text is synchronized with sound or music:



```text id="u1v08f"

MESSAGE

→ TYPOGRAPHIC HIERARCHY

→ TEXT MOTION

→ MUSICAL RELATIONSHIP

→ AUDIO EVENT

→ PERCEPTUAL SYNC

```



Possible routing:



```text id="5htqsy"

typography.md

+

beat-sync.md

+

audio-motion-sync.md

```



Do not force every word onto a beat.



Semantic emphasis outranks mechanical rhythm.



---



# TRANSITION + AUDIO INTERACTION



For an important transition:



```text id="1z6ajl"

transitions.md

+

sfx-language.md

+

audio-motion-sync.md

```



Add:



```text id="t6wfjq"

beat-sync.md

```



when the transition is musically targeted.



The transition should first work visually.



Sound reinforces its behavior.



---



# CAMERA + AUDIO INTERACTION



For strong camera movement:



```text id="32iyzg"

creative/camera-language.md

+

sfx-language.md

+

audio-motion-sync.md

```



Sound:



- fast intentional camera motion

- whip

- push

- pull

- pass-through

- major orbit acceleration



Do not automatically sound:



- slow drift

- subtle parallax

- ambient camera motion



---



# COMPONENT + AUDIO INTERACTION



Examples:



```text id="x6csda"

UI REVEAL

→ ui-reveal.md

→ optional sfx-language.md

→ audio-motion-sync.md when timing matters



UI EXPLOSION

→ ui-explosion.md

→ sound-design.md

→ sfx-language.md

→ audio-motion-sync.md



DATA FLOW

→ data-flow.md

→ sfx-language.md

→ audio-motion-sync.md



CURSOR

→ cursor-animation.md

→ sfx-language.md for important interactions



LOGO REVEAL

→ logo-reveal.md

→ sound-design.md

→ sfx-language.md

→ audio-motion-sync.md

```



---



# AUDIO EVENT PRIORITY



Classify audiovisual events as:



```text id="9ypa3q"

PRIMARY

SECONDARY

AMBIENT

```



PRIMARY events may justify:



- stronger SFX

- precise synchronization

- musical targeting

- layered sound



SECONDARY events should remain lighter.



AMBIENT events often need texture rather than exact transient synchronization.



---



# PRODUCT TRUTH + AUDIO



Audio must not imply a product event that does not occur.



Do not use:



- success sound before success

- connection sound before connection

- notification sound without notification

- confirmation sound without confirmation



Product truth has priority over sonic spectacle.



---



# AUDIO ROUTING AUDIT



Before implementation ask:



```text id="wfj0en"

DOES THIS EVENT NEED SOUND?



WHY?



IS MUSIC INVOLVED?



IS THERE A SPECIFIC MUSICAL TARGET?



WHAT SOUND FAMILY REPRESENTS THE EVENT?



WHAT VISUAL MOMENT IS IMPORTANT?



SHOULD SOUND LEAD, LAND OR TRAIL?



IS THIS EVENT PRIMARY, SECONDARY OR AMBIENT?



CAN IT BE HEARD IN THE MIX?



DOES IT PRESERVE PRODUCT TRUTH?



DOES THE FINAL RENDER FEEL SYNCHRONIZED?

```



---



# UPDATED VISUAL + AUDIO DECISION CHAIN



Use:



```text id="8f9bkv"

MESSAGE

→ PRODUCT GOAL

→ ART DIRECTION

→ COMPOSITION

→ SHOT VOCABULARY

→ COMPONENT PATTERN

→ CAMERA LANGUAGE

→ TYPOGRAPHY

→ TRANSITION

→ EFFECTS

→ SOUND STRATEGY

→ MUSIC / BEAT RELATIONSHIP

→ SFX LANGUAGE

→ AUDIO-MOTION SYNC

→ IMPLEMENTATION ENGINE

→ FINAL VALIDATION

```



Not every shot requires every stage.



Load only what the communication problem requires.



---



# FUSION-04 ROUTING RULE



Do not ask:



```text id="k0fmy6"

"What audio reference should I load?"

```



Ask:



```text id="8y0r6p"

"What audiovisual decision am I trying to make?"

```



Then load the smallest reference set capable of answering it.



Typography communicates.



Music structures time.



SFX gives events sonic identity.



Audio-motion sync binds sound to movement.



Sound design controls the whole sonic hierarchy.


# 41. Engine Routing



After visual design is approved,

route implementation to:



REMOTION



AFTER EFFECTS



DAVINCI / FUSION



or hybrid pipeline.



Technical modules define HOW.



Creative modules define WHAT and WHY.



---



# 42. Remotion Bias



Prefer Remotion when:



- UI is code-driven

- scenes are reusable

- product data is dynamic

- deterministic rendering matters

- responsive variants are needed

- programmatic animation is advantageous



Consult technical Remotion references only after shot design.



---



# 43. After Effects Bias



Prefer After Effects when:



- high-touch art direction

- advanced compositing

- manual visual polish

- complex masks

- detailed vector animation

- premium motion graphics



---



# 44. DaVinci / Fusion Bias



Prefer DaVinci/Fusion when:



- editing already-rendered scenes

- compositing footage

- screen replacement

- finishing

- sound

- color

- delivery

- edit timing



---



# 45. Hybrid Pipeline



A professional sequence may use:



REMOTION

for product/UI generation



→ AFTER EFFECTS

for hero compositing



→ DAVINCI

for edit, sound, color and delivery.



Do not force one tool to solve every problem.



---



# 46. Shot Design Output

Before implementation produce:

SHOT PURPOSE:

MESSAGE:

HERO:

SHOT TYPE:

COMPONENT PATTERN:

COMPOSITION:

CAMERA:

PRIMARY MOTION:

SECONDARY MOTION:

TYPOGRAPHY:

TRANSITION IN:

TRANSITION OUT:

EFFECTS:

SOUND STRATEGY:

MUSIC / BEAT RELATIONSHIP:

SFX LANGUAGE:

AUDIO-MOTION SYNC:

DURATION:

IMPLEMENTATION ENGINE:

VALIDATION TARGET:

Use `N/A` for fields that are intentionally not required.

Do not invent decisions merely to fill the contract.

This becomes the production contract.

For important audiovisual events, optionally expand:

AUDIO EVENT:

VISUAL TARGET:

SFX FAMILY:

SYNC MODE:

TARGET FRAME:

MIX PRIORITY:

The production contract should describe intent before implementation details.

---

# 47. Sequence Design Output



For multiple shots produce:



SHOT 01

purpose / hero / transition



SHOT 02

purpose / hero / transition



SHOT 03

purpose / hero / transition



Then verify:



visual escalation



continuity



pacing



repetition



information density.



---



# 48. Repetition Audit



Check whether sequence repeatedly uses:



push-in



floating cards



glow



cursor click



UI explosion



zoom transition



same camera angle.



If so,

change grammar while preserving consistency.



Consistency is not repetition.



---



# 49. Density Audit



Ask for each shot:



How many things demand attention?



Prefer:



ONE HERO



FEW SUPPORT ELEMENTS



QUIET BACKGROUND.



---



# 50. Spectacle Audit



Ask:



If effects were removed,

would the shot still communicate?



If no,

the concept may be weak.



---



# 51. Transition Audit



Ask:



Why does Shot B emerge from Shot A?



Good answers:



same object



same movement



same concept



same geometry



same data



same camera path



cause and effect.



Bad answer:



"because the transition looks cool."



---



# 52. Camera Audit



Ask:



What information does camera movement reveal?



If answer is unclear,

consider static camera.



---



# 53. Component Audit



Ask:



Is this component pattern actually solving the communication problem?



Do not use:



UI Explosion

because product has cards.



Do not use:



Floating UI

because interface has panels.



Do not use:



Data Flow

because product is technical.



Pattern follows meaning.



---



# 54. Effect Audit



Ask:



What does each effect communicate?



If answer is only:



"more cinematic"



remove or reduce it.



---



# 55. Final Audiovisual Decision Loop

For every shot:

DEFINE MESSAGE

-> VERIFY PRODUCT TRUTH

-> SELECT HERO

-> SELECT SHOT

-> SELECT COMPONENT

-> COMPOSE

-> SELECT CAMERA

-> DESIGN MOTION

-> DESIGN TYPOGRAPHY, IF REQUIRED

-> CONNECT TRANSITION

-> ADD EFFECTS, IF REQUIRED

-> DEFINE SOUND STRATEGY, IF REQUIRED

-> DEFINE MUSIC / BEAT RELATIONSHIP, IF REQUIRED

-> SELECT SFX LANGUAGE, IF REQUIRED

-> DEFINE AUDIO-MOTION SYNC, IF REQUIRED

-> REVIEW VISUAL HIERARCHY

-> REVIEW AUDIOVISUAL CAUSALITY

-> SELECT IMPLEMENTATION ENGINE

-> IMPLEMENT

-> VALIDATE FINAL RENDER

At every optional stage ask whether the module solves a communication problem.

Do not add typography, effects, music synchronization or SFX merely to increase production density.

The final render is the authority for perceptual audiovisual synchronization.

---

# 56. Router Examples



Request:



"Show that the AI automatically qualifies a lead."



Route:



feature-focus

+

data-flow



Optional:

cursor-animation if user triggers qualification.



Shot:



lead context

→ AI process

→ score

→ recommendation.



---



Request:



"Introduce the mobile app."



Route:



device-mockup

+

ui-reveal



Shot:



device hero

→ screen activation

→ push into interface.



---



Request:



"Show all integrations."



Route:



floating-ui



If data actually moves:



+

data-flow.



---



Request:



"Make the dashboard cinematic."



Route:



cinematic-ui

+

composition

+

camera-language.



Effects only after hierarchy is solved.



---



Request:



"End with the logo."



Route:



logo-reveal

+

transitions.



Use preceding product visual as source whenever possible.



---



# 57. Golden Routing Rule

DO NOT SEARCH THE LIBRARY FOR SOMETHING COOL.

SEARCH THE LIBRARY FOR THE SOLUTION TO A SPECIFIC COMMUNICATION PROBLEM.

The system should reason:

WHAT MUST BE UNDERSTOOD?

-> WHAT IS TRUE ABOUT THE PRODUCT?

-> WHAT VISUAL STRUCTURE COMMUNICATES IT?

-> WHAT SHOT GRAMMAR PRESENTS IT?

-> WHAT MOTION MAKES THAT STRUCTURE CLEAR?

-> DOES TYPOGRAPHY NEED TO CARRY MEANING?

-> DOES SOUND NEED TO REINFORCE THE EVENT?

-> DOES MUSIC NEED TO STRUCTURE TIME?

-> DOES AN SFX NEED TO GIVE THE EVENT SONIC IDENTITY?

-> DOES SOUND NEED PRECISE MOTION SYNCHRONIZATION?

-> WHAT IMPLEMENTATION ENGINE SHOULD BUILD IT?

-> HOW WILL THE FINAL RESULT BE VALIDATED?

Meaning chooses the pattern.

The pattern chooses the motion.

The communication problem chooses the required knowledge.

Typography communicates only when typography has a job.

Music structures time only when musical structure matters.

SFX gives sonic identity only to meaningful events.

Audio-motion sync binds perception, not arbitrary clip boundaries.

The motion chooses the implementation.

Product truth constrains every layer.

Final playback validates the audiovisual result.
