# 🌸 Minimal Desktop Todo App

A lightweight, aesthetic desktop todo application designed to enhance **focus** and **intentional digital use**, especially for ADHD users.
Built with **Python Tkinter + Flask + SQLite**, this app provides a persistent desktop overlay and intuitive task interactions — all synced locally.

---

## ✨ Original Intention

> *"Why did I open this computer/app/website?"*

This app serves as a **Digital Purpose Reminder** — a visual anchor on your screen that gently reminds you of your current goal. It aims to reduce digital distraction and help users stick to a singular task at a time.

It was specifically designed to support users with ADHD and other attention fragmentation challenges, combining persistence, minimalism, and seamless task management to help you regain control of your original intent.


## ✨ Features

- 🧊 Always-on-top floating overlay
- 🎨 Rounded white UI, minimal aesthetic
- ✅ Active task mode with inline editing
- 🔁 Local sync via Flask + SQLite
- 🧲 Drag-and-drop sorting, intuitive UX

## 🏗️ Architecture

- **Frontend**: Python Tkinter
- **Backend**: Flask + SQLite (REST API)

## 🚀 Quick Start
### 1. Install dependencies

```bash
pip install Flask Flask-SQLAlchemy requests
```
### 2. Configure API Endpoint

In `desktop_app.py`, update:

```python
API_BASE_URL = "http://127.0.0.1:5000"
```

Change to your local IP if syncing across devices (e.g., `http://192.168.1.100:5000`)

p.s.

To sync across devices on the same local network (LAN), you can take the following steps:

* Find your computer's local IP address:
  On Windows (CMD):

  ```bash
  ipconfig
  ```

  On Mac/Linux (Terminal):

  ```bash
  ifconfig
  ```
* Then replace the address like this:

  ```python
  API_BASE_URL = "http://192.168.0.100:5000"
  ```

### 3. Run the backend server

```bash
python server.py
```

### 4. Run the desktop app in another terminal

```bash
python desktop_app.py
```

## ⚠️ Notes

* The `server.py` **must be running** during use
* Data is stored in `todos.db` locally
* Debug mode is enabled (not production safe)
* Allow port 5000 through firewall if sharing on LAN
