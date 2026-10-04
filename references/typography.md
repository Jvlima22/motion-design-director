\# TYPOGRAPHY



Typography in motion design is not decoration.



Typography communicates hierarchy, meaning, rhythm, emphasis, personality, scale, and timing.



In product films, SaaS videos, application launches, AI demonstrations, explainers, social videos, and cinematic UI sequences, text must remain readable while participating in the motion system.



The objective is not to animate text because text can be animated.



The objective is to make the viewer:



1\. notice the right information;

2\. read it at the right moment;

3\. understand its hierarchy;

4\. connect it to the visual event;

5\. remember the intended message.



Use typography as a communication system first and a motion element second.



\---



\# CORE PRINCIPLE



Every text element must answer:



```text

WHAT MUST THE VIEWER UNDERSTAND?



→ WHAT IS THE ROLE OF THIS TEXT?

→ HOW IMPORTANT IS IT?

→ HOW LONG DOES IT NEED TO BE READ?

→ WHAT VISUAL EVENT DOES IT BELONG TO?

→ SHOULD THE TEXT LEAD OR SUPPORT THE SCENE?

→ WHAT SHOULD MOVE?

→ WHAT SHOULD REMAIN STABLE?

```



Never begin with:



```text

"What cool text animation can I use?"

```



Begin with:



```text

"What must this text accomplish?"

```



Meaning chooses hierarchy.



Hierarchy chooses composition.



Composition chooses motion.



Motion chooses implementation.



\---



\# TYPOGRAPHY DECISION CHAIN



Use this sequence:



```text

MESSAGE

→ TEXT ROLE

→ INFORMATION PRIORITY

→ HIERARCHY

→ TYPE COMPOSITION

→ SCALE

→ LINE STRUCTURE

→ EMPHASIS

→ REVEAL STRATEGY

→ MOTION BEHAVIOR

→ READING HOLD

→ EXIT

→ TRANSITION RELATIONSHIP

→ IMPLEMENTATION

→ RENDER VALIDATION

```



Do not skip directly from copy to animation.



\---



\# 1. IDENTIFY THE TEXT ROLE



Before designing the typography, classify the text.



Possible roles include:



```text

HERO

HEADLINE

SUBHEADLINE

SUPPORTING COPY

LABEL

EYEBROW

UI TEXT

METRIC

NUMBER

CAPTION

ANNOTATION

CTA

BRAND LINE

LOGO WORDMARK

LEGAL / AUXILIARY

```



Different roles require different visual behavior.



\---



\# HERO TEXT



Hero typography is one of the dominant visual objects of the shot.



Use it for:



\- product positioning;

\- primary promise;

\- major launch statement;

\- campaign message;

\- dramatic reveal;

\- section opening;

\- major numerical result.



Hero text can participate strongly in composition and camera movement.



It may:



\- occupy significant frame area;

\- interact with depth;

\- become partially masked;

\- reveal by word or phrase;

\- share composition with a hero device;

\- become the transition mechanism.



But readability remains mandatory.



Hero typography should not become visual noise merely because it is large.



\---



\# HEADLINE



A headline communicates the primary idea of a scene.



Prefer concise language.



For promotional/product motion, shorter headlines usually create stronger hierarchy than paragraph-like headlines.



When possible:



```text

ONE SCENE

→ ONE PRIMARY IDEA

→ ONE PRIMARY HEADLINE

```



Avoid multiple competing headline-sized elements.



\---



\# SUBHEADLINE



A subheadline supports the headline.



It should:



\- clarify;

\- qualify;

\- provide context;

\- explain benefit;

\- connect headline to product.



It should not visually compete with the headline.



Its motion should normally be quieter.



Example hierarchy:



```text

HEADLINE

strong reveal



SUBHEADLINE

slightly delayed

smaller motion amplitude

lower visual contrast

```



\---



\# SUPPORTING COPY



Supporting copy exists to explain rather than dominate.



Prioritize:



\- readability;

\- stable positioning;

\- sufficient reading duration;

\- simple entrance;

\- minimal movement while reading.



Avoid aggressive kinetic animation on long copy.



\---



\# LABEL / EYEBROW



Labels establish context.



Examples:



```text

AI AUTOMATION

NEW FEATURE

REAL-TIME

ANALYTICS

INTEGRATIONS

WORKFLOW

```



They can use:



\- uppercase;

\- tracking;

\- smaller scale;

\- accent color;

\- pill treatment;

\- restrained entrance.



Do not give labels more visual weight than the headline they introduce.



\---



\# UI TEXT



UI typography belongs to the interface first.



Preserve the visual truth of the product.



Do not arbitrarily enlarge, rewrite, reposition, or invent interface text if the video is demonstrating the real product.



When UI must be readable in video, prefer:



```text

camera framing

zoom

feature focus

magnification

crop

spotlight

```



before redesigning the product interface.



Product truth has priority.



\---



\# METRICS AND NUMBERS



Numbers behave differently from prose.



They may represent:



\- revenue;

\- growth;

\- conversion;

\- speed;

\- users;

\- percentage;

\- time;

\- performance;

\- AI confidence;

\- dashboard data.



For changing numbers, use tabular numerals when available:



```css

font-variant-numeric: tabular-nums;

```



This prevents digit-width changes from causing horizontal jitter.



A metric can become the hero of a scene when the number itself is the message.



Example:



```text

+37%

conversion

```



Hierarchy:



```text

NUMBER

→ strongest



UNIT / SYMBOL

→ attached



LABEL

→ supporting

```



Never animate a fabricated metric.



\---



\# CTA



CTA typography should be simple and unmistakable.



Examples:



```text

Start now

Try it

Book a demo

Explore the platform

Get started

```



Do not destroy CTA readability with an elaborate exit animation immediately after it appears.



Give the viewer time to process the action.



\---



\# 2. INFORMATION HIERARCHY



Typography must tell the viewer where to look.



Establish:



```text

PRIMARY

SECONDARY

TERTIARY

AUXILIARY

```



Hierarchy can be created with:



\- scale;

\- weight;

\- contrast;

\- position;

\- spacing;

\- opacity;

\- color;

\- timing;

\- motion amplitude;

\- depth;

\- focus.



Do not use all mechanisms simultaneously.



Strong hierarchy often requires fewer differences, not more.



\---



\# HIERARCHY RULE



At any important moment, the viewer should be able to answer:



```text

"What should I read first?"

```



without thinking.



If two elements compete equally, hierarchy is unresolved.



\---



\# 3. TYPE SCALE



Video typography should be designed for the viewing environment, not treated like webpage typography.



Consider:



\- composition resolution;

\- physical screen size;

\- mobile viewing;

\- platform UI overlays;

\- distance from viewer;

\- camera scale;

\- perspective;

\- final crop.



A value that seems large in CSS can become visually tiny after transforms.



Therefore:



```text

DECLARED FONT SIZE ≠ PERCEIVED FONT SIZE

```



Effective visible size can be affected by:



```text

font size

× ancestor scale

× camera distance

× perspective

× 3D rotation

× crop

× output scaling

```



Validate actual rendered frames.



\---



\# FALLBACK SCALE GUIDANCE



When brand specifications are unavailable, use large video-first typography.



Typical starting ranges for 1920×1080 product motion:



```text

HERO / MAIN HEADLINE

≈ 100–160 px



SUBHEADLINE

≈ 48–72 px



SUPPORTING / IMPORTANT BODY

≈ 32–48 px



AUXILIARY TEXT

≈ 24–32+ px

```



These are starting points, not universal laws.



Composition and viewing context determine the final size.



For vertical video, evaluate actual mobile readability.



Do not mechanically reuse desktop sizes.



\---



\# 4. TYPEFACE SELECTION



Typeface selection communicates personality before motion begins.



Possible signals:



```text

GEOMETRIC SANS

→ technology

→ precision

→ modern SaaS



GROTESK

→ contemporary

→ editorial

→ product-led



HUMANIST SANS

→ approachable

→ service-oriented

→ readable



SERIF / DISPLAY SERIF

→ editorial

→ premium

→ cultural

→ expressive



ROUNDED

→ friendly

→ playful

→ consumer



MONOSPACE

→ technical

→ developer

→ data

→ terminal

```



These are tendencies, not rigid meanings.



Brand identity overrides generic conventions.



\---



\# FONT CONSISTENCY



Prefer a coherent typography system.



For many product videos:



```text

1 PRIMARY FAMILY

\+

OPTIONAL SECONDARY DISPLAY FAMILY

```



is sufficient.



Avoid changing typeface simply to make each scene different.



Variety should come from:



\- scale;

\- composition;

\- timing;

\- weight;

\- motion;

\- layout.



not uncontrolled font switching.



\---



\# DISPLAY FACES



Hero typography benefits from deliberate display typography.



Do not accidentally rely on a system-default font when the visual identity requires something more intentional.



If no brand typeface exists, select a display face deliberately.



Possible open-source/free families may include geometric or grotesk display fonts, but availability and licensing must be verified for the actual project.



\---



\# FONT WEIGHT



Weight is hierarchy.



Typical relationship:



```text

HERO

600–800+



HEADLINE

600–800



SUPPORTING

400–600



LABEL

500–700

```



Use only weights actually available in the font.



Do not request `900` if the font only provides up to `800` and assume it will become heavier.



Validate the rendered result.



\---



\# 5. LANGUAGE AND GLYPH SUPPORT



A visually appropriate font is useless if it cannot render the copy.



Before production, verify support for:



\- Portuguese accents;

\- English;

\- Spanish;

\- Cyrillic;

\- Greek;

\- symbols;

\- currency;

\- mathematical characters;

\- punctuation;

\- required languages.



A missing glyph may silently cause fallback to another font.



That can break:



\- width;

\- alignment;

\- hierarchy;

\- animation;

\- brand consistency.



Never assume font coverage.



\---



\# FONT FALLBACK IS A PRODUCTION ERROR



If a specific brand/display font is required and the renderer silently substitutes another face, treat it as a production issue.



Check:



```text

EXPECTED FONT

vs.

ACTUAL RENDERED FONT

```



Especially for:



```text

After Effects

Remotion

render servers

different operating systems

multilingual copy

```



\---



\# 6. FONT LOADING



Fonts must be ready before text measurement and final rendering.



For Remotion:



```text

Google Fonts

→ @remotion/google-fonts



Local Fonts

→ @remotion/fonts

→ staticFile()

```



Load shared fonts centrally.



Conceptually:



```text

fonts.ts

→ load once

→ export family

→ reuse across compositions

```



Avoid loading the same font independently in every scene.



\---



\# REMOTION — GOOGLE FONT PATTERN



```tsx

import {loadFont} from '@remotion/google-fonts/Inter';



const {fontFamily} = loadFont();



export const FONT\_FAMILY = fontFamily;

```



Then:



```tsx

<div style={{fontFamily: FONT\_FAMILY}}>

&#x20; Product intelligence.

</div>

```



\---



\# REMOTION — LOCAL FONT PATTERN



```tsx

import {loadFont} from '@remotion/fonts';

import {staticFile} from 'remotion';



await loadFont({

&#x20; family: 'BrandFont',

&#x20; url: staticFile('fonts/BrandFont-Regular.woff2'),

});



export const FONT\_FAMILY = 'BrandFont';

```



Ensure the font file actually exists.



\---



\# FONT VALIDATION



Do not merely declare a font.



Verify it loaded.



When text measurement depends on it, use font-loading validation where supported.



A fallback font changes metrics.



That can cause:



```text

wrong line breaks

wrong centering

overflow

unexpected wrapping

misaligned masks

incorrect reveal widths

layout shifts

```



\---



\# 7. TEXT MEASUREMENT



Do not guess text dimensions when layout depends on them.



For Remotion, use layout measurement utilities when appropriate.



Concept:



```tsx

const {width, height} = measureText({

&#x20; text,

&#x20; fontFamily,

&#x20; fontSize,

&#x20; fontWeight,

});

```



The properties used for measurement must match the properties used for rendering.



If rendering uses:



```text

font family

font size

font weight

letter spacing

```



measurement must use the same relevant properties.



\---



\# MEASUREMENT RULE



```text

LOAD FONT

→ MEASURE

→ LAYOUT

→ ANIMATE

→ RENDER

→ VERIFY

```



Not:



```text

GUESS SIZE

→ ANIMATE

→ DISCOVER OVERFLOW DURING FINAL RENDER

```



\---



\# FITTING TEXT



When dynamic text must fit a constrained region, calculate the fit rather than manually guessing.



Concept:



```tsx

const {fontSize} = fitText({

&#x20; text,

&#x20; withinWidth,

&#x20; fontFamily,

&#x20; fontWeight,

});

```



Then apply an intentional maximum:



```tsx

const finalSize = Math.min(fontSize, maxHeroSize);

```



This prevents short copy from becoming absurdly large.



\---



\# OVERFLOW VALIDATION



For dynamic or generated copy, test whether text exceeds its box.



Important cases:



```text

AI-generated copy

user-generated data

localized text

dynamic product names

dashboard values

customer names

captions

```



Do not assume English dimensions will work for every language.



\---



\# 8. COMPOSITION



Typography is part of the frame architecture.



Consider:



```text

grid

safe area

hero object

device

UI

camera

negative space

depth

visual flow

```



Do not place text in leftover space after everything else has been composed.



Text and hero visual should be composed together.



\---



\# TYPOGRAPHY + PRODUCT HERO



Common composition:



```text

TEXT BLOCK

&#x20;     ↘



&#x20;       PRODUCT / DEVICE

```



The relationship may be:



```text

balanced

asymmetric

overlapping

layered

split-screen

foreground/background

```



The headline does not always need to be centered.



Use composition intentionally.



\---



\# SINGLE FOCAL POINT



Avoid:



```text

huge headline

\+

huge device

\+

huge logo

\+

huge metric

```



all competing simultaneously.



Decide the hero.



Possible hierarchy:



```text

DEVICE = HERO

headline = supporting



or



HEADLINE = HERO

device = supporting



or



METRIC = HERO

UI = evidence

```



\---



\# 9. LINE STRUCTURE



Line breaks are design decisions.



Avoid letting browser wrapping determine an important hero composition accidentally.



For controlled hero typography, decide:



```text

phrase structure

line count

line length

emphasis word

visual silhouette

```



Example:



```text

TURN LEADS

INTO CUSTOMERS

```



may communicate differently from:



```text

Turn leads into

customers

```



Line breaks affect rhythm and meaning.



\---



\# NO-WRAP



`whiteSpace: "nowrap"` can be appropriate when a headline must remain one visual unit.



But it is not universal.



Do not force no-wrap when it creates:



```text

overflow

tiny scaling

unsafe cropping

poor mobile adaptation

```



Use it only when composition requires it.



\---



\# 10. SPACING



Spacing affects perceived quality.



Control:



```text

letter spacing

line height

word spacing

element gap

paragraph spacing

```



Avoid blindly using `em` for layout gaps around large type.



An `em` value can resolve relative to a parent size that differs from the intended text size.



For precision motion layouts, explicit pixel or calculated composition-relative spacing can be safer.



\---



\# TRACKING



Tracking can communicate style.



Examples:



```text

WIDE TRACKING

→ labels

→ premium

→ technical

→ restrained



TIGHT TRACKING

→ large display headlines

→ impact

→ density

```



Do not sacrifice legibility.



\---



\# 11. EMPHASIS



Emphasis should reveal meaning.



Possible methods:



```text

COLOR

WEIGHT

SCALE

UNDERLINE

HIGHLIGHT

PILL

CIRCLE

BOX

BRACKET

MASK

POSITION

MOTION

TIMING

```



Usually emphasize one semantic target rather than decorating every word.



\---



\# ONE-WORD EMPHASIS



A useful default for short promotional headlines:



```text

highlight one important word

```



Example:



```text

Turn leads into CUSTOMERS.

```



Possible treatments:



```text

accent color

animated underline

highlight sweep

pill

weight change

subtle scale

```



Do not mechanically highlight one word if the sentence has no meaningful semantic emphasis.



Meaning decides emphasis.



\---



\# ANNOTATIONS



Hand-drawn or annotation-style emphasis can use:



```text

highlight

circle

underline

strike-through

crossed-off

box

bracket

```



Use when the visual language supports it.



Avoid annotation styling in a highly minimal premium composition unless intentionally contrasted.



\---



\# REMOTION ANNOTATION MOTION



Animation progress should remain deterministic.



Concept:



```tsx

const progress = interpolate(

&#x20; frame,

&#x20; \[start, end],

&#x20; \[0, 1],

&#x20; {

&#x20;   extrapolateLeft: 'clamp',

&#x20;   extrapolateRight: 'clamp',

&#x20; }

);

```



Then drive the annotation from `progress`.



The annotation should reinforce the word, not obscure it.



\---



\# 12. TYPOGRAPHY MOTION ROLES



Typography can behave in three primary ways:



```text

A. TYPOGRAPHY AS HERO

B. TYPOGRAPHY AS SUPPORT

C. TYPOGRAPHY AS INTERFACE

```



Do not animate all three identically.



\---



\# A. TYPOGRAPHY AS HERO



Use when the words themselves are the visual event.



Examples:



```text

launch statement

brand manifesto

campaign line

title sequence

kinetic typography

major statistic

```



Motion may include:



```text

large spatial travel

word stagger

line stagger

mask reveals

scale

camera interaction

depth

character animation

morph-like transitions

```



Because typography is the hero, it can own more screen space and motion energy.



\---



\# B. TYPOGRAPHY AS SUPPORT



Use when another element is the hero:



```text

device

UI

dashboard

3D object

product footage

visual demonstration

```



Text motion should support the visual.



Prefer:



```text

small translation

opacity

mask reveal

short stagger

subtle spring

```



Do not make the viewer choose between watching the product action and deciphering elaborate text animation.



\---



\# C. TYPOGRAPHY AS INTERFACE



UI typography should feel connected to product behavior.



Examples:



```text

button labels

cards

notifications

table values

dashboard metrics

AI response

search result

```



Animation should generally follow interface logic.



Examples:



```text

card enters

→ text belongs to card



notification appears

→ label appears with notification



number updates

→ digits animate



AI result streams

→ text reveal reflects generation

```



Avoid treating every UI label like cinematic kinetic typography.



\---



\# 13. REVEAL STRATEGIES



Choose reveal based on message and role.



Possible patterns:



```text

WHOLE BLOCK

LINE BY LINE

WORD BY WORD

CHARACTER BY CHARACTER

MASK REVEAL

CLIP REVEAL

FADE + TRANSLATE

SCALE + FADE

BLUR → SHARP

TRACKING SETTLE

TYPE-ON

HIGHLIGHT REVEAL

DEPTH REVEAL

```



\---



\# WHOLE-BLOCK REVEAL



Best for:



```text

short supporting copy

labels

CTA

simple premium compositions

```



Usually clean and fast.



\---



\# LINE-BY-LINE



Best for:



```text

two-line hero statements

editorial titles

structured messaging

```



Can create hierarchy between phrases.



\---



\# WORD-BY-WORD



Best for:



```text

short headline

kinetic type

spoken emphasis

progressive semantic reveal

```



Use stagger intentionally.



Do not turn a long paragraph into dozens of animated word events.



\---



\# CHARACTER-BY-CHARACTER



Use sparingly.



Appropriate for:



```text

terminal

code

typing

AI generation

specific title treatment

```



Usually inappropriate for ordinary product headlines when it slows reading.



\---



\# MASK REVEAL



Useful for:



```text

premium headline

clean product launch

editorial motion

directional movement

```



Text can enter from behind an invisible or visible boundary.



Direction should agree with scene motion.



\---



\# BLUR TO SHARP



Useful for:



```text

AI

search

focus

recognition

premium atmospheric reveals

```



Keep blur restrained.



Text must become crisp quickly enough to read.



\---



\# TRACKING SETTLE



Characters begin with wider tracking and converge.



Useful for:



```text

brand intro

premium title

technology

logo-adjacent typography

```



Avoid extreme tracking that damages recognition.



\---



\# TYPE-ON



Use when typing itself communicates something:



```text

search

command

chat

AI prompt

terminal

form entry

```



Do not use type-on merely because the content contains text.



\---



\# 14. WORD-BY-WORD REVEAL



Word-by-word reveals should follow semantic rhythm.



Bad:



```text

every word

same delay

same movement

same importance

```



Better:



```text

group words by phrase

emphasize meaningful word

allow important phrase to hold

```



Example:



```text

Automate

your entire

SALES PIPELINE

```



The final phrase may receive:



```text

greater scale

accent

longer hold

stronger landing

```



\---



\# 15. STAGGER



Stagger communicates sequence.



It should not feel like a mechanical loop.



Possible stagger structures:



```text

CONSTANT

ACCELERATING

DECELERATING

PHRASE-BASED

SEMANTIC

BEAT-BASED

```



For text, semantic stagger is often stronger than purely mathematical stagger.



\---



\# 16. READING TIME



Animation duration and reading duration are different.



A headline can finish entering in 500 ms but still require additional time to read.



Think:



```text

ENTER

→ SETTLE

→ READ

→ EXIT

```



Do not immediately exit text when its entrance animation finishes.



\---



\# READING HOLD



The more complex the message, the longer the hold.



Consider:



```text

word count

language

font complexity

contrast

motion around text

viewer familiarity

platform

screen size

```



A three-word headline can hold less than a two-line explanatory sentence.



\---



\# 17. MOTION AMPLITUDE



Text motion amplitude should correspond to role.



Example:



```text

HERO

larger movement



HEADLINE

moderate movement



SUBHEADLINE

smaller movement



LABEL

minimal movement



BODY

very minimal



UI TEXT

attached to parent UI motion

```



This creates motion hierarchy as well as visual hierarchy.



\---



\# 18. DIRECTIONAL LOGIC



Typography should respect scene vectors.



If the camera and UI move left-to-right, arbitrary right-to-left text movement may create unnecessary conflict.



Possible relationships:



```text

SAME DIRECTION

→ continuity



OPPOSITE DIRECTION

→ deliberate counter-motion



PERPENDICULAR

→ separation / new layer



DEPTH

→ foreground/background relationship

```



Counter-motion should be intentional.



\---



\# 19. TYPOGRAPHY AND CAMERA



Text may exist:



```text

SCREEN-LOCKED

WORLD-LOCKED

OBJECT-LOCKED

CAMERA-RELATIVE

```



Choose intentionally.



\---



\# SCREEN-LOCKED TEXT



Remains fixed to the frame.



Useful for:



```text

headline overlays

captions

CTA

labels

editorial information

```



Camera movement occurs behind it.



\---



\# WORLD-LOCKED TEXT



Text exists in the scene's spatial world.



Useful for:



```text

cinematic titles

3D environments

spatial product storytelling

architecture

ecosystem visualization

```



Perspective affects perceived text size.



Validate rendered readability.



\---



\# OBJECT-LOCKED TEXT



Text belongs to an object.



Examples:



```text

callout attached to device

label attached to node

annotation attached to UI

metric attached to card

```



Movement should preserve that relationship.



\---



\# 20. DEPTH



Typography can participate in depth through:



```text

parallax

scale

blur

occlusion

perspective

z-position

camera focus

```



But depth must not destroy readability.



Avoid unnecessary perspective distortion on informational text.



\---



\# 21. TYPOGRAPHY + CINEMATIC UI



When typography accompanies cinematic UI:



```text

UI = evidence

TEXT = interpretation

```



or:



```text

TEXT = promise

UI = proof

```



Determine which relationship applies.



Example:



```text

"Qualify every lead automatically."

&#x20;       ↓

UI demonstrates qualification.

```



Do not simultaneously make the headline, UI, cursor, camera, particles, and annotations compete for attention.



Sequence attention.



\---



\# 22. TYPOGRAPHY + FEATURE FOCUS



Useful pattern:



```text

HEADLINE

→ establishes benefit



FEATURE FOCUS

→ demonstrates feature



SUPPORT TEXT

→ clarifies outcome

```



Text should help the viewer understand what the highlighted feature means.



\---



\# 23. TYPOGRAPHY + DATA



For data-driven scenes:



```text

NUMBER

→ RESULT



LABEL

→ MEANING



CHART / UI

→ EVIDENCE

```



Do not animate data merely as decoration.



Use stable numerical alignment.



For changing digits:



```css

fontVariantNumeric: "tabular-nums"

```



\---



\# 24. TYPOGRAPHY + SOUND



Typography and sound should share event logic.



Possible pairings:



```text

WORD LANDING

→ subtle impact



MASK SWEEP

→ soft whoosh



TYPE-ON

→ restrained typing texture



HIGHLIGHT

→ tick / sparkle



HERO STATEMENT

→ musical accent



CTA

→ subtle confirmation

```



Do not add sound to every word.



Sound hierarchy should follow typography hierarchy.



Detailed decisions belong to:



```text

references/audio/sound-design.md

references/audio/beat-sync.md

references/audio/sfx-language.md

references/audio/audio-motion-sync.md

```



\---



\# 25. TYPOGRAPHY + BEAT



Beat-synced typography does not mean every word must land on every beat.



Use musical hierarchy.



Possible structure:



```text

phrase begins

→ beat



important word

→ accent



hero word

→ downbeat / major hit



support copy

→ between accents



exit

→ phrase boundary

```



Use the audio modules for frame-accurate synchronization.



\---



\# 26. TYPOGRAPHY TRANSITIONS



Text can participate in transitions.



Examples:



```text

WORD MATCH CUT

LETTER SHAPE MATCH

MASK EXPANSION

TEXT WIPE

SCALE THROUGH

DEPTH PASS

BLUR TRANSFER

COLOR FIELD TRANSITION

```



A transition should connect ideas, not merely decorate the cut.



\---



\# 27. RESPONSIVE TYPOGRAPHY



A composition designed for 16:9 should not simply be cropped to 9:16.



Recompose.



Possible vertical adaptation:



```text

16:9

headline left

device right



9:16

headline top

device center/below

```



Re-evaluate:



```text

font size

line breaks

safe zones

CTA position

device scale

hierarchy

```



Vertical video often benefits from larger relative type.



\---



\# 28. SAFE AREAS



Account for platform UI.



Especially in vertical video, avoid placing essential text where interface controls or captions may cover it.



Keep critical information inside a safe visual region.



Do not assume the entire 1080×1920 canvas is equally usable.



\---



\# 29. COPY LENGTH



Motion design cannot rescue weak copy hierarchy.



For hero text, prefer concise language.



A useful promotional default:



```text

3–5 WORD HEADLINE

```



when the message allows it.



This is not a universal rule.



Complex products may require longer explanation.



When copy becomes long:



```text

reduce animation complexity

increase reading hold

improve hierarchy

split information across scenes

```



Do not simply shrink the font.



\---



\# 30. EMPTY SPACE



If a scene feels empty, do not automatically add more text.



Consider:



```text

increase hero scale

increase type scale

improve composition

increase intentional spacing

reframe camera

use negative space deliberately

```



More information is not always better design.



\---



\# 31. KINETIC TYPOGRAPHY



Use kinetic typography when typography itself carries the narrative.



Best for:



```text

manifestos

brand statements

campaigns

music-driven edits

short-form social

title sequences

high-energy launches

```



Less appropriate when the viewer must closely inspect complex UI simultaneously.



\---



\# KINETIC TYPOGRAPHY PRINCIPLE



Motion should express meaning.



Examples:



```text

"FAST"

→ rapid arrival



"EXPAND"

→ spatial expansion



"CONNECTED"

→ elements joining



"FOCUS"

→ blur resolving



"ONE"

→ surrounding elements collapse into one



"FLOW"

→ continuous directional movement

```



Avoid literal animation when it becomes gimmicky.



Meaning is more important than cleverness.



\---



\# 32. TEXT AS TRANSITION OBJECT



A headline can become a scene transition.



Example:



```text

HEADLINE

→ scales toward camera

→ letterform fills frame

→ next scene appears through letter / mask

```



Or:



```text

highlight bar

→ expands

→ becomes next scene background

```



This creates continuity between typography and editing.



\---



\# 33. TYPOGRAPHY PERSONALITIES



Typography motion should follow art direction.



\## PREMIUM



```text

large clean type

restrained palette

longer holds

minimal stagger

smooth easing

small motion amplitude

precise spacing

```



Avoid excessive bounce.



\---



\## TECHNOLOGY



```text

geometric/grotesk type

clear hierarchy

precise motion

controlled depth

data-aware typography

structured reveals

```



Avoid default "hacker" aesthetics unless appropriate.



\---



\## PLAYFUL



```text

bolder scale changes

spring

rhythmic stagger

rounded forms

color emphasis

```



Maintain readability.



\---



\## CORPORATE



```text

stable hierarchy

clean entrances

moderate scale

minimal distortion

predictable reading order

```



Avoid making "professional" synonymous with static.



\---



\## ENERGETIC



```text

shorter phrases

strong contrast

fast reveals

impact accents

dynamic scale

rhythmic editing

```



Use holds to prevent fatigue.



\---



\## EDITORIAL



```text

strong grids

intentional line breaks

large type

negative space

asymmetry

restrained animation

```



\---



\# 34. TYPOGRAPHY MOTION RECIPES



These are starting patterns, not mandatory presets.



\---



\## PREMIUM HERO



```text

opacity: 0 → 1

translateY: 24 → 0

blur: subtle → 0

duration: moderate

easing: smooth ease-out

hold: generous

```



\---



\## PRODUCT HEADLINE



```text

mask reveal

\+

small Y translation

\+

short phrase stagger

```



Use when introducing product value.



\---



\## KINETIC WORD HIT



```text

scale: slightly oversized → 1

opacity: 0 → 1

optional impact

```



Use on one important word.



\---



\## SUPPORTING COPY



```text

opacity: 0 → 1

translateY: 8–16px → 0

```



Keep it quieter than the hero.



\---



\## UI LABEL



```text

parent UI enters

→ label settles with parent

```



Avoid independent cinematic motion unless the label itself is being explained.



\---



\## METRIC



```text

label appears

→ number counts / changes

→ final value settles

→ optional emphasis

```



Do not animate random values unrelated to real product data.



\---



\# 35. ANTI-PATTERNS



Avoid:



```text

EVERY WORD BOUNCES



EVERY LINE USES A DIFFERENT ANIMATION



MULTIPLE DISPLAY FONTS WITHOUT PURPOSE



SYSTEM DEFAULT FONT ON A PREMIUM HERO BY ACCIDENT



TINY WEB-SIZED TYPE IN VIDEO



LONG PARAGRAPH WITH KINETIC WORD ANIMATION



NO READING HOLD



RANDOM LINE BREAKS



HIGHLIGHTING MANY WORDS AT ONCE



UNCONTROLLED FONT FALLBACK



ANIMATING TEXT BEFORE FONT LOAD



MEASURING WITH ONE FONT AND RENDERING WITH ANOTHER



USING EFFECTS TO COMPENSATE FOR WEAK HIERARCHY



SHRINKING TYPE JUST TO FIT MORE COPY



CENTERING EVERYTHING BY DEFAULT



ANIMATING UI TEXT INDEPENDENTLY FROM ITS UI CONTAINER



BEAT-SYNCING EVERY WORD



EXCESSIVE BLUR ON SMALL TEXT

```



\---



\# 36. REMOTION IMPLEMENTATION RULES



For Remotion typography:



```text

LOAD FONT FIRST



USE SHARED FONT CONFIG



MEASURE DYNAMIC TEXT WHEN NEEDED



USE FRAME-DRIVEN DETERMINISTIC ANIMATION



CLAMP INTERPOLATIONS



USE TABULAR NUMBERS FOR CHANGING METRICS



VERIFY OVERFLOW



VERIFY FINAL RENDER

```



\---



\# RESPONSIVE SIZE



For reusable compositions, consider deriving typography from composition dimensions rather than relying entirely on fixed values.



Example concept:



```tsx

const {height} = useVideoConfig();



const heroSize = height \* 0.1;

```



But do not blindly scale everything linearly.



Apply sensible minimums and maximums.



\---



\# 37. AFTER EFFECTS IMPLEMENTATION RULES



For After Effects:



Verify:



```text

font exists

correct PostScript font is used

glyph coverage exists

no silent substitution

text layer dimensions

motion blur

safe areas

rendered readability

```



If scripting typography, inspect the actual font returned by AE rather than assuming the requested face was accepted.



Render previews.



Typography problems often become obvious only in rendered frames.



\---



\# 38. DAVINCI / FUSION



When typography is finished in DaVinci/Fusion:



Use it primarily for:



```text

titles

lower thirds

editorial text

finishing

compositing

delivery adaptation

```



Maintain the same hierarchy and brand rules established upstream.



Do not redesign typography during finishing unless required.



\---



\# 39. RENDER VALIDATION



Never approve typography only from code.



Inspect rendered frames.



Check:



```text

ACTUAL SIZE

ACTUAL FONT

ACTUAL WEIGHT

ACTUAL LINE BREAK

ACTUAL POSITION

ACTUAL CONTRAST

ACTUAL SAFE AREA

ACTUAL OVERFLOW

ACTUAL GLYPHS

ACTUAL MOTION

ACTUAL READING TIME

```



\---



\# 40. TYPOGRAPHY AUDIT



Before approving a scene, ask:



\### MESSAGE



```text

Is the message clear?

Is the headline concise enough?

Does the copy describe real product capability?

```



\### HIERARCHY



```text

What is read first?

What is read second?

Are two elements competing?

```



\### SCALE



```text

Is the type actually readable in the final rendered frame?

Is any essential type too small?

```



\### FONT



```text

Did the intended font actually load?

Does it contain every required glyph?

Is fallback occurring?

```



\### COMPOSITION



```text

Does text have enough space?

Does the product overlap it?

Is the alignment intentional?

```



\### MOTION



```text

Does the motion express the text's role?

Is the motion hierarchy correct?

Is supporting copy quieter than hero copy?

```



\### TIMING



```text

Does the viewer have enough time to read?

Does the important word land at the intended moment?

```



\### EMPHASIS



```text

Is emphasis semantic?

Are too many words highlighted?

```



\### RESPONSIVE



```text

Does 9:16 require recomposition?

Are platform overlays considered?

```



\### TECHNICAL



```text

Is text measured correctly?

Is overflow checked?

Are numbers stable?

Are fonts loaded before measurement?

```



\---



\# 41. TYPOGRAPHY DENSITY AUDIT



If the scene feels crowded, do not immediately reduce all font sizes.



Try in this order:



```text

1\. REMOVE UNNECESSARY COPY

2\. SPLIT INFORMATION ACROSS SHOTS

3\. IMPROVE HIERARCHY

4\. CHANGE LINE BREAKS

5\. RECOMPOSE

6\. REDUCE SECONDARY ELEMENTS

7\. ONLY THEN CONSIDER SMALLER TYPE

```



\---



\# 42. TYPOGRAPHY REPETITION AUDIT



Across a full product film, avoid using exactly the same:



```text

headline entrance

word stagger

highlight

position

scale relationship

```



in every scene.



Maintain brand consistency while varying presentation according to message.



Variation should come from communication needs, not randomness.



\---



\# 43. TYPOGRAPHY SPECTACLE AUDIT



Ask:



```text

Is the typography impressive because it communicates strongly?



or



Is it impressive only because many effects are happening?

```



If the second is true, simplify.



\---



\# 44. TYPOGRAPHY + PRODUCT TRUTH



Never change product language in a way that fabricates capability.



Do not invent:



```text

metrics

AI outputs

customer results

feature names

integrations

system messages

performance numbers

dashboard values

```



unless explicitly presented as fictional/conceptual.



Typography can amplify product truth.



It must not manufacture it.



\---



\# 45. OUTPUT CONTRACT



When designing typography for an important shot, define:



```text

TEXT ROLE:

MESSAGE:

COPY:

PRIMARY PHRASE:

EMPHASIS WORD:

TYPEFACE:

WEIGHT:

SIZE:

LINE STRUCTURE:

ALIGNMENT:

POSITION:

COLOR:

CONTRAST:

REVEAL:

STAGGER:

MOTION:

READING HOLD:

EXIT:

CAMERA RELATIONSHIP:

SOUND RELATIONSHIP:

IMPLEMENTATION ENGINE:

RESPONSIVE ADAPTATION:

VALIDATION:

```



\---



\# 46. TYPOGRAPHY ROUTING



Use this module when the problem concerns:



```text

headline hierarchy

font choice

font loading

text scale

line breaks

kinetic typography

text reveals

word reveals

text emphasis

numbers

metrics

labels

CTA

captions

text composition

text readability

responsive text

font fallback

text overflow

```



Then load supporting modules only when needed.



\---



\# WITH ANIMATION PRINCIPLES



Use:



```text

references/animation-principles.md

```



for:



```text

easing

stagger

timing

spring

anticipation

follow-through

motion rhythm

```



\---



\# WITH ART DIRECTION



Use:



```text

references/art-direction.md

```



for:



```text

visual personality

creative direction

tone

brand expression

```



\---



\# WITH COMPOSITION



Use:



```text

references/creative/composition.md

```



for:



```text

grid

balance

focal point

negative space

visual hierarchy

```



\---



\# WITH CAMERA



Use:



```text

references/creative/camera-language.md

```



when text interacts with:



```text

push-ins

pull-outs

parallax

3D

perspective

world space

object tracking

```



\---



\# WITH CINEMATIC UI



Use:



```text

references/cinematic-ui.md

```



when typography accompanies product UI.



\---



\# WITH FEATURE FOCUS



Use:



```text

components/feature-focus.md

```



when text explains a specific feature.



\---



\# WITH DATA FLOW



Use:



```text

components/data-flow.md

```



when text labels:



```text

nodes

systems

agents

integrations

automation steps

data movement

```



\---



\# WITH AUDIO



Use:



```text

references/audio/sound-design.md

references/audio/beat-sync.md

references/audio/sfx-language.md

references/audio/audio-motion-sync.md

```



when typography must synchronize with music or sound.



\---



\# 47. TYPOGRAPHY DECISION EXAMPLES



\## SaaS Hero



```text

Goal:

introduce the product promise



Typography:

large concise headline



Motion:

restrained mask/translate reveal



Support:

subheadline delayed



Product:

device/UI becomes visual evidence

```



\---



\## AI Feature



```text

Goal:

communicate intelligence/result



Typography:

benefit headline



Motion:

headline stable



UI:

AI result becomes primary motion



Emphasis:

one semantic phrase



Sound:

subtle confirmation at result

```



\---



\## Dashboard Metric



```text

Goal:

show measurable outcome



Typography:

number = hero

label = support



Motion:

stable tabular digits

count/change only if meaningful



UI:

chart/card supports result

```



\---



\## Automation Scene



```text

Goal:

explain sequence



Typography:

short labels



Motion:

labels follow nodes



Primary visual:

data-flow



Avoid:

large kinetic headline competing with flow

```



\---



\## Brand Closing



```text

Goal:

leave final message



Typography:

brand line / CTA



Motion:

minimal



Logo:

logo-reveal



Hold:

long enough for recognition and action

```



\---



\# 48. FINAL TYPOGRAPHY DECISION LOOP



Before implementation:



```text

WHAT MUST BE UNDERSTOOD?

&#x20;       ↓

WHAT TEXT CARRIES THAT MESSAGE?

&#x20;       ↓

WHAT ROLE DOES THE TEXT HAVE?

&#x20;       ↓

WHAT IS THE HIERARCHY?

&#x20;       ↓

WHAT SIZE MAKES IT READABLE?

&#x20;       ↓

WHAT COMPOSITION SUPPORTS IT?

&#x20;       ↓

WHAT WORD, IF ANY, NEEDS EMPHASIS?

&#x20;       ↓

SHOULD TYPOGRAPHY LEAD OR SUPPORT?

&#x20;       ↓

WHAT REVEAL MATCHES THE MESSAGE?

&#x20;       ↓

HOW LONG MUST IT HOLD?

&#x20;       ↓

HOW DOES IT RELATE TO CAMERA / UI / SOUND?

&#x20;       ↓

HOW WILL IT ADAPT TO THE OUTPUT FORMAT?

&#x20;       ↓

HOW WILL THE FINAL RENDER BE VERIFIED?

```



\---



\# GOLDEN RULE



Typography is successful when the viewer reads the right thing at the right moment with the intended emotional weight.



Do not animate text to prove that it can move.



Design the hierarchy first.



Use motion to reveal the hierarchy.



Use timing to protect comprehension.



Use emphasis to direct attention.



Use typography to communicate the product.



The words remain the message.

