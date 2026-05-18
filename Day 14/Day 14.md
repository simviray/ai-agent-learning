# Day 14 — Git, GitHub, and Saving Your AI Project Professionally

## Goal for Today

Learn how to save your project using Git and prepare it for GitHub.

Today you will learn:

* Git basics
* repositories
* commits
* `.gitignore`
* GitHub project workflow

Estimated time: **2.5–3 hours**

---

# PART 1 — Review Day 13

Your project should now include:

```text
ai_btc_agent/
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
├── config.py
├── market_data.py
├── agent_logic.py
├── logger.py
├── check_environment.py
└── logs/
```

Run:

```bash
python main.py
```

---

# Concept Explanation — What Is Git?

Git is a version control tool.

It helps you:

* save project history,
* track changes,
* restore old versions,
* and organize software development.

Think of Git like:

```text
Save points for your code.
```

---

# PART 2 — Check Git Installation

Run:

```bash
git --version
```

If Git is installed, you will see something like:

```text
git version 2.x.x
```

---

# Concept Explanation — Why Git Matters

Professional developers use Git because projects change constantly.

Git helps answer:

```text
What changed?
When did it change?
Who changed it?
Can I go back to an older version?
```

This is essential for:

* AI projects
* cloud apps
* GitHub
* team collaboration
* professional portfolios

---

# PART 3 — Initialize Git Repository

Inside your project folder, run:

```bash
git init
```

---

# Concept Explanation — What Is a Repository?

A repository, or repo, is a folder tracked by Git.

When you run:

```bash
git init
```

Git starts watching your project for changes.

---

# PART 4 — Check Project Status

Run:

```bash
git status
```

You will see files that are not yet tracked.

---

# Concept Explanation — What Is `git status`?

`git status` shows:

* new files,
* modified files,
* deleted files,
* and what is ready to commit.

Use it often.

---

# PART 5 — Review `.gitignore`

Make sure your `.gitignore` contains:

```text
.env
logs/
__pycache__/
.venv/
```

---

# Concept Explanation — Why `.gitignore` Matters

`.gitignore` tells Git:

```text
Do not track these files.
```

This protects:

* private settings,
* API keys,
* logs,
* virtual environment files,
* and temporary Python files.

Never upload `.env` to GitHub.

---

# PART 6 — Stage Your Files

Run:

```bash
git add .
```

---

# Concept Explanation — What Is Staging?

Staging means:

```text
Prepare files to be saved in the next commit.
```

Git does not automatically save everything.

You choose what to include.

---

# PART 7 — Make Your First Commit

Run:

```bash
git commit -m "Initial AI BTC agent project"
```

---

# Concept Explanation — What Is a Commit?

A commit is a saved snapshot of your project.

A good commit message explains what changed.

Example:

```text
Initial AI BTC agent project
```

---

# PART 8 — Create a GitHub Repository

On GitHub, create a new repository named:

```text
ai-btc-agent
```

Recommended settings:

* Public if you want portfolio visibility
* Private if you want to keep it personal
* Do NOT add README because you already have one
* Do NOT add `.gitignore` because you already have one

---

# PART 9 — Connect Local Project to GitHub

GitHub will show commands similar to this:

```bash
git remote add origin https://github.com/YOUR_USERNAME/ai-btc-agent.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

---

# Concept Explanation — What Is `origin`?

`origin` is the nickname for your GitHub repository.

It tells Git:

```text
This is where my online project lives.
```

---

# PART 10 — Professional Git Workflow

Use this cycle:

```bash
git status
git add .
git commit -m "Describe your change"
git push
```

---

# Concept Explanation — What Is `git push`?

`git push` uploads your local commits to GitHub.

This makes your code:

* backed up online,
* shareable,
* and portfolio-ready.

---

# PART 11 — Add Git Command Notes

Create:

```text
git_notes.py
```

Code:

```python
# This file is not part of the AI agent system.
# It is a simple reference file for Git commands.

# Check Git version:
# git --version

# Start Git tracking in the current folder:
# git init

# Check file status:
# git status

# Stage all files:
# git add .

# Save a project snapshot:
# git commit -m "Your message here"

# Connect to GitHub:
# git remote add origin https://github.com/YOUR_USERNAME/ai-btc-agent.git

# Rename branch to main:
# git branch -M main

# Upload code to GitHub:
# git push -u origin main
```

---

# Concept Explanation — Why Keep Notes?

Beginner developers forget commands often.

Keeping notes helps you:

* practice faster,
* reduce mistakes,
* and build confidence.

---

# DAY 14 CHECKLIST

## Concepts Understood

* [ ] Git
* [ ] Repository
* [ ] Commit
* [ ] Staging
* [ ] `.gitignore`
* [ ] GitHub remote
* [ ] Push

## Tasks Completed

* [ ] Checked Git installation
* [ ] Initialized Git repo
* [ ] Checked `git status`
* [ ] Confirmed `.gitignore`
* [ ] Created first commit
* [ ] Created GitHub repo
* [ ] Connected local repo to GitHub
* [ ] Pushed project to GitHub
* [ ] Created `git_notes.py`

---

# What You Learned Today

Today you learned how professional developers save and share projects.

This is important for:

* AI portfolios
* job applications
* cloud deployment
* GitHub projects
* team collaboration
* software version control

---

# Bonus Task

Update your `README.md` and add this section:

````markdown
# Git Workflow

Check project status:

```bash
git status
````

Stage changes:

```bash
git add .
```

Commit changes:

```bash
git commit -m "Describe your update"
```

Push to GitHub:

```bash
git push
```

```

This makes your project documentation more complete.
```
