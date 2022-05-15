from tkinter import messagebox
import mysql.connector
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import os
import numpy as np
import csv
from tkinter import filedialog
from datetime import datetime


mydata=[]

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")
        self.homepage()

###############################Home Page##################################

    def homepage(self):
        for i in self.root.winfo_children():
            i.destroy()

        img = Image.open(r"C:\Users\Sandesh\Desktop\face_recognition system\images\herald.png")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        fibl = Label(self.root, image=self.photoimg)
        fibl.place(x=0, y=0, width=1500, height=130)

        title_lbl = Label(self.root, text="Face Recognition Attendance System", font=("Times", 35, "bold"),
                          fg="black")
        title_lbl.place(x=0, y=180, width=1500, height=70)

        # Face Detect
        img2 = Image.open(r"C:\Users\Sandesh\Desktop\face_recognition system\images\FaceD.png")
        img2 = img2.resize((150, 150), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        fibl = Label(self.root, image=self.photoimg2)
        fibl.place(x=150, y=300, width=150, height=150)

        b2 = Button(self.root, text = "Face Detection", command=self.face_recognition, cursor="hand2", font=("Times", 15, "bold"), fg="black")
        b2.place(x=150, y=450, width=150, height=40)

        # Admin
        img5 = Image.open(r"C:\Users\Sandesh\Desktop\face_recognition system\images\Admin.png")
        img5 = img5.resize((150, 150), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        fibl = Label(self.root, image=self.photoimg5)
        fibl.place(x=400, y=300, width=150, height=150)

        b2 = Button(self.root, text = "Admin", cursor="hand2",command=self.login_window, font=("Times", 15, "bold"), fg="black")
        b2.place(x=400, y=450, width=150, height=40)

###############################Admin Page################################################


    def admin(self):
        for i in self.root.winfo_children():
            i.destroy()


        img = Image.open(r"C:\Users\Sandesh\Desktop\face_recognition system\images\herald.png")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        fibl = Label(self.root, image=self.photoimg)
        fibl.place(x=0, y=0, width=1500, height=130)

        title_lbl = Label(self.root, text="Face Recognition Attendance System", font=("Times", 35, "bold"),
                          fg="black")
        title_lbl.place(x=0, y=180, width=1500, height=70)

        b1 = ttk.Button(text="Back", cursor="hand2", command=self.homepage)
        b1.place(x=100, y=110)

        # student
        img1 = Image.open(r"C:\Users\Sandesh\Desktop\face_recognition system\images\Student.png")
        img1 = img1.resize((150, 150), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        fibl = Label(self.root, image=self.photoimg1)
        fibl.place(x=150, y=300, width=150, height=150)

        b1 = Button(self.root, text = "Student Details", command=self.student_details, cursor="hand2", font=("Times", 15, "bold"), fg="black")
        b1.place(x=150, y=450, width=150, height=40)

        # Attendance
        img3 = Image.open(r"C:\Users\Sandesh\Desktop\face_recognition system\images\attendance.png")
        img3 = img3.resize((150, 150), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        fibl = Label(self.root, image=self.photoimg3)
        fibl.place(x=400, y=300, width=150, height=150)

        b2 = Button(self.root, text = "Attendance",command=self.attendance, cursor="hand2", font=("Times", 15, "bold"), fg="black")
        b2.place(x=400, y=450, width=150, height=40)

        # Train
        img4 = Image.open(r"C:\Users\Sandesh\Desktop\face_recognition system\images\teacher.png")
        img4 = img4.resize((150, 150), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        fibl = Label(self.root, image=self.photoimg4)
        fibl.place(x=650, y=300, width=150, height=150)

        b2 = Button(self.root, text = "Train", cursor="hand2",command=self.train_data, font=("Times", 15, "bold"), fg="black")
        b2.place(x=650, y=450, width=150, height=40)




################################mark CSV attendance###########################

    def mark_attendance(self, i, r, n, d):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])

            if((i not in name_list) and (r not in name_list) and (n not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1}, Present")

#############################Login Window#########################################

    def login_window(self):
        for i in self.root.winfo_children():
            i.destroy()

        img = Image.open(r"C:\Users\Sandesh\Desktop\face_recognition system\images\herald.png")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        fibl = Label(self.root, image=self.photoimg)
        fibl.place(x=0, y=0, width=1500, height=130)

        title_lbl = Label(self.root, text="Login Panel", font=("Times", 25, "bold"),
                          fg="black")
        title_lbl.place(x=0, y=180, width=1500, height=70)

        b1 = ttk.Button(text="Back", cursor="hand2", command=self.homepage)
        b1.place(x=100, y=110)

        frame = Frame(self.root, bg="White")
        frame.place(x=600, y=300, width=340, height=450)

        get_str = Label(frame, text="Login", font=("Arial", 20, "bold"), fg="Black", bg="white")
        get_str.place(x=120, y=60)

        username = lbl = Label(frame, text="Username", font=("Arial", 15, "bold"), fg="Black", bg="white")
        username.place(x=20, y=150)

        self.txtuser = ttk.Entry(frame, font=("Arial", 10))
        self.txtuser.place(x=130, y=150, width=200, height=30)

        password = lbl = Label(frame, text="Password", font=("Arial", 15, "bold"), fg="Black", bg="white")
        password.place(x=20, y=250)

        self.txtpass = ttk.Entry(frame,show="*", font=("Arial", 10))
        self.txtpass.place(x=130, y=250, width=200, height=30)

        self.b = Button(self.root, command=self.login, text="Login", cursor="hand2", font=("Times", 15, "bold"),
                        fg="black")
        self.b.place(x=700, y=660, width=150, height=40)

############################Login connect to mysql#######################################
    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "all field required")
        else:
            conn = mysql.connector.connect(user='root', password='trade1', host='127.0.0.1',
                                           port=3306, database='login', auth_plugin='mysql_native_password')
            my_cursor = conn.cursor()
            my_cursor.execute("select * from Login where username=%s and password=%s", (
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid Username or Password")
            else:
                open_main = messagebox.askyesno("YesNo", "Access only admin")
                if open_main > 0:
                    for i in self.root.winfo_children():
                        i.destroy()
                    self.admin()
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()


#################################Student Details#######################
    def student_details(self):
        for i in self.root.winfo_children():
            i.destroy()

            self.root = root
            self.root.geometry("1920x1080+0+0")
            self.root.title("Face Recognition System")

            # Variables
            self.var_dep = StringVar()
            self.var_course = StringVar()
            self.var_year = StringVar()
            self.var_semester = StringVar()
            self.var_std_id = StringVar()
            self.var_std_name = StringVar()
            self.var_div = StringVar()
            self.var_roll = StringVar()
            self.var_gender = StringVar()
            self.var_dob = StringVar()
            self.var_email = StringVar()
            self.var_phone = StringVar()
            self.var_address = StringVar()
            self.var_teacher = StringVar()

            img = Image.open(r"C:\Users\Sandesh\Desktop\face_recognition system\images\herald.png")
            img = img.resize((500, 130), Image.ANTIALIAS)
            self.photoimg = ImageTk.PhotoImage(img)

            fibl = Label(self.root, image=self.photoimg)
            fibl.place(x=0, y=0, width=1500, height=130)

            title_lbl = Label(self.root, text="Face Recognition Attendance System", font=("Times", 20, "bold"),
                              fg="black")
            title_lbl.place(x=0, y=180, width=1500, height=70)

            b1 = ttk.Button(text="Back", cursor="hand2", command=self.admin)
            b1.place(x=100, y=110)

            main_frame = Frame(self.root, bd=2)
            main_frame.place(x=60, y=250, width=1400, height=500)

            # left side frame

            Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details",
                                    font=("Times new roman", 12, "bold"))
            Left_frame.place(x=10, y=0, width=660, height=490)

            # CurrentCourse side frame

            Current_Course = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Course Information",
                                        font=("Times new roman", 12, "bold"))
            Current_Course.place(x=10, y=0, width=640, height=150)

            # Department
            dep_label = Label(Current_Course, text="Department", font=("Times new roman", 12, "bold"))
            dep_label.grid(row=0, column=0, padx=10, sticky=W)

            dep_combo = ttk.Combobox(Current_Course, textvariable=self.var_dep, font=("Times new roman", 12, "bold"),
                                     state="readonly")
            dep_combo["values"] = ("Select Department", "BIT", "BBA")
            dep_combo.current(0)
            dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

            # Courses
            Course_label = Label(Current_Course, text="Course", font=("Times new roman", 12, "bold"))
            Course_label.grid(row=0, column=2, padx=10, sticky=W)

            Course_combo = ttk.Combobox(Current_Course, textvariable=self.var_course,
                                        font=("Times new roman", 12, "bold"), state="readonly")
            Course_combo["values"] = ("Select Course", "AI", "Object Oriented")
            Course_combo.current(0)
            Course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

            # Year
            Year_label = Label(Current_Course, text="Year", font=("Times new roman", 12, "bold"))
            Year_label.grid(row=1, column=0, padx=10, sticky=W)

            Year_combo = ttk.Combobox(Current_Course, textvariable=self.var_year, font=("Times new roman", 12, "bold"),
                                      state="readonly")
            Year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23")
            Year_combo.current(0)
            Year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

            # Semester
            Semester_label = Label(Current_Course, text="Semester", font=("Times new roman", 12, "bold"))
            Semester_label.grid(row=1, column=2, padx=10, sticky=W)

            Semester_combo = ttk.Combobox(Current_Course, textvariable=self.var_semester,
                                          font=("Times new roman", 12, "bold"), state="readonly")
            Semester_combo["values"] = ("Select Semester", "Semester-1", "Semester-2")
            Semester_combo.current(0)
            Semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

            # Class Student information
            class_student_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Class student Information",
                                             font=("Times new roman", 12, "bold"))
            class_student_frame.place(x=10, y=150, width=640, height=300)

            # student id
            studentId_label = Label(class_student_frame, text="Student ID", font=(
                "Times new roman", 12, "bold"))
            studentId_label.grid(row=0, column=0, padx=10, sticky=W)

            studentID_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id, width=20, font=(
                "Times new roman", 12, "bold"))
            studentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

            # student name
            studentName_label = Label(class_student_frame, text="Student Name", font=(
                "Times new roman", 12, "bold"))
            studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

            studentName_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_name, width=20, font=(
                "Times new roman", 12, "bold"))
            studentName_entry.grid(row=0, column=3, padx=10, sticky=W)

            # class division
            class_div_label = Label(class_student_frame, text="Class Division", font=(
                "Times new roman", 12, "bold"))
            class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

            div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div, font=(
                "Times new roman", 12, "bold"), state="readonly", width=20)
            div_combo['values'] = ("A", "B",
                                   "C", "D")
            div_combo.current(0)
            div_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

            # roll_no
            roll_no_label = Label(class_student_frame, text="Roll No.", font=(
                "Times new roman", 12, "bold"))
            roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

            roll_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, width=20, font=(
                "Times new roman", 12, "bold"))
            roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

            # gender
            gender_label = Label(class_student_frame, text="Gender", font=(
                "Times new roman", 12, "bold"))
            gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

            gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=(
                "Times new roman", 12, "bold"), state="readonly", width=20)
            gender_combo['values'] = ("Male", "Female",
                                      "Other")
            gender_combo.current(0)
            gender_combo.grid(row=2, column=1, padx=2, pady=10, sticky=W)

            # dob
            dob_label = Label(class_student_frame, text="DOB", font=(
                "Times new roman", 12, "bold"))
            dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

            dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20, font=(
                "Times new roman", 12, "bold"))
            dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

            # email
            email_label = Label(class_student_frame, text="Email", font=(
                "Times new roman", 12, "bold"))
            email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

            email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=(
                "Times new roman", 12, "bold"))
            email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

            # phone
            phone_label = Label(class_student_frame, text="Phone No.", font=(
                "Times new roman", 12, "bold"))
            phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

            phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20, font=(
                "Times new roman", 12, "bold"))
            phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

            # address
            address_label = Label(class_student_frame, text="Address", font=(
                "Times new roman", 12, "bold"))
            address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

            address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20, font=(
                "Times new roman", 12, "bold"))
            address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

            # teacher
            teacher_label = Label(class_student_frame, text="Teacher Name", font=(
                "Times new roman", 12, "bold"))
            teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

            teacher_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacher, width=20, font=(
                "Times new roman", 12, "bold"))
            teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

            # radio buttons
            self.var_radio1 = StringVar()
            radiobtn1 = ttk.Radiobutton(
                class_student_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
            radiobtn1.grid(row=6, column=0, padx=10, pady=5)

            # self.var_radio2 = StringVar()
            radiobtn2 = ttk.Radiobutton(
                class_student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
            radiobtn2.grid(row=6, column=1, padx=10, pady=5)

            # buttons frame
            btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE)
            btn_frame.place(x=20, y=220, width=600, height=50)

            save_btn = Button(btn_frame, text='Save', command=self.add_data, width=11, font=(
                "Times new roman", 10), bg='grey', fg='white')
            save_btn.grid(row=0, column=0, padx=3, pady=7)

            update_btn = Button(btn_frame, text='Update', command=self.update_data, width=11, font=(
                "Times new roman", 10), bg='grey', fg='white')
            update_btn.grid(row=0, column=1, padx=3, pady=7)

            delete_btn = Button(btn_frame, text='Delete', command=self.delete_data, width=11, font=(
                "Times new roman", 10), bg='grey', fg='white')
            delete_btn.grid(row=0, column=2, padx=3, pady=7)

            reset_btn = Button(btn_frame, text='Reset', command=self.reset_data, width=11, font=(
                "Times new roman", 10,), bg='grey', fg='white')
            reset_btn.grid(row=0, column=3, padx=3, pady=7)

            take_photo_btn = Button(btn_frame, text='Take Photo', command=self.generate_dataset, width=11, font=(
                "Times new roman", 10), bg='grey', fg='white')
            take_photo_btn.grid(row=0, column=4, padx=3, pady=7)

            # Right side frame
            Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details",
                                     font=("Times new roman", 12, "bold"))
            Right_frame.place(x=680, y=0, width=660, height=490)



            # Table Frame
            table_frame = Frame(
                Right_frame, bd=2, relief=RIDGE)
            table_frame.place(x=10, y=10, width=645, height=450)

            scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
            scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

            self.student_table = ttk.Treeview(table_frame, column=(
            'dep', 'course', 'year', 'sem', 'id', 'name', 'div', 'roll', 'gender', 'dob', 'email', 'phone', 'address',
            'teacher', 'photo'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_x.config(command=self.student_table.xview)
            scroll_y.config(command=self.student_table.yview)

            self.student_table.heading('dep', text='Department')
            self.student_table.heading('course', text='Course')
            self.student_table.heading('year', text='Year')
            self.student_table.heading('sem', text='Semester')
            self.student_table.heading('id', text='StudentId')
            self.student_table.heading('name', text='Name')
            self.student_table.heading('roll', text='Roll No')
            self.student_table.heading('gender', text='Gender')
            self.student_table.heading('div', text='Division')
            self.student_table.heading('dob', text='DOB')
            self.student_table.heading('email', text='Email')
            self.student_table.heading('phone', text='Phone')
            self.student_table.heading('address', text='Address')
            self.student_table.heading('teacher', text='Teacher')
            self.student_table.heading('photo', text='PhotoSampleStatus')
            self.student_table['show'] = 'headings'

            self.student_table.column('dep', width=100)
            self.student_table.column('course', width=100)
            self.student_table.column('year', width=100)
            self.student_table.column('sem', width=100)
            self.student_table.column('id', width=100)
            self.student_table.column('name', width=100)
            self.student_table.column('roll', width=100)
            self.student_table.column('gender', width=100)
            self.student_table.column('div', width=100)
            self.student_table.column('dob', width=100)
            self.student_table.column('email', width=100)
            self.student_table.column('phone', width=100)
            self.student_table.column('address', width=100)
            self.student_table.column('teacher', width=100)
            self.student_table.column('photo', width=100)

            self.student_table.pack(fill=BOTH, expand=1)
            self.student_table.bind("<ButtonRelease>", self.get_cursor)
            self.fetch_data()

            # function declaration

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(user='root', password='trade1', host='127.0.0.1', port=3306,
                                               database='face_recognizer',
                                               auth_plugin='mysql_native_password')
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_id.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get()

                    ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Student Details has been added successfully", parent=self.root)
                self.reset_data()

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to :{str(es)}", parent=self.root)

            # Fetch data

    def fetch_data(self):
        conn = mysql.connector.connect(user='root', password='trade1', host='127.0.0.1',
                                       port=3306, database='face_recognizer', auth_plugin='mysql_native_password')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(
                *self.student_table.get_children())
            for i in data:
                self.student_table.insert('', END, values=i)
            conn.commit()
        conn.close()

    # get cursor

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # update function

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno(
                    "Update", "Do you want to update this data?", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(user='root', password='trade1', host='127.0.0.1', port=3306,
                                                   database='face_recognizer',
                                                   auth_plugin='mysql_native_password')
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "UPDATE student SET Dep=%s,course=%s,Year=%s, Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,dob=%s, Email=%s,Phone=%s, Address=%s, Teacher=%s,PhotoSample=%s where Student_id=%s",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get()

                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo(
                    "Success", "Student details successfully updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
                self.reset_data()

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to: {str(es)}", parent=self.root)

    # Delete Function

    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "Student id is not selected", parent=self.root)
        else:
            try:
                Delete = messagebox.askyesno(
                    "Delete", "Are you sure you want to delete this data?", parent=self.root)
                if Delete > 0:
                    conn = mysql.connector.connect(user='root', password='trade1', host='127.0.0.1', port=3306,
                                                   database='face_recognizer',
                                                   auth_plugin='mysql_native_password')
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Delete", "Data deleted successfully", parent=self.root)
                self.reset_data()

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to: {str(es)}", parent=self.root)

    # Reset Button
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

        # Generate dataset or take picture samples

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(user='root', password='trade1', host='127.0.0.1', port=3306,
                                               database='face_recognizer',
                                               auth_plugin='mysql_native_password')
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute(
                    "UPDATE student SET Dep=%s,course=%s,Year=%s, Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,dob=%s, Email=%s,Phone=%s, Address=%s, Teacher=%s,PhotoSample=%s where Student_id=%s",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get() == id + 1

                    ))
                conn.commit()
                self.fetch_data()
                # self.reset_data()
                conn.close()

                # Load predefined data on face frontal from open cv

                face_classifier = cv2.CascadeClassifier(
                    "haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # scaling factor = 1.3
                    # minimum neighbor = 5

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(
                            face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "Face/user." + \
                                         str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo(
                    "Result", "Generating data completed successfully")

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to: {str(es)}", parent=self.root)

####################### Train#######################################################################

    def train_data(self):
        data_dir = "face"
        location = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in location:
            img = Image.open(image).convert('L')  # grayscale image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13

        ids = np.array(ids)

        # Train the classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training successful!")

###############################Face Detection###################################################
    def face_recognition(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbors)

            coordinates = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(user='root', password='trade1', host='127.0.0.1', port=3306, database='face_recognizer', auth_plugin='mysql_native_password')
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Name FROM student WHERE Student_id =" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("SELECT Roll FROM student WHERE Student_id =" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("SELECT Dep FROM student WHERE Student_id =" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                my_cursor.execute("SELECT Student_id FROM student WHERE Student_id =" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)


                if confidence > 80:
                    cv2.putText(
                        img, f"Id:{i}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Roll:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Name:{n}", (x, y-35), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Department:{d}", (x, y-15), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i, r, n, d)

                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(
                    img, "Unknown", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coordinates = [x, y, w, y]

            return coordinates

        def recognize(img, clf, faceCascade):
            coordinates = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

#################################################Attendance Import Export######################################

    def attendance(self):
        for i in self.root.winfo_children():
            i.destroy()

        # -----------Variables-------------------
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        img = Image.open(r"C:\Users\Sandesh\Desktop\face_recognition system\images\herald.png")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        fibl = Label(self.root, image=self.photoimg)
        fibl.place(x=0, y=0, width=1500, height=130)

        title_lbl = Label(self.root, text="Face Recognition Attendance System", font=("Times", 35, "bold"),
                          fg="black")
        title_lbl.place(x=0, y=180, width=1500, height=70)

        b1 = ttk.Button(text="Back", cursor="hand2", command=self.admin)
        b1.place(x=100, y=110)

        main_frame = Frame(self.root, bd=2)
        main_frame.place(x=60, y=250, width=1400, height=500)

        # left side frame

        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Attendance Details",
                                font=("Times new roman", 12, "bold"))
        Left_frame.place(x=10, y=0, width=660, height=490)

        # Right side frame
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Attendance Details",
                                 font=("Times new roman", 12, "bold"))
        Right_frame.place(x=680, y=0, width=660, height=490)

        # attendance id
        attendanceId_label = Label(Left_frame, text="Attendance ID", font=("arial", 12, "bold"))
        attendanceId_label.grid(row=0, column=0, padx=10, sticky=W)

        attendanceID_entry = ttk.Entry(Left_frame, width=20, textvariable=self.var_atten_id,
                                       font=("arial", 12, "bold"))
        attendanceID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # roll
        rollLabel = Label(Left_frame, text="Roll No.", font=(
            "arial", 12, "bold"))
        rollLabel.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        atten_roll = ttk.Entry(Left_frame, textvariable=self.var_atten_roll, width=20, font=(
            "arial", 12, "bold"))
        atten_roll.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Name
        nameLabel = Label(Left_frame, text="Name", font=(
            "arial", 12, "bold"))
        nameLabel.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        atten_name = ttk.Entry(Left_frame, textvariable=self.var_atten_name, width=20, font=(
            "arial", 12, "bold"))
        atten_name.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Department
        depLabel = Label(Left_frame, text="Department", font=(
            "arial", 12, "bold"))
        depLabel.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        atten_dep = ttk.Entry(Left_frame, width=20, textvariable=self.var_atten_dep, font=(
            "arial", 12, "bold"))
        atten_dep.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Time
        timeLabel = Label(Left_frame, text="Time", font=(
            "arial", 12, "bold"))
        timeLabel.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        atten_time = ttk.Entry(Left_frame, width=20, textvariable=self.var_atten_time, font=(
            "arial", 12, "bold"))
        atten_time.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Date
        dateLabel = Label(Left_frame, text="Date", font=(
            "arial", 12, "bold"))
        dateLabel.grid(row=5, column=0, padx=10, pady=5, sticky=W)

        atten_date = ttk.Entry(Left_frame, textvariable=self.var_atten_date, width=20, font=(
            "arial", 12))
        atten_date.grid(row=5, column=1, padx=10, pady=5, sticky=W)

        # attendace
        attendanceLabel = Label(Left_frame, text="Attendance Status", font=(
            "arial", 12, "bold"))
        attendanceLabel.grid(row=6, column=0, padx=10, pady=5, sticky=W)

        self.atten_status = ttk.Combobox(Left_frame, width=20, font="arial 12",
                                         textvariable=self.var_atten_attendance, state="readonly")
        self.atten_status['values'] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=6, column=1, padx=10, pady=5, sticky=W)
        self.atten_status.current(0)

        # buttons frame
        btn_frame = Frame(Left_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=5, y=400, width=500, height=50)

        import_btn = Button(btn_frame, text='Import csv', command=self.importCsv, width=15, font=(
            "arial", 12, "bold"), bg='grey', fg='white')
        import_btn.grid(row=0, column=0, padx=2, pady=7)

        export_btn = Button(btn_frame, text='Export csv', command=self.exportCsv, width=15, font=(
            "arial", 12, "bold"), bg='grey', fg='white')
        export_btn.grid(row=0, column=1, padx=2, pady=7)

        reset_btn = Button(btn_frame, text='Reset', command=self.reset_data_attendance, width=15, font=(
            "arial", 12, "bold"), bg='grey', fg='white')
        reset_btn.grid(row=0, column=3, padx=2, pady=7)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=10, y=10, width=640, height=450)

        # Scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column=(
        "id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set,
                                                  yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable['show'] = "headings"

        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor_attendance)

    # Fetch csv data

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(
            *self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    # import csv file
    def importCsv(self):
        global mydata
        mydata.clear()
        filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open csv", filetypes=(
            ("CSV File", ".csv"), ("All file", ".*")), parent=self.root)
        with open(filename) as myfile:
            readfile = csv.reader(myfile, delimiter=",")
            for i in readfile:
                mydata.append(i)
            self.fetchData(mydata)

    # export csv file
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror(
                    "No data found", "No data found to export", parent=self.root)
                return False
            filename = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open csv", filetypes=(
                ("CSV File", ".csv"), ("All file", ".*")), parent=self.root)
            with open(filename, mode="w", newline="") as myfile:
                export_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    export_write.writerow(i)
                messagebox.showinfo(
                    "Information", "Data exported successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror(
                "Error", f"Due to :{str(es)}", parent=self.root)

    def get_cursor_attendance(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data_attendance(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")




if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
