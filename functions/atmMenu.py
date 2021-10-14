
def atmMenu(): 
    print('Welcome to techSeals Bank')
    print('Please select an option below')
    print ('1. Withdrawal')
    print ('2. Check Balance')
    print ("3. Add-Ons")
    print ('4. Log Out/Quit')
    choice = str(input('Please enter your choice (1, 2, 3 or 4): '))

    if choice == '1':
        withdrawUpdate()
    
    elif choice == '2':
        crntBalance()

    elif choice == '3':
        addOns()
    
    elif choice == '4':
        exit()
    
    else: 
        print('Sorry your choice is invalid')
        atmMenu()




        
        
# MODIFICATIONS TO MAKE CODE RUN IN MAIN PROGRAM

def atmMenu():

    # DISPLAY WELCOME MESSAGE
    print (' \n_______________________________________________________________________________\n  \n')
    print (('Tech Seals Banking App\n \nPlease follow the instructions for a successful transaction').upper())
    print (' \n_______________________________________________________________________________\n  \n')
    print ("Welcome " + str(userName.upper()) + "\n \nWhat would you like to do today?\n \n")
    
    # CHECK USER TRANSACTION SELECTION
    while True:
        # REQUEST USER TRANSACTION SELECTION
        print ("Type the number associated with the transaction you want to perform and \nPress enter to select")
        print (' \n_______________________________________________________________________________\n  \n')   
            
        try:
            transaction = int(input("1) Check Balance  2) Make Withdrawal  3) Mobile Money  99) Quit / Log Out\n \n"))

            # CHECK IF USER WANTS TO CHECK BALANCE AND RUN
            if transaction == 1:
                # RUN THE BALANCE CHECK FUNCTION
                crntBalance()
                pause = input('\n \nPress Enter to return to the Main Menu ')
                continue
                
            # CHECK IF USER WANTS TO MAKE A WITHDRAWAL AND RUN
            elif transaction == 2:
                # RUN THE WITHDRAWAL FUNCTION AND SAVE ALL OUTPUTS TO THE VARIABLE
                withdrawn = withdrawUpdate()
                # RUN THE RECEIPT REQUEST FUNCTION
                rcptPrint(withdrawn)
                break
            
            # CHECK IF USER WANTS TO MAKE A MOBILE MONEY WITHDRAWAL
            #elif transaction == 3:
                # RUN THE MOBILE MONEY FUNCTION
                #withdrawn = withdrawUpdate()
                # break
            
            # CHECK IF USER WANTS QUIT OR LOG OFF
            elif transaction == 99:
                while True:
                    # REQUEST INPUT FROM USER
                    print (' \n_______________________________________________________________________________\n  \n')
                    quitConfirm = str(input('\n \nAre you sure you want to quit? (Y/N):  ')).upper()
                    print (' \n_______________________________________________________________________________\n  \n')

                    # IF USER SAYS YES END PROGRAM
                    if quitConfirm == 'Y':
                        print("""
                            -----------------------------------------
                            | Thank you for choosing Tech Seals Bank |
                            |         Visit us again!                |
                            -----------------------------------------
                        """)
                        exit()

                    # IF USER SAYS NO RELOAD THE MAIN MENU
                    elif quitConfirm == 'N':
                        break
                    
                    # IF USER RESPONSE IS INVALID ASK FOR A VALID INPUT
                    else:
                        print (' \n_______________________________________________________________________________\n  \n')
                        print ('Invalid input. Try again')
                        print (' \n_______________________________________________________________________________\n  \n')
                        continue

                continue

            else:
                print (' \n_______________________________________________________________________________\n  \n')
                print ('Invalid selection input. Try again')
                print (' \n_______________________________________________________________________________\n  \n')
                continue
        
        except ValueError:
            print (' \n_______________________________________________________________________________\n  \n')
            print ('Invalid selection input. Please input a whole number')
            print (' \n_______________________________________________________________________________\n  \n')
            continue


    # CHECK IF USER WOULD LIKE TO PERFORM ANOTHER TRANSACTION
    while True:
        # REQUEST INPUT FROM USER
        print (' \n_______________________________________________________________________________\n  \n')
        backtoMain = str(input('Would you like to perform another another transaction? Y/N :  ')).upper()
        print (' \n_______________________________________________________________________________\n  \n')

        # IF USER SAYS YES RELOAD THE MAIN MENU
        if  backtoMain == 'Y':
            return atmMenu()
        
        # IF USER SAYS NO END PROGRAM
        elif  backtoMain == 'N':
            print("""
                -----------------------------------------
                | Thank you for choosing Tech Seals Bank |
                |         Visit us again!                |
                -----------------------------------------
            """)
            exit()

        # IF USER RESPONSE IS INVALID ASK FOR A VALID INPUT
        else:
            print ('Invalid input. Try again')
            continue










