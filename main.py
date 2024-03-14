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
window.geometry('900x600')
ttkb.Frame()
ttkb.Entry()

test_label = ttkb.Label(text = 'Student Information System', font=("Helvetica", 20))
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

def enc(plaintext, keyword):
    encrypted_text = ''
    keyword_index = 0

    for char in plaintext:
        if char.isalpha() or char.isdigit():
            # Determine the shift amount based on the keyword character
            shift = ord(keyword[keyword_index % len(keyword)].lower()) - ord('a')
            keyword_index += 1

            # Apply the shift to the current character
            if char.islower():
                shifted = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            elif char.isupper():
                shifted = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            elif char.isdigit():
                shifted = chr(((ord(char) - ord('0') + shift) % 10) + ord('0'))
        else:
            shifted = char

        encrypted_text += shifted

    return encrypted_text

def dec(ciphertext, keyword):
    decrypted_text = ''
    keyword_index = 0

    for char in ciphertext:
        if char.isalpha() or char.isdigit():
            # Determine the shift amount based on the keyword character
            shift = ord(keyword[keyword_index % len(keyword)].lower()) - ord('a')
            keyword_index += 1

            # Apply the reverse shift to decrypt the current character
            if char.islower():
                shifted = chr(((ord(char) - ord('a') - shift + 26) % 26) + ord('a'))
            elif char.isupper():
                shifted = chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
            elif char.isdigit():
                shifted = chr(((ord(char) - ord('0') - shift + 10) % 10) + ord('0'))
        else:
            shifted = char

        decrypted_text += shifted

    return decrypted_text

def submit_form(studentID, entries):
    # Retrieve values from entry widgets
    values = [entry.get() for entry in entries]
    
    # Encrypt the values using the Vigenère cipher with a keyword
    keyword = 'SECRET'  # You can use any keyword here
    encrypted_values = [enc(value, keyword) for value in values]
    
    # Write encrypted values to a text file
    with open('student_records.txt', 'a') as file:
        file.write(studentID + ",")
        file.write(','.join(encrypted_values) + '\n')
    
    print("Data saved to student_records.txt")
# def encrypt_data(data, shift):
#     encrypted = ''
#     for char in data:
#         if char.isalpha():
#             shifted = ord(char) + shift
#             if char.islower():
#                 if shifted > ord('z'):
#                     shifted -= 26
#             elif char.isupper():
#                 if shifted > ord('Z'):
#                     shifted -= 26
#             encrypted += chr(shifted)
#         else:
#             encrypted += char
#     return encrypted

# def submit_form(studentID, entries):
#       # Retrieve values from entry widgets
#     values = [entry.get() for entry in entries]
    
#     # Write values to a text file
#     with open('student_records.txt', 'a') as file:
#         file.write(studentID+",")
#         file.write(','.join(values) + '\n')
    
#     print("Data saved to student_records.txt")
    
def show_deleteStudent(content):
    for widget in right_frame.winfo_children():
        widget.destroy()

    frame = ttkb.Frame(right_frame)
    frame.pack()
    frame.config(width=500, height=600)

    del_label_title = Label(frame, text=content, font=("Helvetica", 20))
    del_label_title.place(x=120, y=20)

    del_label_searchID = Label(frame, text='Search ID:', font=("Helvetica", 12))
    del_label_searchID.place(x=50, y=80)

    del_entry_searchID = Entry(frame, font=("Helvetica", 12))
    del_entry_searchID.place(x=150, y=80)
    
    search_button = ttkb.Button(frame, text="Search", width=10, bootstyle=ttkb.PRIMARY, command=lambda: search_student(del_entry_searchID.get()))
    search_button.place(x=350, y=77)

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
            # Decrypt the relevant data
            decrypted_data = [dec(value, 'SECRET') for value in data[1:]]
            decrypted_data.insert(0, data[0])  # Insert student ID without decryption
            show_student_details(decrypted_data)
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
    
    label_title = Label(right_frame, text=content, font=("Helvetica", 20))
    label_title.pack()

    scrollbar = Scrollbar(right_frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    text_area = Text(right_frame, wrap=NONE, yscrollcommand=scrollbar.set)
    text_area.pack(expand=True, fill=BOTH)

    scrollbar.config(command=text_area.yview)

    with open('student_records.txt', 'r') as file:
        lines = file.readlines()

    for line in lines:
        student_data_encrypted = line.strip().split(',')
        text_area.insert(END, f"Student ID: {student_data_encrypted[0]}\n")
        student_data_decrypted = [dec(data, "SECRET") for data in student_data_encrypted]
        
        text_area.insert(END, f"Name: {student_data_decrypted[1]}\n")
        text_area.insert(END, f"Birth Date: {student_data_decrypted[2]}\n")
        text_area.insert(END, f"Age: {student_data_decrypted[3]}\n")
        text_area.insert(END, f"Gender: {student_data_decrypted[4]}\n")
        text_area.insert(END, f"Address: {student_data_decrypted[5]}\n")
        text_area.insert(END, f"Course: {student_data_decrypted[6]}\n")
        text_area.insert(END, f"Year Level: {student_data_decrypted[7]}\n\n")

    text_area.config(state=DISABLED)

def show_updateStudent(content):
    for widget in right_frame.winfo_children():
        widget.destroy()

    frame = ttkb.Frame(right_frame)
    frame.pack()
    frame.config(width=500, height=600)
    
    label_title = Label(frame, text=content, font=("Helvetica", 20))
    label_title.place(x=120, y=20)

    search_label = Label(frame, text='Enter Student ID:', font=("Helvetica", 12))
    search_label.place(x=50, y=80)

    search_entry = Entry(frame, font=("Helvetica", 12))
    search_entry.place(x=200, y=80)

    search_button = Button(frame, text="Search", width=10, command=lambda: search_student_for_update(search_entry.get()))
    search_button.place(x=400, y=80)

def search_student_for_update(student_id):
    with open('student_records.txt', 'r') as file:
        lines = file.readlines()

    found = False
    for line in lines:
        data = line.strip().split(',')
        if data[0] == student_id:
            found = True
            decrypted_data = [dec(value, 'SECRET') for value in data[1:]]
            decrypted_data.insert(0, data[0])  # Insert student ID without decryption
            show_update_form(decrypted_data)
            break
    
    if not found:
        print(f"Student with ID {student_id} not found.")

def show_update_form(student_data):
    for widget in right_frame.winfo_children():
        widget.destroy()

    label_title = Label(right_frame, text="Update Student Information", font=("Helvetica", 20))
    label_title.place(x=70, y=20)

    label_id = Label(right_frame, text=f'Student ID: {student_data[0]}', font=("Helvetica", 12))
    label_id.place(x=50, y=80)

    label_name = Label(right_frame, text='Name:', font=("Helvetica", 12))
    label_name.place(x=50, y=120)

    entry_name = Entry(right_frame, font=("Helvetica", 12))
    entry_name.insert(0, student_data[1])  # Populate with existing name
    entry_name.place(x=150, y=120)

    label_birthdate = Label(right_frame, text='Birth Date:', font=("Helvetica", 12))
    label_birthdate.place(x=50, y=160)

    entry_birthdate = Entry(right_frame, font=("Helvetica", 12))
    entry_birthdate.insert(0, student_data[2])  # Populate with existing birthdate
    entry_birthdate.place(x=150, y=160)

    label_age = Label(right_frame, text='Age:', font=("Helvetica", 12))
    label_age.place(x=50, y=200)

    entry_age = Entry(right_frame, font=("Helvetica", 12))
    entry_age.insert(0, student_data[3])  # Populate with existing age
    entry_age.place(x=150, y=200)

    label_gender = Label(right_frame, text='Gender:', font=("Helvetica", 12))
    label_gender.place(x=50, y=240)

    entry_gender = Entry(right_frame, font=("Helvetica", 12))
    entry_gender.insert(0, student_data[4])  # Populate with existing gender
    entry_gender.place(x=150, y=240)

    label_address = Label(right_frame, text='Address:', font=("Helvetica", 12))
    label_address.place(x=50, y=280)

    entry_address = Entry(right_frame, font=("Helvetica", 12))
    entry_address.insert(0, student_data[5])  # Populate with existing address
    entry_address.place(x=150, y=280)

    label_course = Label(right_frame, text='Course:', font=("Helvetica", 12))
    label_course.place(x=50, y=320)

    entry_course = Entry(right_frame, font=("Helvetica", 12))
    entry_course.insert(0, student_data[6])  # Populate with existing course
    entry_course.place(x=150, y=320)

    label_yearlvl = Label(right_frame, text='Year Level:', font=("Helvetica", 12))
    label_yearlvl.place(x=50, y=360)

    entry_yearlvl = Entry(right_frame, font=("Helvetica", 12))
    entry_yearlvl.insert(0, student_data[7])  # Populate with existing year level
    entry_yearlvl.place(x=150, y=360)

    update_button = Button(right_frame, text="Update", width=10, command=lambda: update_student_info(student_data[0], entry_name.get(), entry_birthdate.get(), entry_age.get(), entry_gender.get(), entry_address.get(), entry_course.get(), entry_yearlvl.get()))
    update_button.place(x=180, y=400)

# def update_student_info(student_id, name, birthdate, age, gender, address, course, yearlvl):
#     with open('student_records.txt', 'r') as file:
#         lines = file.readlines()

#     updated_lines = []
#     for line in lines:
#         data = line.strip().split(',')

#         if data[0] == student_id:
#             data[1] = name
#             data[2] = birthdate
#             data[3] = age
#             data[4] = gender
#             data[5] = address
#             data[6] = course
#             data[7] = yearlvl
#             updated_lines.append(','.join(data) + '\n')
#         else:
#             updated_lines.append(line)

#     with open('student_records.txt', 'w') as file:
#         file.writelines(updated_lines)

#     print(f"Student with ID {student_id} updated.")
    
def update_student_info(student_id, name, birthdate, age, gender, address, course, yearlvl):
    with open('student_records.txt', 'r') as file:
        lines = file.readlines()

    keyword = "SECRET"
    updated_lines = []
    for line in lines:
        data = line.strip().split(',')
        
        if data[0] == student_id:
            data[1] = enc(name, keyword)
            data[2] = enc(birthdate, keyword)
            data[3] = enc(age, keyword)
            data[4] = enc(gender, keyword)
            data[5] = enc(address, keyword)
            data[6] = enc(course, keyword)
            data[7] = enc(yearlvl, keyword)
            updated_lines.append(','.join(data) + '\n')
        else:
            updated_lines.append(line)

    with open('student_records.txt', 'w') as file:
        file.writelines(updated_lines)

    print(f"Student with ID {student_id} updated.")

# Create buttons on the left side

button1 = ttkb.Button(left_frame, text="Add Student", width=20, bootstyle=SUCCESS, command=lambda: show_addStudent('Add Student'))
button1.pack(pady=15)

button2 = ttkb.Button(left_frame, text="Delete Student", width=20, bootstyle=SUCCESS, command=lambda: show_deleteStudent('Delete Student'))
button2.pack(pady=15)

button3 = ttkb.Button(left_frame, text="View Students", width=20, bootstyle=SUCCESS, command=lambda: show_students('View Students'))
button3.pack(pady=15)

button4 = ttkb.Button(left_frame, text="Update Students", width=20, bootstyle=SUCCESS, command=lambda: show_updateStudent('Update Students'))
button4.pack(pady=15)

# button5 = ttkb.Button(left_frame, text="Search Students", width=20, bootstyle=SUCCESS, command=lambda: show_content('Search Students'))
# button5.pack(pady=15)

window.mainloop()