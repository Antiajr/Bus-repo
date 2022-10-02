import time

import mysql.connector
from login import userdb

cur = mysql.connector.connect(user='root',password='',
                              host='localhost',
                              database='bus_reseveration')
myconn = cur.cursor()

print('VIEW BOOKING\n____________')

user = userdb()
ID = {'user_id':user[0][0]}

def view_bookings():
    myconn.execute(f'''
    SELECT * from bookings where user_id = {ID.get('user_id')} and booking_status = 'active' ''')

    print('_____' * 18)
    print(f'| ID | UID | BID  | NOS | TOTAL_PRICE | SEAT_NUM | BOOKING_DATE | STATUS')
    for bookings in myconn:
        id, user_id, booking_id, number_of_seat, price, seat_num, booking_date, booking_status = bookings
        print('_____' * 18)
        print(f'| {id} | {user_id} | {booking_id} | {number_of_seat} | {seat_num} | {price} | {booking_date} | {booking_status} | ')
    print('_____' * 18)
    time.sleep(1)
    from home import Home

view_bookings()