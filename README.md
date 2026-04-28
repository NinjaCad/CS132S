# CS132S Portfolio (Spring 2026)

A portfolio of **TMU CS132S (Data Structures & Algorithms)** homework assignments written in **Python**.

## How to run
Most assignments are standalone scripts:

```bash
python Homework01.py
```

Notes:
- Assignments may prompt for interactive input.
- `Homework10.py` reads `prereq.txt`.

## Repository contents (file-by-file)

### Assignments
- **`Homework01.py`** — Compares two algorithms for finding the smallest difference between two list elements (O(n²) vs. sort-based approach) and times them.
- **`Homework02.py`** — Converts a prefix expression to postfix using a simple `Stack`.
- **`Homework03.py`** — Implements radix sort using per-digit `Queue`s and prints each radix pass.
- **`Homework04.py`** — Recursive turtle drawing (a subdividing pattern) based on a user-supplied recursion level.
- **`Homework05.py`** — Dynamic programming solution to the string edit distance (“STORE”: insert/delete/substitute) including printing the DP table.
- **`Homework06.py`** — Implements and compares classic sorting algorithms (bubble/selection/insertion/shell/merge/quick) and reports comparisons/assignments.
- **`Homework07.py`** — Double-ended priority queue (DEPQ) implemented with a binary min–max heap; includes a demo driver.
- **`Homework08.py`** — Binary Search Tree implementation with insertion, lookup, deletion, iteration, and a formatted `__str__` display.
- **`Homework09.py`** — “Flipper” coin puzzle solver: models the 3×3 flip game as a graph, uses BFS to find a solution path, and can auto-solve.
- **`Homework10.py`** — Reads course prerequisites from `prereq.txt` and performs a topological sort using DFS timestamps.

### Assignment references / data
- **`instructions.txt`** — Assignment writeups, sample I/O, and rubrics for the homework set.
- **`prereq.txt`** — Input data for `Homework10.py` (course prerequisites).

## Overview
This repo is organized as one script per homework assignment (`Homework01.py` … `Homework10.py`). The assignments focus on core data structures (stacks, queues, trees, heaps, graphs), algorithm analysis (Big-O and timing), and classic algorithms (radix sort, multiple comparison sorts, BFS/DFS, topological sorting, and dynamic programming).
