import tkinter as tk

top = tk.Tk()

# Title
top.title("Mark Calculation")

# Adjust size
top.geometry("700x400+100+100")


'''         Name            '''
# Label
name_label = tk.Label(top, text="Name")
name_label.grid(row=0,column=0)

# Entry
name_var = tk.StringVar()
name_entry = tk.Entry(top, textvariable=name_var)
name_entry.grid(row=0,column=1)



'''         ID            '''
# Label
student_id_label = tk.Label(top, text="Student ID Number")
student_id_label.grid(row=0,column=3)

# Entry
student_id_var = tk.StringVar()
id_entry = tk.Entry(top, textvariable=student_id_var)
id_entry.grid(row=0,column=4)



# Coursesc
course_ids_label = tk.Label(top, text='Course ID')
course_ids_label.grid(row=1, column=0)

course1_label = tk.Label(top, text='1')
course1_label.grid(row=2, column=0)

course2_label = tk.Label(top, text='2')
course2_label.grid(row=3, column=0)

course3_label = tk.Label(top, text='3')
course3_label.grid(row=4, column=0)

course4_label = tk.Label(top, text='4')
course4_label.grid(row=5, column=0)



# Course Names
course_name_label = tk.Label(top, text='Course Name')
course_name_label.grid(row=1, column=1)

autonomy_label = tk.Label(top, text='Autonomy')
autonomy_label.grid(row=2, column=1)

electro_label = tk.Label(top, text='Electro')
electro_label.grid(row=3, column=1)

ai_label = tk.Label(top, text='AI')
ai_label.grid(row=4, column=1)

oop_label = tk.Label(top, text='OOP')
oop_label.grid(row=5, column=1)



# Grades
grade_label = tk.Label(top, text='Grades')
grade_label.grid(row=1, column=2)

autonomy_grade_var = tk.StringVar()
autonomy_entry = tk.Entry(top, textvariable=autonomy_grade_var)
autonomy_entry.grid(row=2, column=2)

electro_grade_var = tk.StringVar()
electro_entry = tk.Entry(top, textvariable=electro_grade_var)
electro_entry.grid(row=3, column=2)

ai_grade_var = tk.StringVar()
ai_entry = tk.Entry(top, textvariable=ai_grade_var)
ai_entry.grid(row=4, column=2)

oop_grade_var = tk.StringVar()
oop_entry = tk.Entry(top, textvariable=oop_grade_var)
oop_entry.grid(row=5, column=2)



# Sub Credit
subcredit_autonomy = 4
subcredit_electro = 4
subcredit_ai = 3
subcredit_oop = 4

sub_credit_label = tk.Label(top, text='Sub Credit')
sub_credit_label.grid(row=1, column=3)

autonomy_sub_credit_label = tk.Label(top, text=subcredit_autonomy)
autonomy_sub_credit_label.grid(row=2, column=3)

electro_sub_credit_label = tk.Label(top, text=subcredit_electro)
electro_sub_credit_label.grid(row=3, column=3)

ai_sub_credit_label = tk.Label(top, text=subcredit_ai)
ai_sub_credit_label.grid(row=4, column=3)

oop_sub_credit_label = tk.Label(top, text=subcredit_oop)
oop_sub_credit_label.grid(row=5, column=3)


grade_dict = {
    'A': 10,
    'B': 9,
    'C': 8,
    'D': 7,
    'E': 0,
    'F': 0
}

def calc_credit():
    # Autonomy
    autonomy_grade = autonomy_grade_var.get()
    
    if autonomy_grade in grade_dict:
        autonomy_credit = grade_dict[autonomy_grade] * subcredit_autonomy
    elif autonomy_grade not in grade_dict:
        autonomy_credit = 0

    # Credit per Course
    autonomy_credit_label = tk.Label(top, text=autonomy_credit)
    autonomy_credit_label.grid(row=2, column=4)

    # Electro
    electro_grade = electro_grade_var.get()
    
    if electro_grade in grade_dict:
        electro_credit = grade_dict[electro_grade] * subcredit_autonomy
    elif electro_grade not in grade_dict:
        electro_credit = 0

    # Credit per Course
    electro_credit_label = tk.Label(top, text=electro_credit)
    electro_credit_label.grid(row=3, column=4)


    # AI
    ai_grade = ai_grade_var.get()
    
    if ai_grade in grade_dict:
        ai_credit = grade_dict[ai_grade] * subcredit_autonomy
    elif ai_grade not in grade_dict:
        ai_credit = 0

    # Credit per Course
    ai_credit_label = tk.Label(top, text=ai_credit)
    ai_credit_label.grid(row=4, column=4)


    # OOP
    oop_grade = oop_grade_var.get()
    
    if oop_grade in grade_dict:
        oop_credit = grade_dict[oop_grade] * subcredit_autonomy
    elif oop_grade not in grade_dict:
        oop_credit = 0

    # Credit per Course
    oop_credit_label = tk.Label(top, text=oop_credit)
    oop_credit_label.grid(row=5, column=4)

    # Total Credit
    total_credit = autonomy_credit + electro_credit + ai_credit + oop_credit
    total_credit_label = tk.Label(top, text="Total Credit")
    total_credit_label.grid(row=6, column=2)

    total_credit_number_label = tk.Label(top, text=total_credit)
    total_credit_number_label.grid(row=6, column=4)



# Buttons
button = tk.Button(top, text="Submit", command=calc_credit)
button.grid(row=7, column=1)



top.mainloop()