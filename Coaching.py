from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import mysql.connector

root = Tk()
root.title('Epistêmê')
root.geometry("800x500")
root.state('zoomed')

# Secondary Windows
result_window = Toplevel(root)
result_window.title('Results')
result_window.withdraw()

fee_window = Toplevel(root)
fee_window.title('Fees')
fee_window.withdraw()

regis_window = Toplevel(root)
regis_window.title('Registration')
regis_window.withdraw()

# Logo
my_img = ImageTk.PhotoImage(Image.open("C:\\Users\\mohan\\OneDrive\\Desktop\\Resume Projects\\Episteme Coaching Management\\episteme logo.png"))
image_label = Label(root, image=my_img)
image_label.place(x=0, y=10, relwidth=1, relheight=1)

episteme = Label(root, text="Epistêmê", font=("Times New Roman", 30, 'bold'), fg="#ff8080")
episteme.grid(row=1, column=8)

# Dropdown options
standard_list = ['11th', '12th', 'Dropper']
target_exams_list = ['JEE (Main)', 'JEE (Main + Adv)', 'BITSAT']

# Entry Fields
first_name = Entry(regis_window, width=30)
last_name = Entry(regis_window, width=30)
aadhaar_num = Entry(regis_window, width=30)
age = Entry(regis_window, width=30)
stud_class = ttk.Combobox(regis_window, values=standard_list, width=27)
target_exams = ttk.Combobox(regis_window, values=target_exams_list, width=27)
address = Entry(regis_window, width=50)
guardf_name = Entry(regis_window, width=30)
guardl_name = Entry(regis_window, width=30)
guard_aadhaar_num = Entry(regis_window, width=30)
guardians_mobile = Entry(regis_window, width=30)

# Show Registration Form
def regisfunc():
    regis_window.deiconify()
    for widget in regis_window.winfo_children():
        widget.grid_forget()

    Label(regis_window, text="Student's First Name:", font=("Times New Roman", 12)).grid(row=0, column=0, sticky=W, padx=20, pady=5)
    first_name.grid(row=0, column=1, padx=20, pady=5)

    Label(regis_window, text="Student's Last Name:", font=("Times New Roman", 12)).grid(row=1, column=0, sticky=W, padx=20, pady=5)
    last_name.grid(row=1, column=1, padx=20, pady=5)

    Label(regis_window, text="Student's Aadhaar Number:", font=("Times New Roman", 12)).grid(row=2, column=0, sticky=W, padx=20, pady=5)
    aadhaar_num.grid(row=2, column=1, padx=20, pady=5)

    Label(regis_window, text="Student's Age:", font=("Times New Roman", 12)).grid(row=3, column=0, sticky=W, padx=20, pady=5)
    age.grid(row=3, column=1, padx=20, pady=5)

    Label(regis_window, text="Current Class:", font=("Times New Roman", 12)).grid(row=4, column=0, sticky=W, padx=20, pady=5)
    stud_class.grid(row=4, column=1, padx=20, pady=5)

    Label(regis_window, text="Target Exam:", font=("Times New Roman", 12)).grid(row=5, column=0, sticky=W, padx=20, pady=5)
    target_exams.grid(row=5, column=1, padx=20, pady=5)

    Label(regis_window, text="Current Address:", font=("Times New Roman", 12)).grid(row=6, column=0, sticky=W, padx=20, pady=5)
    address.grid(row=6, column=1, padx=20, pady=5)

    Label(regis_window, text="Guardian's First Name:", font=("Times New Roman", 12)).grid(row=7, column=0, sticky=W, padx=20, pady=5)
    guardf_name.grid(row=7, column=1, padx=20, pady=5)

    Label(regis_window, text="Guardian's Last Name:", font=("Times New Roman", 12)).grid(row=8, column=0, sticky=W, padx=20, pady=5)
    guardl_name.grid(row=8, column=1, padx=20, pady=5)

    Label(regis_window, text="Guardian's Aadhaar Number:", font=("Times New Roman", 12)).grid(row=9, column=0, sticky=W, padx=20, pady=5)
    guard_aadhaar_num.grid(row=9, column=1, padx=20, pady=5)

    Label(regis_window, text="Guardian's Contact Number:", font=("Times New Roman", 12)).grid(row=10, column=0, sticky=W, padx=20, pady=5)
    guardians_mobile.grid(row=10, column=1, padx=20, pady=5)

    submit_button.grid(row=11, column=0, columnspan=2, pady=20)

# Submit Function with Validation & Correct Insert Order
def submitfunc():
    f_name_user = first_name.get().strip()
    l_name_user = last_name.get().strip()
    name_user = f"{f_name_user} {l_name_user}"
    age_user = age.get().strip()
    address_user = address.get().strip()
    guardf_user = guardf_name.get().strip()
    guardl_user = guardl_name.get().strip()
    guard_user = f"{guardf_user} {guardl_user}"
    target_exam_user = target_exams.get().strip()
    std_user = stud_class.get().strip()
    guardians_mobile_user = guardians_mobile.get().strip()
    aadhaar_num_user = aadhaar_num.get().strip()
    guard_aadhar_user = guard_aadhaar_num.get().strip()

    if not all([f_name_user, l_name_user, age_user, address_user, guardf_user,
                guardl_user, target_exam_user, std_user, guardians_mobile_user,
                aadhaar_num_user, guard_aadhar_user]):
        messagebox.showwarning("Validation", "Blank entries in any of the fields won't be accepted")
        return

    def is_valid_name(name): return name.replace(" ", "").isalpha()

    if not all(map(is_valid_name, [f_name_user, l_name_user, guardf_user, guardl_user])):
        messagebox.showwarning("Validation", "Please enter valid names (alphabets and spaces only)")
        return

    if not age_user.isdigit() or int(age_user) < 10 or int(age_user) > 100:
        messagebox.showwarning("Validation", "Enter a valid age between 10 and 100")
        return

    if not guardians_mobile_user.isdigit() or len(guardians_mobile_user) != 10:
        messagebox.showwarning("Validation", "Enter a valid 10-digit mobile number")
        return

    if (not aadhaar_num_user.isdigit() or not guard_aadhar_user.isdigit() or
            len(aadhaar_num_user) != 12 or len(guard_aadhar_user) != 12):
        messagebox.showwarning("Validation", "Enter valid 12-digit Aadhaar numbers")
        return

    if aadhaar_num_user == guard_aadhar_user:
        messagebox.showwarning("Validation", "Student and Guardian Aadhaar numbers must be different")
        return

    if std_user not in standard_list or target_exam_user not in target_exams_list:
        messagebox.showwarning("Validation", "Select valid class and target exam")
        return

    try:
        my_connect = mysql.connector.connect(
            host="localhost", user="root", passwd="dbms2312", database="coaching_project"
        )
        my_conn = my_connect.cursor()

        # Check for duplicates
        my_conn.execute("SELECT student_aadhaar FROM student_details WHERE student_aadhaar = %s", (aadhaar_num_user,))
        if my_conn.fetchone():
            messagebox.showerror("Duplicate Entry", "Student Aadhaar already exists.")
            return

        my_conn.execute("SELECT guardian_aadhaar FROM guardian_details WHERE guardian_aadhaar = %s", (guard_aadhar_user,))
        if my_conn.fetchone():
            messagebox.showerror("Duplicate Entry", "Guardian Aadhaar already exists.")
            return

        # Insert Guardian First
        sql_guardian = "INSERT INTO guardian_details VALUES (%s, %s, %s, %s)"
        guard_value = (aadhaar_num_user, guard_aadhar_user, guard_user, guardians_mobile_user)
        my_conn.execute(sql_guardian, guard_value)

        # Then insert Student
        sql_student = "INSERT INTO student_details VALUES (%s, %s, %s, %s, %s, %s, %s)"
        stud_value = (aadhaar_num_user, name_user, guard_aadhar_user, std_user, target_exam_user, address_user, age_user)
        my_conn.execute(sql_student, stud_value)

        my_connect.commit()
        messagebox.showinfo("Success", "Registration successful")
    except Exception as e:
        messagebox.showerror("Database Error", str(e))

submit_button = Button(regis_window, text='Submit', borderwidth=7.5, width=10, command=submitfunc)

# Results Button
def resultfunc():
    result_window.deiconify()
    for widget in result_window.winfo_children():
        widget.destroy()
    try:
        my_connect = mysql.connector.connect(
            host="localhost", user="root", passwd="dbms2312", database="coaching_project"
        )
        my_conn = my_connect.cursor()
        my_conn.execute("SELECT * FROM results")

        headers = [i[0] for i in my_conn.description]
        for j, header in enumerate(headers):
            Label(result_window, text=header, font=('Arial', 10, 'bold')).grid(row=0, column=j)

        i = 1
        for row in my_conn:
            for j in range(len(row)):
                e = Entry(result_window, width=30, fg='blue')
                e.grid(row=i, column=j)
                e.insert(END, row[j])
            i += 1
    except Exception as e:
        messagebox.showerror("Database Error", str(e))

# Fee Structure Button
def feefunc():
    fee_window.deiconify()
    for widget in fee_window.winfo_children():
        widget.destroy()
    try:
        my_connect = mysql.connector.connect(
            host="localhost", user="root", passwd="dbms2312", database="coaching_project"
        )
        my_conn = my_connect.cursor()
        my_conn.execute("SELECT * FROM fee_structure")

        headers = [i[0] for i in my_conn.description]
        for j, header in enumerate(headers):
            Label(fee_window, text=header, font=('Arial', 10, 'bold')).grid(row=0, column=j)

        i = 1
        for row in my_conn:
            for j in range(len(row)):
                e = Entry(fee_window, width=30, fg='blue')
                e.grid(row=i, column=j)
                e.insert(END, row[j])
            i += 1
    except Exception as e:
        messagebox.showerror("Database Error", str(e))

# Main Buttons
result = Button(root, text='Results', command=resultfunc, width=20, height=5, bg="#006A4E", fg="#FFD700", font=("Times New Roman", 20, 'bold'))
result.grid(row=3, column=7)

fee_structure = Button(root, text='Fee Structure', command=feefunc, width=20, height=5, bg="#FF7F50", fg="#AAFF00", font=("Times New Roman", 20, 'bold'))
fee_structure.grid(row=3, column=8)

registration = Button(root, text='Register Now', command=regisfunc, width=20, height=5, bg="#FF6347", fg="#808080", font=("Times New Roman", 20, 'bold'))
registration.grid(row=3, column=9)

root.mainloop()
