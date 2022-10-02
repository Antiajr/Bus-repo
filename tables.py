import mysql.connector
cur = mysql.connector.connect(user='root',password='',
                              host='localhost',
                              database='bus_reseveration')
myconn = cur.cursor()
# print(myconn)
def user_info():
    try:
        myconn.execute("""CREATE TABLE user_info(
                            User_ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                            First_Name VARCHAR(20) NOT NULL,
                            Last_Name VARCHAR(20) NOT NULL,
                            User_Name VARCHAR(20) UNIQUE NOT NULL,
                            Email VARCHAR(50) UNIQUE NOT NULL,
                            Mobile_Number VARCHAR(11) UNIQUE NOT NULL,
                            Gender VARCHAR(6) NOT NULL,
                            Pass_word VARCHAR(4) NOT NULL,
                            Sign_Up DATETIME NOT NULL
                            )
                            """)
        cur.commit()
    except:
        print('User_Info Table Already Exist')

user_info()

def booking():
    try:
        myconn.execute("""CREATE TABLE bookings(
                            ID INT NOT NULL AUTO_INCREMENT,
                            User_ID INT NOT NULL,
                            Booking_ID INT NOT NULL,
                            NUmber_of_seats INT NOT NULL,
                            Seat_Number INT NOT NULL,
                            Total_Amount float NOT NULL,
                            date_of_booking datetime NOT NULL,
                            booking_status varchar(20) NOT NULL,
                            PRIMARY KEY(ID, Booking_id),
                            UNIQUE (User_ID, Booking_ID, Seat_Number)
                            )""")
        cur.commit()
    except:
        print('Booking Table Already Exist')
booking()