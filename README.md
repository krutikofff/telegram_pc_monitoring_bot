# 💻 PC Hardware Monitoring Telegram Bot

An asynchronous Python application built with **Aiogram 3** and **Psutil** that allows users to remotely monitor their computer's hardware metrics (CPU workload, RAM utilization, storage capacity, and active processes) via Telegram messages. 

The project features a modular architecture, robust security layers, comprehensive unit testing, and an automated CI/CD pipeline.

---

## 🚀 Key Features

* **Real-time Hardware Metrics**: Dynamically fetches CPU percent, virtual memory (RAM), and automatically aggregates statistics across all connected logical drives (SSD/HDD).
* **Process Manager (`/top`)**: Features a custom process tracker. Users can pass an optional argument (e.g., `/top 10`) to view the most memory-consuming active processes with full `ValueError` validation.
* **Interactive CLI Startup**: Prompts the user in the console upon boot to configure proxy connections dynamically and choose whether to send a startup notification message to the administrator.
* **Resilient Connection**: Optimized for restricted network environments by leveraging explicit `AiohttpSession` routing via custom proxy inputs.
* **Terminal UI Theme**: Clean, professional HTML-formatted output with custom pseudo-graphic layout frames for seamless readability.
* **Advanced Security**: Restricts access strictly to the system administrator based on their unique Telegram ID. Unauthorized users are blocked with a localized alert.

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
│   └── tests.yml         # Automated GitHub Actions testing pipeline
│
├── handlers/             # Bot controllers (Routing & Input processing)
│   ├── common.py         # Basic commands (/start, /help, /?)
│   └── monitor.py        # Core analytics processing (/status, /top)
│
├── services/             # Core business logic
│   └── system_info.py    # Hardcore psutil system data collection
│
├── tests/                # Automated isolated test suite
│   ├── __init__.py       
│   └── test_system.py    # Mock-based unit tests for services & handlers
│
├── .env                  # Local secret tokens (Ignored by Git)
├── .gitignore            # Git exclusion rules
├── config.py             # Resilient configuration loader with fallback defaults
├── main.py               # Interactive CLI bootstrapper & entry point
└── requirements.txt      # Project dependencies
```

---

## 🧪 Testing & Automated CI/CD

The application includes an isolated unit testing module utilizing `unittest.mock`. It mocks system metrics and asynchronous Telegram interactions (using `AsyncMock`), making the tests completely independent of local machine workloads or hardware configurations.

### Run Tests Locally
To execute the test suite on your local machine, run:
```bash
python -m unittest discover -s tests
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
