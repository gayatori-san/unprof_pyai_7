# 📊 Student Marks Analysis & Visualization

A comprehensive Python project that demonstrates **data analysis**, **data cleaning**, and **data visualization** using **Pandas**, **NumPy**, and **Matplotlib**.

This application allows users to enter student marks interactively, processes the data, calculates performance metrics, assigns grades, and generates **7 professional-quality charts** for visual analysis.

---

## 🚀 Features

* 📝 Interactive student data entry
* 📊 Automatic DataFrame creation using Pandas
* 🧹 Handles missing values with `fillna()`
* ➕ Calculates Total Marks
* 📈 Calculates Average Marks
* 🏅 Automatically assigns grades
* 📉 Generates 7 different visualization charts
* 💾 Saves every chart as a high-quality PNG image

---

# 📚 Concepts Covered

### Pandas

* DataFrame
* Data Cleaning
* `fillna()`
* Row & Column Operations
* Statistical Calculations

### NumPy

* Numerical Arrays
* Positioning for Grouped Bar Charts

### Matplotlib

* Bar Charts
* Horizontal Bar Charts
* Grouped Bar Charts
* Pie Charts
* Scatter Plots
* Dashboard (Multiple Subplots)
* Line Charts

---

# 📁 Project Structure

```text
Student-Marks-Analysis/
│
├── student_analysis.py
├── requirements.txt
├── README.md
│
├── chart1_student_averages.png
├── chart2_subject_averages.png
├── chart3_grouped_bars.png
├── chart4_grade_pie.png
├── chart5_scatter.png
├── chart6_dashboard.png
└── chart7_top3_trend.png
```

---

# 🛠️ Technologies Used

* Python 3.x
* Pandas
* NumPy
* Matplotlib

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/gayatori-san/unprof_pyai_7
```

Move into the project folder:

```bash
cd Student-Marks-Analysis
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

or

```bash
pip install pandas numpy matplotlib
```

---

# ▶️ Running the Project

Execute the Python file:

```bash
python student_analysis.py
```

---

# 💻 Sample Execution

```
Enter student marks for analysis.

How many students do you want to enter? 3

Student 1 ID: S001
Student 1 Name: Alice
Math: 95
Science: 89
English: 91
History: 87

Student 2 ID: S002
Student 2 Name: Bob
Math: 78
Science: 81
English: 74
History: 80

Student 3 ID: S003
Student 3 Name: Charlie
Math: 88
Science: 90
English: 85
History: 92
```

After entering the data, the program automatically:

* Creates a DataFrame
* Cleans missing values
* Calculates Total Marks
* Calculates Average Marks
* Assigns Grades
* Generates and saves all charts

---

# 📊 Charts Generated

## 1️⃣ Student Average Marks

* Compares each student's average score
* Displays the class average as a reference line
* Highlights high and low performers using different colors

**Output File**

```
chart1_student_averages.png
```

---

## 2️⃣ Subject-wise Average

* Shows the average score for each subject
* Uses a horizontal bar chart for better readability

**Output File**

```
chart2_subject_averages.png
```

---

## 3️⃣ Subject-wise Comparison

* Grouped bar chart comparing every student's marks across all subjects

**Output File**

```
chart3_grouped_bars.png
```

---

## 4️⃣ Grade Distribution

* Pie chart displaying the percentage of students in each grade category

**Output File**

```
chart4_grade_pie.png
```

---

## 5️⃣ Total vs Average Scatter Plot

* Shows the relationship between total marks and average marks
* Labels each student for easy identification

**Output File**

```
chart5_scatter.png
```

---

## 6️⃣ Student Performance Dashboard

A dashboard containing four visualizations:

* Student Average Marks
* Subject-wise Average
* Grade Distribution
* Subject Marks Box Plot

**Output File**

```
chart6_dashboard.png
```

---

## 7️⃣ Top 3 Students Trend Analysis

* Displays subject-wise performance trends of the top three students
* Helps compare strengths and weaknesses across subjects

**Output File**

```
chart7_top3_trend.png
```

---

# 🧮 Grade Criteria

| Average Marks | Grade |
| ------------: | :---: |
|      90 – 100 |   A+  |
|       80 – 89 |   A   |
|       70 – 79 |   B   |
|       60 – 69 |   C   |
|      Below 60 |   F   |

---

# 📌 Learning Outcomes

By completing this project, you will learn how to:

* Build DataFrames using Pandas
* Clean and preprocess datasets
* Calculate statistical metrics
* Work with multiple visualization techniques
* Create dashboards using Matplotlib
* Save graphs as image files
* Analyze student performance using Python

---

# 📷 Output

The program generates and saves the following images:

```
chart1_student_averages.png
chart2_subject_averages.png
chart3_grouped_bars.png
chart4_grade_pie.png
chart5_scatter.png
chart6_dashboard.png
chart7_top3_trend.png
```

---

