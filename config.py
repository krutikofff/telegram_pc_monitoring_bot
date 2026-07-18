import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

ALERT_ENABLED = True
CPU_THRESHOLD = 85
RAM_THRESHOLD = 85
ALERT_INTERVAL = 300