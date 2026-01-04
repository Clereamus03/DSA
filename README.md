# DSA Practice Repository

This repository contains my solutions to Data Structures and Algorithms problems in both Python and Java.

## Repository Structure

```
DSA/
├── category-name/                 # Data structure category (e.g., arrays, trees)
│   └── problems/
│       └── problem-name/
│           ├── README.md          # Problem link, description, and metadata
│           ├── attempts/         # All solutions (attempts and revisions)
│           │   ├── python/
│           │   │   ├── attempt_1.py
│           │   │   ├── attempt_2.py
│           │   │   └── ...
│           │   ├── java/
│           │   │   ├── attempt_1.java
│           │   │   ├── attempt_2.java
│           │   │   └── ...
│           │   └── cpp/
│           │       ├── attempt_1.cpp
│           │       ├── attempt_2.cpp
│           │       └── ...
│           └── reflection.md     # Approach, complexity analysis, learnings
├── arrays/                        # Example: Arrays category
├── linked-list/                   # Example: Linked List category
├── trees/                         # Example: Trees category
└── README.md                      # This file
```

## How to Use

1. **Starting a New Problem**: Use the helper script: `python create_problem.py <category> <problem-name>`
2. **Problem Setup**: Fill in the `README.md` with the problem link and description
3. **First Solution**: Write your solution in `attempts/python/attempt_1.py`, `attempts/java/attempt_1.java`, or `attempts/cpp/attempt_1.cpp`
4. **Track Attempts**: Save all your attempts in the `attempts/python/` and `attempts/java/` folders
5. **Revision**: When practicing again, save new attempts with higher numbers (e.g., `attempt_2.py`, `attempt_3.py`)
6. **Reflection**: Document your approach, time/space complexity, and key learnings in `reflection.md`

## Testing Solutions

Use the `test.py` script to run and test your solutions. Supported languages: **Python**, **Java**, and **C++**. There are two ways to use it:

### Quick Testing (Recommended for Active Development)

Test your solutions directly with command-line arguments:

**Test latest attempt:**
```bash
python test.py <category> <problem> <language>
```

**Test specific attempt:**
```bash
python test.py <category> <problem> <attempt> <language>
```

**Examples:**
```bash
# Test latest Python solution for three-sum
python test.py arrays three-sum python

# Test C++ solution
python test.py arrays three-sum cpp

# Test specific attempt
python test.py arrays three-sum attempt_1 python

# Test Java solution
python test.py arrays three-sum attempt_1 java
```

### Interactive Mode

Run without arguments for an interactive menu:
```bash
python test.py
```

This will guide you through selecting:
1. Language (Python, Java, or C++)
2. Category
3. Problem
4. Attempt

**Note:** 
- For Java solutions, the script automatically compiles the code before running and cleans up `.class` files afterward.
- For C++ solutions, the script uses `g++` compiler with C++17 standard. On Windows, you may need MinGW or WSL.

## Categories

Problems are organized by data structure/algorithm category:
- `arrays` - Array manipulation problems
- `linked-list` - Linked list problems
- `trees` - Binary trees, BST, etc.
- `hash-table` - Hash map/table problems
- `strings` - String manipulation
- `dynamic-programming` - DP problems
- `graphs` - Graph algorithms
- `stacks` - Stack-based problems
- `queues` - Queue-based problems
- `heaps` - Heap/priority queue problems
- `sorting` - Sorting algorithms
- `searching` - Search algorithms
- `backtracking` - Backtracking problems
- `greedy` - Greedy algorithm problems
- `math` - Mathematical problems
- `bit-manipulation` - Bit manipulation problems

## Problem Naming Convention

Use descriptive names like:
- `two-sum` (in `arrays` or `hash-table`)
- `reverse-linked-list` (in `linked-list`)
- `binary-tree-inorder-traversal` (in `trees`)
- `merge-intervals` (in `arrays`)

## Notes

- Keep solutions clean and well-commented
- Update reflection.md after each significant attempt
- Use attempts folder for both initial attempts and revision practice

