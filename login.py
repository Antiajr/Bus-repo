import mysql.connector

cur = mysql.connector.connect(user='root',password='',
                              host='localhost',
                              database='bus_reseveration')
myconn = cur.cursor()

print("\tLOGIN\n\t-----".expandtabs(10))
try:
    user = input('Enter User Name: ')
    password = input('Enter Password: ')

    myconn.execute(f"SELECT * FROM user_info WHERE User_Name = '{user}' AND Pass_Word = '{password}'")
    if myconn.fetchall():
        print('\nLogin Succesfull')
    else:
        print('\nError: Invalid Details')
except:
    print('Error: Invalid Input')

def userdb():
    myconn.execute(f"SELECT * FROM user_info WHERE User_Name = '{user}' AND Pass_Word = '{password}'")
    return myconn.fetchall()
# userdb()