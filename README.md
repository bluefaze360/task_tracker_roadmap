

<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">


# Task Tracker CLI Application

<em>Transform Tasks Into Triumphs with Seamless Clarity</em>

<!-- BADGES -->
<img src="https://img.shields.io/github/last-commit/bluefaze360/task_tracker_roadmap?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/bluefaze360/task_tracker_roadmap?style=flat&color=0080ff" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/bluefaze360/task_tracker_roadmap?style=flat&color=0080ff" alt="repo-language-count">

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/JSON-000000.svg?style=flat&logo=JSON&logoColor=white" alt="JSON">


</div>
<br>

---

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Testing](#testing)
- [Running the Task Tracker CLI](#running-the-task-tracker-cli)
    - [List of Commands](#list-of-commands)
    - [Examples](#examples)
- [Project Link](#project-link)

---

## Overview

Task Tracker Roadmap is a lightweight command-line tool that helps developers organize, update, and monitor project tasks efficiently. It leverages JSON files for persistent storage and provides a straightforward interface for managing task statuses and workflows.

**Why task_tracker_roadmap?**

This project aims to simplify task management within your development process. The core features include:

- **📝** **Memo**: Command-line interface for adding, updating, deleting, and listing tasks
- **🌟** **Star**: Persistent JSON storage ensures your task data is always saved and retrievable
- **🚦** **Traffic Light**: Track task statuses like pending, in progress, and completed for clear progress visibility
- **🔧** **Wrench**: Supports workflow updates and milestone monitoring to keep projects on track
- **📋** **Clipboard**: Provides a structured overview of tasks, facilitating prioritization and accountability

---

## Getting Started

### Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python
- **Package Manager:** Conda

### Installation

Build task_tracker_roadmap from the source and install dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/bluefaze360/task_tracker_roadmap
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd task_tracker_roadmap
    ```

3. **Install the dependencies:**

**Using [conda](https://docs.conda.io/):**

```sh
❯ conda env create -f conda.yml
```

### Usage

Run the project with:

**Using [conda](https://docs.conda.io/):**

```sh
conda activate {venv}
python {entrypoint}
```

### Testing

Task_tracker_roadmap uses the {__test_framework__} test framework. Run the test suite with:

**Using [conda](https://docs.conda.io/):**

```sh
conda activate {venv}
pytest
```

## Running the Task Tracker CLI

When the CLI initializes, the CLI will wait for you to enter a command:<br>
<img width="118" height="26" alt="Screenshot 2025-08-23 at 10 41 52 PM" src="https://github.com/user-attachments/assets/a2251adf-8886-42fb-bc39-e2423c551a86" />
<br>

### List of Commands:

**add "Task description"** - adds the task to the tracker <br>
**update "task id" "Task description"** - finds task using the id, then updates the task description <br>
**delete "task id"** - finds task using the id, then deletes task <br>
<br>
**mark-in-progress "task id"** - changes the status of the task to "in-progress"<br>
**mark-done "task id** - changes the status of the task to "done"<br>
<br>
**list** - lists all tasks<br>
**list-done** - lists finished tasks<br>
**list-in-progress** - lists in progress tasks<br>
**list-todo** - lists pending tasks<br>

### Examples:


**add "Do dishes"** - Adds task "Do dishes" to the tracker <br>
**update 1 "Do the dishes in the sink"** - Updates "Do dishes" task description (since the task has an id of 1) to "Do the dishes in the sink" <br>
**mark-in-progress 1** - Marks task - that has an id of 1 - to "in-progress" <br>
**delete 1** <br>

## Project Link

https://roadmap.sh/projects/task-tracker

---

<div align="left"><a href="#top">⬆ Return</a></div>

---
