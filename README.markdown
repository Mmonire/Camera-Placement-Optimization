# Camera Placement Optimization Project

## Overview
This project focuses on solving the **Camera Placement Optimization Problem**, a combinatorial optimization problem aimed at minimizing the number of cameras required to cover a set of points while ensuring all points are monitored. The project implements two distinct approaches: a **Tabu Search** heuristic algorithm and an **Integer Programming (IP)** model. Additionally, a data generation script is included to create test instances.

The project is implemented in Python and includes scripts for generating test data, solving the problem using Tabu Search, and solving it using Integer Programming with CPLEX. The accompanying presentation provides detailed explanations of the methodologies and results.

## Project Structure
The repository contains the following files:
- **CM.py**: Implements the Tabu Search algorithm to optimize camera placement.
- **IP.py**: Implements the Integer Programming model using CPLEX to find the optimal camera placement.
- **make.py**: Generates random test instances for the camera placement problem.
- **Presentation-pdf.pdf**: A presentation (in Persian) explaining the problem, algorithms, and results.
- **p12-c6.txt**: A sample input file containing points and camera coverage data.

## Prerequisites
To run the scripts, you need the following dependencies:
- **Python 3.x**
- **CPLEX**: Required for running the Integer Programming model (`IP.py`). Install the IBM CPLEX Optimizer and the `docplex` Python package.
  ```bash
  pip install docplex
  ```
- **Standard Python Libraries**: `random`, `time` (included in Python standard library).

Ensure the input file (`p12-c6.txt`) is in the same directory as the scripts.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Install the required Python packages:
   ```bash
   pip install docplex
   ```
3. Ensure CPLEX is installed and configured for use with `docplex`. Refer to the [IBM CPLEX documentation](https://www.ibm.com/docs/en/cplex) for setup instructions.

## Usage

### 1. Generating Test Data
The `make.py` script generates random test instances with points and camera coverage groups.
- **Run the script**:
  ```bash
  python make.py
  ```
- **Output**: The script prints a list of points (e.g., `p1, p2, ..., p200`) and camera groups (e.g., `c1: p1, p3, p5`), which can be saved to a file (e.g., `p12-c6.txt`) for use with the other scripts.
- **Customization**:
  - Modify `num_groups` (20–50) to change the number of initial camera groups.
  - Adjust `target_groups` (default: 100) to set the total number of camera groups.
  - Change the group size range (3–4 points per group) in the script if needed.

### 2. Running the Tabu Search Algorithm
The `CM.py` script implements the Tabu Search algorithm to find a near-optimal solution for camera placement.
- **Run the script**:
  ```bash
  python CM.py
  ```
- **Input**: The script reads from `p12-c6.txt` (or another specified input file).
- **Output**:
  - Selected cameras and their count.
  - Execution time.
  - Number of aspiration criteria uses.
  - A log file (`tabu_search_log.txt`) containing iteration details (best cost, tabu violations, aspiration uses).
- **Customization**:
  - Adjust `max_iter` (default: 500) to change the number of iterations.
  - Modify `tabu_size` (default: 20) to set the tabu list size.
  - Enable/disable `aspiration_criteria` (default: `True`) to control aspiration usage.

### 3. Running the Integer Programming Model
The `IP.py` script uses CPLEX to solve the camera placement problem optimally.
- **Run the script**:
  ```bash
  python IP.py
  ```
- **Input**: The script reads from `p12-c6.txt` (or another specified input file).
- **Output**:
  - Optimal number of cameras.
  - List of selected cameras with their coverage.
  - Warning if any points are uncovered.
- **Note**: Requires CPLEX to be installed and configured.

### 4. Input File Format
The input file (e.g., `p12-c6.txt`) should follow this format:
```
points: p1, p2, p3, ..., pn
c1: p1, p3, p5
c2: p2, p4, p6
...
```
- The first line lists all points to be covered, separated by commas.
- Subsequent lines define cameras (e.g., `c1`, `c2`) and the points they cover.

## Presentation
The `Presentation-pdf.pdf` file contains a detailed explanation of the project (in Persian), including:
- Introduction to the camera placement problem.
- Description of the Tabu Search and Integer Programming approaches.
- Mathematical formulations.
- Sample results and analysis.

Note: The OCR-extracted content from the PDF contains repetitive and potentially corrupted text, making some sections unreadable. Key sections (e.g., Tabu Search and Integer Programming explanations) are referenced, but the presentation may require manual review for clarity.

## Results
- **Tabu Search (CM.py)**: Provides a heuristic solution that is typically fast but may not guarantee optimality. Suitable for large instances where computation time is a concern.
- **Integer Programming (IP.py)**: Guarantees an optimal solution but may be slower for large instances due to the computational complexity of CPLEX.
- **Sample Output** (for `p12-c6.txt`):
  - Tabu Search: Outputs selected cameras, number of cameras, execution time, and aspiration uses.
  - Integer Programming: Outputs the optimal number of cameras and their coverage details.

## References
The presentation cites the following works:
1. Hu Teng, Ishtiaq Ahmad, Alamqir MSM, "3D Optimal Surveillance Trajectory Planning for Multiple UAVs by Using Particle Swarm Optimization With Surveillance Area Priority."
2. Quadri Nooruhasan Naveed, Hamed Alqhtani, "An Intelligent Traffic Surveillance System Using Integrated Wireless Sensor Network and Improved Phase Timing Optimization."
3. Andries M. Heyys, "Optimisation of surveillance camera site locations and viewing angles using a novel multiattribute, multi-objective genetic algorithm. A day/night anti-poaching application."
4. Maged Faiban Aloaubi, "Computational Intelligence-Based Harmony Search Algorithm for Real-Time Object Detection and Tracking in Video Surveillance Systems."
