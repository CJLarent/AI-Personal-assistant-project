"""First standard-library tests; run with: python -m unittest discover -s tests."""
import unittest

from core.permissions import Action, check_permission


class PermissionTests(unittest.TestCase):
    def test_answer_is_allowed(self):
        self.assertTrue(check_permission(Action.ANSWER).allowed)

    def test_file_write_is_denied_by_default(self):
        self.assertFalse(check_permission(Action.WRITE_LOCAL_FILE).allowed)

    def test_approved_action(self):
        # A future controller must establish approval from trusted UI input.
        self.assertTrue(check_permission(Action.READ_LOCAL_FILE, user_approved=True).allowed)

    # TODO (learner exercise): add a test for RUN_COMMAND without approval.


if __name__ == "__main__":
    unittest.main()
