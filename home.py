import login
def Home():
    try:
        print('\n\tWELCOME TO OBG MOTORS\n\t---------------------'.expandtabs(5))
        print('''
                >>>> Press 1 For BOOKING
                >>>> Press 2 TO VIEW BOOKING
                >>>> Press 3 To DELETE BOOKING
                >>>> Press 4 To UPDATE BOOKING
                >>>> Press 5 To LOGOUT
                ''')
        user_input = int(input('ENTER INPUT: '))
        if user_input == 1:
            import bookings
        elif user_input == 2:
            import view
        elif user_input == 3:
            import delete
        elif user_input == 4:
            import update
        elif user_input == 5:
            print('Logged Out!!!')
        else:
            print('Out of Range')
            return Home()
    except:
        print('INVALID INPUT')
        return Home()
Home()
