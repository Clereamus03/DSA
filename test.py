"""
Test Runner Script for DSA Solutions
Usage: 
    python test.py                                    # Interactive menu
    python test.py <category> <problem> <language>    # Test latest attempt
    python test.py <category> <problem> <attempt> <language>  # Test specific attempt
"""

import os
import sys
import subprocess
from pathlib import Path


def find_categories():
    """Find all category directories in the current directory."""
    categories = []
    for item in os.listdir('.'):
        if os.path.isdir(item) and item != '__pycache__' and not item.startswith('.'):
            # Check if it has a problems subdirectory
            if os.path.isdir(os.path.join(item, 'problems')):
                categories.append(item)
    return sorted(categories)


def find_problems(category):
    """Find all problems in a category."""
    problems_path = Path(category) / 'problems'
    if not problems_path.exists():
        return []
    
    problems = []
    for item in problems_path.iterdir():
        if item.is_dir():
            problems.append(item.name)
    return sorted(problems)


def find_attempts(category, problem, language):
    """Find all attempt files for a problem in a specific language."""
    attempts_path = Path(category) / 'problems' / problem / 'attempts' / language
    if not attempts_path.exists():
        return []
    
    attempts = []
    for file in attempts_path.iterdir():
        if file.is_file():
            if language == 'python' and file.suffix == '.py':
                attempts.append(file.stem)  # Get filename without extension
            elif language == 'java' and file.suffix == '.java':
                attempts.append(file.stem)
    return sorted(attempts, key=lambda x: int(x.split('_')[1]) if '_' in x and x.split('_')[1].isdigit() else 0)


def get_latest_attempt(category, problem, language):
    """Get the latest attempt number for a problem."""
    attempts = find_attempts(category, problem, language)
    if not attempts:
        return None
    return attempts[-1]  # Last one is the latest (sorted)


def run_python_test(category, problem, attempt):
    """Run a Python solution file."""
    file_path = Path(category) / 'problems' / problem / 'attempts' / 'python' / f'{attempt}.py'
    
    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        return False
    
    print(f"\n{'='*60}")
    print(f"Running Python Solution")
    print(f"{'='*60}")
    print(f"Category: {category}")
    print(f"Problem: {problem}")
    print(f"Attempt: {attempt}")
    print(f"File: {file_path}")
    print(f"{'='*60}\n")
    
    try:
        # Run the Python file
        result = subprocess.run(
            [sys.executable, str(file_path)],
            capture_output=False,
            text=True
        )
        print(f"\n{'='*60}")
        print(f"Exit code: {result.returncode}")
        print(f"{'='*60}")
        return result.returncode == 0
    except Exception as e:
        print(f"Error running Python file: {e}")
        return False


def run_java_test(category, problem, attempt):
    """Compile and run a Java solution file."""
    file_path = Path(category) / 'problems' / problem / 'attempts' / 'java' / f'{attempt}.java'
    attempts_dir = Path(category) / 'problems' / problem / 'attempts' / 'java'
    
    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        return False
    
    print(f"\n{'='*60}")
    print(f"Running Java Solution")
    print(f"{'='*60}")
    print(f"Category: {category}")
    print(f"Problem: {problem}")
    print(f"Attempt: {attempt}")
    print(f"File: {file_path}")
    print(f"{'='*60}\n")
    
    try:
        # Compile the Java file
        print("Compiling Java file...")
        compile_result = subprocess.run(
            ['javac', str(file_path)],
            capture_output=True,
            text=True,
            cwd=str(attempts_dir)
        )
        
        if compile_result.returncode != 0:
            print(f"Compilation failed:")
            print(compile_result.stderr)
            return False
        
        print("Compilation successful!\n")
        
        # Find the class name (assume it's the same as the filename or 'Solution')
        # Try to extract class name from file
        class_name = None
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Look for class definition
            if 'class' in content:
                # Simple extraction - look for "class ClassName"
                for line in content.split('\n'):
                    if 'class' in line and '{' in line:
                        parts = line.split('class')
                        if len(parts) > 1:
                            class_name = parts[1].split()[0].split('{')[0].strip()
                            break
        
        # If we couldn't find a class name, try common names
        if not class_name:
            # Try common class names
            if 'Solution' in content:
                class_name = 'Solution'
            else:
                class_name = attempt.replace('-', '_').replace('attempt_', '')
        
        # Run the compiled class
        print("Running Java program...\n")
        run_result = subprocess.run(
            ['java', '-cp', str(attempts_dir), class_name],
            capture_output=False,
            text=True
        )
        
        print(f"\n{'='*60}")
        print(f"Exit code: {run_result.returncode}")
        print(f"{'='*60}")
        
        # Clean up .class files
        for class_file in attempts_dir.glob('*.class'):
            class_file.unlink()
        
        return run_result.returncode == 0
        
    except FileNotFoundError:
        print("Error: Java compiler (javac) not found. Make sure Java is installed and in PATH.")
        return False
    except Exception as e:
        print(f"Error running Java file: {e}")
        return False


def run_test_direct(category, problem, attempt, language):
    """Run a test directly with provided parameters."""
    # Validate language
    if language not in ['python', 'java']:
        print(f"Error: Invalid language '{language}'. Use 'python' or 'java'.")
        return False
    
    # Validate that the attempt exists
    attempts = find_attempts(category, problem, language)
    if not attempts:
        print(f"Error: No {language} attempts found for problem '{problem}' in category '{category}'.")
        return False
    
    if attempt not in attempts:
        print(f"Error: Attempt '{attempt}' not found.")
        print(f"Available attempts: {', '.join(attempts)}")
        return False
    
    # Run the test
    if language == 'python':
        return run_python_test(category, problem, attempt)
    else:
        return run_java_test(category, problem, attempt)


def main():
    """Main function to run the test runner."""
    # Check for command-line arguments
    if len(sys.argv) > 1:
        # Command-line mode
        if len(sys.argv) == 4:
            # Format: python test.py <category> <problem> <language>
            category = sys.argv[1]
            problem = sys.argv[2]
            language = sys.argv[3].lower()
            
            # Get latest attempt
            attempt = get_latest_attempt(category, problem, language)
            if not attempt:
                print(f"Error: No {language} attempts found for problem '{problem}' in category '{category}'.")
                return
            
            print(f"Testing latest {language} attempt: {attempt}")
            run_test_direct(category, problem, attempt, language)
            
        elif len(sys.argv) == 5:
            # Format: python test.py <category> <problem> <attempt> <language>
            category = sys.argv[1]
            problem = sys.argv[2]
            attempt = sys.argv[3]
            language = sys.argv[4].lower()
            
            run_test_direct(category, problem, attempt, language)
            
        else:
            print("Usage:")
            print("  python test.py                                    # Interactive menu")
            print("  python test.py <category> <problem> <language>    # Test latest attempt")
            print("  python test.py <category> <problem> <attempt> <language>  # Test specific attempt")
            print("\nExamples:")
            print("  python test.py arrays three-sum python")
            print("  python test.py arrays three-sum attempt_1 python")
            print("  python test.py arrays three-sum attempt_2 java")
        return
    
    # Interactive mode (no arguments)
    print("\n" + "="*60)
    print("DSA Test Runner")
    print("="*60)
    print("\nSelect an option:")
    print("1. Test Python solution")
    print("2. Test Java solution")
    print("0. Exit")
    
    choice = input("\nEnter your choice (0-2): ").strip()
    
    if choice == '0':
        print("Exiting...")
        return
    
    if choice not in ['1', '2']:
        print("Invalid choice. Please select 1 or 2.")
        return
    
    language = 'python' if choice == '1' else 'java'
    
    # Find categories
    categories = find_categories()
    if not categories:
        print("No categories found. Make sure you're in the repository root.")
        return
    
    # Select category
    print("\nAvailable categories:")
    for i, cat in enumerate(categories, 1):
        print(f"  {i}. {cat}")
    
    try:
        cat_choice = int(input(f"\nSelect category (1-{len(categories)}): ").strip())
        if cat_choice < 1 or cat_choice > len(categories):
            print("Invalid category selection.")
            return
        category = categories[cat_choice - 1]
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    # Find problems in category
    problems = find_problems(category)
    if not problems:
        print(f"No problems found in category '{category}'.")
        return
    
    # Select problem
    print(f"\nAvailable problems in '{category}':")
    for i, prob in enumerate(problems, 1):
        print(f"  {i}. {prob}")
    
    try:
        prob_choice = int(input(f"\nSelect problem (1-{len(problems)}): ").strip())
        if prob_choice < 1 or prob_choice > len(problems):
            print("Invalid problem selection.")
            return
        problem = problems[prob_choice - 1]
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    # Find attempts
    attempts = find_attempts(category, problem, language)
    if not attempts:
        print(f"No {language} attempts found for problem '{problem}'.")
        return
    
    # Select attempt
    print(f"\nAvailable {language} attempts:")
    for i, att in enumerate(attempts, 1):
        print(f"  {i}. {att}")
    
    try:
        att_choice = int(input(f"\nSelect attempt (1-{len(attempts)}): ").strip())
        if att_choice < 1 or att_choice > len(attempts):
            print("Invalid attempt selection.")
            return
        attempt = attempts[att_choice - 1]
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    # Run the test
    if choice == '1':
        run_python_test(category, problem, attempt)
    else:
        run_java_test(category, problem, attempt)


if __name__ == "__main__":
    main()

