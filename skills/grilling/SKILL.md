---
name: grilling
description: Relentlessly stress-test a plan, decision, design, or idea through a structured one-question-at-a-time interview. Use when the user wants to challenge assumptions, resolve dependencies, or explore every branch before acting.
---

# Grilling

Interview the user relentlessly about the plan, decision, or idea until both sides reach a shared understanding.

Do not act on the plan during the interview. The purpose of this skill is to clarify and stress-test thinking, not to implement the resulting decision.

## Interview protocol

1. Restate the topic in one sentence and identify the current decision branch.
2. Ask exactly one question. Never bundle multiple questions into one turn.
3. Immediately provide a recommended answer and explain the trade-off in one or two sentences.
4. Wait for the user's answer before asking the next question.
5. After each answer, record the decision in plain language and identify the next unresolved dependency.
6. Continue through assumptions, alternatives, constraints, interfaces, ownership, sequencing, failure modes, security, reversibility, cost, timeline, and success criteria as relevant.
7. When a fact can be established from the environment, inspect the filesystem, repository, tools, or other available sources instead of asking the user. Ask the user only for decisions, preferences, priorities, or facts that cannot be discovered safely.
8. When the user changes an earlier decision, revisit every dependent branch before proceeding.

## Question format

Use this compact format:

> Pergunta: [one decision question]
>
> Recomendação: [the answer you recommend]
>
> Motivo: [the key consequence or trade-off]

Then stop and wait for feedback. Do not ask a follow-up question in the same message.

## Decision-tree coverage

Cover the branches that materially affect the outcome, including:

- desired outcome and measurable success criteria;
- users, stakeholders, owner, scope, and non-goals;
- constraints, assumptions, dependencies, and ordering;
- competing options and the reason to reject each one;
- inputs, outputs, integrations, data, permissions, and operational workflow;
- risks, edge cases, abuse cases, failure recovery, and rollback;
- cost, schedule, maintenance burden, and reversibility;
- validation plan, launch criteria, and what would change the decision.

Prioritize questions by dependency: resolve decisions that constrain other decisions first. Avoid trivia and do not prolong the interview after all consequential branches are resolved.

## Completion gate

When the branches are resolved, provide a concise shared-understanding summary containing:

- objective and success criteria;
- confirmed decisions and rejected alternatives;
- constraints, dependencies, risks, and open questions;
- the agreed next step, without executing it.

Ask: "This is my understanding. Confirm that we reached shared understanding before I act."

Do not perform implementation, send messages, change files, call external systems, or otherwise act until the user explicitly confirms the shared understanding.
