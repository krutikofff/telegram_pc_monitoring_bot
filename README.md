# 💻 PC Hardware Monitoring Telegram Bot

An asynchronous Python application built with **Aiogram 3** and **Psutil**.
It allows users to remotely monitor their PC hardware metrics via Telegram messages.

---

## 🚀 Key Features

* **Real-time metrics** — dynamically reads your PC hardware status (CPU, RAM, disk usage).
* **Get metrics anywhere** — since the bot runs through Telegram, you can check your PC status from anywhere.
* **Process Manager (`/top`)** — a custom process tracker. Users can pass an optional argument (e.g. `/top 10`) to see the top N processes by memory usage.
* **Load Alerts** — automatically sends a warning message to Telegram if CPU or RAM load goes above a set threshold. The threshold and the on/off state can both be changed directly from the bot.
* **Customizable startup** — prompts the user in the console upon boot to configure connection settings.
* **Embedded proxy** — since Telegram is banned in Russia, a proxy is required to connect people from the region.
* **Terminal UI theme** — clean, readable output with custom formatting.
* **Advanced security** — the bot only responds to commands from the admin's Telegram ID. Any other user is blocked and shown a warning message.

---

## 🛠️ Architecture & Tech Stack

* **Language:** Python 3.12+
* **Framework:** Aiogram 3.x (Asynchronous Telegram Bot API)
* **System Metrics:** Psutil
* **Testing:** Unittest & Unittest.mock (Mocking system environments and async handlers)
* **CI/CD:** GitHub Actions (Automated workflow execution)

```text
project_root/
│
├── .github/workflows/
│   └── tests.yml           # Automated GitHub Actions testing pipeline
│
├── handlers/                # Bot controllers (Routing & Input processing)
│   ├── common.py            # Basic commands (/start, /help, /?)
│   └── monitor.py           # Core analytics processing (/status, /top, /alert_on, /alert_off, /alert_threshold)
│
├── services/                 # Core business logic
│   ├── system_info.py        # Hardcore psutil system data collection
│   └── alert_monitor.py      # Background load-checking loop and alert logic
│
├── tests/                    # Automated isolated test suite
│   ├── __init__.py
│   └── test_system.py        # Mock-based unit tests for services & handlers
│
├── .env                       # Local secret tokens (Ignored by Git)
├── .gitignore                 # Git exclusion rules
├── config.py                  # Resilient configuration loader with fallback defaults
├── main.py                    # Interactive CLI bootstrapper & entry point
└── requirements.txt           # Project dependencies
```

---

## 🧪 Testing & Automated CI/CD

The application includes an isolated unit testing module utilizing `unittest.mock`. It mocks system metrics and asynchronous Telegram interactions (using `AsyncMock`), making the tests completely independent of local machine workloads or hardware configurations.

### Run Tests Locally
To execute the test suite on your local machine, run:
```bash
python -m unittest discover -s tests -v
```

### Automated CI/CD
A GitHub Actions pipeline (`tests.yml`) is integrated into the repository. Every time code is pushed or a pull request is created on the `main` branch, an automated cloud runner spins up an Ubuntu environment, installs project dependencies, and verifies code integrity against the test suite.

---

## ⚙️ Installation & Local Setup

### 1. Clone the Repository
```bash
git clone https://github.com/krutikofff/telegram_pc_monitoring_bot
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
Execute the interactive bootstrapper:
```bash
python main.py
```
You will be prompted to choose whether a proxy connection is needed, provide a custom proxy path, and decide if a Telegram startup alert should be dispatched to the admin.

---

## 🔒 Security & Admin Access Block
The application intercepts every incoming message and validates metadata. If an unauthorized user triggers a tracking handler, the pipeline short-circuits safely:

```text
Your Telegram ID does not coincide with the ID in config.py at your PC.
Please change it to yours!
Your Telegram ID is XXXXXXXXX
```