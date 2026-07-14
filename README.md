# 💻 PC Hardware Monitoring Telegram Bot

An asynchronous Python application built with **Aiogram 3** and **Psutil** that allows users to remotely monitor their computer's hardware metrics (CPU workload, RAM utilization, and storage capacity) via Telegram messages. 

---

## 🚀 Key Features

* **Real-time Hardware Metrics**: Dynamically fetches CPU percent, virtual memory (RAM), and automatically scans all connected logical drives (SSD/HDD).
* **Advanced Security**: Restricts access strictly to the system administrator based on their unique Telegram ID. Unknown users receive a localized English warning message block.
* **Resilient Connection**: Optimized for restricted network environments by leveraging explicit `AiohttpSession` routing via local proxy clients (such as Happ/Hiddify).
* **Terminal UI Theme**: Clean, professional HTML-formatted output with pseudo-graphic frames for seamless scannability.

---

## 🛠️ Architecture & Tech Stack

* **Language:** Python 3.12+
* **Framework:** Aiogram 3.x (Asynchronous Telegram Bot API)
* **System Metrics:** Psutil
* **Environment Configuration:** Python-dotenv
* **Network & Proxy Support:** Aiohttp-socks

```
project_root/
│
├── .env                  # Local secret tokens (Ignored by Git)
├── config.py             # Configuration loader & Environment variables
├── main.py               # Main asynchronous execution entry point
│
├── handlers/             # Bot controllers (Routing & Input processing)
│   ├── common.py         # Basic commands (/start)
│   └── monitor.py        # Core analytics processing (/status)
│
└── services/             # Core business logic
    └── system_info.py    # Hardcore psutil system data collection
```

---

## ⚙️ Installation & Local Setup

### 1. Clone the Repository
```bash
git clone https://github.com
cd telegram_pc_monitoring_bot
```

### 2. Configure Environment Variables
Create a `.env` file in the root directory:
```text
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN_FROM_BOTFATHER
ADMIN_ID=YOUR_NUMERIC_TELEGRAM_CHAT_ID
```

### 3. Establish Virtual Environment & Install Dependencies
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
```

### 4. Run the Application
```bash
python main.py
```

*Note: If you are running the bot in a restricted network, ensure your local SOCKS5/HTTP proxy client is active on the ports specified in `main.py`.*

---

## 🔒 Security & Admin Access Block
The application intercepts every message and validates the sender's metadata. If an unauthorized user triggers the `/status` command, the bot securely short-circuits the pipeline:

```text
Your Telegram ID does not coincide with the ID in config.py at your PC.
Please change it to yours!
Your Telegram ID is XXXXXXXXX
```
