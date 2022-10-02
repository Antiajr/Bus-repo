import mysql.connector
from login import userdb
from datetime import datetime
cur = mysql.connector.connect(user='root',password='',
                              host='localhost',
                              database='bus_reseveration')
myconn = cur.cursor()

now = datetime.now()
date = now.strftime('%y-%m-%d')

user = userdb()
ID = {'user_id':user[0][0]}

print('UPDATE BOOKING\n_______________')
def update_booking():
    row_number = 0
    price_of_seats = 250
    booking = 0

    myconn.execute(f'''
        SELECT count(*) from bookings where user_id = {ID.get('user_id')} and booking_status = 'active' 
                    '''
                   )

    for count in myconn:
        for row in count:
            row_number = row
    booking_available = 2- row_number
    print(f' only {booking_available} booking left for you ')
    if row_number == 1:
        number_of_seat = int(input('Enter Seat For Booking: '))
        if number_of_seat > 1 or number_of_seat < 1:
            print('\nError: Can Only Book One Seat..')
            return update_booking()

        # myconn.execute(f'''
        #         SELECT * from bookings where User_ID = {ID.get('user_id')}''')

        # if myconn.fetchall():
        #     print('\nNotice: You Have Already Booked... You Can Only "Update" Your Booking\n')
        #     print('\nDo You Wish To Update Booking ?: ')
        #     try:
        #         update = int(input('>>> Press 1 to Update: '))
        #         if update == 1:
        #             import update
        #         elif str(update) == '':
        #             import home
        #         else:
        #             import home
        #     except:
        #         import home
        else:
            for seat in range(number_of_seat):
                myconn.execute(f'''
                        SELECT count(*)from bookings where booking_status = 'active' ''')

                # count the row of seat the user has booking
                for count in myconn:
                    for row in count:
                        row_number = row
                        if row_number == 10:
                            print('Notice: Booking Not Available Now')
                import home

                myconn.execute(f'''
                        SELECT Seat_Number from bookings order by Seat_Number desc
                        limit 1''')
                for seat1 in myconn:
                    for seat in seat1:
                        seat_id = seat
                myconn.execute(f'''
                            SELECT booking_id from bookings where user_id = {ID.get('user_id')}''')
                for booking in myconn:
                    for booking_id in booking:
                        booking = booking_id
                myconn.execute(f'''
                        INSERT into bookings(User_ID,Booking_ID,Number_of_seats,Total_Amount,Seat_Number,date_of_booking,booking_status)
                        VALUES({ID.get('user_id')},{ID.get('user_id')}{booking_id}, {number_of_seat}, {price_of_seats},{seat_id + 1},'{date}','active')
                        ''')
                cur.commit()

    elif row_number < 1:
        print('You Have No Booking')
    else:
        print('You Have Reach The Limit')

update_booking()