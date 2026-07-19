# Matriz AI Registry Guide

This repository publishes skills for the Matriz AI Marketplace. A skill is an installable package of instructions and optional application assets.

## Required structure

```text
skills/<skill-name>/
├── SKILL.md
└── .mycodex/
    └── manifest.json
```

Use lowercase, numbers, and hyphens for `<skill-name>`. The folder name, `SKILL.md` frontmatter `name`, and manifest `name` must match.

## SKILL.md

Every skill must begin with valid YAML frontmatter:

```yaml
---
name: example-skill
description: Use when the user needs help with a clearly defined workflow.
---
```

The description is the trigger. State the concrete situations, products, and keywords that should activate the skill. Keep instructions specific, safe, and independently usable.

## Marketplace manifest

Create `skills/<skill-name>/.mycodex/manifest.json` with, at minimum:

```json
{
  "name": "example-skill",
  "version": "0.1.0",
  "description": "Short Marketplace description.",
  "author": { "name": "Matriz AI" },
  "homepage": "https://github.com/Matriz-AI/registry/tree/main/skills/example-skill",
  "repository": "https://github.com/Matriz-AI/registry",
  "path": "skills/example-skill",
  "license": "MIT",
  "interface": {
    "displayName": "Example Skill",
    "shortDescription": "Short Marketplace description.",
    "category": "Productivity"
  }
}
```

Allowed categories: `Productivity`, `Development`, `Finance`, `Communication`, `Data`, `Design`, `DevOps`, `AI`, and `Research`.

## Review rules

- Do not add secrets, tokens, or private endpoints.
- Declare any network, write, execute, or persistence capability in the manifest.
- Pin third-party references to a version or commit whenever practical.
- Review a skill's license and content before importing it from another registry.
- Increment the manifest version for every published change.
