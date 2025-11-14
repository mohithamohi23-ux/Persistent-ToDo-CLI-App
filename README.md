# Persistent-ToDo-CLI-App
A persistent command-line To-Do application built in Python. This application demonstrates file handling, lists and string manipulation by saving tasks to a text file and allowing add, view, remove and mark-done operations.

**📌 Features**

✅ Add tasks

Add new tasks to your to-do list.

✅ View tasks

Display all tasks with clear status indicators

[ ] → Pending

[x] → Completed

✅ Remove tasks

Delete a specific task using its task number.

✅ Mark tasks as done

Change the status of a task from pending to completed.

✅ Clear completed tasks

Remove all tasks that are marked as done.

✅ Persistent storage

Tasks are saved in tasks.txt, so they remain even after closing the program.

**🗂️ FILES INCLUDED**

todo.py      → Main application code

tasks.txt    → Stores all tasks (auto-created if not present)

README.md    → Documentation (this file)

**AVAILABLE COMMANDS**

Command	Description

| Command        | Description                     |
| -------------- | ------------------------------- |
| `view`         | Shows all tasks                 |
| `add <task>`   | Adds a new task                 |
| `remove <num>` | Removes task number `<num>`     |
| `done <num>`   | Marks task `<num>` as completed |
| `clear`        | Deletes all completed tasks     |
| `help`         | Shows available commands        |
| `exit`         | Closes the application          |

**HOW PERSISTENCE WORKS**

The program saves each task in the following format inside tasks.txt:

0|Buy groceries
1|Complete homework
0|Call mom

0 → not done

1 → done

When you restart the app, it loads tasks back into a Python list automatically.

**WHAT I LEARNED**

Working on this Python To-Do List application helped me understand several important programming concepts. Here are the key things I learned:

**1. File Handling in Python**

I learned how to:

Open files using different modes (r, w, a, r+)

Read and write data to a text file

Use file handling to store data permanently (persistence)

Use with open() to automatically close files and avoid errors

**2. Lists and Data Structures**

I used a Python list to store tasks in memory.
Through this, I learned:

How to append, insert, update, and remove items

Difference between append() and insert()

How to access and modify list elements using indexing

How to filter lists using list comprehensions

**3. String Manipulation**

I used string functions like:

.strip() to remove extra spaces and newlines

.split() to separate task status and text

String formatting to display clean output

**4. Building a CLI (Command Line Interface) Application**

I learned how to:

Take user input continuously using loops

Parse commands like add, view, done, remove

Provide a simple text-based menu

Handle invalid inputs safely

**5. Data Persistence Logic**

I learned how to store each task in a text file in the format:

status|task_text


This helped me understand:

How to load data when the program starts

How to save updated tasks after every operation

**6. Clean Code Practices**

I improved my understanding of:

Breaking logic into small, reusable functions

Keeping code readable

Using comments and docstrings

Handling edge cases (empty input, invalid task numbers)



