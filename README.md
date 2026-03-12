# 🛡️ Web-Health-Monitor

This **Python 3.13** system uses `httpx` and `asyncio` to monitor website health in parallel, storing real-time status and HTTP codes in a persistent **SQLite** database. It features an automated heartbeat loop that logs performance history and triggers alerts whenever a target site is unreachable.

## 🚀 Features
* **Asynchronous I/O:** Monitors multiple sites simultaneously without blocking.
* **Persistent Storage:** Logs all check results using `aiosqlite`.
* **Real-time Alerts:** Instant console warnings for "DOWN" status.
* **Automated Heartbeat:** Runs on a 60s configurable loop.

---

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/KilladiJoel/Sentinel_project.git](https://github.com/KilladiJoel/Sentinel_project.git)
   cd Sentinel_project
