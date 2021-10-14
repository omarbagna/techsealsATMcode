


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
