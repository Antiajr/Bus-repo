import mysql.connector
import re
import string
from datetime import datetime
cur = mysql.connector.connect(user='root',password='',
                              host='localhost',
                              database='bus_reseveration')
myconn = cur.cursor()

now = datetime.now()
date = now.strftime('%y-%m-%d')

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def Sign_Up():
    print('\tSIGN UP\n\t-------'.expandtabs(10))
    firstname = input('Enter First Name: ').strip()
    if firstname == '':
        print('\nError: Invalid Input\n')
        return Sign_Up()
    elif len(firstname) < 3 or len(firstname) > 20:
        print('\nError: First Name must be greater than 3 and Less than 20\n')
        return Sign_Up()
    for letters in firstname:
        if letters.isnumeric():
            print('\nError: First Name Cannot Contain NUmbers\n')
            return Sign_Up()
        elif letters not in string.ascii_letters:
            print('\nError: First Name Must Contain Alphabets\n')
            return Sign_Up()

    lastname = input('Enter Last Name: ').strip()
    if lastname == '':
        print('\nError: Invalid Input\n')
        return Sign_Up()
    elif len(lastname) < 3 or len(lastname) > 20:
        print('\nError: Last Name must be greater than 3 and Less than 20\n')
        return Sign_Up()
    for letters in lastname:
        if letters.isnumeric():
            print('\nError: Last Name Cannot Contain NUmbers\n')
            return Sign_Up()
        elif letters not in string.ascii_letters:
            print('\nError: Last Name Must Contain Alphabets\n')
            return Sign_Up()

    user_name = input('Create User Name: ').strip()
    if user_name == '':
        print('\nError: Invalid Input\n')
        return Sign_Up()
    elif len(user_name) < 3 or len(user_name) > 20:
        print('\nError: User Name must be greater than 3 and Less than 20\n')
        return Sign_Up()

    email = input('Enter Email: ').strip()
    if (re.fullmatch(regex, email)):
        pass
    else:
        print('\nInvalid Email')
        return Sign_Up()

    try:
        number = int(input('Enter Phone NUmber: '))
        if number == '':
            print('\nError: Invalid Number')
            return Sign_Up()
        elif len(str(number)) < 10 or len(str (number)) > 10:
            print('\nError: Numbers Must be 11')
            return Sign_Up()
    except:
        print('\nError: Invalid Input')
        return Sign_Up()

    print("Gender \n M for male, F for female")
    gender = input('Enter Option: ').strip()
    gender = gender.upper()
    if gender == 'M':
        gender = 'Male'
    elif gender == 'F':
        gender = 'Female'
    else:
        print('Invalid Input')

    password = input('Enter Password: ')
    if password == '':
        print('\nError: Invalid Input\n')
        return Sign_Up()
    elif len(password) < 4 or len(password) > 4:
        print('\nError: User Password must be greater than 4 and Less than 4\n')
        return Sign_Up()


    # values = firstname, lastname, user_name, email, number, gender, password
    myconn.execute(f"SELECT * FROM user_info WHERE User_Name = '{user_name}' ")
    if myconn.fetchall():
        print('\nError: User_Name already Exist\n')
        return Sign_Up()

    myconn.execute(f"SELECT * FROM user_info WHERE Email = '{email}' ")
    if myconn.fetchall():
        print('\nError: Email Already Exist\n')
        return Sign_Up()

    myconn.execute(f"SELECT * FROM user_info WHERE Mobile_Number = '{number}' ")
    if myconn.fetchall():
        print('\nError: Phone Number Already Exist\n')
        return Sign_Up()

    myconn.execute(f'''
    INSERT INTO user_info(First_Name, Last_Name, User_Name, Email, Mobile_Number, Gender, Pass_word, Sign_Up) values
    ('{firstname}', '{lastname}','{user_name}', '{email}', '{number}', '{gender}', '{password}','{date}') ''')

    cur.commit()
    print('\n Account Creared Succesfully')
Sign_Up()

