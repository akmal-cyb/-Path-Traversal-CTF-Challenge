# 🛡️ Path Traversal CTF Challenge

A simple web-based CTF challenge designed to teach and test **path traversal** vulnerabilities.
![image](https://github.com/user-attachments/assets/a55f4329-52b9-4a83-878d-04039357945f)


## 🕹️ Challenge Description

The application displays two images with download buttons. Clicking the buttons downloads the respective image files from the server:

http://localhost:5000/download?file=image1.jpg

However, the download endpoint is vulnerable to **path traversal**. If you manipulate the URL like this:

http://localhost:5000/download?file=../../../../etc/passwd

You can access sensitive system files such as `etc/passwd`. Somewhere in these files, a **flag** is hidden for the player to find.
## 🛠️ Features

- Built with **Python (Flask)** and **HTML/CSS**
- Vulnerable file download endpoint
- Classic Linux path traversal scenario
- Hidden flag in a sensitive file
- Great for beginner/intermediate web exploit practice

---

## 🚀 Getting Started
To run this CTF challenge locally:
📥 Installation
bash
git clone https://github.com/akmal-cyb/Path-Traversal-CTF-Challenge.git
You can run and debug the project easily in PyCharm by opening the project folder and running app.py.

🧪 Recommended Tools
Burp Suite or any intercepting proxy (to modify requests)

