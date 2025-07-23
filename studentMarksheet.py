# Student marks data: each row is a student, each column is a subject
marks = [
    [85, 78, 92, 88],
    [76, 81, 79, 75],
    [90, 94, 88, 92],
    [65, 70, 72, 68],
    [88, 85, 91, 89]
]

num_students = len(marks)
num_subjects = len(marks[0])

# 1. Average marks for each student
print("Average marks per student:")
for i, student_marks in enumerate(marks):
    avg = sum(student_marks) / num_subjects
    print(f"Student {i+1}: {avg:.2f}")

# 2. Average marks for each subject
print("\nAverage marks per subject:")
for j in range(num_subjects):
    subject_total = sum(marks[i][j] for i in range(num_students))
    avg = subject_total / num_students
    print(f"Subject {j+1}: {avg:.2f}")

# 3. Highest and lowest marks per student
print("\nHighest and lowest marks per student:")
for i, student_marks in enumerate(marks):
    highest = max(student_marks)
    lowest = min(student_marks)
    print(f"Student {i+1}: Highest = {highest}, Lowest = {lowest}")

# 4. Overall average
total_marks = sum(sum(student) for student in marks)
overall_avg = total_marks / (num_students * num_subjects)
print(f"\nOverall class average: {overall_avg:.2f}")
