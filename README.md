Minimal Desktop Todo App
A lightweight, aesthetic desktop todo application designed to enhance focus and intentional digital device use, powered by a local Flask server and SQLite database.

✨ Original Intention
This application was created to address digital distraction and attention fragmentation, particularly for ADHD individuals. In a world of constant information overload, it serves as a "Digital Purpose Reminder" to help users remember and stick to their original goals when interacting with digital devices. It achieves this by providing a persistent, minimalist visual anchor and intuitive task management.

✨ Key Features
Desktop Overlay: Stays on top, non-intrusive.

Aesthetic Design: White, rounded interface.

Local Synchronization: Data syncs via local network (requires backend server server.py to be running).

Drag-and-Drop Sorting: Intuitive reordering with a clear blue arrow indicator.

Active Task: Drag any task to the collapsed window to set it as the current focus, marked with a small circle.

Inline Editing: Double-click text to edit directly.

Stable Operations: Window remains expanded during task interactions (complete, delete, drag).

Text Wrapping: Long task descriptions automatically wrap.

🏗️ Architecture
Frontend (Desktop App): Built with Python Tkinter for the user interface and interaction with the backend API.

Backend (Flask Server): A Python Flask application managing data storage in a local SQLite database and providing a RESTful API.

🚀 Quick Start
1. Prerequisites
Python 3.x

pip

2. Get the Code
Download server.py and desktop_app.py to the same folder.

3. Install Dependencies
Open your command line (CMD or PowerShell), navigate to the project directory, and run:

pip install Flask Flask-SQLAlchemy requests

4. Configure Frontend (desktop_app.py)
Open desktop_app.py and locate API_BASE_URL.

For Local Use: You can use http://127.0.0.1:5000.

For Local Network Sharing: Replace with the local IP address of the computer running server.py (e.g., http://192.168.101.6:5000).

5. Run the Application
This application requires both the backend server and the frontend desktop app to be running simultaneously.

Start Backend (server.py):

Open your first command line window, cd to the directory, and run python server.py. Keep this window open.

Start Frontend (desktop_app.py):

Open your second separate command line window, cd to the directory, and run python desktop_app.py. The desktop overlay window should appear.

💡 Usage Guide
Desktop Overlay Window (Collapsed Mode)
Expand/Collapse: Click any blank area of the window.

Drag Window: Hold and drag any blank area of the window.

Active Task: Displays the current task; click "✔" to complete.

Expanded List Mode
Operations: Add via input box, complete with checkbox, delete with "X" button, double-click text to edit.

Drag-and-Drop Sorting: Click and hold text to drag; a blue arrow indicates the drop position. Release to reorder. Can be set as the active task by dragging to the collapsed window area.

Stability: Window remains expanded during all operations.

⚠️ Important Notes
Server Must Run: The server.py backend must be running whenever you use the desktop app or wish to sync data.

Firewall: For sharing the service, ensure your computer's firewall allows incoming connections on port 5000.

Data Storage: Data is stored in the local todos.db file. Deleting this file will result in data loss.

Production Environment: The Flask server is configured with debug=True, which is not suitable for production.

极简桌面待办事项软件
轻量、美观的桌面待办事项应用，旨在帮助您专注使用数字设备，通过本地 Flask 服务器和 SQLite 数据库实现数据管理与同步。

✨ 初心
本应用旨在解决数字时代信息碎片化和注意力分散的问题，尤其对 ADHD (注意力缺陷多动障碍) 人群友好。在浏览网页时，我们常被大量信息干扰，忘记使用设备的初衷。

本软件作为**“数字目的提醒器”**，通过以下方式提供帮助：

持续视觉锚点： 桌面顶部的悬浮待办事项，时刻提醒核心任务，防止注意力漂移。

极简无干扰： 界面极致简约，避免额外信息干扰，助您聚焦。

直观操作： 拖放排序、双击编辑等，降低认知负担，简化任务管理。

即时反馈： 任务完成、编辑、排序等操作的即时视觉反馈和数据同步，增强掌控感。

我们希望此工具能帮助用户，特别是 ADHD 群体，在数字世界中保持专注，明确使用设备的“初心”，从而更高效、有目的地利用时间。

✨ 主要功能
桌面悬浮： 窗口置顶，不干扰。

美观设计： 白色圆角界面。

本地同步： 局域网内数据同步（需后端运行）。

拖放排序： 直观拖放，蓝色箭头指示。

“进行中”任务： 拖至悬浮框设为当前任务，有小圆点。

内联编辑： 双击文本直接修改。

操作稳定： 任务操作时窗口保持展开。

文本换行： 长文本自动换行。

🏗️ 架构
前端 (桌面应用): Python Tkinter，负责界面与后端交互。

后端 (Flask 服务器): Python Flask + SQLite，负责数据存储和 API。

🚀 快速开始
1. 前提
Python 3.x

pip

2. 获取代码
下载 server.py 和 desktop_app.py 至同一文件夹。

3. 安装依赖
打开命令行，导航到项目目录，运行：

pip install Flask Flask-SQLAlchemy requests

4. 配置前端 (desktop_app.py)
打开 desktop_app.py，找到 API_BASE_URL。

本机使用： 可用 http://127.0.0.1:5000。

局域网共享： 替换为运行 server.py 电脑的局域网 IP (如 http://192.168.101.6:5000)。

5. 运行应用
本应用需要同时运行后端服务器和前端桌面应用。

启动后端 (server.py)：

打开第一个命令行窗口，cd 到文件目录，运行 python server.py。保持窗口打开。

启动前端 (desktop_app.py)：

打开第二个独立的命令行窗口，cd 到文件目录，运行 python desktop_app.py。桌面悬浮窗口将出现。

💡 使用指南
桌面悬浮窗口 (收缩模式)
展开/收缩： 单击窗口空白区域。

拖动窗口： 按住窗口空白区域拖动。

“进行中”任务： 显示当前任务，点击“✔”完成。

展开模式下的列表
操作： 输入框添加，复选框完成，X 按钮删除，双击文本编辑。

拖放排序： 单击并按住文本拖动，蓝色箭头指示位置，释放重排。可设为“进行中”任务。

稳定性： 操作期间窗口保持展开。

⚠️ 重要提示
服务器运行： 每次使用桌面应用或同步时，都必须先启动 server.py。

防火墙： 共享服务需配置防火墙。

数据存储： 数据在本地 todos.db，删除文件会丢失数据。

生产环境： Flask 服务器 debug=True 不适用于生产环境。
