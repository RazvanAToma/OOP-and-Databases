import tkinter as tk

class MarkCalculationApp:
    def __init__(self, master):
        self.master = master
        master.title("Mark Calculation")
        master.geometry("700x400+100+100")

        # Create variables for grades
        self.autonomy_grade_var = tk.StringVar()
        self.electro_grade_var = tk.StringVar()
        self.ai_grade_var = tk.StringVar()
        self.oop_grade_var = tk.StringVar()

        # Create labels and entries for Name and ID
        self.create_label_and_entry("Name", 0, 0, 1)
        self.create_label_and_entry("Student ID Number", 0, 3, 4)

        # Create labels for Courses, Course Names, Grades, and Sub Credits
        self.create_label("Course ID", 1, 0)
        self.create_label("Course Name", 1, 1)
        self.create_label("Grades", 1, 2)
        self.create_label("Sub Credit", 1, 3)

        # Define course information
        courses = [("Autonomy", 4), ("Electro", 4), ("AI", 3), ("OOP", 4)]

        # Create labels, entries, and sub-credit labels for each course
        for row, (course_name, sub_credit) in enumerate(courses, start=2):
            self.create_label(str(row), row, 0)
            self.create_label(course_name, row, 1)

            grade_var = getattr(self, f"{course_name.lower()}_grade_var")
            self.create_entry(grade_var, row, 2)

            self.create_label(sub_credit, row, 3)

        # Create a Submit button
        self.create_button("Submit", self.calc_credit, 7, 1)

    def create_label_and_entry(self, text, row, col_label, col_entry):
        label = self.create_label(text, row, col_label)
        entry_var = tk.StringVar()
        entry = self.create_entry(entry_var, row, col_entry)
        return label, entry_var, entry

    def create_label(self, text, row, col):
        label = tk.Label(self.master, text=text)
        label.grid(row=row, column=col)
        return label

    def create_entry(self, entry_var, row, col):
        entry = tk.Entry(self.master, textvariable=entry_var)
        entry.grid(row=row, column=col)
        return entry

    def create_button(self, text, command, row, col):
        button = tk.Button(self.master, text=text, command=command)
        button.grid(row=row, column=col)
        return button

    def calculate_credit(self, grade, sub_credit):
        if grade == "A":
            return 10 * sub_credit
        elif grade == "B":
            return 9 * sub_credit
        elif grade == "C":
            return 8 * sub_credit
        elif grade == "D":
            return 7 * sub_credit
        else:
            return 0

    def calc_credit(self):
        courses = [("Autonomy", 4), ("Electro", 4), ("AI", 3), ("OOP", 4)]

        total_credit = 0

        for row, (course_name, sub_credit) in enumerate(courses, start=2):
            grade_var = getattr(self, f"{course_name.lower()}_grade_var")
            grade = grade_var.get()
            credit = self.calculate_credit(grade, sub_credit)

            # Display credit per course
            credit_label = self.create_label(credit, row, 4)

            total_credit += credit

        # Display total credit
        total_credit_label = self.create_label("Total Credit", 6, 2)
        total_credit_number_label = self.create_label(total_credit, 6, 4)

if __name__ == "__main__":
    root = tk.Tk()
    app = MarkCalculationApp(root)
    root.mainloop()
