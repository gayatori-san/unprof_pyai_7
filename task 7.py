import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# SETUP & DATA
# ============================================================
plt.style.use('seaborn-v0_8-whitegrid')

subjects = ['Math', 'Science', 'English', 'History']

print('Enter student marks for analysis.')
print('Marks must be numbers from 0 to 100.')

while True:
    try:
        num_students = int(input('\nHow many students do you want to enter? ').strip())
        if num_students > 0:
            break
        print('Please enter a positive number of students.')
    except ValueError:
        print('Please enter a valid whole number.')

student_records = []
for i in range(1, num_students + 1):
    student_id = input(f'\nStudent {i} ID (press Enter for default): ').strip() or f'S{i:03d}'
    name = input(f'Student {i} name: ').strip() or f'Student {i}'

    marks = {}
    for subject in subjects:
        while True:
            value = input(f'Enter {subject} mark for {name}: ').strip()
            try:
                mark = float(value)
                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                print('Please enter a value between 0 and 100.')
            except ValueError:
                print('Please enter a valid number.')

    student_records.append({'Student_ID': student_id, 'Name': name, **marks})

df = pd.DataFrame(student_records)

# Clean data
for subject in subjects:
    df[subject] = df[subject].fillna(round(df[subject].mean(), 1))

df['Total'] = df[subjects].sum(axis=1)
df['Average'] = df[subjects].mean(axis=1).round(2)
df['Grade'] = df['Average'].apply(lambda x: 'A+' if x >= 90 else 'A' if x >= 80 else 'B' if x >= 70 else 'C' if x >= 60 else 'F')

# ============================================================
# CHART 1: Student Average Marks (Bar)
# ============================================================
fig, ax = plt.subplots(figsize=(10, 6))
colors = ['#FF6B6B' if avg < 80 else '#4ECDC4' for avg in df['Average']]
bars = ax.bar(df['Name'], df['Average'], color=colors, edgecolor='black', linewidth=0.5)
ax.axhline(y=df['Average'].mean(), color='#FF4757', linestyle='--', linewidth=2, label=f'Class Avg: {df["Average"].mean():.1f}%')
ax.set_xlabel('Student', fontsize=12, fontweight='bold')
ax.set_ylabel('Average Marks (%)', fontsize=12, fontweight='bold')
ax.set_title('Student Average Marks Comparison', fontsize=14, fontweight='bold', pad=20)
ax.set_ylim(0, 100)
ax.legend()
for bar, avg in zip(bars, df['Average']):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, f'{avg:.1f}', ha='center', va='bottom', fontweight='bold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('chart1_student_averages.png', dpi=150, bbox_inches='tight')
plt.show()

# ============================================================
# CHART 2: Subject-wise Averages (Horizontal Bar)
# ============================================================
fig, ax = plt.subplots(figsize=(8, 5))
subject_avgs = df[subjects].mean().sort_values(ascending=True)
colors = ['#FF6B6B', '#FFA502', '#2ED573', '#1E90FF']
bars = ax.barh(subject_avgs.index, subject_avgs.values, color=colors, edgecolor='black', height=0.6)
ax.set_xlabel('Average Marks', fontsize=12, fontweight='bold')
ax.set_title('Subject-wise Average Marks', fontsize=14, fontweight='bold', pad=20)
ax.set_xlim(0, 100)
for bar, val in zip(bars, subject_avgs.values):
    ax.text(val + 1, bar.get_y() + bar.get_height()/2, f'{val:.1f}', va='center', fontweight='bold')
plt.tight_layout()
plt.savefig('chart2_subject_averages.png', dpi=150, bbox_inches='tight')
plt.show()

# ============================================================
# CHART 3: Grouped Bar - All Subjects per Student
# ============================================================
fig, ax = plt.subplots(figsize=(12, 6))
x = np.arange(len(df['Name']))
width = 0.2
ax.bar(x - 1.5*width, df['Math'], width, label='Math', color='#FF6B6B')
ax.bar(x - 0.5*width, df['Science'], width, label='Science', color='#4ECDC4')
ax.bar(x + 0.5*width, df['English'], width, label='English', color='#45B7D1')
ax.bar(x + 1.5*width, df['History'], width, label='History', color='#96CEB4')
ax.set_xlabel('Students', fontsize=12, fontweight='bold')
ax.set_ylabel('Marks', fontsize=12, fontweight='bold')
ax.set_title('Subject Marks Breakdown per Student', fontsize=14, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(df['Name'], rotation=45)
ax.legend()
ax.set_ylim(0, 105)
plt.tight_layout()
plt.savefig('chart3_grouped_bars.png', dpi=150, bbox_inches='tight')
plt.show()

# ============================================================
# CHART 4: Grade Distribution (Pie)
# ============================================================
fig, ax = plt.subplots(figsize=(8, 8))
grade_counts = df['Grade'].value_counts()
colors = ['#2ED573', '#FFA502']
explode = [0.05] * len(grade_counts)
ax.pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%', colors=colors, explode=explode, startangle=90, textprops={'fontsize': 12, 'fontweight': 'bold'})
ax.set_title('Grade Distribution', fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('chart4_grade_pie.png', dpi=150, bbox_inches='tight')
plt.show()

# ============================================================
# CHART 5: Scatter - Total vs Average
# ============================================================
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(df['Total'], df['Average'], s=200, c='#FF6B6B', edgecolors='black', alpha=0.7, zorder=3)
for i, name in enumerate(df['Name']):
    ax.annotate(name, (df['Total'].iloc[i], df['Average'].iloc[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontweight='bold')
ax.set_xlabel('Total Marks', fontsize=12, fontweight='bold')
ax.set_ylabel('Average Marks (%)', fontsize=12, fontweight='bold')
ax.set_title('Total vs Average Marks Correlation', fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('chart5_scatter.png', dpi=150, bbox_inches='tight')
plt.show()

# ============================================================
# CHART 6: Dashboard (4 subplots)
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
colors = ['#FF6B6B' if avg < 80 else '#4ECDC4' for avg in df['Average']]
axes[0,0].bar(df['Name'], df['Average'], color=colors)
axes[0,0].axhline(y=df['Average'].mean(), color='red', linestyle='--')
axes[0,0].set_title('Student Averages', fontweight='bold')
axes[0,0].tick_params(axis='x', rotation=45)
subject_avgs = df[subjects].mean()
axes[0,1].bar(subjects, subject_avgs, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'])
axes[0,1].set_title('Subject Averages', fontweight='bold')
grade_counts = df['Grade'].value_counts()
axes[1,0].pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%', colors=['#2ED573', '#FFA502'])
axes[1,0].set_title('Grade Distribution', fontweight='bold')
df[subjects].boxplot(ax=axes[1,1])
axes[1,1].set_title('Marks Distribution per Subject', fontweight='bold')
axes[1,1].tick_params(axis='x', rotation=45)
fig.suptitle('Student Marks Analysis Dashboard', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('chart6_dashboard.png', dpi=150, bbox_inches='tight')
plt.show()

# ============================================================
# CHART 7: Top 3 Students - Line Trend
# ============================================================
top3 = df.nlargest(3, 'Average')
fig, ax = plt.subplots(figsize=(10, 6))
for _, student in top3.iterrows():
    ax.plot(subjects, [student[s] for s in subjects], marker='o', linewidth=2.5, markersize=8, label=student['Name'])
ax.set_xlabel('Subject', fontsize=12, fontweight='bold')
ax.set_ylabel('Marks', fontsize=12, fontweight='bold')
ax.set_title('Top 3 Students - Subject-wise Trend', fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.set_ylim(60, 100)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('chart7_top3_trend.png', dpi=150, bbox_inches='tight')
plt.show()

print("✅ All 7 charts generated!")