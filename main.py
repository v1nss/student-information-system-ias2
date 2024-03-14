import os 

os.environ['TCL_LIBRARY'] = 'C:/Users/vince/AppData/Local/Programs/Python/Python312/tcl/tcl8.6'
os.environ['TK_LIBRARY'] = 'C:/Users/vince/AppData/Local/Programs/Python/Python312/tcl/tk8.6'

import random
from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as ttkb
from ttkbootstrap import Style

window = ttkb.Window(themename="darkly")
# style = Style(themename="darkly")
window.title('Student Record Program')
window.geometry('800x600')
ttkb.Frame()
ttkb.Entry()

test_label = ttkb.Label(text = 'Student Record Program', font=("Helvetica", 20))
test_label.pack(pady=60)

left_frame = ttkb.Frame(window)
# left_frame.pack(side=LEFT, padx=80, pady=0)
left_frame.place(x=100, y=200)
# left_frame.configure()

# Create a frame to display content on the right
right_frame = ttkb.Frame(window)
right_frame.place(x=330, y=130)
right_frame.config(width=400, height=600)

def random_num():
    header = "TUPM-21-"
    randnum = str(random.randint(1000,9999))
    studentID = ("".join([header, randnum]))

    return studentID

# Function to display content based on the button clicked
def show_content(content):
    # Clear the previous content
    for widget in right_frame.winfo_children():
        widget.destroy()
    
    # Display new content based on the button clicked
    label = Label(right_frame, text=content, font=("Helvetica", 16))
    label.pack()

def show_addStudent(content):

    studentID = random_num()
    # Clear the previous content
    for widget in right_frame.winfo_children():
        widget.destroy()

    frame = ttkb.Frame(right_frame)
    frame.pack()
    frame.config(width=400, height=600)

  # Display new content based on the button clicked
    label_title = Label(frame, text=content, font=("Helvetica", 20))
    label_title.place(x=130, y=20)

    label_id = Label(frame, text='Student ID:', font=("Helvetica", 12))
    label_id.place(x=50, y=80)

    label_id = Label(frame, text=studentID, font=("Helvetica", 12))
    label_id.place(x=150, y=80)

    label_name = Label(frame, text='Name:', font=("Helvetica", 12))
    label_name.place(x=50, y=120)

    entry_name = Entry(frame, font=("Helvetica", 12))
    entry_name.place(x=150, y=120)

    label_birthdate = Label(frame, text='Birth Date:', font=("Helvetica", 12))
    label_birthdate.place(x=50, y=160)

    entry_birthdate = Entry(frame, font=("Helvetica", 12))
    entry_birthdate.place(x=150, y=160)

    label_age = Label(frame, text='Age:', font=("Helvetica", 12))
    label_age.place(x=50, y=200)

    entry_age = Entry(frame, font=("Helvetica", 12))
    entry_age.place(x=150, y=200)

    label_gender = Label(frame, text='Gender:', font=("Helvetica", 12))
    label_gender.place(x=50, y=240)

    entry_gender = Entry(frame, font=("Helvetica", 12))
    entry_gender.place(x=150, y=240)

    label_address = Label(frame, text='Address:', font=("Helvetica", 12))
    label_address.place(x=50, y=280)

    entry_address = Entry(frame, font=("Helvetica", 12))
    entry_address.place(x=150, y=280)

    label_course = Label(frame, text='Course:', font=("Helvetica", 12))
    label_course.place(x=50, y=320)

    entry_course = Entry(frame, font=("Helvetica", 12))
    entry_course.place(x=150, y=320)

    label_yearlvl = Label(frame, text='Year Level:', font=("Helvetica", 12))
    label_yearlvl.place(x=50, y=360)

    entry_yearlvl = Entry(frame, font=("Helvetica", 12))
    entry_yearlvl.place(x=150, y=360)

    # Create a button to submit the form
    submit_button = ttkb.Button(frame, text="Add Student", width=20, bootstyle=SUCCESS, command=lambda: submit_form(studentID, [ entry_name, entry_birthdate, entry_age, entry_gender, 
                                                                                                                entry_address, entry_course, entry_yearlvl]))
    submit_button.place(x=150, y=410)


def submit_form(studentID, entries):
      # Retrieve values from entry widgets
    values = [entry.get() for entry in entries]
    
    # Write values to a text file
    with open('student_records.txt', 'a') as file:
        file.write(studentID+",")
        file.write(','.join(values) + '\n')
    
    print("Data saved to student_records.txt")
    
def show_deleteStudent(content):
    for widget in right_frame.winfo_children():
        widget.destroy()

    frame = ttkb.Frame(right_frame)
    frame.pack()
    frame.config(width=400, height=600)

    del_label_title = Label(frame, text=content, font=("Helvetica", 20))
    del_label_title.place(x=120, y=20)

    del_label_searchID = Label(frame, text='Search ID:', font=("Helvetica", 12))
    del_label_searchID.place(x=50, y=80)

    del_entry_searchID = Entry(frame, font=("Helvetica", 12))
    del_entry_searchID.place(x=150, y=80)
    
    search_button = ttkb.Button(frame, text="Search", width=10, bootstyle=ttkb.PRIMARY, command=lambda: search_student(del_entry_searchID.get()))
    search_button.place(x=300, y=80)

def delete_student(student_id):
    # Read data from the text file
    with open('student_records.txt', 'r') as file:
        lines = file.readlines()

    # Filter out the student record to be deleted
    new_lines = [line for line in lines if not line.startswith(student_id + ',')]

    # Write the updated data back to the file
    with open('student_records.txt', 'w') as file:
        file.writelines(new_lines)

    print(f"Student with ID {student_id} deleted.")

def search_student(student_id):
    # Read data from the text file
    with open('student_records.txt', 'r') as file:
        lines = file.readlines()

    # Search for the student record based on the student ID
    found = False
    for line in lines:
        data = line.strip().split(',')
        if data[0] == student_id:
            found = True
            show_student_details(data)
            break
    
    if not found:
        print(f"Student with ID {student_id} not found.")

def show_student_details(student_data):
    # Display the student details in a separate frame or messagebox
    # messagebox.showinfo
    for widget in right_frame.winfo_children():
        widget.destroy()

    frame = ttkb.Frame(right_frame)
    frame.pack()
    frame.config(width=400, height=600)

    del_label_title = Label(frame, text="Delete Student", font=("Helvetica", 20))
    del_label_title.place(x=120, y=20)

    label_name = Label(frame, text='Name:', font=("Helvetica", 12))
    label_name.place(x=50, y=120)

    entry_name = Label(frame, text=student_data[1], font=("Helvetica", 12))
    entry_name.place(x=150, y=120)

    label_birthdate = Label(frame, text='Birth Date:', font=("Helvetica", 12))
    label_birthdate.place(x=50, y=160)

    entry_birthdate = Label(frame, text=student_data[2], font=("Helvetica", 12))
    entry_birthdate.place(x=150, y=160)

    label_age = Label(frame, text='Age:', font=("Helvetica", 12))
    label_age.place(x=50, y=200)

    entry_age = Label(frame, text=student_data[3], font=("Helvetica", 12))
    entry_age.place(x=150, y=200)

    label_gender = Label(frame, text='Gender:', font=("Helvetica", 12))
    label_gender.place(x=50, y=240)

    entry_gender = Label(frame, text=student_data[4], font=("Helvetica", 12))
    entry_gender.place(x=150, y=240)

    label_address = Label(frame, text='Address:', font=("Helvetica", 12))
    label_address.place(x=50, y=280)

    entry_address = Label(frame, text=student_data[5], font=("Helvetica", 12))
    entry_address.place(x=150, y=280)

    label_course = Label(frame, text='Course:', font=("Helvetica", 12))
    label_course.place(x=50, y=320)

    entry_course = Label(frame, text=student_data[6], font=("Helvetica", 12))
    entry_course.place(x=150, y=320)

    label_yearlvl = Label(frame, text='Year Level:', font=("Helvetica", 12))
    label_yearlvl.place(x=50, y=360)

    entry_yearlvl = Label(frame, text=student_data[7], font=("Helvetica", 12))
    entry_yearlvl.place(x=150, y=360)

    delete_button = ttkb.Button(frame, text="Delete", width=10, bootstyle=ttkb.DANGER, command=lambda: delete_student(student_data[0]))
    delete_button.place(x=300, y=400)
    
    # print("Student Details", f"Name: {student_data[1]}\nBirthdate: {student_data[2]}\nAge: {student_data[3]}\nGender: {student_data[4]}\nAddress: {student_data[5]}\nCourse: {student_data[6]}\nYear Level: {student_data[7]}")

def show_students(content):
    for widget in right_frame.winfo_children():
        widget.destroy()

    frame = ttkb.Frame(right_frame)
    frame.pack()
    frame.config(width=400, height=600)
    
    del_label_title = Label(frame, text=content, font=("Helvetica", 20))
    del_label_title.place(x=120, y=20)

    with open('student_records.txt', 'r') as file:
        lines = file.readlines()

    # Display the student information
    y_position = 50  # Starting y-position for the first label
    for line in lines:
        student_data = line.strip().split(',')
        label_student_id = Label(frame, text=f"Student ID: {student_data[0]}", font=("Helvetica", 12))
        label_student_id.place(x=50, y=y_position)
        y_position += 40  # Increment y-position for the next label

        label_name = Label(frame, text=f"Name: {student_data[1]}", font=("Helvetica", 12))
        label_name.place(x=50, y=y_position)
        y_position += 40

        label_birthdate = Label(frame, text=f"Birth Date: {student_data[2]}", font=("Helvetica", 12))
        label_birthdate.place(x=50, y=y_position)
        y_position += 40

        label_age = Label(frame, text=f"Age: {student_data[3]}", font=("Helvetica", 12))
        label_age.place(x=50, y=y_position)
        y_position += 40

        label_gender = Label(frame, text=f"Gender: {student_data[4]}", font=("Helvetica", 12))
        label_gender.place(x=50, y=y_position)
        y_position += 40

        label_address = Label(frame, text=f"Address: {student_data[5]}", font=("Helvetica", 12))
        label_address.place(x=50, y=y_position)
        y_position += 40

        label_course = Label(frame, text=f"Course: {student_data[6]}", font=("Helvetica", 12))
        label_course.place(x=50, y=y_position)
        y_position += 40

        label_yearlvl = Label(frame, text=f"Year Level: {student_data[7]}", font=("Helvetica", 12))
        label_yearlvl.place(x=50, y=y_position)
        y_position += 40

# Create buttons on the left side

button1 = ttkb.Button(left_frame, text="Add Student", width=20, bootstyle=SUCCESS, command=lambda: show_addStudent('Add Student'))
button1.pack(pady=15)

button2 = ttkb.Button(left_frame, text="Delete Student", width=20, bootstyle=SUCCESS, command=lambda: show_deleteStudent('Delete Student'))
button2.pack(pady=15)

button3 = ttkb.Button(left_frame, text="View Students", width=20, bootstyle=SUCCESS, command=lambda: show_students('View Students'))
button3.pack(pady=15)

button4 = ttkb.Button(left_frame, text="Update Students", width=20, bootstyle=SUCCESS, command=lambda: show_content('Update Students'))
button4.pack(pady=15)

button5 = ttkb.Button(left_frame, text="Search Students", width=20, bootstyle=SUCCESS, command=lambda: show_content('Search Students'))
button5.pack(pady=15)



window.mainloop()