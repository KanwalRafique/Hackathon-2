# Todo App Feature Specifications

## Overview
A CLI-based Todo application for managing tasks in-memory.

## Data Model
- **Task**:
  - `id`: Unique integer identifier.
  - `title`: String (required).
  - `description`: String (optional).
  - `is_completed`: Boolean (default: False).

## Core Features

### 1. Add Task
- **Input**: Title and Description.
- **Behavior**: Create a new Task object with a unique ID and `is_completed=False`.
- **Output**: Success message with the task ID.

### 2. View Tasks
- **Input**: None.
- **Behavior**: List all tasks currently in memory.
- **Output**: Formatted table or list showing ID, Status ([x] for complete, [ ] for incomplete), Title, and Description.

### 3. Update Task
- **Input**: ID, new Title (optional), new Description (optional).
- **Behavior**: Find task by ID. Update provided fields.
- **Output**: Success or "Task not found" error.

### 4. Delete Task
- **Input**: ID.
- **Behavior**: Remove task from memory by ID.
- **Output**: Success or "Task not found" error.

### 5. Mark Task Complete/Incomplete
- **Input**: ID, toggle action.
- **Behavior**: Set `is_completed` to True or False for the specific ID.
- **Output**: Success message showing the new status.

## Acceptance Criteria
- CLI interface handles all inputs.
- Invalid IDs handle gracefully.
- IDs are persistent/sequential during the session.
