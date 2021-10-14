


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