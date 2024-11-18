from numpy import character

from department import Department


class University:
    departments: list[Department] = []

    def __init__(self, name):
        self.name = name

    def list_departments(self):
        for dept in self.departments:
            print(f"Departmento: {dept.name}")

    def create_department(self, department: Department):
        if len(self.departments) <= 5:
            self.departments.append(department)
        else:
            print("Não dá para adicionar mais departamento")
