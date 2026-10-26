from core.permissions import Approval, Action, ApprovalLifetime
from history_logger.action_logger import ActionRecord, log_action
from datetime import datetime, timezone
from uuid import uuid4

# Create an approval object
approval = Approval(
    action=Action.READ_LOCAL_FILE,
    resource="notes.txt",
    lifetime=ApprovalLifetime.ONE_TIME
)

network_approval =Approval(
    action=Action.NETWORK_REQUEST,
    resource="https://example.com",
    lifetime=ApprovalLifetime.SESSION
)
record= ActionRecord(
        action_id=str(uuid4()),
        timestamp= datetime.now(timezone.utc).isoformat(),
        action= "READ_LOCAL_FILE",
        resource="notes.txt",
        allowed=False,
        status="not authorized!",
        reason=" user authorization required."

    )

# Display the object
print(approval)
print(network_approval)

action_matches = approval.action == Action.READ_LOCAL_FILE
resource_matches = approval.resource == "passwords.txt"

print(action_matches and resource_matches)
print(record)
log_action(record)
