import os
from functions import (
    load_data, 
    process_student_data, 
    get_subject_averages, 
    get_top_performers
)

def main():
    print("=" * 60)
    print("       STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 60)
    
    # Dynamically find the path to data/student.csv relative to this script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, '..', 'data', 'student.csv')
    
    df = load_data(data_path)
    
    if df is not None:
        print(f"\n[INFO] Loaded {len(df)} records from 'data/student.csv'.\n")
        
        # Process Student Data
        processed_df = process_student_data(df)
        
        # Summary & Metrics
        total_students = len(processed_df)
        passed_students = (processed_df['Status'] == 'Pass').sum()
        failed_students = total_students - passed_students
        class_avg = processed_df['Average_Marks'].mean()
        
        print("=" * 60)
        print("                 SUMMARY & RESULTS")
        print("=" * 60)
        print(f"Total Students      : {total_students}")
        print(f"Passed Students     : {passed_students}")
        print(f"Failed Students     : {failed_students}")
        print(f"Overall Class Avg   : {class_avg:.2f}%\n")
        
        # Best Student
        top_student = processed_df.loc[processed_df['Average_Marks'].idxmax()]
        print(f"Top Performer       : {top_student['Name']} ({top_student['Department']}) - {top_student['Average_Marks']:.2f}%\n")
        
        # Subject Performance
        print("--- Subject Averages ---")
        sub_avgs = get_subject_averages(processed_df)
        for sub, avg in sub_avgs.items():
            print(f"  * {sub:15s}: {avg:.2f}%")
            
        best_sub = sub_avgs.idxmax()
        print(f"\nHighest Performing Subject : {best_sub} ({sub_avgs[best_sub]:.2f}%)\n")
        
        # Top 3 List
        print("--- Top 3 Students ---")
        top_3 = get_top_performers(processed_df, 3)
        print(top_3.to_string(index=False))
        
        print("\n" + "=" * 60)
        print("Analysis Complete!")
        print("=" * 60)

if __name__ == '__main__':
    main()