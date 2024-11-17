from subject import Subject


class Professor:
    def __init__(self, name):
        self.name = name
        self.subjects = []

    def add_subject(self, subject: Subject):
        if len(self.subjects) < 5:
            self.subjects.append(subject)
        else:
            print("The professor already has the maximum number of subjects.")

    def list_subjects(self):
        for sub in self.subjects:
            print(f"Subject: {sub.name}")
