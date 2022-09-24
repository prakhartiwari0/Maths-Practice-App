from tkinter import *
from tkinter import ttk
# from PIL import Image, ImageTk
import random
import time
quesno = 1
answers_list = []
ques = []

def print_out_the_details():
    details = f""


def o():
    if sel_difflvl=="Easy":
        a = random.randint(0, 50)
        b = random.randint(0, a)
    elif sel_difflvl=="Intermediate":
        a = random.randint(0, 100)
        b = random.randint(0, a)
    elif sel_difflvl=="Hard":
        a = random.randint(100, 500)
        b = random.randint(100, a)
    else:
        a = random.randint(100, 1000)
        b = random.randint(100, a)
    return a, b

def answer_creator(f, s):
    if sel_arith=="Multiplication":
        ans = f * s
    elif sel_arith=="Addition":
        ans = f + s
    else:
        ans = f - s
    return ans

def result_maker():
    full_end_time = time.time()
    full_time_taken = float(format(((full_end_time)-(full_start_time)), '.2f'))
    if full_time_taken>59:
        full_printable_time= f"""The time taken to complete the whole test is : {format((full_time_taken)/60, '.2f')} minutes"""
    else:
        full_printable_time = f"""The time taken to complete the whole test is : {full_time_taken} seconds"""
    lf.destroy()
    back_button.destroy()
    # Submitter.destroy()
    heading_label.destroy()
    maxmarks = number_of_ques.get()
    n = 0
    marks_obtained = 0
    for i in range(number_of_ques.get()):
        if answers_list[n][0]==answers_list[n][1]:
            marks_obtained = marks_obtained+1
        else:
            pass
        n = n+1
    if (negmon.get()) == 1:
        marks_obtained = marks_obtained-((maxmarks-marks_obtained)*1)
    else:
        pass
    percentage = (100*marks_obtained)/maxmarks
    you_have_obtained = f"You have obtained {marks_obtained} marks out of {maxmarks}"
    you_got_percent = f"You have got {percentage}%"

    if 99<=percentage<=100:
        grade = "A++"
        remark = "OUTSTANDING!!"
    elif 95<=percentage<=99:
        grade = "A+"
        remark = "EXCELLENT!!"
    elif 90<=percentage<=95:
        grade = "A"
        remark = "VERY GOOD!"
    elif 85<=percentage<=90:
        grade = "B"
        remark = "GOOD"
    elif 80<=percentage<=85:
        grade = "C"
        remark = "NICE TRY"
    elif 70<=percentage<=80:
        grade = "D"
        remark = "YOU CAN BE SATISFIED"
    elif 50<=percentage<=70:
        grade = "E"
        remark = "YOU NEED IMPROVEMENT"
    elif 30<=percentage<=50:
        grade = "-E"
        remark = "YOU ARE AT MARGIN,"
    else:
        grade = "F"
        remark = "YOU FAILED,"
    
    # print(grade)
    global result_label, grade_label, remark_label, marks_label, percent_label, time_taken_label, retest_button, grade_info_button, average_time_time_taken_label
    result_label = Label(root, text="YOUR RESULT", fg="black", bg="lightgreen", font="orbitron 30 bold", relief=SUNKEN, borderwidth=5)
    result_label.pack(fill=X)
    grade_label = Label(root, text=f"GRADE {grade}", fg="red", bg="yellow", font="orbitron 80 bold")
    grade_label.pack()
    remark_label = Label(root, text=f"{remark} {name_of_the_student.get()}", fg="orange", bg="yellow", font="orbitron 30 bold")
    remark_label.pack()
    marks_label = Label(root, text=you_have_obtained, fg="black", bg="yellow", font="orbitron 40 bold")
    marks_label.pack()
    percent_label = Label(root, text=f"{you_got_percent}", fg="blue", bg="yellow", font="orbitron 70 bold")
    percent_label.pack()
    time_taken_label = Label(root, text=full_printable_time, fg="darkgreen", bg="yellow", font="orbitron 25 bold")
    time_taken_label.pack()
    average_time_time_taken_label = Label(root, text=f"Average time taken to complete each question {format(((full_end_time-full_start_time)/number_of_ques.get()), '.2f')} seconds", fg="purple", bg="yellow", font="orbitron 20 bold")
    average_time_time_taken_label.pack()
    grade_info_button = Button(root, text="ABOUT GRADES", fg="white", bg="black", font="orbitron 18 bold", command=grade_info_window)
    grade_info_button.pack(side=LEFT, anchor="s")
    retest_button = Button(root, text="TEST ME AGAIN", fg="white", bg="black", font="orbitron 18 bold", command=gobacktooptions)
    retest_button.pack(side=BOTTOM, anchor="w")

def grade_info_window():
    gw = Tk()
    gw.title("GRADES INFO")
    #gw.iconbitmap("ICON.ico")
    gw.geometry("600x600")
    gw.maxsize(600, 600)
    gw.minsize(600, 600)
    gw.config(bg="green")
    grades = "A++  -->  100-99 PERCENTAGE\nA+  -->  99-95 PERCENTAGE\nA  -->  95-90 PERCENTAGE\nB  -->  90-85 PERCENTAGE\nC  -->  85-80  PERCENTAGE\nD  -->  80-70 PERCENTAGE\nE  -->  70-50 PERCENTAGE\n-E  -->  50-30 PERCENTAGE\nF  -->  30-0 PERCENTAGE"
    gl = Label(gw, text=grades, fg="white", font="orbitron 18 bold", bg="green", justify="left")
    gl.pack()
    gw.mainloop()
printable_time = ""
con = ""
def singles_R(event):
    global printable_time, con, quesno

    lf.destroy()
    conl.destroy()
    btl.destroy()
    question_no_label.destroy()
    end_time = time.time()
    time_taken = str(end_time-start_time)
    c = time_taken.index(".")+1
    c1 = len(time_taken)-2
    c2 = time_taken[c:c1]
    total_time_taken = time_taken.replace(c2, "")
    printable_time = f"""Previous question was solved in : {total_time_taken} seconds"""
    ques.append(1)
    quesno = len(ques)+1
    # print(qeun)
    q = len(ques)
    w = number_of_ques.get()
    answers_list.append([real_answer, int(user_answer.get())])
    if real_answer==int(user_answer.get()):
        con = "PREVIOUS ANSWER WAS CORRECT"
    else:
        con = "PREVIOUS ANSWER WAS INCORRECT"
    if q==w:
        result_maker()
    else:
        singles()


def singles():
    global lf, lf, start_time, l, le, answer, real_answer, user_answer, live_correction_status_frame, btl, printable_time, con, conl, question_no_label, quesno #,Submitter
    # try:
    #     question_no_label.update()
    # except:
    #     pass
    n = o()
    real_answer = answer_creator(n[0], n[1])
    user_answer = StringVar()
    btl = Label(root, text=printable_time, font="orbitron 20 bold", fg="black", bg="yellow")
    btl.pack(side=TOP, anchor="n")
    conl = Label(root, text=con, font="orbitron 20 bold", fg="black", bg="yellow")
    conl.pack(side=TOP)
    question_no_label = Label(root, text=f"Question No.{quesno}/{number_of_ques.get()}", font="orbitron 20 bold", fg="black", bg="yellow")
    question_no_label.pack(side=TOP)
    lf = Frame(root, relief=SUNKEN, borderwidth=30)
    lf.pack(side=TOP, anchor="n")
    l = Label(lf, text=f"{n[0]}\n{signer()} {n[1]}", justify=RIGHT, font="orbitron 70 bold")
    l.pack(side=TOP, anchor="n")
    le = Entry(lf,font="orbitron 50", width=5, textvariable=user_answer, justify="right",)
    le.pack(side=RIGHT, anchor="se")
    le.icursor(0)
    le.bind('<Return>', singles_R)
##    Submitter = Button(text="SUBMIT", command=singles_R, font="orbitron 35 bold")
##    Submitter.pack(side=BOTTOM, anchor="s")
    
##    root.bind('<space>', le)
    
    start_time = time.time()

def signer():
    if sel_arith=="Multiplication":
        sign = "x"
    elif sel_arith=="Addition":
        sign = "+"
    else:
        sign = "-"
    return sign


def test_page_single_questions():
    global sel_arith, sel_difflvl, heading_label, full_start_time, back_button

    full_start_time = time.time()
    test_options_frame.destroy()
    sel_arith = selected_arithmetic.get()
    sel_difflvl = selected_difficulty_level.get()
    root.config(bg="yellow")
    heading_label = Label(root, text="TEST PAGE", fg="black", bg="lightgreen", font="orbitron 20 bold", relief=SUNKEN, borderwidth=5)
    heading_label.pack(fill=X)
    back_button = Button(root, text="<- GO BACK", fg="white", bg="black", font="orbitron 15 bold", command=gobacktooptions)
    back_button.pack(side=BOTTOM, anchor="w")
    singles()

def gobacktooptions():
    global printable_time, con, quesno
    root.config(bg="green")
    printable_time = "Time taken is :"
    con = ""
    quesno = 1
    answers_list.clear()
    ques.clear()
    heading_label.destroy()
    back_button.destroy()
    btl.destroy()
    conl.destroy()
    question_no_label.destroy()
    lf.destroy()
    try:
        result_label.destroy()
        grade_label.destroy()
        remark_label.destroy()
        marks_label.destroy()
        percent_label.destroy()
        time_taken_label.destroy()
        average_time_time_taken_label.destroy()
        retest_button.destroy()
        grade_info_button.destroy()
    except Exception as e:
        pass
    test()


sv = 0
def OnMouseWheel(event):
    global sv
    e = str(event)
    if "-" in e:
        number_of_ques_entry.delete(0, END)
        number_of_ques_entry.insert(0, sv)
        sv = sv-1
    else:
        number_of_ques_entry.delete(0, END)
        number_of_ques_entry.insert(0, sv)
        sv = sv+1
    jj = number_of_ques.get()
    if "-" in str(jj):
        a = 0
        number_of_ques_entry.delete(0, END)
        number_of_ques_entry.insert(0, a)


def test():
    global selected_arithmetic, selected_difficulty_level, negmon, test_options_frame, number_of_ques, tell_number_of_ques, number_of_ques_entry, name_of_the_student
    arithmetics = ["Multiplication", "Addition", "Subtraction"]
    difficulty_levels = ["Easy", "Intermediate", "Hard", "Very hard"]
    test_options_frame = Frame(root, bg="green")
    test_options_frame.pack()
    enl = Label(test_options_frame, text="YOUR NAME PLEASE", fg="white",bg="green", font="orbitron 15 bold underline")
    enl.pack()
    name_of_the_student = StringVar()
    name_of_the_student_entry = Entry(test_options_frame, textvariable=name_of_the_student, font="orbitron 20 bold" )
    name_of_the_student_entry.pack()
    Label(test_options_frame, text="", bg="green", pady=10).pack()
    select_arithmetic = Label(test_options_frame, text="Choose one of the arithmetic",fg="white",bg="green", font="orbitron 20 bold underline")
    select_arithmetic.pack()
    selected_arithmetic = StringVar()
    arithmetics_dropdown = ttk.Combobox(test_options_frame, width=20, textvariable=selected_arithmetic, font="orbitron 20 bold")
    arithmetics_dropdown['values'] = (arithmetics)
    arithmetics_dropdown.pack()
    Label(test_options_frame, text="", bg="green", pady=10).pack()
    select_arithmetic = Label(test_options_frame, text="Choose difficulty level", fg="white", bg="green",font="orbitron 20 bold underline")
    select_arithmetic.pack()
    selected_difficulty_level = StringVar()
    difficulty_level_dropdown = ttk.Combobox(test_options_frame, width=20, textvariable=selected_difficulty_level, font="orbitron 20 bold")
    difficulty_level_dropdown['values'] = (difficulty_levels)
    difficulty_level_dropdown.pack()
    Label(test_options_frame, text="", bg="green", pady=10).pack()
    negmon = IntVar()
    negmon_checkbutton = Checkbutton(test_options_frame, cursor="cross",text="Negative marking (Additional 1 marks will be deducted for every wrong answers)", font="orbitron 14 bold", variable=negmon)
    negmon_checkbutton.pack()
    Label(test_options_frame, text="", bg="green", pady=10).pack()

    number_of_ques = IntVar()
    tell_number_of_ques = Label(test_options_frame, text="Tell the number of questions you want (Only EVEN NUMBERS)", fg="white", bg="green", font="orbitron 20 bold underline")
    tell_number_of_ques.pack()
    number_of_ques_entry = Entry(test_options_frame, textvariable=number_of_ques, font="orbitron 20 bold", cursor="plus")
    number_of_ques_entry.pack()
    number_of_ques_entry.bind("<MouseWheel>", OnMouseWheel)
    Label(test_options_frame, text="", bg="green", pady=10).pack()
    submit_button = Button(test_options_frame, text="START TEST", font="orbitron 20 bold", command=test_page_single_questions, pady=9)
    submit_button.pack()

root = Tk()
root.title("YOUR MATHS SKILL")
#root.iconbitmap("ICON.ico")
headimg = PhotoImage(file="HEADIMG.png")
headimg_label = Label(image=headimg, bg="green")
headimg_label.pack(fill=X)
root.geometry("1300x610")
root.config(bg="green")
test()
root.mainloop()
