# Matriz AI Skill Registry

The public registry of installable skills for Matriz AI.

## Repository layout

```text
skills/
  <skill-name>/
    SKILL.md
    .mycodex/
      manifest.json
```

Each skill is self-contained. `SKILL.md` supplies agent instructions and trigger metadata; `.mycodex/manifest.json` supplies the Marketplace card and installation metadata.

## Publishing a skill

1. Create `skills/<lowercase-hyphenated-name>/`.
2. Add a `SKILL.md` with YAML frontmatter containing `name` and `description`.
3. Add `.mycodex/manifest.json` with the same `name`, a semantic version, category, and `repository` set to `https://github.com/Matriz-AI/registry`.
4. Validate the skill before merging it into `main`.

See [AGENTS.md](AGENTS.md) for the complete authoring and review rules.

## Imported skills

Some skills are imported from third-party registries with their original license and attribution preserved. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

Original Matriz AI skills are licensed under [MIT](LICENSE). Third-party skill licenses take precedence for their own folders.
