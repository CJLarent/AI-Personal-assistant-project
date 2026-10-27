import unittest
import tempfile
from pathlib import Path
import json 
from history_logger.history_logger import HistoryLogger
from history_logger.action_logger import ActionRecord

class TestHistoryLogger(unittest.TestCase):
    def test_append_creates_file(self):
        record = ActionRecord(
    action_id="test-001",
    timestamp="2026-10-27T00:00:00+00:00",
    action="READ_LOCAL_FILE",
    resource="notes.txt",
    allowed=False,
    status="not authorized",
    reason="User authorization required"
    )

        with tempfile.TemporaryDirectory()as temp_dir:
            history_path=Path(temp_dir)/ "actions.jsonl"
            history=HistoryLogger(history_path)
            history.append(record)

            self.assertTrue(history_path.exists())
    def test_reads_record(self):
        #Verify that a saved action record can be read from history.
        record = ActionRecord(
            action_id="test-001",
            timestamp="2026-10-27T00:00:00+00:00",
            action="READ_LOCAL_FILE",
            resource="notes.txt",
            allowed=False,
            status="not authorized",
            reason="User authorization required"
            )
        with tempfile.TemporaryDirectory() as temp_dir :
            history_path= Path(temp_dir) / "actions.jsonl"
            history= HistoryLogger(history_path)
            history.append(record)
            saved_record = history.read()
            self.assertEqual(saved_record["action_id"],record.action_id)

        
    

    