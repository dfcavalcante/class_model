from university import University
from department import Department
from professor import Professor
from subject import Subject

# Create university
university = University("XYZ University")

# Create departments
dept1 = Department("Mathematics Department")
dept2 = Department("Physics Department")

# Add departments to university
university.add_department(dept1)
university.add_department(dept2)

# Create professors
prof1 = Professor("Dr. John")
prof2 = Professor("Dr. Anna")

# Add professors to department
dept1.add_professor(prof1)
dept1.add_professor(prof2)

# Create subjects
sub1 = Subject("Calculus I")
sub2 = Subject("Linear Algebra")

# Add subjects to professors
prof1.add_subject(sub1)
prof1.add_subject(sub2)

# List information
print("\n--- University ---")
university.list_departments()

print("\n--- Department ---")
dept1.list_professors()

print("\n--- Professor ---")
prof1.list_subjects()
