import os
from flask import Flask, render_template
from models.functions import load_data, process_student_data, get_subject_averages, get_top_performers

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "data", "student.csv")


@app.route("/")
def index():
    df = load_data(CSV_PATH)
    if df is None:
        return "Could not load student.csv, check the file path.", 500

    data = process_student_data(df)

    total = len(data)
    passed = int((data["Status"] == "Pass").sum())
    failed = total - passed
    class_avg = round(data["Average_Marks"].mean(), 2)

    top = data.loc[data["Average_Marks"].idxmax()]
    topper = {
        "name": top["Name"],
        "id": top["StudentID"],
        "avg": round(top["Average_Marks"], 2),
    }

    subject_avg = get_subject_averages(data)
    subjects = {s: round(a, 2) for s, a in subject_avg.items()}
    best = subject_avg.idxmax()

    top3 = get_top_performers(data, 3).to_html(index=False, classes="table")
    preview = data.head(10).to_html(index=False, classes="table")

    return render_template(
        "index.html",
        total=total,
        passed=passed,
        failed=failed,
        class_avg=class_avg,
        topper=topper,
        subjects=subjects,
        best=best,
        best_avg=round(subject_avg[best], 2),
        top3=top3,
        preview=preview,
    )


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5002)