# Todo App Feature Specifications (v2)

## Overview
A CLI-based Todo application for managing tasks in-memory with a user-friendly interface.

## Data Model
- **Task**:
  - `id`: Unique integer identifier.
  - `title`: String (required).
  - `description`: String (optional).
  - `is_completed`: Boolean (default: False).

## Core Features

### 1. ➕ Add Task
- **Input**: Title and Description.
- **Output**: 📝 Success message with the task ID.

### 2. 👀 View All Tasks
- **Format**: `ID | Status | Title`
- **Status Icons**: `✅` (Complete), `⏳` (Incomplete)
- **Output**: A clean list showing all tasks.

### 3. ✏️ Update Task
- **Input**: ID, new Title, and/or new Description.
- **Output**: 🔄 Success message with updated details.

### 4. 🗑 Delete Task
- **Input**: ID.
- **Output**: ❌ Success message confirming deletion.

### 5. ✔️ Mark Complete / 🔄 Mark Incomplete
- **Input**: ID.
- **Behavior**: Toggle status.
- **Output**: ✨ Updated status message.

## Acceptance Criteria
- CLI displays emojis in prompts and success messages.
- Command: `python main.py` triggers the app.
- No data persistence (In-memory only).
