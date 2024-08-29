from collections import Counter

students_scores = {
    'student_1': 40.0,
    'student_2': 60.5,
    'student_3': 70.2,
    'student_4': 80.6,
    'student_5': 89.1,
    'student_6': 79.9,
    'student_7': 92.4,
    'student_8': 55.3,
    'student_9': 67.8,
    'student_10': 72.1,
    'student_11': 85.6,
    'student_12': 45.9,
    'student_13': 101.3,  # Invalid score
    'student_14': 68.4,
    'student_15': 100,
    'student_16': 59.0,
    'student_17': 84.3,
    'student_18': 91.7,
    'student_19': -5.0,  # Invalid score
    'student_20': 77.2,
    'student_21': 63.9,
    'student_22': 100,
    'student_23': 99.4,
    'student_24': 88.6,
    'student_25': 106.7,  # Invalid score
    'student_26': 38.4,
    'student_27': 90.1,
    'student_28': 50.0,
    'student_29': 89.5,
    'student_30': 0.0,
}

def main():
    # Categorize grades
    categorized_grades = {student_name: categorize_grade(student_name, score) for student_name, score in students_scores.items()}

    # Count grades
    grades_count = Counter([grade for grade in categorized_grades.values() if grade is not None])

    # Print grades count
    [print(f'{grade}: {grade_count}') for grade, grade_count in grades_count.items()]

def categorize_grade(student_name, score):
    score = round(score)
    if score < 0 or score > 100:
        print(f'Student {student_name} has an invalid grade of {score}')
        return None

    if score >= 0 and score < 60:
        return 'F'

    if score >= 60 and score <= 69:
        return 'D'

    if score >= 70 and score <= 79:
        return 'C'

    if score >= 80 and score <= 89:
        return 'B'

    if score >= 90 and score <= 100:
        if score == 100:
            print(f'Congratulations to {student_name} they scored {score}!')
        return 'A'

if __name__ == '__main__':
    main()

