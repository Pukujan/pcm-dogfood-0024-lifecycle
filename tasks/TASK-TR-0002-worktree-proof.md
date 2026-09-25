# TASK-TR-0002 — Worktree Proof

<!-- continuity:task {"acceptance":["replace this with observable, task-specific acceptance checks"],"depends_on":[],"goal":"Exercise the managed-worktree path end-to-end in the disposable adoption: create, work, merge, verified remove","id":"TR-0002","issue_url":"https://github.com/Pukujan/pcm-dogfood-0024-lifecycle/issues/1","next_action":"define scope and observable acceptance checks, then begin bounded work","owner":"owner lifecycle trial","priority":"P3","protocol_version":"0.1.0-draft","schema":"project-continuity.task.v1","status":"active","why":"Item 41 requires task-owned worktrees be cleaned up after merge"} -->

- Status: active
- Owner: owner lifecycle trial
- Priority: P3
- Depends on: none

## Goal

Exercise the managed-worktree path end-to-end in the disposable adoption: create, work, merge, verified remove

## Why

Item 41 requires task-owned worktrees be cleaned up after merge

## Allowed files

- define bounded paths before implementation.

## Human outcome

Describe what becomes easier, safer, clearer, or possible when this task is complete.

## Scope and boundaries

- In scope:
- Out of scope:
- Dependencies/uncertainty:

## Acceptance criteria

- [ ] state observable, task-specific outcomes.

## Evidence and sources

Link repository state at a revision and cite external factual claims directly. Record commands and results for claims that need verification.

## Reproduction details (only when needed)

Starting revision, material inputs/configuration, runtime, exact command or prompt, observed result, and limitations.

## Related records

- Required leaf owning issue, parent ancestry and dependencies (or explicitly none):
- Primary writer / branch / source issue revision / as-of status:
- Related PR/CI evidence and push receipt (request ID / SHA):

## Checkpoint log

No checkpoints yet.

### 2026-09-25 10:29:30 UTC — owner lifecycle trial

<!-- continuity:checkpoint {"agent":"owner lifecycle trial","blocked":[],"changed":["trial/worktree_note.py; tests/test_trial_module.py"],"completed":["Worktree-owned change committed and pushed from pcm/worktree/TR-0002."],"decisions":["no new decisions"],"evidence":["unittest 5 OK; validate VALID"],"next_action":"PR, auto-merge, then verified worktree remove.","protocol_version":"0.1.0-draft","schema":"project-continuity.checkpoint.v1","task_id":"TR-0002","timestamp":"2026-09-25T10:29:30Z"} -->
<!-- continuity:checkpoint-operation {"payload_sha256":"404c501baaa3ab867046d3700604c67f93488c684213e467705e35a7b0ab370a","request_id":"tr0002-worktree-20260925","schema":"project-continuity.checkpoint-operation.v1","task_id":"TR-0002"} -->

Completed:
- Worktree-owned change committed and pushed from pcm/worktree/TR-0002.

Evidence:
- unittest 5 OK; validate VALID

Decisions:
- no new decisions

Changed:
- trial/worktree_note.py; tests/test_trial_module.py

Blocked/uncertain:
- none

Next:
- PR, auto-merge, then verified worktree remove.

## Handoff

Read PROJECT → CURRENT → this task → minimum relevant spec. Checkpoint before stopping.
