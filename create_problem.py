"""
Helper script to create a new problem folder structure.
Usage: python create_problem.py <category> <problem-name>
Example: python create_problem.py arrays two-sum
"""

import os
import sys
from pathlib import Path


def create_problem_structure(category: str, problem_name: str):
    """
    Create a new problem folder with all necessary files.
    
    Args:
        category: Data structure category (e.g., 'arrays', 'linked-list', 'trees')
        problem_name: Name of the problem (e.g., 'two-sum')
    """
    # Convert to lowercase with hyphens
    category = category.lower().replace(' ', '-')
    problem_name = problem_name.lower().replace(' ', '-')
    
    # Base path: <category>/problems/<problem-name>
    base_path = Path(category) / 'problems' / problem_name
    
    # Create directories
    (base_path / 'attempts' / 'python').mkdir(parents=True, exist_ok=True)
    (base_path / 'attempts' / 'java').mkdir(parents=True, exist_ok=True)
    
    # Create README.md
    readme_content = f"""# {problem_name.replace('-', ' ').title()}

## Problem Link
[Add problem link here]

## Description
[Add problem description here]

## Examples

### Example 1:
```
Input: 
Output: 
Explanation: 
```

## Constraints
- [Add constraints here]

## Tags
- [Tag 1]
- [Tag 2]

## Difficulty
[Easy/Medium/Hard]

## Notes
- First attempt: [Date]
- Last revision: [Date]
- Total attempts: 0
"""
    
    # Create reflection.md
    reflection_content = f"""# Reflection: {problem_name.replace('-', ' ').title()}

## Problem Link
[Add problem link here]

## My Approach

### First Attempt
**Date:** [Date]
**Status:** Not Started

**Approach:**
- [Describe your initial thought process]

### Final Solution Approach

**Strategy:**
[Describe the approach you used in your final solution]

**Key Insights:**
1. [Insight 1]

## Time Complexity
**O([complexity])**

**Explanation:**
[Explain why this is the time complexity]

## Space Complexity
**O([complexity])**

**Explanation:**
[Explain why this is the space complexity]

## Edge Cases Considered
1. [Edge case 1]

## Key Learnings
1. [Learning point 1]

## Revision Notes
- [Date]: [Notes about revision attempt]
"""
    
    # Write all files
    (base_path / 'README.md').write_text(readme_content, encoding='utf-8')
    (base_path / 'reflection.md').write_text(reflection_content, encoding='utf-8')
    
    print(f"[OK] Created problem structure for: {problem_name}")
    print(f"Category: {category}")
    print(f"Location: {base_path}")
    print(f"\nNext steps:")
    print(f"1. Fill in the README.md with problem details")
    print(f"2. Implement your solution in attempts/python/attempt_1.py and attempts/java/attempt_1.java")
    print(f"3. Update reflection.md after solving")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python create_problem.py <category> <problem-name>")
        print("Example: python create_problem.py arrays two-sum")
        print("Example: python create_problem.py linked-list reverse-linked-list")
        print("\nCommon categories:")
        print("  - arrays")
        print("  - linked-list")
        print("  - trees")
        print("  - hash-table")
        print("  - strings")
        print("  - dynamic-programming")
        print("  - graphs")
        print("  - stacks")
        print("  - queues")
        print("  - heaps")
        sys.exit(1)
    
    category = sys.argv[1]
    problem_name = sys.argv[2]
    create_problem_structure(category, problem_name)

