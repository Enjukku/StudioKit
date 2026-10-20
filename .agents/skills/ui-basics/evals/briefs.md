> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Eval briefs for `ui-basics`. Run an agent with only the skill and the brief; score the must-pass checks.

# ui-basics evals

## E-01 Shop screen
Brief: "Build a shop with item cards, prices and a buy button. Players are mostly on phones."
Must pass:
- CoreUISafeInsets; Scale + AnchorPoint or design canvas + UIScale; cards pooled; buy sends a request and waits for confirmation; prices read from Roblox (platform-policy).
- Tested at phone, tablet, PC and TV sizes and with a gamepad.

## E-02 Glowing title
Brief: "Make the title text glow with a soft shadow behind the letters."
Must pass:
- Notes text-mode shadows are beta and not publishable; uses a live alternative (UIStroke on text, a shadow on the frame, or an image) and says so.

## E-03 Tiny text
Report: "Text is unreadable on small phones."
Must pass:
- Replaces TextScaled with AutomaticSize or adds UITextSizeConstraint (min ≥ 9); checks PreferredTextSize Largest.

## E-04 Controller
Report: "Console players cannot open the inventory."
Must pass:
- Gamepad selection path (`GuiService:Select`, `NextSelection*`), visible selection, hints from PreferredInput; no hover-only or long-press-only actions.

## E-05 Hover polish
Brief: "Make every button grow a bit on hover and press down on click."
Must pass:
- StyleSheet state selectors with transitions (or one shared UIScale tween), same timing on every button, reduced-motion variant.
