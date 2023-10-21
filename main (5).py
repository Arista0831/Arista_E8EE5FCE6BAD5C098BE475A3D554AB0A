

class student:
  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

  def sort_students(student_list):

    sorted_students = sorted(student_list,key=lambda student: student.cgpa,reverse=True)
    return sorted_students
    
  

students = [
  student("Arista","A123",7.8),
  student("Sherly","A124",8.9),
  student("Asvitha","A125",9.1),
  student("Rohini","A126",9.9),
]

sorted_students = student.sort_students(students)
print(sorted_students)

for student in sorted_students:
  print(student.name,student.roll_number,student.cgpa)