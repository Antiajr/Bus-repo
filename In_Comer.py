def header():
    try:
        print('1 for Sign Up, 2 for Login')

        header1 = int(input("Enter Option: "))
        if header1 == 1:
            import main
            import home


        elif header1 == 2:
            import home

        else:
            print("Input Out Of Range....")
            return header()
    except:
        print('\nError: Only Numbers Input..')

header()