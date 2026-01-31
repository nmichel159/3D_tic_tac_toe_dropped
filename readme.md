# 3D Falling Tic-Tac-Toe

## Overview

**3D Falling Tic-Tac-Toe** is a school project implemented in Python using the Tkinter GUI framework.
The application extends the classical Tic-Tac-Toe game into a three-dimensional environment with gravity mechanics, allowing players to compete on dynamically sized cubic boards.

The game supports board sizes ranging from **3×3×3 up to 5×5×5**, making it adaptable in both complexity and strategy depth.

The application runs as a standalone desktop window and is available both as a Python project (`main.py`) and as a compiled executable (`.exe`) that can be launched without a Python installation.

---

## Game Description

The game is a three-dimensional variant of Tic-Tac-Toe with the following properties:

* The board is a cubic grid of size:

  * 3×3×3
  * 4×4×4
  * 5×5×5

* A gravity mechanic is applied — pieces “fall” along one axis (similarly to Connect Four).

* The winning condition depends on the selected board size (aligning the required number of symbols in a straight line).

* The game internally supports:

  * Conversion between 2D visual representation and 3D board model
  * Dynamic board resizing

---

## Features

* Adaptive board size (3D cube from 3 to 5)
* Graphical user interface implemented in Tkinter
* Save and load game functionality
* Persistent statistics storage
* Color customization
* Conversion between 2D rendering and 3D internal representation
* Standalone executable version (.exe)
* Help screen and rules display

---

## Project Structure

```
3D_Piskvorky/
│
├── resources/               
│   ├── rules.txt
│   ├── score.db
│   ├── game.pickle
│   └── *.png
│
├── src/
│   ├── model/
│   │   ├── types.py
│   │   ├── game_logic.py
│   │   └── score_service.py
│   │
│   ├── controller/
│   │   └── persistence.py
│   │
│   └── view/
│       ├── menu.py
│       ├── help.py
│       ├── settings.py
│       ├── statistics.py
│       ├── game_graphics.py
│       └── game_plan.py
│
└── main.py
```

---

## Architectural Overview

The project follows a layered architecture inspired by the Model–View–Controller (MVC) design pattern.

### Model Layer (`src/model/`)

Responsible for core logic and data handling:

* `GameLogic` – Implements the 3D game mechanics and win detection.
* `Types` – Defines data structures and constants.
* `ScoreService` – Manages statistics and interaction with the database.

### Controller Layer (`src/controller/`)

Handles persistence operations:

* `GamePickleController` – Implements saving and loading game state using serialization (`pickle`).

### View Layer (`src/view/`)

Implements graphical components using Tkinter:

* `Menu` – Main menu interface.
* `Help` – Rules display.
* `ChoiceColor` – Color customization.
* `Statistics` – Statistics window.
* `GameGraphics` – Main game rendering.
* `GamePlan` – Auxiliary drawing logic.

---

## Installation and Execution

### Option 1 – Run via Python

Requirements:

* Python 3.x

Run the application:

```bash
python main.py
```

No additional external libraries are required beyond the Python standard library.

---

### Option 2 – Run Executable

If the `.exe` file is provided:

* Double-click the executable.
* No Python installation is required.

---

## Data Persistence

The application uses:

* `score.db` – Persistent storage of statistics
* `game.pickle` – Serialized game state for save/load functionality
* `rules.txt` – Text-based rules display

---

## Educational Purpose

This project was developed as a school assignment to demonstrate:

* Object-oriented programming in Python
* GUI development using Tkinter
* Multi-layered architecture design
* Data persistence techniques (SQLite / Pickle)
* 3D logical modeling with 2D visualization

---

## Future Improvements

Possible extensions include:

* AI opponent implementation
* Network multiplayer support
* Improved 3D visualization
* Performance optimization for larger boards

---

If you would like, I can also:

* Add a more academic-style version
* Add badges and GitHub formatting improvements
* Add UML architecture diagram
* Add a section describing the 3D win-detection algorithm formally
* Write a short project description suitable for CV / portfolio
* Create a Slovak version for school submission

Tell me which direction you prefer.
