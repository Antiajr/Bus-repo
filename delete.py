import mysql.connector
from login import userdb
import time

cur = mysql.connector.connect(user='root',password='',
                              host='localhost',
                              database='bus_reseveration')
myconn = cur.cursor()

print('DELETE BOOKING\n_______________')

user = userdb()
ID = {'user_id':user[0][0]}

def delete_booking():
    myconn.execute(f'''
    SELECT * from bookings where user_id = {ID.get('user_id')} and booking_status = 'active' ''')

    print('______' * 18)
    print(f'| ID | UID | NOS | TOTAL_PRICE | SEAT_NUM | BOOKING_DATE    | STATUS |')
    for booking in myconn:
        id, user_id, booking_id, number_of_seat, price, seat_num, booking_date, booking_status = booking
        print('____' * 18)
        print(f'| {id} | {user_id} | {number_of_seat} | | {price} | {seat_num} | | {booking_date} | {booking_status} |')
    print('_____' * 18)

    print('\n Delete Booking By ID NUMBER\n___________________________\n')

    delete = int(input('ENTER ID NUMBER: '))

    # booking as to be active to be deleted
    myconn.execute(f'''
        SELECT * from bookings where user_id = {ID.get('user_id')} and ID = {delete} and booking_status = 'active' ''')

    if myconn.fetchall():
        myconn.execute(f'''
            Update bookings set booking_status = 'cancel' where user_id = {ID.get('user_id')} and ID = {delete} and booking_status = 'active' ''')
        cur.commit()
        time.sleep(1)
        from home import Home
    else:
        print('\nError: ID does not belong to you\n')
        return delete_booking()
delete_booking()