# Composition Standards (Defaults)

These apply to **photographic** prompts unless the draft or the user specifies otherwise.
They do not apply to informational-graphic prompts (charts, diagrams).

| Setting | Default |
|---|---|
| Aspect ratio | 16:9 (3840 x 2160). Aspect ratio is a variable, not a constant — honor any ratio the user names, and adjust the resolution spec to match. |
| Text overlay space | Reserve negative space in the upper-left third (primary); upper-right or right acceptable when specified. **COVER/HERO images only** — in-body images get no reserved overlay space. |
| Perspective | Low three-quarter angle unless the scene calls for otherwise. Change this default to your house style. |
| Human subjects | Rear-facing, over-the-shoulder, or blurred background figures. No face-forward subjects. No identifiable real individuals. |
| Demographic assumptions | None. Do not inject age/gender/ethnicity unless the draft explicitly specifies it. |
| Legible text on surfaces | Never in photographic prompts — vehicle wraps, screens, signage, chalkboards, name tags. Flag as a regeneration trigger if the concept pushes for it. |
| Overhead / flat-lay | Never for cover/hero images. |
| Branded / real-world IP | None. No logos, no trademarked products, no recognizable brand marks. |

## Negative space rule (important)

The reserved negative space is for the client's text overlay. Never place prompted copy,
watermarks, captions, or labels in it. This applies to the **cover only**. In-body
photographic images should be composed as complete scenes with no reserved empty zone.

## Prompt text bleed (Seedream 4.5 and any model like it)

Some models paint the words of the prompt into the picture as readable type.
Seedream 4.5 has been seen to render palette hex codes and a named
photographer into the reserved overlay zone.

Two rules, for every photographic prompt:

- Never put hex codes or a photographer's name in the prompt text. Name the
  colors in words ("deep navy, warm brass, cream"). Name the style anchor by
  tradition, not by person, when a model is prone to this.
- Never name a document, form, sign, screen, or field. Describe printed matter
  as "abstract illegible texture" instead.

Then look at the render. This failure mode is silent, and only your eye catches
it.

## One coherent scene

Every photographic prompt describes a single, grounded, cinematically logical setting.
No split-narrative, no multi-location montage, no "on one side X, on the other Y." A
simpler coherent scene beats a clever fragmented one — fragmented concepts get rejected
by the model or read as collage.
