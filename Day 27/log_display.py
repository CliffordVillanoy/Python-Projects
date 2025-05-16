# Show only error or critical logs from a log list
logs = [
    {"level": "INFO", "message": "System started."},
    {"level": "ERROR", "message": "Null pointer exception."},
    {"level": "CRITICAL", "message": "Database unreachable."},
]

for log in logs:
    if log["level"] in ("ERROR", "CRITICAL"):
        print(f"[{log['level']}] - {log['message']}")
