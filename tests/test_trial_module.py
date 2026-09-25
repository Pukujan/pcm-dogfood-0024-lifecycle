import unittest

from trial.handoff_note import next_action


class NextActionTests(unittest.TestCase):
    def test_returns_recorded_next_action(self) -> None:
        self.assertEqual(next_action({"next_action": "run checkpoint"}), "run checkpoint")

    def test_falls_back_to_current_pointer(self) -> None:
        self.assertEqual(next_action({}), "read checkpoints/CURRENT.md")


class WorktreeNoteTests(unittest.TestCase):
    def test_worktree_change_is_clean(self) -> None:
        from trial.worktree_note import cleaned
        self.assertTrue(cleaned())
