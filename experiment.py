from core.permissions import Approval, Action, ApprovalLifetime


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
# Display the object
print(approval)
print(network_approval)

action_matches = approval.action == Action.READ_LOCAL_FILE
resource_matches = approval.resource == "passwords.txt"

print(action_matches and resource_matches)