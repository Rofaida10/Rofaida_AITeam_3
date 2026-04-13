import numpy as np
grades = np.array([[85, 78, 92, 88],
[70, 76, 80, 65],
[90, 88, 94, 91],
[60, 65, 58, 62],
[100, 95, 98, 97]])
print("Grades: ",grades)
print("\nArray shape: ",grades.shape)

student_m=np.mean(grades, axis=1)
print("\nThe mean grade of each student: ", student_m)

grade_m=np.mean(grades, axis=0)
print("\nThe mean grade of each subject: ",grade_m)

top=grades[student_m>85]
print("\nStudents with average grade greater than 85: ",top )

bonus=grades+5
print("\nGrades with 5 marks bonus: ",bonus)

min_g=grades.min(axis=0)
max_g=grades.max(axis=0)
norm= (grades - min_g)/(max_g - min_g)
print("\nNormalized grades: ",norm)

flat= grades.flatten()
print("\nFlattened grades: ",flat)
