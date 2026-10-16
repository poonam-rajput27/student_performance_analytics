# Student Performance Analytics System

## 1. Project Title
* **Project Name:** Student Performance Analytics System[cite: 1]
* **Student Name:** Poonam Rajput[cite: 1]
* **Course:** Python with AI (EWB Courses)[cite: 1]

## 2. Objective
The goal of this project is to build a Python-based data analysis tool that reads student academic records, processes marks and attendance using NumPy and Pandas, and generates meaningful analytical insights such as student averages, grades, pass/fail statistics, subject-wise trends, and top performers[cite: 1].

## 3. Technologies Used
* **Python** (Core logic, loops, custom functions)[cite: 3]
* **Pandas** (Data loading, DataFrame manipulation, filtering)[cite: 3]
* **NumPy** (Numerical calculations and vectorised array operations)[cite: 3]

## 4. Dataset Description (`students.csv`)
* **Overview:** Contains 15 realistic student records[cite: 2].
* **Columns Included:** `StudentID`, `Name`, `Department`, `Maths`, `Science`, `English`, `ComputerScience`, and `Attendance`.

## 5. Implementation Summary
1. **Data Loading:** Used Pandas `read_csv()` to ingest data safely into a DataFrame[cite: 2].
2. **Data Processing:** Created custom modular functions (`functions.py`) utilizing loops and conditional statements to calculate total marks, average marks, grades, and status[cite: 2].
3. **Numerical Operations:** Integrated NumPy/Pandas aggregate methods (`sum()`, `mean()`, `nlargest()`) to compute analytics[cite: 2].
4. **Analysis Generation:** Computed class-wide averages, identified subject-wise performances, and determined pass/fail counts[cite: 2].

## 6. Key Features
* Automated total and average score calculation.
* Dynamic grading logic (A, B, C, D, F)[cite: 1, 2].
* Pass/Fail criteria evaluation[cite: 1, 2].
* Subject-wise performance summary breakdown[cite: 1, 2].
* Identification of top-performing students[cite: 1, 2].

## 7. Final Outcome
The project successfully processes raw tabular student data and produces an automated terminal-based analytics dashboard that yields clear insights into institutional student performance without needing advanced machine learning models[cite: 1, 2].

## 8. Challenges & Learning
* **Challenge:** Ensuring individual subject thresholds were correctly evaluated alongside aggregate totals for pass/fail statuses.
* **Solution:** Used row-wise iteration with custom conditional checks.
* **Learning:** Gained strong hands-on experience structuring a multi-file Python project using Pandas and NumPy.