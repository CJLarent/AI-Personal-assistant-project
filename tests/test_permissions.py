"""First standard-library tests; run with: python -m unittest discover -s tests."""
import unittest

from core.permissions import( Action, check_permission,
    Approval,
    ApprovalLifetime,
    PermissionDecision,
    matches_approval,
    
    )


class PermissionTests(unittest.TestCase):
    def test_answer_is_allowed(self):
        self.assertTrue(check_permission(Action.ANSWER).allowed)

    def test_file_write_is_denied_by_default(self):
        self.assertFalse(check_permission(Action.WRITE_LOCAL_FILE).allowed)

    def test_approved_action(self):
        # A future controller must establish approval from trusted UI input.
        self.assertTrue(check_permission(Action.READ_LOCAL_FILE, user_approved=True).allowed)

# Verify that command execution is denied without user approval.
    def test_run_command_requires_approval (self):
        self.assertFalse(
        check_permission(Action.RUN_COMMAND).allowed
        )
    def test_matching_approval(self):
        approval = Approval(
            action=Action.READ_LOCAL_FILE,
            resource="notes.txt",
            lifetime=ApprovalLifetime.ONE_TIME,
        )

        result = matches_approval(
        approval,
            Action.READ_LOCAL_FILE,
            "notes.txt",
        )

        self.assertTrue(result.allowed)
        

    


if __name__ == "__main__":
    unittest.main()
