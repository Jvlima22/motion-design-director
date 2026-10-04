\# Animation Principles



\## Purpose



This reference defines how motion should behave before implementation in

Remotion, After Effects, DaVinci Resolve, CSS, Framer Motion, or another engine.



Motion is not decoration.



Every animation must support at least one of:



\- communication

\- hierarchy

\- continuity

\- emotion

\- physical intuition

\- interaction feedback

\- storytelling



Implementation comes after motion intent.



\---



\# 1. Motion Decision Framework



Before choosing duration, easing, spring values, or keyframes, determine:



\## Emotional Intent



What should the viewer feel?



Examples:



\- premium

\- calm

\- precise

\- energetic

\- playful

\- powerful

\- elegant

\- futuristic

\- trustworthy



The emotional intent influences:



\- acceleration

\- duration

\- overshoot

\- amplitude

\- camera behavior

\- secondary motion



\## Visual Narrative



Determine the micro-story:



SETUP → ACTION → RESOLUTION



Example:



Dashboard card is inactive

→ feature activates

→ card becomes the visual focus

→ supporting information settles

→ frame breathes.



\## Motion Craft



Determine what makes the movement believable:



\- acceleration

\- deceleration

\- anticipation

\- inertia

\- overlap

\- arcs

\- follow-through

\- secondary motion

\- depth

\- weight



Never choose animation values before understanding these three layers.



\---



\# 2. Motion Hierarchy



Professional motion should have hierarchy.



Use three layers:



\## Primary / Hero Motion



The movement the viewer should notice first.



Examples:



\- hero UI entering

\- device rotating

\- dashboard zoom

\- feature card expanding

\- primary headline reveal



\## Secondary / Support Motion



Movement that reinforces the hero.



Examples:



\- shadow settling

\- supporting labels appearing

\- icons reacting

\- secondary cards staggering

\- highlights following the primary action



\## Ambient / Texture Motion



Low-attention environmental motion.



Examples:



\- subtle gradient drift

\- particles

\- slow glow

\- background noise

\- very slow parallax



Ambient motion must never compete with the hero.



A useful mapping is:



Primary = Hero  

Secondary = Support  

Ambient = Texture



\---



\# 3. Staging



The viewer should understand where to look.



Prefer:



ONE HERO

\+

SUPPORTING MOTION

\+

CONTROLLED BACKGROUND



Avoid several elements competing for attention simultaneously.



When introducing an important feature:



1\. establish the environment

2\. reduce competing visual energy

3\. introduce the hero

4\. allow the hero action to complete

5\. reveal supporting information

6\. hold briefly

7\. transition



Motion hierarchy is more important than motion quantity.



\---



\# 4. Timing



Timing communicates:



\- weight

\- scale

\- urgency

\- importance

\- personality



Useful starting ranges:



| Event | Typical duration |

|---|---:|

| Tap / press feedback | 80–150ms |

| Hover | 100–180ms |

| Toggle | 150–220ms |

| Tooltip / dropdown | 150–250ms |

| Small UI transition | 180–300ms |

| Panel / modal | 250–450ms |

| Card reveal | 350–550ms |

| Page region | 300–550ms |

| Hero element | 450–800ms |

| Number count | 600–1200ms |

| Cinematic camera | 800–2000ms+ |



These are starting points, not immutable laws.



Always evaluate:



\- travel distance

\- element size

\- perceived mass

\- narrative importance

\- surrounding pacing



Large/heavy objects generally require more time.



Small/light objects can respond faster.



\---



\# 5. Distance and Duration



Do not give every movement the same duration.



A useful heuristic:



duration ≈ baseDuration × sqrt(distance / baseDistance)



Example:



base:

200px → 300ms



movement:

800px



300 × sqrt(800 / 200)

= approximately 600ms



This prevents:



\- long movements feeling unnaturally fast

\- short movements feeling sluggish



Use visual judgment after calculation.



The formula is a starting point, not the final decision.



\---



\# 6. Easing



Linear motion usually feels mechanical when representing a discrete event.



Reserve linear motion primarily for continuous processes:



\- spinners

\- constant rotation

\- marquees

\- endless loops

\- intentionally mechanical movement



For most discrete motion, accelerate and/or decelerate.



\## Enter



Prefer strong deceleration.



Default:



cubic-bezier(0.16, 1, 0.3, 1)



Alternative balanced:



cubic-bezier(0.33, 1, 0.68, 1)



The object arrives with energy and settles smoothly.



\## Exit



Prefer acceleration away.



Default:



cubic-bezier(0.7, 0, 0.84, 0)



\## Reposition



For an object that remains visible:



cubic-bezier(0.65, 0, 0.35, 1)



\## Playful / Branded



Controlled overshoot:



cubic-bezier(0.34, 1.56, 0.64, 1)



Do not add overshoot merely because it looks animated.



Overshoot should communicate:



\- elasticity

\- energy

\- personality

\- impact



Premium restrained interfaces often need little or no visible bounce.



\---



\# 7. Easing Selection



Use this reasoning:



ENTER

→ ease-out



EXIT

→ ease-in



MOVE BETWEEN VISIBLE STATES

→ ease-in-out



INTERACTIVE / PHYSICAL

→ consider spring



PLAYFUL BRAND MOMENT

→ controlled overshoot



CONTINUOUS LOOP

→ linear may be appropriate



CINEMATIC CAMERA

→ smooth controlled ease-in-out



When uncertain, prioritize a confident launch and controlled deceleration.



\---



\# 8. Useful Easing Library



\## Ease Out



Gentle:

`cubic-bezier(0.5, 1, 0.89, 1)`



Balanced:

`cubic-bezier(0.33, 1, 0.68, 1)`



Snappy:

`cubic-bezier(0.25, 1, 0.5, 1)`



Very snappy:

`cubic-bezier(0.22, 1, 0.36, 1)`



Premium / dramatic:

`cubic-bezier(0.16, 1, 0.3, 1)`



\## Ease In



Balanced:

`cubic-bezier(0.32, 0, 0.67, 0)`



Sharp:

`cubic-bezier(0.5, 0, 0.75, 0)`



Dramatic:

`cubic-bezier(0.7, 0, 0.84, 0)`



\## Ease In-Out



Neutral:

`cubic-bezier(0.45, 0, 0.55, 1)`



Balanced:

`cubic-bezier(0.65, 0, 0.35, 1)`



Punchy:

`cubic-bezier(0.76, 0, 0.24, 1)`



\## Overshoot



`cubic-bezier(0.34, 1.56, 0.64, 1)`



Use selectively.



\---



\# 9. Springs



Use springs when motion should feel:



\- physical

\- interruptible

\- interactive

\- gesture-driven

\- naturally settling



Prefer duration/easing when motion must be:



\- timeline locked

\- synchronized to music

\- frame precise

\- choreographed for video



Useful conceptual presets:



\## Snappy UI



stiffness: 300  

damping: 30  

mass: 1



\## Playful



stiffness: 400  

damping: 17  

mass: 1



\## Gentle / Heavy



stiffness: 120  

damping: 20  

mass: 1



\## Precise / Minimal Bounce



stiffness: 500  

damping: 50  

mass: 1



Treat values as starting presets.



Tune according to implementation engine.



\---



\# 10. Anticipation



Anticipation prepares the viewer for an action.



Examples:



button:

scale 1 → 0.95 → release



modal:

y 0 → +8px → launch upward



card:

small opposite rotation → primary rotation



Typical anticipation duration:



60–120ms



Keep anticipation subtle in professional product UI.



Too much anticipation makes software feel cartoonish.



\---



\# 11. Follow-Through



Objects should not necessarily stop simultaneously.



Example:



Hero card lands.



Then:



+40ms shadow settles  

+50ms title settles  

+70ms metadata settles



This creates overlapping action.



Avoid:



everything starts together  

everything stops together



That usually creates mechanical motion.



\---



\# 12. Secondary Motion



Secondary action reinforces primary action.



Example:



PRIMARY:

dashboard card expands



SECONDARY:

icon rotates slightly



SUPPORT:

label appears



AMBIENT:

background gradient shifts



Secondary action must remain subordinate.



If the viewer notices the secondary action before the hero, reduce it.



\---



\# 13. Arcs



Organic and cinematic movement often benefits from curved trajectories.



Avoid using straight X/Y translation for every object.



Consider:



\- bezier paths

\- camera arcs

\- orbit movement

\- curved fly-ins

\- slight vertical drift during horizontal travel



Use straight paths when they reinforce:



\- precision

\- grid structure

\- mechanical systems

\- interface alignment



\---



\# 14. Squash and Stretch



Use carefully in software/product motion.



Suitable for:



\- playful loaders

\- mascots

\- expressive icons

\- micro-interactions

\- branded moments



Example impact:



scaleY: 0.8

scaleX: 1.15



Try to preserve perceived volume.



Avoid cartoon-like deformation on serious enterprise interfaces unless explicitly part of the brand.



\---



\# 15. Exaggeration



Exaggeration improves readability when restrained.



Possible uses:



\- slightly stronger overshoot

\- larger initial scale difference

\- clearer depth separation

\- stronger camera push

\- more visible highlight



Ask:



Would the motion still communicate if the effect were 20% weaker?



If yes, consider reducing it.



\---



\# 16. Stagger



Groups should rarely appear as one flat event.



Useful starting offsets:



Lists:

40–80ms



Dense grids:

20–40ms



Large cinematic sequences:

can use larger offsets when intentionally paced



Formula:



totalReveal =

(count - 1) × offset

\+ itemDuration



For normal UI group reveals, try to keep the overall reveal around 600–800ms.



If it becomes too long:



\- reduce offset

\- group elements

\- use distance-based stagger

\- reveal in waves



\---



\# 17. Stagger Direction



Stagger should follow visual logic.



Possible origins:



\- top → bottom

\- left → right

\- focal point → outward

\- cursor position → outward

\- hero element → supporting elements

\- center → perimeter

\- depth front → back



Never stagger randomly without a compositional reason.



\---



\# 18. The One-Third Heuristics



Use as diagnostic heuristics, not absolute laws.



\## Travel



If an element crosses a large portion of the frame, consider adding:



\- intermediate state

\- scale change

\- opacity transition

\- camera movement

\- depth change

\- another narrative beat



Long uninterrupted slides often feel template-like.



\## Simultaneous Motion



Avoid having every visible element in strong motion simultaneously.



At any moment:



Hero motion should dominate.



Support motion should remain limited.



Ambient motion should be subtle.



\---



\# 19. Rhythm



Professional motion needs contrast.



Use:



MOVE → SETTLE → BREATHE → NEXT MOVE



instead of:



MOVE → MOVE → MOVE → MOVE



Stillness is part of animation.



A pause is not necessarily dead time.



It can create:



\- emphasis

\- comprehension

\- anticipation

\- contrast

\- premium pacing



Important information should remain readable after landing.



\---



\# 20. Information Holds



When important information appears, give the viewer time to understand it.



Possible examples:



\- headline

\- metric

\- feature name

\- result

\- logo

\- CTA



Brand-memory moments can justify longer holds than ordinary UI elements.



Do not blindly enforce a fixed one-second hold.



Determine the hold from:



\- reading time

\- pacing

\- music

\- importance

\- format



\---



\# 21. Beat Synchronization



Music should influence timing without controlling every property.



Land important events on meaningful accents:



\- cut

\- reveal

\- impact

\- logo formation

\- major transition

\- payoff



Do not shake, zoom, flash, or pump the entire frame on every beat.



Beat sync should create rhythm, not visual jitter.



Use major full-frame hits sparingly.



Smaller beats can affect:



\- hero element

\- typography

\- highlights

\- particles

\- secondary components



\---



\# 22. Camera Motion



Camera movement must have narrative purpose.



Possible purposes:



PUSH IN

→ importance / discovery



PULL OUT

→ context / reveal



PAN

→ exploration



ORBIT

→ dimensionality / product hero



CRANE / vertical movement

→ scale / elevation



MACRO PUSH

→ feature detail



Camera movement should not exist merely to make the shot feel cinematic.



Avoid arbitrary shake in clean product/UI presentations.



\---



\# 23. Camera and Legibility



Stylized perspective must not destroy information.



Dense interface:

prefer frontal or mild perspective.



Product hero:

perspective can become more dramatic.



Text-heavy UI:

prioritize legibility.



Feature close-up:

controlled side angle may establish depth.



Always ask:



Can the viewer still understand the product?



\---



\# 24. UI Motion



For software interfaces, motion should clarify state.



Good UI motion communicates:



\- where something came from

\- where something went

\- what changed

\- what is interactive

\- what deserves attention

\- how elements relate



Avoid:



\- excessive bounce

\- random rotation

\- unnecessary floating

\- simultaneous entrances

\- decorative movement that hides usability



\---



\# 25. Cinematic UI Motion



Cinematic UI can combine:



\- interface

\- camera

\- depth

\- lighting

\- shadows

\- parallax

\- macro framing

\- controlled reflections

\- spatial typography



But the UI must remain recognizable.



A product film is still communicating a product.



Do not sacrifice comprehension for spectacle.



\---



\# 26. Hero Reveal Pattern



Useful premium product reveal:



1\. establish dark/light environment

2\. isolate hero

3\. begin camera push

4\. hero enters or activates

5\. supporting depth appears

6\. secondary UI settles

7\. highlight reaches hero

8\. movement decelerates

9\. hold

10\. transition



Not every shot needs all ten steps.



Use them as a design vocabulary.



\---



\# 27. Feature Reveal Pattern



For a SaaS feature:



CONTEXT

→ TARGET

→ ACTION

→ RESPONSE

→ RESULT

→ HOLD



Example:



dashboard visible

→ analytics card emphasized

→ cursor activates filter

→ chart transforms

→ result number increases

→ camera holds on result



This is usually stronger than simply animating the card into frame.



\---



\# 28. Motion Metaphors



When many objects move, find a physical metaphor.



Examples:



cards

→ dealing / stacking



data

→ flowing / routing



notifications

→ queue / cascade



documents

→ layering / filing



connections

→ linking / branching



AI processing

→ propagation / pulse / convergence



A coherent metaphor produces more believable choreography than arbitrary animation.



\---



\# 29. Motion Restraint



One technique should not dominate every scene.



If one scene uses:



\- stacking



the next might use:



\- macro focus



then:



\- data flow



then:



\- spatial transition



then:



\- typography



Repetition should establish identity, not expose a template.



\---



\# 30. After Effects Translation



When implementing these principles in After Effects:



Easy Ease (`F9`) is a starting point, not automatically a finished result.



For a snappy UI-style move, a useful starting shape is:



Outgoing influence:

15–25%



Incoming influence:

80–90%



Velocity at rest:

0



This produces:



fast launch

→ long controlled settle



Use the Graph Editor to refine visually.



Do not confuse:



Value Graph

with

Speed Graph.



Temporal easing and spatial paths are separate problems.



\---



\# 31. After Effects Overshoot



A controlled overshoot can use:



START

→ PAST TARGET

→ TARGET



Example scale:



80%

→ 112%

→ 100%



Tune:



\- overshoot amount

\- time between overshoot and settle

\- easing influence



Do not automatically use 112%.



The correct amount depends on:



\- element size

\- brand personality

\- visual weight



\---



\# 32. After Effects Bounce



For hand-keyed bounce:



1\. impact

2\. rebound

3\. smaller impact

4\. smaller rebound

5\. settle



Amplitude should decay.



Time intervals should generally shrink.



Use only enough rebounds to communicate the physical behavior.



Product UI usually needs fewer rebounds than character animation.



\---



\# 33. Motion Diagnostic



\## Feels Robotic



Check:



\- linear movement

\- symmetric easing

\- simultaneous starts/stops

\- straight paths everywhere



Try:



\- stronger deceleration

\- stagger

\- follow-through

\- arc



\## Feels Floaty



Check:



\- duration too long

\- easing too gentle

\- excessive ambient movement

\- weak landing



Try:



\- shorter duration

\- sharper launch

\- stronger settle



\## Feels Cheap



Check:



\- everything moves

\- too many glows

\- excessive bounce

\- repeated effects

\- no hierarchy

\- constant camera movement



Try:



\- simplify

\- choose one hero

\- remove effects

\- introduce stillness



\## Feels Mechanical



Check:



\- no anticipation

\- no overlap

\- no secondary motion

\- identical durations



\## Feels Chaotic



Check:



\- competing hero motions

\- excessive stagger

\- camera + UI + text all moving strongly

\- effects responding to every beat



Reduce active motion layers.



\---



\# 34. SaaS / Product Motion Decision Matrix



\## User needs to notice a feature



Use:



\- focal isolation

\- camera push

\- controlled scale

\- supporting dim

\- feature activation



Avoid:



\- random fly-in



\## User needs to understand interaction



Use:



\- cursor/touch

\- human-readable timing

\- state transition

\- result hold



Avoid:



\- interaction faster than comprehension



\## User needs to feel premium quality



Use:



\- strong hierarchy

\- restrained motion

\- smooth deceleration

\- depth

\- precise typography

\- stillness



Avoid:



\- constant bouncing

\- excessive glow

\- camera shake



\## User needs energy



Use:



\- acceleration

\- fast stagger

\- strong transitions

\- rhythmic cuts

\- selected impacts



Avoid:



\- full-frame hit on every beat



\## User needs trust



Use:



\- stable camera

\- smooth transitions

\- predictable hierarchy

\- low overshoot

\- readable UI



\---



\# 35. Motion Design Workflow



For every important animation:



\## Step 1 — Intent



What must the viewer understand or feel?



\## Step 2 — Hero



What is the focal subject?



\## Step 3 — Start State



Where does the subject begin?



\## Step 4 — End State



What visual state communicates completion?



\## Step 5 — Path



Straight, arc, depth, orbit, scale, morph?



\## Step 6 — Timing



How much time does comprehension require?



\## Step 7 — Easing



How does energy enter and leave?



\## Step 8 — Secondary Motion



What reacts to the hero?



\## Step 9 — Sound



What sonic event reinforces the motion?



\## Step 10 — Hold



Does the viewer have time to read the result?



\---



\# 36. Quality Review



Before accepting motion, inspect:



\### Intent



Can I explain why the movement exists?



\### Hierarchy



Is there a clear hero?



\### Timing



Can the viewer follow the action?



\### Easing



Does the object accelerate/decelerate naturally?



\### Weight



Does size/distance correspond to timing?



\### Rhythm



Are movement and stillness contrasted?



\### Secondary Motion



Does support motion reinforce rather than compete?



\### Camera



Does movement improve the shot?



\### Legibility



Can UI and typography still be understood?



\### Restraint



Could removing an effect improve the scene?



\---



\# 37. Golden Rules



Motion is controlled change with purpose.



Do not animate everything.



Do not make everything arrive simultaneously.



Do not use one easing curve blindly.



Do not use one duration for every object.



Do not use camera movement without narrative purpose.



Do not sacrifice UI legibility for cinematic style.



Do not synchronize every visual property to every beat.



Do not confuse activity with quality.



Use stillness.



Use hierarchy.



Use acceleration.



Use controlled secondary motion.



Let important moments breathe.



The best motion feels inevitable rather than merely animated.

