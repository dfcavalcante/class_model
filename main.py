from university import University
from department import Department
from professor import Professor
from subject import Subject

# Create professors
prof1 = Professor("Professor Carlos")
prof2 = Professor("Professora Raquel")
prof3 = Professor("Professora Júlia")

# Create university
university = University("Universidade do Estado do Amazonas")


# Add departments to university
university.create_department(Department("EST", prof1))
university.create_department(Department("ESAT", prof2))

university.departments[0].add_professor(prof3)

# Create subjects
sub1 = Subject("Cálculo I")
sub2 = Subject("Algebra Linear")
sub3 = Subject("Artes")

# Add subjects to professors
prof3.add_subject(sub1)
prof3.add_subject(sub2)

prof2.add_subject(sub3)
prof1.add_subject(sub3)

# List information
print("\n|--- Departamentos ---|")
university.list_departments()

print("\n|--- Professores ---|")
print(f"\n--- {university.departments[0].name} ---")
university.departments[0].list_professors()
print(f"\n--- {university.departments[1].name} ---")
university.departments[1].list_professors()

print("\n|--- Disciplinas ---|")
print(f"\n--- {prof1.name} ---")
prof1.list_subjects()
print(f"\n--- {prof2.name} ---")
prof2.list_subjects()
print(f"\n--- {prof3.name} ---")
prof3.list_subjects()