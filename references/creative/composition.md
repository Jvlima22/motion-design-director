\# Composition System



\## Purpose



Define how elements are organized inside every frame before animation begins.



Composition determines:



\- where the viewer looks first

\- what feels important

\- how information is grouped

\- how depth is perceived

\- how motion has room to happen

\- how a shot survives different aspect ratios



Motion should reinforce composition, not repair it.



\---



\# 1. Core Principle



Every frame must have a clear visual hierarchy.



Ask:



1\. What is the hero?

2\. What supports the hero?

3\. What is merely texture?

4\. Where should the eye go first?

5\. Where should it go second?

6\. What can be removed?



Use:



HERO

→ SUPPORT

→ TEXTURE



Avoid multiple equally dominant focal points.



\---



\# 2. Hierarchy Order



Useful hierarchy controls:



1\. Size

2\. Contrast

3\. Color

4\. Position

5\. Depth

6\. Sharpness

7\. Motion

8\. Lighting



The strongest combination wins attention.



If the wrong object is attracting attention,

do not immediately animate the correct object more.



First reduce competition.



\---



\# 3. Grid System



For 16:9 product films and SaaS videos, use a 12-column grid as a useful starting point.



At 1920px width:



Outer margin:

80–120px



Columns:

12



Gutter:

24–32px



Formula:



content\_width =

frame\_width - (2 × margin)



column\_width =

(content\_width - ((columns - 1) × gutter)) / columns



Example:



frame = 1920

margin = 100

gutter = 24

columns = 12



content\_width = 1720



column\_width ≈ 121.3px



The grid is a construction system, not a visual prison.



Break it deliberately when the composition benefits.



\---



\# 4. Baseline Rhythm



For UI-based compositions, an 8px baseline system is a useful default.



Common spacing:



8

16

24

32

48

64

96

128



This helps create visual consistency between:



\- cards

\- labels

\- interface elements

\- typography

\- spacing

\- overlays

\- annotations



\---



\# 5. Focal Point



Every frame should have one primary focal point.



Useful starting positions:



33% / 33%

67% / 33%

33% / 67%

67% / 67%



These approximate rule-of-thirds intersections.



Use off-center composition when you want:



\- movement

\- progression

\- visual tension

\- space for typography

\- space for future animation



Use centered symmetry when you want:



\- authority

\- stillness

\- product heroism

\- logo reveal

\- monumentality

\- final payoff



Do not mechanically apply either.



\---



\# 6. Negative Space



Negative space is an active design element.



Use empty space to:



\- isolate the product

\- improve readability

\- increase perceived quality

\- create anticipation

\- prepare an entrance

\- accommodate typography

\- create asymmetry

\- direct attention



Avoid filling every region simply because space exists.



\---



\# 7. Visual Weight



Visual weight increases with:



\- size

\- brightness

\- contrast

\- saturation

\- sharpness

\- movement

\- proximity

\- dimensionality



Balance the frame by considering perceived weight rather than only physical size.



A small bright glowing object can outweigh a large dark panel.



\---



\# 8. Composition and Motion



Before animating an object, determine its destination composition.



Design:



START FRAME

→ KEY COMPOSITION

→ END FRAME



not merely:



OBJECT

→ ANIMATION



The strongest key frames should work as still images.



\---



\# 9. Motion Distance



Avoid making interface elements travel huge distances without reason.



For large movement across the frame, consider:



\- intermediate composition

\- camera movement

\- scale transformation

\- masking

\- transition

\- opacity hierarchy



Long arbitrary travel often feels mechanical.



\---



\# 10. Depth Layers



Use three conceptual layers:



BACKGROUND

MIDGROUND

FOREGROUND



Map them to:



AMBIENT

SECONDARY

PRIMARY



Typical starting parallax relationships:



BACKGROUND

0.1–0.3×



MIDGROUND

0.5–0.7×



FOREGROUND

1.0–1.5×



These are relationships, not fixed constants.



\---



\# 11. Background Layer



Background should normally have:



\- lowest contrast

\- slowest motion

\- lowest information density

\- softer focus

\- reduced saturation when appropriate



Examples:



\- gradient

\- texture

\- environment

\- subtle grid

\- distant UI

\- atmospheric light

\- particles



Background supports context.



It should rarely become the accidental hero.



\---



\# 12. Midground Layer



Midground commonly contains:



\- product environment

\- supporting UI

\- secondary cards

\- labels

\- diagrams

\- feature context



It should help explain the hero without competing with it.



\---



\# 13. Foreground Layer



Foreground can contain:



\- hero product

\- primary UI

\- device

\- dimensional object

\- intentionally passing depth element



Foreground may move faster to reinforce depth.



Foreground objects crossing the camera can use:



\- motion blur

\- defocus

\- partial framing



but should not destroy product legibility.



\---



\# 14. Overlap



Overlap is one of the easiest ways to create depth.



Instead of:



object

object

object



with equal spacing,



allow controlled overlap.



Examples:



device overlapping text region slightly



floating card partially leaving frame



foreground object masking a background object



UI card extending beyond device boundary during transformation



Overlap should look intentional.



\---



\# 15. Cropping



Objects do not always need to fit completely inside the frame.



Intentional cropping can make scenes feel larger and more cinematic.



Useful for:



\- device hero shots

\- oversized typography

\- interface close-ups

\- foreground props

\- large logos

\- dimensional objects



Never crop important information accidentally.



\---



\# 16. Scale Contrast



Avoid making every object approximately the same size.



Create relationships such as:



LARGE HERO

\+

MEDIUM SUPPORT

\+

SMALL DETAIL



Scale contrast strengthens hierarchy.



\---



\# 17. UI Composition



For software/product videos, distinguish between:



PRODUCT UI



and



VIDEO COMPOSITION.



Do not simply place a full screenshot in the middle of the frame for every shot.



Possible treatments:



\- full product

\- cropped interface

\- isolated feature

\- enlarged component

\- floating card

\- exploded interface

\- layered screens

\- device mockup

\- macro UI detail

\- spatial UI environment



Choose based on the message.



\---



\# 18. Product Hero Composition



When introducing the product:



prioritize recognition before complexity.



Good initial hero treatments:



\- clean frontal interface

\- device with mild perspective

\- product emerging from darkness

\- controlled scale reveal

\- environment reveal

\- UI floating in depth



Avoid immediately exploding the interface before viewers understand what they are seeing.



\---



\# 19. Feature Composition



When demonstrating one feature:



remove irrelevant UI when possible.



Use:



FEATURE

→ SUPPORTING CONTEXT



not:



ENTIRE APPLICATION

→ tiny highlighted button



If necessary:



zoom

crop

isolate

dim

blur

recompose



to make the feature visually dominant.



\---



\# 20. Data Composition



For metrics and charts:



make the data the hero.



Reduce:



\- decorative objects

\- background movement

\- unnecessary labels

\- competing color



Preserve:



\- scale

\- relationships

\- values

\- context

\- legibility



\---



\# 21. Typography + Product



Typography and product should share the composition.



Useful structures:



TEXT | PRODUCT



PRODUCT | TEXT



TEXT

PRODUCT



PRODUCT

TEXT



TEXT BEHIND PRODUCT



TEXT IN ENVIRONMENT



Avoid automatically placing headline top-center and product center-bottom.



Choose a layout based on narrative intent.



\---



\# 22. Leading Space



When a subject moves horizontally,

leave more space in the direction of movement.



When the camera follows a moving subject,

frame the subject slightly toward the trailing side.



This creates visual room for progression.



\---



\# 23. Directional Continuity



Maintain spatial logic between shots.



If the product exits right,

the next shot can continue the energy from the left.



If the camera pushes into a feature,

the next shot should feel spatially related to that feature.



Avoid arbitrary directional changes unless used intentionally for disruption.



\---



\# 24. Safe Areas



Critical elements include:



\- logo

\- CTA

\- important text

\- faces

\- important metrics

\- essential product controls



Keep them away from unsafe platform regions.



Starting heuristics:



16:9

≈ 5% protection



1:1

≈ 6–8%



4:5

≈ 6–8%



9:16

requires stronger top and bottom protection.



Always verify against the actual destination platform.



\---



\# 25. 16:9 → 9:16



Do not simply crop.



RESTACK.



Example:



16:9



TEXT        PRODUCT



can become:



9:16



TEXT



PRODUCT



SUPPORT



Potential adaptations:



\- reduce secondary cards

\- enlarge headline

\- move hero vertically

\- change camera framing

\- simplify background

\- reposition CTA

\- alter typography wrapping



Preserve hierarchy, not coordinates.



\---



\# 26. Composition Density



Control how much information exists simultaneously.



LOW DENSITY



Useful for:



\- hooks

\- hero moments

\- premium branding

\- logo reveal

\- CTA



MEDIUM DENSITY



Useful for:



\- feature explanation

\- UI demo

\- product context



HIGH DENSITY



Useful selectively for:



\- ecosystem reveal

\- dashboard overview

\- complexity payoff



Do not maintain maximum density throughout the entire video.



\---



\# 27. Reveal Complexity Gradually



A strong product sequence can progress:



ONE OBJECT

→ PRODUCT

→ FEATURE

→ RELATED COMPONENTS

→ SYSTEM

→ ECOSYSTEM



This allows complexity to feel earned.



\---



\# 28. Composition Before Effects



Never solve weak framing by adding:



\- glow

\- particles

\- blur

\- lens effects

\- camera shake

\- more animation



First solve:



\- hierarchy

\- alignment

\- spacing

\- scale

\- depth

\- negative space



Effects come afterward.



\---



\# 29. Frame Test



Freeze the animation.



Ask:



Can I understand what matters without seeing it move?



If not, improve the composition.



Perform this check at:



START

MID

PEAK

END



for important shots.



\---



\# 30. Squint Test



Reduce visual detail mentally or physically.



Ask:



What shape/region dominates the frame?



It should correspond to the intended hero.



If background decoration dominates,

the hierarchy is broken.



\---



\# 31. Thumbnail Test



View the frame very small.



Important hierarchy should still survive.



This is particularly useful for:



\- bold product reveals

\- title frames

\- brand moments

\- CTA frames



\---



\# 32. Common Failure: Dashboard Dump



Problem:



full dashboard

\+

many labels

\+

many animations

\+

camera movement.



Result:



viewer does not know where to look.



Fix:



isolate one task or feature at a time.



\---



\# 33. Common Failure: Floating Card Soup



Problem:



many random floating cards around a device.



Result:



generic SaaS aesthetic without meaning.



Fix:



each floating component must represent:



\- feature

\- input

\- output

\- relationship

\- result



Otherwise remove it.



\---



\# 34. Common Failure: Center Everything



Problem:



every shot has product perfectly centered.



Result:



repetitive rhythm.



Fix:



alternate deliberately between:



\- centered hero

\- asymmetric feature shot

\- close-up

\- split composition

\- spatial composition



while maintaining visual consistency.



\---



\# 35. Common Failure: No Breathing Room



Problem:



every region contains content.



Fix:



remove 20–40% of nonessential visual information and reevaluate.



\---



\# 36. Composition Checklist



Before approving a shot:



\[ ] One clear hero



\[ ] Support elements are subordinate



\[ ] Background is not competing



\[ ] Negative space exists



\[ ] Grid/alignment feels intentional



\[ ] Product remains readable



\[ ] Typography has hierarchy



\[ ] Depth has a purpose



\[ ] Cropping is intentional



\[ ] Movement has room



\[ ] Important content is safe



\[ ] Composition works when frozen



\[ ] Composition can adapt to target aspect ratio



\---



\# Golden Rule



A premium motion-design frame should already feel designed when paused.



Animation should make a strong composition more meaningful,

not make a weak composition tolerable.

