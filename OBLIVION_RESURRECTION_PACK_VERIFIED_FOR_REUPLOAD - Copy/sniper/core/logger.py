# Oblivion Logger Core – Phase 3.2
# Logs events to console and resurrection log files

import datetime
import os

LOG_FILE = "Patchnote_Log.csv"
WAR_LOG_PATH = "WAR LOG JOURNAL.txt"
PATCHBOOK_PATH = "OBLIVION PATCHBOOK.txt"


def log_event(message: str, tag: str = "SYSTEM"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{timestamp},{tag},{message}"
    
    # Console Output
    print(f"[{tag}] {message}")

    # CSV Logging
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as file:
            file.write(line + "\n")
    except Exception as e:
        print(f"[ERROR] Failed to write to log: {e}")

def log_to_war_log(message: str):
    try:
        with open(WAR_LOG_PATH, "a", encoding="utf-8") as war_log:
            war_log.write(f"- {message}\n")
    except Exception as e:
        print(f"[ERROR] Failed to write to WAR LOG: {e}")

def log_to_patchbook(message: str):
    try:
        with open(PATCHBOOK_PATH, "a", encoding="utf-8") as patchbook:
            patchbook.write(f"### {message}\n")
    except Exception as e:
        print(f"[ERROR] Failed to write to PATCHBOOK: {e}")
