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


@dataclass(frozen=True)
class PermissionDecision:
    """An immutable result that a future tool controller must enforce."""

    allowed: bool
    reason: str


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


# TODO (learner exercise, no need to solve immediately):
# Propose a design for one-time versus session-long approvals.
# What should happen when the assistant requests a different action?
# Keep approval state OUT of model-generated text and prompts.
