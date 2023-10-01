# input
student_score = 80

# Process: Your Solution Code Here
if student_score >= 80 and student_score <= 100:
    nilai = "A"
elif student_score >= 65 and student_score < 80:
    nilai = "B+"
elif student_score >= 50 and student_score < 65:
    nilai = "B"
elif student_score >= 35 and student_score < 50:
    nilai = "C"
else:
    nilai = "D"

# Output "Nilai A"
print("Niai " + nilai)