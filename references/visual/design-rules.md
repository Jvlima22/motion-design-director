\# Visual Design Rules



\## Purpose



Define the visual system used by motion-design projects before effects and

animation polish are added.



The objective is not to make every frame visually complex.



The objective is to create:



CLARITY

\+

HIERARCHY

\+

BRAND

\+

DEPTH

\+

CONSISTENCY

\+

POLISH



Visual design must support the product and the story.



\---



\# 1. Visual Decision Order



Always decide visual direction in this order:



BRAND

→ MOOD

→ BASE

→ HERO COLOR

→ ACCENT

→ NEUTRALS

→ TYPOGRAPHY

→ SURFACES

→ DEPTH

→ LIGHT

→ BACKGROUND

→ EFFECTS



Do not begin with glow, particles or gradients.



\---



\# 2. Restrained Palette



Strong product motion usually needs fewer colors than expected.



Useful structure:



1 BASE

\+

1 HERO COLOR

\+

1 OPTIONAL ACCENT

\+

2–3 NEUTRALS



Create richness through:



\- lightness

\- chroma

\- opacity

\- depth

\- texture

\- illumination



rather than continuously adding new hues.



\---



\# 3. Color Hierarchy



Color directs attention.



The strongest accent should normally correspond to:



\- hero feature

\- important metric

\- active state

\- CTA

\- key brand moment



If every object uses the hero color,

nothing is visually heroic.



\---



\# 4. 60 / 30 / 10



Useful heuristic:



60%

dominant environment/base



30%

secondary surfaces



10%

accent/hero



This is not a mathematical requirement.



It is a hierarchy principle.



\---



\# 5. Hero Color Budget



Try to keep one dominant hero-color event per frame.



Exceptions are allowed when brand or composition requires otherwise.



Before adding another accent ask:



Does this improve hierarchy?



If not, use a neutral or derived tone.



\---



\# 6. Dark Interfaces



Avoid relying entirely on:



\#000000



Use subtly tinted dark values to create depth.



Possible structure:



BACKGROUND

near-black



SURFACE 1

slightly lighter



SURFACE 2

another small step



BORDER

low-opacity light



TEXT PRIMARY

near-white



TEXT SECONDARY

muted



HERO

brand color



This creates depth without excessive shadows.



\---



\# 7. Light Interfaces



Avoid pure white everywhere.



Create subtle separation between:



BACKGROUND

SURFACE

CARD

BORDER



Use:



\- warm/cool off-whites

\- subtle gray

\- restrained shadow

\- small contrast steps



A premium light interface should not look like an empty white document.



\---



\# 8. Contrast



Contrast should establish hierarchy.



Use contrast intentionally between:



HERO vs BACKGROUND



PRIMARY TEXT vs SECONDARY TEXT



ACTIVE vs INACTIVE



FOREGROUND vs BACKGROUND



Avoid maximum contrast everywhere.



If everything is high contrast,

nothing has hierarchy.



\---



\# 9. Color and Depth



Objects farther away can use:



\- lower contrast

\- lower saturation

\- lower opacity

\- softer focus



Objects closer to the viewer can use:



\- higher contrast

\- stronger detail

\- sharper edges



This reinforces spatial hierarchy.



\---



\# 10. Color Interpolation



For animated color transitions,

prefer perceptually uniform color spaces where supported:



OKLCH

OKLab

Lab



Avoid blindly interpolating saturated colors directly in RGB.



Check transition midpoints for:



\- gray/muddy colors

\- unwanted hue shifts

\- uneven brightness

\- banding



\---



\# 11. Gradient Construction



A premium gradient should normally be controlled rather than rainbow-like.



Useful structures:



BASE

\+

RADIAL HERO LIGHT



BASE

\+

2–3 LARGE RADIAL FIELDS



SUBTLE MESH

\+

GRAIN



AURORA

\+

DARK SCRIM



Avoid adding many saturated stops without a reason.



\---



\# 12. Gradient Movement



For ambient gradients:



prefer slow movement.



Useful starting loop range:



8–30 seconds



Background movement should usually be slower than foreground movement.



The viewer should feel the environment is alive without actively watching it.



\---



\# 13. Gradient Banding



If gradients show visible bands:



consider:



\- higher bit depth

\- subtle noise/grain

\- better interpolation

\- smoother lightness transitions

\- reducing extreme gradients



Grain can hide banding,

but should not become visually dominant.



\---



\# 14. Glow



Glow is an attention mechanism.



Good uses:



\- active AI state

\- selected feature

\- CTA

\- important data

\- logo payoff

\- energy source



Avoid glowing every element.



A useful principle:



ONE HERO GLOW

>

MANY SMALL GLOWS



\---



\# 15. Glow Layers



Instead of one huge blur,

build glow with controlled layers.



Example concept:



CORE

sharp bright source



INNER GLOW

small radius



OUTER GLOW

large low-opacity radius



AMBIENT SPILL

very subtle environmental influence



This creates more believable illumination.



\---



\# 16. Bloom



Bloom should affect genuinely bright elements.



Avoid applying strong bloom globally.



Excessive bloom:



\- reduces sharpness

\- damages UI legibility

\- makes dark scenes hazy

\- creates generic neon aesthetics



Use it selectively.



\---



\# 17. Shadows



Shadows communicate:



\- elevation

\- separation

\- depth

\- hierarchy



Prefer subtle layered shadows over one heavy black shadow.



For dark scenes,

consider colored environmental shadow/light relationships.



For light scenes,

use restrained neutral shadows.



\---



\# 18. Borders



Borders are useful for dark SaaS UI.



Prefer:



low-opacity borders



instead of:



bright solid outlines everywhere.



Borders should define structure,

not become decoration.



\---



\# 19. Glass



Glassmorphism should be used when it supports depth.



Useful ingredients:



\- transparency

\- backdrop blur

\- subtle border

\- environmental tint

\- controlled highlight



Avoid:



many translucent floating cards with no narrative purpose.



Glass is a material,

not a substitute for composition.



\---



\# 20. Surface Hierarchy



Define a limited elevation system.



Example:



LEVEL 0

background



LEVEL 1

base surface



LEVEL 2

card



LEVEL 3

floating feature



LEVEL 4

hero overlay



Do not invent a different shadow/material treatment for every component.



\---



\# 21. Typography System



Use a small typographic system.



Typical roles:



DISPLAY

HEADLINE

BODY

LABEL

METRIC

CAPTION



Avoid excessive font-family variation.



Usually:



one display family

\+

one supporting sans



is sufficient.



\---



\# 22. Hero Typography



Hero typography can use:



\- strong weight

\- tight tracking

\- controlled line-height

\- large scale

\- selective color

\- dimensional interaction



Starting direction:



weight:

600–800



tracking:

approximately -0.01em to -0.04em for large display text



line height:

tight but readable



Adjust according to typeface.



\---



\# 23. Body Typography



Body/caption text should prioritize readability.



Prefer:



\- regular/medium weight

\- controlled width

\- comfortable line height

\- reduced visual emphasis



Do not animate body text aggressively.



\---



\# 24. Metrics



Numbers often need their own treatment.



Use:



\- tabular numerals when appropriate

\- clear units

\- strong hierarchy

\- stable alignment

\- restrained animation



Metrics communicate credibility.



Avoid excessive bounce or overshoot.



\---



\# 25. Highlight One Idea



Within a headline,

usually emphasize one meaningful phrase or word.



Possible methods:



\- hero color

\- weight

\- underline

\- pill

\- mask

\- subtle glow

\- kinetic transformation



If several words are highlighted,

hierarchy weakens.



\---



\# 26. Text Animation



Typography animation should reflect meaning.



Possible approaches:



REVEAL

for introduction



MASK

for precision



STAGGER

for rhythm



TRACKING

for expansion



SCALE

for emphasis



COLOR

for semantic change



MORPH

for transformation



Do not use character-by-character animation merely because it is available.



\---



\# 27. Background Roles



Background can be:



STATIC

LIVING

CINEMATIC



Choose intentionally.



\---



\# 28. Static Background



Best for:



\- dense dashboard

\- charts

\- text-heavy scenes

\- interaction demos

\- already-complex motion



Static background gives motion somewhere to contrast against.



\---



\# 29. Living Background



Possible techniques:



\- mesh gradient

\- slow radial movement

\- grain

\- subtle particles

\- faint grid

\- low-frequency light movement



Motion should remain subordinate.



\---



\# 30. Cinematic Background



Possible techniques:



\- shader

\- volumetric lighting

\- dimensional geometry

\- strong depth

\- environmental particles

\- atmospheric haze



Use when environment participates in storytelling.



Do not automatically use it for every SaaS shot.



\---



\# 31. Background Technique Selection



If a simple gradient achieves the visual goal:



use CSS/basic gradients.



If organic flow is required:



consider shader/noise.



If network/data atmosphere is required:



consider particles/constellation.



If depth is required:



consider parallax.



Choose the least complex technique that achieves the intended visual result.



\---



\# 32. Background Readability



Foreground always wins.



If background reduces text readability:



\- reduce contrast

\- reduce saturation

\- reduce movement

\- add scrim

\- reposition light

\- blur background

\- darken local region



Never sacrifice communication for background spectacle.



\---



\# 33. Grain



Grain can:



\- reduce gradient banding

\- unify elements

\- add texture

\- make digital gradients feel less sterile



Use subtly.



If viewers consciously notice the grain,

it may be too strong.



\---



\# 34. Noise



Noise can drive:



\- gradients

\- displacement

\- particles

\- masks

\- distortion

\- organic movement



But visible noise should have a visual purpose.



Avoid adding random noise to every layer.



\---



\# 35. Lighting



Think of digital scenes as having lighting.



Possible lights:



KEY

main illumination



FILL

softens contrast



RIM

separates hero from background



ACCENT

brand-colored highlight



ENVIRONMENT

ambient scene light



This mental model improves dimensional UI scenes.



\---



\# 36. UI Lighting



For floating UI:



use lighting to reinforce hierarchy.



Hero card:



slightly stronger illumination.



Supporting card:



lower contrast.



Background UI:



darker / softer.



Avoid giving every card identical brightness.



\---



\# 37. Reflections



Reflections can increase perceived material quality on:



\- devices

\- glass surfaces

\- 3D logos

\- polished UI panels



Keep reflections controlled.



Do not let them cross important text at high intensity.



\---



\# 38. Blur



Blur has several roles:



DEPTH BLUR

spatial separation



MOTION BLUR

velocity



BACKGROUND BLUR

focus



TRANSITION BLUR

continuity



GLOW BLUR

light diffusion



Use the correct type for the correct purpose.



\---



\# 39. Motion Blur



Motion blur should correspond to velocity.



Fast object:

more blur may be justified.



Slow UI:

minimal blur.



Important text:

preserve readability.



Do not use motion blur simply to hide poor animation.



\---



\# 40. Depth of Field



Depth of field can isolate the hero.



Useful for:



\- cinematic device shots

\- dimensional UI

\- foreground transitions



Avoid strong DOF while viewers need to read multiple interface elements.



\---



\# 41. Particles



Particles should represent something.



Possible metaphors:



DATA

ENERGY

NETWORK

PROCESSING

ATMOSPHERE

CONNECTION



Avoid meaningless particle clouds.



Use:



fewer particles

\+

clear behavior



instead of visual noise.



\---



\# 42. Data Lines



Connection lines can represent:



\- automation

\- data flow

\- relationships

\- integrations

\- AI reasoning

\- system architecture



Control:



\- thickness

\- opacity

\- direction

\- pulse

\- speed



Lines should explain structure.



\---



\# 43. Grid Backgrounds



Grid backgrounds communicate:



\- technology

\- systems

\- precision

\- spatial environment



Use subtle contrast.



Do not let grid intersections compete with interface text.



\---



\# 44. Vignette



A subtle vignette can:



\- focus attention

\- darken unsafe edges

\- increase depth

\- unify composition



Avoid obvious black circular borders.



\---



\# 45. Chromatic Effects



Chromatic aberration can communicate:



\- digital disruption

\- glitch

\- speed

\- transition



Use sparingly.



Usually inappropriate as a constant effect for premium SaaS.



\---



\# 46. Glitch



Glitch should have narrative meaning.



Useful for:



\- error

\- disruption

\- transformation

\- cyber aesthetic

\- state change



Avoid random glitch transitions in products whose brand does not support them.



\---



\# 47. Premium Visual Language



Premium often means:



LESS

\+

BETTER CONTROL



Common characteristics:



\- restrained palette

\- large negative space

\- confident typography

\- precise alignment

\- limited glow

\- slow environmental movement

\- controlled depth

\- deliberate camera

\- strong hero

\- fewer simultaneous effects



Premium does not automatically mean dark mode.



\---



\# 48. Futuristic Visual Language



Futuristic does not automatically mean:



neon

\+

purple

\+

particles.



Other futuristic directions:



\- monochrome precision

\- translucent spatial systems

\- minimal white environments

\- technical typography

\- data architecture

\- intelligent motion

\- procedural geometry

\- adaptive interfaces



Choose based on brand.



\---



\# 49. AI Visual Language



Avoid defaulting every AI project to:



purple gradient

\+

glowing orb

\+

particle network.



Possible AI metaphors:



\- transformation

\- synthesis

\- branching

\- convergence

\- semantic relationships

\- adaptive UI

\- prediction

\- contextual layers

\- intelligent data flow



The visual metaphor should relate to the actual product.



\---



\# 50. SaaS Visual Language



For SaaS:



PRODUCT UI

is usually the most valuable visual asset.



Do not hide it behind decoration.



Use visual effects to:



\- isolate

\- elevate

\- clarify

\- connect

\- contextualize



the actual interface.



\---



\# 51. Visual Consistency



Across scenes preserve:



\- palette

\- typography

\- radius language

\- border language

\- shadow language

\- glow behavior

\- background behavior

\- depth system

\- icon style

\- illustration style



A video should feel like one visual system.



\---



\# 52. Contrast Across Scenes



Consistency does not mean every scene looks identical.



Create contrast through:



\- density

\- scale

\- camera distance

\- background intensity

\- typography size

\- amount of negative space



while maintaining the same design language.



\---



\# 53. Visual Restraint Pass



Before finalizing each shot ask:



Can I remove:



\- one glow?

\- one particle layer?

\- one gradient?

\- one card?

\- one color?

\- one shadow?

\- one line of text?



If removal improves hierarchy,

remove it.



\---



\# 54. Accessibility



Visual quality includes accessibility.



Maintain:



\- readable contrast

\- safe font sizes

\- clear hierarchy

\- reduced-motion alternatives when interactive

\- meaningful color usage



Do not rely exclusively on color to communicate critical states.



\---



\# 55. Performance



For real-time/browser visuals:



choose the least expensive solution that achieves the intended result.



Possible priority:



CSS

→ DOM/SVG

→ Canvas

→ WebGL



For WebGL:



cap excessive pixel density where appropriate.



Pause continuous animation when:



\- hidden

\- offscreen

\- reduced-motion is active



A dropped-frame "premium" background is not premium.



\---



\# 56. Frozen Frame Review



Review important scenes at:



START

MID

PEAK

END



Check:



\- hierarchy

\- contrast

\- gradient quality

\- banding

\- typography

\- UI legibility

\- accidental tangencies

\- glow intensity

\- background competition



The frame should work without motion.



\---



\# 57. Visual Quality Checklist



Before approval:



\[ ] Palette is restrained



\[ ] Hero color has hierarchy



\[ ] Typography system is consistent



\[ ] Product UI remains recognizable



\[ ] Background supports foreground



\[ ] Glow is selective



\[ ] Gradients are clean



\[ ] No muddy color transitions



\[ ] Shadows communicate depth



\[ ] Borders are controlled



\[ ] Blur has purpose



\[ ] Particles have meaning



\[ ] Lighting supports hierarchy



\[ ] Effects match brand



\[ ] Scene works when frozen



\[ ] Multi-aspect readability survives



\[ ] Performance is appropriate



\---



\# 58. Common Failure — Glow Everywhere



Problem:



everything glows.



Result:



nothing is important.



Fix:



reserve glow for the hero.



\---



\# 59. Common Failure — Generic AI Purple



Problem:



purple/blue gradient applied automatically.



Fix:



derive palette from brand and product meaning first.



\---



\# 60. Common Failure — Too Many Colors



Problem:



many saturated colors compete.



Fix:



return to:



BASE

\+

HERO

\+

ACCENT

\+

NEUTRALS



\---



\# 61. Common Failure — Decoration Before Product



Problem:



particles, gradients and 3D effects dominate the interface.



Fix:



make the product the hero.



\---



\# 62. Common Failure — Everything Is Glass



Problem:



every UI surface is translucent.



Fix:



create material hierarchy.



Glass should be one material option,

not the entire visual language.



\---



\# 63. Common Failure — Maximum Effects



Problem:



glow

\+ blur

\+ noise

\+ particles

\+ chromatic aberration

\+ lens flare

\+ gradient



all simultaneously.



Fix:



choose effects according to narrative function.



\---



\# 64. Visual Decision Matrix



\## Need Premium



Use:



\- restraint

\- negative space

\- precise typography

\- controlled depth

\- selective glow



\## Need Energy



Use:



\- stronger contrast

\- faster visual changes

\- bold scale relationships

\- selected high-intensity effects



\## Need Trust



Use:



\- stable hierarchy

\- readable UI

\- neutral surfaces

\- predictable color behavior



\## Need Futuristic



Use:



\- spatial depth

\- technical systems

\- procedural elements

\- controlled illumination



Do not automatically use neon.



\## Need AI



Use:



\- meaningful processing metaphor

\- relationships

\- transformation

\- adaptive behavior



Do not automatically use particles.



\---



\# 65. Golden Rule



Visual polish is not the number of effects applied.



Professional visual design is the control of:



COLOR

\+

TYPE

\+

SPACE

\+

DEPTH

\+

LIGHT

\+

MATERIAL

\+

CONTRAST

\+

HIERARCHY



Effects are only tools inside that system.



The product must remain the hero.

