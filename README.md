# Claire

Claire is a Python-based AI agent that automatically fixes and debugs code using Google's Gemini API. This project demonstrates how modern AI development tools like Cursor and Claude Code work under the hood.

## What It Does
Claire acts as an intelligent coding assistant that can:

* Analyze your codebase by scanning directories and reading files
* Identify bugs and issues in your code
* Automatically write fixes and improvements
* Test changes by executing Python files
* Iterate until problems are resolved

Simply describe your coding problem in natural language, and the agent will work autonomously to solve it.

## Example Usage
```
python3 main.py "fix my calculator app, its not starting correctly"
# Agent automatically scans files, identifies issues, applies fixes, and tests the solution
```

## Technical Features
* Autonomous operation - Agent decides which tools to use and when
* File system integration - Read, write, and analyze code files
* Code execution - Test fixes by running Python scripts
* Iterative problem-solving - Continues working until task completion
* Natural language interface - Describe problems in plain English

## Prerequisites
* Python 3.10+
* Google Gemini API access
* Unix-like shell environment
