import pandas as pd
import numpy as np

def load_data(file_path):
    """Loads student dataset from specified path using Pandas[cite: 2]."""
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: File not found at path '{file_path}'")
        return None

def calculate_totals_and_averages(df):
    """Calculates total and average marks using NumPy/Pandas[cite: 1, 2]."""
    subject_cols = ['Maths', 'Science', 'English', 'ComputerScience']
    
    # Using pandas/numpy numerical calculations
    df['Total_Marks'] = df[subject_cols].sum(axis=1)
    df['Average_Marks'] = df[subject_cols].mean(axis=1)
    
    return df

def assign_grade(avg):
    """Assigns letter grade based on average score[cite: 1, 2]."""
    if avg >= 85:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 60:
        return 'C'
    elif avg >= 50:
        return 'D'
    else:
        return 'F'

def check_pass_fail(df, min_pass_mark=50):
    """Determines pass/fail status for each student[cite: 1, 2]."""
    subject_cols = ['Maths', 'Science', 'English', 'ComputerScience']
    
    statuses = []
    for idx, row in df.iterrows():
        # Pass if student scores >= min_pass_mark in all subjects
        if row[subject_cols].min() >= min_pass_mark:
            statuses.append('Pass')
        else:
            statuses.append('Fail')
            
    df['Status'] = statuses
    return df

def process_student_data(df):
    """Applies calculation, pass/fail check, and grading loops[cite: 2]."""
    df = calculate_totals_and_averages(df)
    df = check_pass_fail(df)
    
    # Simple loop to apply grades
    grades = []
    for avg in df['Average_Marks']:
        grades.append(assign_grade(avg))
    df['Grade'] = grades
    
    return df

def get_subject_averages(df):
    """Calculates mean performance per subject[cite: 1, 2]."""
    subject_cols = ['Maths', 'Science', 'English', 'ComputerScience']
    return df[subject_cols].mean()

def get_top_performers(df, top_n=3):
    """Fetches top N students sorted by average marks[cite: 1, 2]."""
    return df.nlargest(top_n, 'Average_Marks')[['StudentID', 'Name', 'Department', 'Average_Marks', 'Grade']]