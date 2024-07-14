grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
student = (sorted(students))
average_grade = []
dictionary = {}
for i in range(0, len(grades)):
    average_grade.append(sum(grades[i]) / len(grades[i]))
dictionary = dict(zip(student, average_grade))
print(dictionary)
