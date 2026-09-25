# TASK-TR-0001 — Coldstart

<!-- continuity:task {"acceptance":["replace this with observable, task-specific acceptance checks"],"depends_on":[],"goal":"Prove fresh-session continuation end-to-end: recover state from PROJECT/CURRENT/TASK, checkpoint a bounded change, and merge through protected CI","id":"TR-0001","issue_url":"https://github.com/Pukujan/pcm-dogfood-0024-lifecycle/issues/1","next_action":"define scope and observable acceptance checks, then begin bounded work","owner":"owner lifecycle trial","priority":"P2","protocol_version":"0.1.0-draft","schema":"project-continuity.task.v1","status":"active","why":"Adopters must trust cold-start handoff and the GitHub-owned lifecycle"} -->

- Status: active
- Owner: owner lifecycle trial
- Priority: P2
- Depends on: none

## Goal

Prove fresh-session continuation end-to-end: recover state from PROJECT/CURRENT/TASK, checkpoint a bounded change, and merge through protected CI

## Why

Adopters must trust cold-start handoff and the GitHub-owned lifecycle

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

### 2026-09-25 10:16:37 UTC — owner lifecycle trial

<!-- continuity:checkpoint {"agent":"owner lifecycle trial","blocked":["None."],"changed":["trial/handoff_note.py; tests/test_trial_module.py; tasks/TASK-TR-0001-coldstart.md; checkpoints/CURRENT.md"],"completed":["Added trial/handoff_note.py + tests; CURRENT points at TR-0001; bounded change proves checkpoint+push path."],"decisions":["Trial stays disposable; deleted after evidence."],"evidence":["python3.12 -m unittest discover -s tests: 3 OK; continuity validate --root .: VALID"],"next_action":"Open PR, enable auto-merge, verify required checks, reconcile issue status.","protocol_version":"0.1.0-draft","schema":"project-continuity.checkpoint.v1","task_id":"TR-0001","timestamp":"2026-09-25T10:16:37Z"} -->
<!-- continuity:checkpoint-operation {"payload_sha256":"15b9411c05d2208735ab80f55b2165410820664c1063c0d9846d55a96cf0de43","request_id":"tr0001-lifecycle-20260925","schema":"project-continuity.checkpoint-operation.v1","task_id":"TR-0001"} -->

Completed:
- Added trial/handoff_note.py + tests; CURRENT points at TR-0001; bounded change proves checkpoint+push path.

Evidence:
- python3.12 -m unittest discover -s tests: 3 OK; continuity validate --root .: VALID

Decisions:
- Trial stays disposable; deleted after evidence.

Changed:
- trial/handoff_note.py; tests/test_trial_module.py; tasks/TASK-TR-0001-coldstart.md; checkpoints/CURRENT.md

Blocked/uncertain:
- None.

Next:
- Open PR, enable auto-merge, verify required checks, reconcile issue status.

## Handoff

Read PROJECT → CURRENT → this task → minimum relevant spec. Checkpoint before stopping.
