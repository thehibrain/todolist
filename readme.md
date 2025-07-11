# ✅ ToDoCLI

**ToDoCLI** is a simple command-line to-do list manager written in Python. Tasks are stored in a JSON file so they persist between runs. Great for practicing structured data, file I/O, and user interaction.

---

##  Features

- Add tasks
- List all tasks with completion status
- Mark tasks as complete 
- Delete tasks 
- Data saved automatically to `todo.json`

---

##  Project Structure

ToDoCLI/
├── todo.py # Main program file
├── todo.json # Task storage (auto-created)
└── README.md # This file


---

## ▶️ How to Run

```bash
python todo.py


1. View Tasks
2. Add Task
3. Mark Complete
4. Delete Task
5. Exit

Data File

Tasks are saved in todo.json.
Here’s an example of what it looks like:

[
  { "title": "Fix leaking pipe", "done": false },
  { "title": "Call supplier", "done": true }
]

Requirements

    Python 3.x

    No external libraries

 Notes

    If todo.json is missing or corrupted, the app starts fresh

    Designed for freelance/demo use, but easily expandable

 License

This project is free to use, modify, or share.
