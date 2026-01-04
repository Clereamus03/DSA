# DSA Practice Workflow Guide

This guide explains how to use this repository structure effectively for practicing DSA problems.

## Quick Start

### Creating a New Problem

**Option 1: Using the helper script (Recommended)**
```bash
python create_problem.py arrays two-sum
python create_problem.py linked-list reverse-linked-list
python create_problem.py trees binary-tree-inorder-traversal
```

**Option 2: Manual creation**
1. Create a category folder in `problems/` if it doesn't exist (e.g., `arrays`)
2. Create a problem folder inside the category (e.g., `problems/arrays/two-sum/`)
3. Copy the structure from an existing problem
4. Update all files with your problem details

### Problem Workflow

#### 1. Initial Setup
- Fill in `README.md` with:
  - Problem link (LeetCode, HackerRank, etc.)
  - Problem description
  - Examples and constraints
  - Tags and difficulty

#### 2. First Attempt
- Read the problem carefully
- Think about the approach
- Implement in `attempts/python/attempt_1.py` and `attempts/java/attempt_1.java`
- Test your solution
- If you have multiple attempts, save them with incrementing numbers:
  - `attempts/python/attempt_1.py`
  - `attempts/java/attempt_1.java`
  - `attempts/python/attempt_2.py`
  - `attempts/java/attempt_2.java`
  - etc.

#### 3. Reflection
After solving, update `reflection.md` with:
- Your approach and thought process
- Time and space complexity analysis
- Edge cases considered
- Key learnings
- Alternative approaches (if any)

#### 4. Revision Practice
When you want to practice again (spaced repetition):
1. **Don't look at previous attempts** in the attempts folder
2. Try solving again and save as a new attempt in `attempts/python/` or `attempts/java/`
3. Use the next attempt number (e.g., if last was `attempt_3.py`, use `attempt_4.py`)
4. After solving, compare with your previous attempts
5. Update `reflection.md` with revision notes

## File Structure Explained

```
category-name/             # Data structure category (e.g., arrays, trees)
└── problems/
    └── problem-name/
        ├── README.md      # Problem metadata and description
        ├── attempts/      # All solutions (initial attempts and revisions)
        │   ├── python/
        │   │   ├── attempt_1.py
        │   │   ├── attempt_2.py
        │   │   └── ...
        │   └── java/
        │       ├── attempt_1.java
        │       ├── attempt_2.java
        │       └── ...
        └── reflection.md  # Your analysis and learnings
```

## Best Practices

### Category Organization
- Organize problems by data structure/algorithm type
- Common categories: `arrays`, `linked-list`, `trees`, `hash-table`, `strings`, `dynamic-programming`, `graphs`, etc.
- If a problem fits multiple categories, choose the primary one

### Problem Naming
- Use lowercase with hyphens: `two-sum`, `reverse-linked-list`
- Be descriptive: `merge-k-sorted-lists` not `merge-lists`

### Solution Files
- Keep solutions clean and well-commented
- Include test cases in your solution files
- Document your approach in comments

### Attempts Tracking
- Save attempts when:
  - You had a bug and fixed it
  - You tried a different approach
  - You want to track your progress
  - You're practicing again (revision) - use the next attempt number

### Revision Practice
- Practice problems you solved 1-2 weeks ago
- Don't peek at solutions while revising
- Save revision attempts in `attempts/python/` or `attempts/java/` with the next attempt number
- Update reflection after each revision
- Note what you remembered vs. what you forgot

### Reflection Notes
- Be honest about your thought process
- Document mistakes and learnings
- Note time taken to solve
- Record alternative approaches you considered

## Example Workflow Timeline

**Day 1: First Encounter**
1. Create problem folder: `python create_problem.py arrays two-sum`
2. Fill in README.md
3. Solve in Python → `attempts/python/attempt_1.py`
4. Solve in Java → `attempts/java/attempt_1.java`
5. Update `reflection.md`

**Day 2: If needed**
- If you want to try a different approach, save as `attempts/python/attempt_2.py`
- Update reflection with new insights

**Week 2: First Revision**
1. Don't look at previous solutions
2. Solve again and save as `attempts/python/attempt_3.py` (or next number)
3. Compare with original solutions
4. Update `reflection.md` with revision notes

**Month 1: Second Revision**
- Repeat revision process (save as next attempt number)
- Note improvement in speed/understanding

## Tips

1. **Consistency**: Solve at least one problem daily
2. **Review**: Regularly review your reflections
3. **Pattern Recognition**: Note common patterns in your reflection
4. **Time Tracking**: Note how long each problem takes
5. **Difficulty Progression**: Gradually increase problem difficulty

## Tracking Progress

You can track your progress by:
- Counting problems in `problems/` folder
- Reviewing `reflection.md` files
- Noting revision dates in each problem's README.md
- Counting total attempts across all problems

