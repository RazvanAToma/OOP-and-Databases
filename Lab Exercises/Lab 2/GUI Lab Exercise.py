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




def calc_credit():
    # Autonomy
    autonomy_grade = autonomy_grade_var.get()
    
    if autonomy_grade == "A":
        autonomy_credit = 10 * subcredit_autonomy
    elif autonomy_grade == "B":
        autonomy_credit = 9 * subcredit_autonomy
    elif autonomy_grade == "C":
        autonomy_credit = 8 * subcredit_autonomy
    elif autonomy_grade == "D":
        autonomy_credit = 7 * subcredit_autonomy
    else:
        autonomy_credit = 0

    # Credit per Course
    autonomy_credit_label = tk.Label(top, text=autonomy_credit)
    autonomy_credit_label.grid(row=2, column=4)

    # Electro
    electro_grade = electro_grade_var.get()
    
    if electro_grade == "A":
        electro_credit = 10 * subcredit_electro
    elif electro_grade == "B":
        electro_credit = 9 * subcredit_electro
    elif electro_grade == "C":
        electro_credit = 8 * subcredit_electro
    elif electro_grade == "D":
        electro_credit = 7 * subcredit_electro
    else:
        electro_credit = 0

    # Credit per Course
    electro_credit_label = tk.Label(top, text=electro_credit)
    electro_credit_label.grid(row=3, column=4)


    # AI
    ai_grade = ai_grade_var.get()
    
    if ai_grade == "A":
        ai_credit = 10 * subcredit_ai
    elif ai_grade == "B":
        ai_credit = 9 * subcredit_ai
    elif ai_grade == "C":
        ai_credit = 8 * subcredit_ai
    elif ai_grade == "D":
        ai_credit = 7 * subcredit_ai
    else:
        ai_credit = 0

    # Credit per Course
    ai_credit_label = tk.Label(top, text=ai_credit)
    ai_credit_label.grid(row=4, column=4)


    # OOP
    oop_grade = oop_grade_var.get()
    
    if oop_grade == "A":
        oop_credit = 10 * subcredit_oop
    elif oop_grade == "B":
        oop_credit = 9 * subcredit_oop
    elif oop_grade == "C":
        oop_credit = 8 * subcredit_oop
    elif oop_grade == "D":
        oop_credit = 7 * subcredit_oop
    else:
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