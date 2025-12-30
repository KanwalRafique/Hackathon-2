
---

# 📝 Todo App — CLI Edition

A **command-line Todo application** built with **Spec-Driven Development (SDD)** principles and fully generated via **Claude Code** and **Spec-Kit Plus**.

Manage your tasks efficiently, with a **clean interface**, **emoji-enhanced feedback**, and **in-memory storage**.

---

## 🚀 Features

* ➕ **Add Task** — Create new tasks with title & description
* 👀 **View Tasks** — List all tasks with **ID | Status | Title** and emojis
* ✏️ **Update Task** — Edit task details selectively
* 🗑 **Delete Task** — Remove tasks by ID
* ✔️ **Toggle Complete/Incomplete** — Mark tasks done or pending with ✨ feedback

---

## 🛠 Requirements

* Python 3.13+
* UV package manager
* (Windows Users) WSL2 Ubuntu recommended

---

## ⚡ Setup & Installation

1. Ensure you have **Python 3.13+** and **UV** installed.
2. Clone the repository:

   ```bash
   git clone <your-repo-link>
   cd Todo-App
   ```
3. Run the application:

   ```bash
   python main.py
   ```

---

## 🧩 Spec-Driven Development

This project strictly follows **SDD principles**:

* Every feature is defined in `/specs`
* Code is **automatically generated** via Claude Code
* Manual coding is only allowed for **minor documented adjustments**
* Full **traceability** from specs → implementation → CLI

---

## 🎨 UI Highlights

* Menu-driven interface with clear prompts
* Emojis for better UX:

  * 📝 Task added successfully
  * 🔄 Task updated
  * ⚠️ Warnings for invalid inputs
  * ✅ / ⏳ Task completion status

Example Menu:

```
--- 📝 Todo App Menu ---
1. ➕ Add Task
2. 👀 View All Tasks
3. ✏️ Update Task
4. 🗑 Delete Task
5. ✔️ Mark Complete / 🔄 Incomplete
6. 🚪 Exit
```

---

## 📂 Repository Structure

```
/src           # Generated Python code
/specs         # Feature specifications
/specs/history # Spec evolution & revision history
README.md      # Project overview
CLAUDE.md      # Claude Code generation instructions
```

---

## 💡 About

* Fully in-memory CLI Todo App
* Built for **Hackathon II** — Spec-Driven Development mastery
* Designed as a foundation for **Phase II Full-Stack & AI integration**

---

## 🎬 Demo

Run the app:

```bash
python main.py
```

Add, view, update, delete, and toggle tasks with a smooth **emoji-enhanced experience**.

---

