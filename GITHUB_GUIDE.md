# VS Code, GitHub, and Submission Guide

## 1. Open and test the project in VS Code

1. Extract the downloaded `grade-system.zip` file.
2. Open VS Code.
3. Select **File > Open Folder** and choose the extracted `grade-system` folder.
4. Select **Terminal > New Terminal**.
5. Create a virtual environment:

   ```powershell
   python -m venv venv
   ```

6. Activate it:

   ```powershell
   venv\Scripts\Activate.ps1
   ```

7. Run the program:

   ```powershell
   python grade_system.py
   ```

8. Test it at least three times. Suggested marks are `95`, `75`, and `55`.

## 2. Take the required terminal screenshot

1. Run the program with a mark.
2. Repeat until the terminal shows at least three different marks and grades.
3. Press **Windows + Shift + S**.
4. Select the terminal-output area and save the screenshot.

The `TEST_RESULTS.md` file also contains paste-ready test evidence.

## 3. Create the GitHub repository

1. Sign in at [GitHub](https://github.com/).
2. Select the **+** button and then **New repository**.
3. Enter the repository name: `student-grade-system`.
4. Add the description: `Python assignment that converts a student mark into a letter grade.`
5. Choose **Public** unless your trainer instructed you to use **Private**.
6. Do not add another README, `.gitignore`, or license because the project already contains the required files.
7. Select **Create repository**.

## 4. Upload from the VS Code terminal

Run these commands one at a time inside the `grade-system` folder:

```powershell
git init
git add .
git commit -m "Complete student grade system assignment"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/student-grade-system.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your actual GitHub username. If Git asks you to sign in, complete the browser sign-in and return to VS Code.

## 5. Verify as the trainer

1. Open the repository page in a private/incognito browser window.
2. Confirm these files are visible:
   - `grade_system.py`
   - `README.md`
   - `TEST_RESULTS.md`
   - `GITHUB_GUIDE.md`
3. Confirm that the `venv` folder is not visible.
4. Select **Code > Download ZIP**.
5. Extract it and run `python grade_system.py` to confirm the shared copy works.

## 6. Message to the trainer

```text
Hello [Trainer Name],

I have completed the Student Grade System assignment. I tested all grade bands, boundary values, and invalid inputs. Please find my GitHub repository here:

[PASTE YOUR GITHUB REPOSITORY LINK]

Thank you.
```

## Final checklist

- [ ] The program runs successfully in VS Code.
- [ ] At least three different marks were tested.
- [ ] A terminal screenshot was saved.
- [ ] Invalid input handling was explained.
- [ ] The GitHub repository opens correctly.
- [ ] The `venv` folder was not uploaded.
- [ ] The repository link was sent to the trainer.
