


username = "Akua"
userbal = 140
code = 1234 #the momo code 
pin = 4040
useraccN = 987654
verification_code = "D0Ne"





def addOns():  
    print("Would you like to withdraw using your Debit or Mobile Money account?")
    ques1 = int(input("1)Debit or 2)Momo: "))
    print("-----------------------------------------------------------")
    if ques1 == 2:
        print("Which service?" "\n" "1)MTN," "\n" , "2)Vodafone", "\n" , "3)AirtelTigo")
        userService = int(input("Type in your option : "))
        print("-----------------------------------------------------------")
        userIn_1 = int(input("Kindly input the code sent to your number "))
        userIn_1 = code
        print("-----------------------------------------------------------")
        print("How much would you want to withdraw?")
        userIn_2 = int(input("Enter amount: "  ))
        userIn_2a = str(input("Would you want variety of denominations? Y/N: "))
        balance = userbal - userIn_2
        if userIn_2 < userbal:
            print("-----------------------------------------------------------")
            print("Your remaining balance is: " , balance, "cedis")
            print("Thank you for banking with TS Bank " + username)
        else:
            print("Your balance is insufficient")
            

    elif ques1 == 1:
        userIn_3 = int(input("Kindly input your account pin: "))
        userIn_3 = pin
        print("-----------------------------------------------------------")
        print("How much would you like to withdraw?")
        userIn_4 = int(input("Enter amount: "))
        balance2 = userbal - userIn_4
        if userIn_4 < userbal:
            print("-----------------------------------------------------------")
            print("Your remaining balance is: " , balance2, "cedis")
            print("Thank you for banking with TS Bank " + username)
        else:
            print("Your balance is insufficient")
    
    else:
        print("Invalid")
addOns()


def updatePin():
        
    #user inputs pin
    print("A confirmation code has been sent to your phone")
    
    verificationCode = random.randint(1000,9999)

    print(verificationCode)
    
    #after the user has been verified, he/she proceeds with the change
    while True:
        
        codeVerify = int(input("Enter verification code here: "))
        
        if codeVerify == verificationCode:
            while True:
                newPin = int(getpass.getpass(" Enter new 4 digit pin: "))
                newPinConfirm = int(getpass.getpass(" Please repeat new 4 digit pin: "))
                
                if newPin == newPinConfirm:
                    print("Congratulations! Your pin has been changed!")
                    session['pin'] = newPin
                    pause = input('Press Enter to return to the main menu. ')
                    break

                elif newPin != newPinConfirm:
                    print('Sorry Pin codes do not match. Please Try again.')
                    continue
            break

        elif codeVerify != verificationCode:
            print("Wrong Verification code entered. Please enter code again")
            continue
    
    return
    
    
    
    
    # MODIFICATIONS TO RUN WITH THE REST OF THE CODE
    
      def momo():
        print ('########################################### MOBILE MONEY WITHDRAWAL #####################################################\n \n')
        print("Select Your Network Provider\n1) MTN\n2) Vodafone\n3) AirtelTigo \n \n")
        while True:
            try:
                userService = str(input("Select option number 1, 2, 3: "))
                print (' \n_______________________________________________________________________________\n  \n')
                if userService == "1":
                    print ('MTN MOBILE MONEY WITHDRAWAL')
                    break

                elif userService == "2":
                    print ('VODAFONE CASH WITHDRAWAL')
                    break

                elif userService == "3":
                    print ('AIRTELTIGO MONEY WITHDRAWAL')
                    break
                
                else:
                    print (' \n_______________________________________________________________________________\n  \n')
                    print("Sorry Incorrect Input. Try Again")
                    print (' \n_______________________________________________________________________________\n  \n')
                    continue
            
            except ValueError:
                print (' \n_______________________________________________________________________________\n  \n')
                print("Sorry Incorrect Input. Try Again")
                print (' \n_______________________________________________________________________________\n  \n')
                continue
        
        
        while True:
            print (' \n_______________________________________________________________________________\n  \n')
            print("A Transaction Code has been sent to your phone number")
            transactionCode = random.randint(100000,999999)
            print ("Transaction Code: "+ str(transactionCode))
            
            try:
                print (' \n_______________________________________________________________________________\n  \n')
                userTransactionCode = int(input("Kindly input the code sent to your number: "))
                if userTransactionCode == transactionCode:
                    while True:
                        print (' \n_______________________________________________________________________________\n  \n')
                        print("How much would you want to withdraw?")
                        try:
                            momoAmount = int(input("Enter amount: "))

                            if momoAmount <= 2000:
                                print (' \n_______________________________________________________________________________\n  \n')
                                print ("Confirm withdrawal of GHS "+ str(momoAmount))
                                while True:
                                    momoConfirm = str(input("Type 'Y' to confirm / 'N' to cancel:  ")).upper()

                                    if momoConfirm not in ('Y', 'N'):
                                        print (' \n_______________________________________________________________________________\n  \n')
                                        print ("Invalid input. Try again.")
                                        print (' \n_______________________________________________________________________________\n  \n')
                                        continue
                                    
                                    elif momoConfirm == 'Y':
                                        while True:
                                            momoPin = random.randint(1000,9999)
                                            print (' \n_______________________________________________________________________________\n  \n')
                                            print (" Enter momo pin to confirm")
                                            print ("MOMO PIN = "+ str(momoPin))
                                            print (' \n_______________________________________________________________________________\n  \n')
                                            momoPinValid = int(getpass.getpass(" Enter Momo Pin: "))
                                            
                                            if momoPinValid == momoPin:
                                                print (' \n_______________________________________________________________________________\n  \n')
                                                print("Successful Withdrawal!")
                                                print (' \n_______________________________________________________________________________\n  \n')
                                                pause = input('Press Enter to return to the main menu. ')
                                                break

                                            elif momoPinValid != momoPin:
                                                print (' \n_______________________________________________________________________________\n  \n')
                                                print('Sorry Pin codes do not match. Please Try again.')
                                                print (' \n_______________________________________________________________________________\n  \n')
                                                continue
                                    
                                    elif momoConfirm == 'N':
                                        break

                                    else:
                                        print (' \n_______________________________________________________________________________\n  \n')
                                        print ("Invalid input. Try again.")
                                        print (' \n_______________________________________________________________________________\n  \n')
                                        continue
                                
                                break

                            elif momoAmount > 2000:
                                while True:
                                    print (' \n_______________________________________________________________________________\n  \n')
                                    momoContinue = str(input("Unsuccessful. You cannot withdraw more than GHS 2000\n \nWould you like to try again or return to the main Menu?\n \n Type 'Y' to try agin or Type 'N' to return to the main Menu:  ")).upper()
                                    print (' \n_______________________________________________________________________________\n  \n')

                                    # IF THE USER INPUT IS INCORRECT ASK FOR CORRECT INPUT
                                    if momoContinue not in ('Y', 'N'):
                                        print (' \n_______________________________________________________________________________\n  \n')
                                        print ('Invalid Input, try again.')
                                        print (' \n_______________________________________________________________________________\n  \n')
                                        continue
                                    
                                    # IF USER SAYS YES RESTART FUNCTION AND TAKE CORRECT AMOUNT INPUT
                                    elif momoContinue == 'Y':
                                        break

                                    # IF USER SAYS NO RETURN TO THE MAIN MENU
                                    elif momoContinue == 'N':
                                        return atmMenu()
                                
                                continue

                        except ValueError:
                            print (' \n_______________________________________________________________________________\n  \n')
                            print ('Invalid input. Please enter a number')
                            print (' \n_______________________________________________________________________________\n  \n')
                            continue

                    break 
                else:
                    print (' \n_______________________________________________________________________________\n  \n')
                    print("Sorry Incorrect Code. Try Again")
                    print (' \n_______________________________________________________________________________\n  \n')
                    continue

            except ValueError:
                print (' \n_______________________________________________________________________________\n  \n')
                print("Sorry Incorrect Code. Enter the 6 digit code")
                print (' \n_______________________________________________________________________________\n  \n')
                continue
        
