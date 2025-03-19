# Lab 3: Grid-Based Robot Navigation Simulation

This repository contains code for a grid-based robot navigation simulation built using Python and Pygame. The simulation evolves through three versions (Lab 3(a), Lab 3(b), and Lab 3(c)) with each version introducing new functionality.

# Table of Contents

* Introduction
* Setup
* Running the Simulation

* Lab Versions
* > Lab 3(a): Basic Navigation
* > Lab 3(b): Enhanced Pathfinding
* > Lab 3(c): Nearest Task Selection
* Code Structure
* Features
* Additional Notes

# Introduction
This lab explores basic principles of autonomous navigation using an agent-based model. The agent (robot) navigates a grid to reach tasks while avoiding barriers, implementing pathfinding techniques such as BFS and nearest task selection. Through progressive versions, the lab demonstrates key concepts in simulation, pathfinding, and interactive programming.

# Setup

* Requirements
* Python 3.6 or later
* Pygame library

# Installation

Clone this repository to your local machine:

``git clone https://github.com/yourusername/lab3-grid-simulation.git``

Navigate to the repository:

``cd lab3-grid-simulation``

Install Pygame if it's not already installed:

``pip install pygame``

# Running the Simulation

Each version of the lab (Lab 3(a), Lab 3(b), Lab 3(c)) contains its own run.py file. Run each version independently to see the functionality evolve.

To Run a Version:

Navigate to the desired lab version directory (e.g., simulation_grid_lab_3(a)).

Execute the run.py script:

``python run.py``

A Pygame window will open, displaying the grid, agent, tasks, and barriers.

# Lab Versions

## Lab 3(a): Basic Navigation

**Description:** In this version, the agent navigates to complete tasks by following the Breadth-First Search (BFS) algorithm. The environment includes randomly placed barriers, which the agent avoids while navigating.

### Features:

* Basic BFS-based pathfinding.
* Simple user interface with a start button to initiate the simulation.

### Usage:

* Run run.py in simulation_grid_lab_3(a) directory.
* The agent moves to the designated tasks and avoids barriers.

## Lab 3(b): Enhanced Pathfinding

**Description:** This version builds on the basic navigation by adding additional visualization and control elements. It further optimizes pathfinding for larger grids, making the simulation more interactive and efficient.

### Features:

* Improved pathfinding with optimizations for performance.
* Enhanced UI with status updates for the agent’s position and tasks completed.

### Usage:

* Run run.py in simulation_grid_lab_3(b) directory.
* Observe the optimized pathfinding and user interface updates as the agent completes tasks.

## Lab 3(c): Nearest Task Selection
**Description:** In this final version, the agent intelligently selects the nearest task using BFS-based shortest path computation. This allows for faster task completion, as the agent always moves toward the closest task available.

### Features:

* Nearest-task pathfinding using BFS.
* Enhanced agent behavior to dynamically choose the nearest task.

### Usage:

* Run run.py in simulation_grid_lab_3(c) directory.
* The agent dynamically recalculates paths to the closest task, demonstrating efficient task completion.

# Code Structure

Each version of the lab contains the following main files:

* **agent.py:** Defines the Agent class. This class handles the agent’s properties and behaviors, including movement and pathfinding.
* **environment.py:** Defines the Environment class. This class manages the grid setup, task and barrier placement, and utility functions for boundary checking.
* **run.py:** The main script for each version. It initializes the Pygame window, environment, and agent, and handles user inputs and display rendering.

# Features
General Features

* **Grid Navigation:** The agent moves within a grid to reach designated task locations.
* **Pathfinding:** The agent navigates using Breadth-First Search and nearest-task selection to demonstrate different pathfinding strategies.
* **Dynamic Visualization:** Tasks, barriers, and agent movement are visualized on the grid, with real-time updates in each simulation.

# Specific Features by Version

## Lab 3(a):
* BFS-based pathfinding
* Basic user interface with a start button

## Lab 3(b):
* Optimized pathfinding
* Enhanced status panel with task completion updates

## Lab 3(c):
* Nearest-task selection for efficient navigation
* Real-time dynamic updates for nearest task selection

# Additional Notes
* **Adjusting Parameters:** In each run.py, you can modify parameters such as num_tasks and num_barriers in the environment setup to see how the agent responds to different configurations.
* **Troubleshooting:** If Pygame doesn’t start, ensure it is installed in the correct Python environment, and verify all file paths.

# Potential Extensions:
* Experiment with A* search algorithm for more advanced pathfinding.
* Add more agents to observe multi-agent interactions.
* Implement dynamic environments with moving barriers or randomly appearing/disappearing tasks.
