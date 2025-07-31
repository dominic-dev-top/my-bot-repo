import os
import datetime
import json
from github import Github

# Access token from environment variable
token = os.getenv('GH_PAT')
if not token:
    raise Exception("Missing GH_PAT token")

g = Github(token)
repo = g.get_user().get_repo("my-bot-repo")

# Log something
log = f"Bot ran at {datetime.datetime.utcnow().isoformat()}Z"
with open("logs/bot-log.txt", "a") as f:
    f.write(log + "\n")

# Dummy update to achievements
achievements = {"last_run": log}
with open("bot/achievements.json", "w") as f:
    json.dump(achievements, f, indent=2)
