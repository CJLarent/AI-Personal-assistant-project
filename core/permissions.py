"""Permission decisions for the personal assistant.

Learning goal: practice Enum, dataclass, functions, and explicit return values.
This module evaluates a request; it does NOT execute commands or open files.
"""

from dataclasses import dataclass
from enum import Enum


class Action(Enum):
    """Types of actions the assistant may eventually request."""

    ANSWER = "answer"
    READ_LOCAL_FILE = "read_local_file"
    WRITE_LOCAL_FILE = "write_local_file"
    RUN_COMMAND = "run_command"
    NETWORK_REQUEST = "network_request"
    

class ApprovalLifetime(Enum):
    ONE_TIME = "one_time"
    SESSION = " session"
    PERSISTENT ="persistent"
   

@dataclass(frozen=True)
class PermissionDecision:
    """An immutable result that a future tool controller must enforce."""

    allowed: bool
    reason: str

@dataclass(frozen=True)
class Approval:
    action:Action
    resource: str 
    lifetime: ApprovalLifetime

def check_permission(action: Action, *, user_approved: bool = False) -> PermissionDecision:
    """Return whether an action may proceed; never perform the action here.

    For now, answering is the only action permitted by default.
    ``user_approved`` represents approval verified by application UI code,
    NOT text from a model. This is a prototype, not secure authorization.
    """
    if action is Action.ANSWER:
        return PermissionDecision(True, "Information-only response")

    # A later controller must verify user approval outside the language model.
    if user_approved:
        return PermissionDecision(True, "Explicit approval supplied by caller")

    return PermissionDecision(False, "Action requires explicit user approval")

def matches_approval(
        approval: Approval,
        action: Action,
        resource: str
)->PermissionDecision:
    if action!=approval.action:
        
        return PermissionDecision(
            allowed=False,
            reason="This action is not permitted Sir!\n "
            "Please ask for an appropriate permission.\n "
            "Thank You\n "
            "Your unliving servant\n "
            "Zombie Master"
        )
    if approval.resource!= resource:
        return PermissionDecision(
            allowed=False,
            reason= "Sorry Sir ! I cannot find the requested resource.\n "
            "My mind is not that sharp please excuse my shortcomings.\n"
            "I will always try my best to serve you"
        )
    return PermissionDecision(
        allowed=True,
        reason=" good news Sir this action has been approved\n"
        " I shall comply with your request"
    )
        
# TODO (learner exercise, no need to solve immediately):
# Propose a design for one-time versus session-long approvals.
# What should happen when the assistant requests a different action?
# Keep approval state OUT of model-generated text and prompts.


