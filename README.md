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

### 2. Run the backend server

```bash
python server.py
```

### 3. Run the desktop app in another terminal

```bash
python desktop_app.py
```
