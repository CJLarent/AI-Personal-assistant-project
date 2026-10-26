from dataclasses import dataclass
#from datetime import datetime, timezone
#from uuid import uuid4
from dataclasses import asdict
import json
from pathlib import Path
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
    history_path = Path("history/data/actions.jsonl")
    history_path.parent.mkdir(parents=True, exist_ok=True)
    record_dictionary = asdict(record)
    record_json= json.dumps(record_dictionary)
    history_path.parent.mkdir(parents=True, exist_ok=True)
    with history_path.open("a", encoding="utf-8") as history_file:
        history_file.write(record_json + "\n")