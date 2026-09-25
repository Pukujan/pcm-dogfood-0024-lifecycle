"""Bounded trial change proving cold-start continuation (TR-0001)."""


def next_action(recovered: dict[str, str]) -> str:
    """Return the single next action a fresh session should take."""
    return recovered.get("next_action", "read checkpoints/CURRENT.md")
