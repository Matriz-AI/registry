---
name: matriz-skill-authoring
description: Create, update, and validate installable Matriz AI Marketplace skills with clear triggers, safe workflows, and correct registry metadata. Use when adding a skill to a Matriz AI registry, improving a SKILL.md, or reviewing a marketplace manifest.
---

# Matriz skill authoring

Create skills that another agent can use without hidden platform assumptions. Follow the registry's `AGENTS.md` for its required layout and manifest schema.

## Define the skill

- Choose a lowercase hyphenated name that describes the capability.
- Write a concise frontmatter description that states both the function and concrete trigger situations.
- Add only reusable procedural guidance. Prefer references, scripts, and assets when they remove repeated work; do not add process logs or filler documentation.
- State user-controlled boundaries for external writes, network access, credentials, and destructive operations.

## Package it

1. Create `skills/<name>/SKILL.md` with `name` and `description` frontmatter matching the folder name.
2. Create `.mycodex/manifest.json` with matching name, semantic version, Matriz AI repository/path, license, category, and declared capabilities.
3. Use original content or explicitly redistributable third-party material. Retain licenses and notices for imports.
4. Increment the version for published changes.

## Validate

- Parse the frontmatter and manifest; verify the three names match.
- Confirm the category is permitted and every capability is justified.
- Test the key workflow against a realistic local example when the skill includes scripts or fragile steps.
- Run whitespace and repository-status checks before committing.

## Review checklist

- Is the trigger precise enough to avoid activating for unrelated work?
- Can the instructions run without Claude-specific tools, paths, or assumptions?
- Are secrets, private URLs, and unsupported claims absent?
- Are all files necessary to execute the advertised workflow?
