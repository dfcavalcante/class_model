from professor import Professor

class Department:
    def __init__(self, name, professor: Professor):
        self.name = name
        self.professors = [professor]

    def add_professor(self, professor: Professor):
        if len(self.professors) < 5:
            self.professors.append(professor)
        else:
            print("The department already has the maximum number of professors.")

    def list_professors(self):
        for prof in self.professors:
            print(f"Professor: {prof.name}")
