import json
import os

def log_chat(user_input, response_text, log_file="chat_log.json"):
    log_entry = {"user": user_input, "response": response_text}
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            logs = json.load(f)
    else:
        logs = []
    logs.append(log_entry)
    with open(log_file, "w") as f:
        json.dump(logs, f, indent=2)

def load_chat(log_file="chat_log.json"):
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            return json.load(f)
    return []

