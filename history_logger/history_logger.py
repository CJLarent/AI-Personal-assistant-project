import json
from dataclasses import asdict
from pathlib import Path
class HistoryLogger: 
 # Initialize the root 
    def __init__(self, history_path: Path)-> None:
        self.history_path = history_path
    # append the history.json 
    def append(self, record )-> None:
        # make sure the directory exists
        self.history_path.parent.mkdir(parents=True, exist_ok=True)
        # create the dictionary record
        record_dictionary = asdict(record)
        # utilize the special json func
        # to ensure that the file created gets organized correctly 
        record_json= json.dumps(record_dictionary)

        with self.history_path.open("a", encoding= "utf-8") as history_file:
            history_file.write(record_json + "\n")

    def read(self):
        with self.history_path.open("r",encoding= "utf-8")as history_file:
            saved_line = history_file.readline()
            saved_record= json.loads(saved_line)
            return saved_record