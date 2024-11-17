from department import Department


class University:
    def __init__(self, name, department: Department):
        self.name = name
        self.departments = [department]

    def add_department(self, department: Department):
        if len(self.departments) < 5:
            self.departments.append(department)
        else:
            print("The university already has the maximum number of departments.")

    def list_departments(self):
        for dept in self.departments:
            print(f"Department: {dept.name}")
