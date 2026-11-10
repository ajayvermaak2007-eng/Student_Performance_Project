# Student Performance Data Cleaning & Visualization Project

## About
This beginner-friendly project uses a **synthetic practice dataset** to demonstrate data cleaning, analysis, and visualization. It is not real student data.

## Files
- `student_performance_raw.csv` — raw dataset with intentionally introduced missing values, duplicates, and invalid values.
- `student_performance_analysis.py` — complete Python analysis script.
- `REPORT_TEMPLATE.md` — report outline to complete after running the script.
- `output/` — generated cleaned dataset and charts will be saved here.

## Requirements
Python 3.9 or later is recommended.

Install packages:
```bash
pip install pandas numpy matplotlib seaborn
```

## Run the project
Keep the CSV and Python script in the same folder. Open a terminal in that folder and run:
```bash
python student_performance_analysis.py
```

## Cleaning decisions
- Exact duplicate rows are removed.
- Values outside sensible ranges are treated as missing:
  - Study hours: 0 to 16 per day
  - Attendance and exam scores: 0 to 100
- Missing numeric values are filled with the median.
- Missing gender values (if any) are filled with the most common category.
- An average score and performance level are added.

## Important
The dataset is synthetic and created for learning. In a real project, explain and justify cleaning rules using the real dataset's documentation and context.
