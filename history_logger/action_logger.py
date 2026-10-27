from dataclasses import dataclass
from pathlib import Path
from history_logger.history_logger import HistoryLogger
@dataclass(frozen=True)
class ActionRecord:
    action_id: str
    timestamp: str
    action: str
    resource: str
    allowed: bool
    status: str
    reason: str
    
def log_action(record: ActionRecord)->None:
    history= HistoryLogger(
       Path("history/data/actions.jsonl")
    )  
    history.append(record)