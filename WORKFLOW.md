# DSA Practice Workflow Guide

This guide explains how to use this repository structure effectively for practicing DSA problems.

## Quick Start

> **Note:** For creating new problems, see the [README.md](README.md#creating-a-new-problem) file.

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
- Implement in `attempts/python/attempt_1.py`, `attempts/java/attempt_1.java`, or `attempts/cpp/attempt_1.cpp`
- Test your solution using `test.py` (see [README.md](README.md#testing-solutions))
- If you have multiple attempts, save them with incrementing numbers:
  - `attempts/python/attempt_1.py`
  - `attempts/java/attempt_1.java`
  - `attempts/cpp/attempt_1.cpp`
  - `attempts/python/attempt_2.py`
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
2. Try solving again and save as a new attempt in `attempts/python/`, `attempts/java/`, or `attempts/cpp/`
3. Use the next attempt number (e.g., if last was `attempt_3.py`, use `attempt_4.py`)
4. After solving, compare with your previous attempts
5. Update `reflection.md` with revision notes

## Best Practices

> **Note:** For repository structure, categories, and naming conventions, see the [README.md](README.md) file.

### Solution Files
- Keep solutions clean and well-commented
- Document your approach in comments
- Test your solutions using `test.py` (see [README.md](README.md#testing-solutions))

### Attempts Tracking
- Save attempts when:
  - You had a bug and fixed it
  - You tried a different approach
  - You want to track your progress
  - You're practicing again (revision) - use the next attempt number

### Revision Practice
- Practice problems you solved 1-2 weeks ago
- Don't peek at solutions while revising
- Save revision attempts in `attempts/python/`, `attempts/java/`, or `attempts/cpp/` with the next attempt number
- Update reflection after each revision
- Note what you remembered vs. what you forgot

### Reflection Notes
- Be honest about your thought process
- Document mistakes and learnings
- Note time taken to solve
- Record alternative approaches you considered

## Example Workflow Timeline

**Day 1: First Encounter**
1. Create problem folder (see [README.md](README.md#creating-a-new-problem))
2. Fill in README.md
3. Solve in Python → `attempts/python/attempt_1.py`
4. Solve in Java → `attempts/java/attempt_1.java` (or C++ → `attempts/cpp/attempt_1.cpp`)
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

