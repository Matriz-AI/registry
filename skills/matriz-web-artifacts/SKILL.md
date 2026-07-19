---
name: matriz-web-artifacts
description: Build polished standalone web artifacts, interactive prototypes, and small browser tools with accessible UI, maintainable components, and local verification. Use when the user asks for an interactive HTML, React, or browser-based deliverable outside a full application repository.
---

# Web artifact workflows

Deliver a runnable browser artifact that is independent of a chat platform. Clarify the task, expected interactions, target device, and whether the result is a single file, a component set, or a small application.

## Plan and build

- Choose the smallest appropriate stack: semantic HTML/CSS/JavaScript for focused tools; React only when state or composition justifies it.
- Define the primary action, empty states, validation, loading behavior, and error recovery before styling.
- Use semantic elements, keyboard-accessible controls, visible focus states, and meaningful labels.
- Keep data local by default. Ask before connecting third-party APIs, storing personal data, or publishing the artifact.
- Structure the code so content, presentation, and behavior can be changed without editing an opaque bundle.

## Quality gate

1. Run the artifact locally and test the primary flow, invalid input, empty data, and narrow viewport.
2. Check keyboard navigation and sufficient contrast.
3. Inspect the browser console for errors and confirm that all declared dependencies load.
4. Deliver the source, clear startup instructions, and any requested preview or build output.

## Handoff

Describe the artifact's entry point, chosen stack, local data assumptions, and any command required to run it. Do not claim that a preview has been hosted unless it was actually published.
