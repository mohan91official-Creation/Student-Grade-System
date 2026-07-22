# Student Grade System

A simple Python terminal program that converts a mark from 0 to 100 into a letter grade.

## Grading scale

| Mark | Grade |
|---|---|
| 90-100 | A |
| 80 to below 90 | B |
| 70 to below 80 | C |
| 60 to below 70 | D |
| Below 60 | E |

## Requirements

- Python 3
- No external packages

## Run in VS Code on Windows

1. Open the `grade-system` folder in VS Code.
2. Open **Terminal > New Terminal**.
3. Create a virtual environment:

   ```powershell
   python -m venv venv
   ```

4. Activate it in PowerShell:

   ```powershell
   venv\Scripts\Activate.ps1
   ```

5. Run the program:

   ```powershell
   python grade_system.py
   ```

6. Enter a mark when prompted.
7. When finished, deactivate the environment:

   ```powershell
   deactivate
   ```

No package installation is required.

## Example

```text
Enter your mark (0-100): 85
Mark: 85 -> Grade: B
```

## Invalid input handling

The program converts the user's entry to a number and checks that it is finite and between 0 and 100. If the entry is text, below 0, above 100, or a special value such as `nan`, it displays a clear error message and exits normally instead of crashing.

## Files

- `grade_system.py` - the complete Python program
- `TEST_RESULTS.md` - terminal-style evidence of testing
- `GITHUB_GUIDE.md` - step-by-step publishing and sharing instructions
- `.gitignore` - prevents the local virtual environment from being uploaded

## Test as the trainer would

The trainer can download the repository as a ZIP, extract it, open the folder in VS Code, and run:

```powershell
python grade_system.py
```

The trainer does not need to install any packages.
