"""Worktree-owned bounded change for the lifecycle trial (TR-0002)."""


def cleaned() -> bool:
    """The managed worktree for this task was created and removed after merge."""
    return True
