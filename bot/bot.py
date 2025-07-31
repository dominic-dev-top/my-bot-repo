import os, datetime, json
from github import Github

now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
token = os.getenv("GH_PAT")
repo = Github(token).get_repo("dominic-dev-top/dhairya-dom")

# Load or init achievements
file = "bot/achievements.json"
ach = json.load(open(file)) if os.path.exists(file) else {"issues":0,"commits":0,"badges":[]}

# Update logs
with open("logs/bot-log.txt","a") as f:
    f.write(f"Activity at {now}\n")
ach["commits"] += 1

# Save achievements
ach["issues"] = ach.get("issues", 0) + 1
if ach["issues"] >= 10 and "🚀 Explorer" not in ach["badges"]:
    ach["badges"].append("🚀 Explorer")
with open(file,"w") as f:
    json.dump(ach, f, indent=2)
