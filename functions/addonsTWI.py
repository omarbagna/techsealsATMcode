
username = "Akua"
userbal = 140
code = 1234 #the momo code 
pin = 4040
useraccN = 987654
verification_code = "D0Ne"


denominations = [10, 20, 50]
dictionary = [username, pin, userbal]
   

def Ulang():
    userLang = int(input("What language do you want? 1. English 2. Asante Twi : "))
    if userLang == 2:
         print("Wob3yi sika 3di wo Momo number anaa Debit card?")
         ques1 = int(input("1)Debit or 2)Momo: "))
         print("-----------------------------------------------------------") 
         if ques1 == 2:
               print("Wo Momo network y3 den?" "\n" "1)MTN," "\n" , "2)Vodafone", "\n" , "3)AirtelTigo")
               userService = int(input("Yi wo de3 : "))
               print("-----------------------------------------------------------")
               userIn_1 = int(input("B) code a w) wo phone so "))
               userIn_1 = code
               print("-----------------------------------------------------------")
               userIn_2 = int(input("Wob3 yi sen?: "  ))
               balance = userbal - userIn_2
               if userIn_2 < userbal:
                   print("-----------------------------------------------------------")
                   print("Aka wo : " , balance, "cedis")
                   print("Y3daase " + username)
               else:
                   print("Wo sika no, 3nso")
        
         elif ques1 == 1:
                userIn_3 = int(input("B) wo Bank pin "))
                
                def update_pin():
                #user inputs pin
                  if userIn_3 != pin:
                #user is asked to input a new pin
                    print("Wo pin ny3 papa")  
                    userAsk = str(input("Wop3 s3 3y3 fofo) Y/N: "))
                  if userAsk == "Y":
                
            #after the user has been verfied, he/she proceeds with the change
                    userAuth = str(input("B) confirmation code: "))
                  if userAuth == verification_code:
                    userAuth2 = int(input(" B) nnumre 3nan: "))
                    userAuth2 == pin
                    dictionary.append(userAuth2)
                    print("Mo! Wo Debit card pin asesa!")
                  else:
                    print("Akwaaba ", username, "!")
                update_pin()
                print("-----------------------------------------------------------")
                userIn_4 = int(input("Wob3 yi sen?: "))
                balance2 = userbal - userIn_4
                if userIn_4 < userbal:
                     print("-----------------------------------------------------------")
                     print("Aka wo :  " , balance2, "cedis")
                     print("Y3daase  " + username)
                else:
                     print("Wo sika no, 3nso")
    
    elif userLang == 1:
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

        
            userIn_3  = int(input("To continue this service, Enter your pin: "))
            if userIn_3 != pin:
              #user is asked to input a new pin
                 print("The pin you have entered is incorrect")  
                 userAsk = str(input("Would you like to change your pin? Y/N: "))
                 if userAsk == "Y":
                     print("A confirmation code has been sent to your phone")
                      #after the user has been verfied, he/she proceeds with the change
                     userAuth = str(input("Proceed to enter verification code here: "))
                     if userAuth == verification_code:
                             userAuth2 = int(input(" Enter new 4 digit pin: "))
                             userAuth2 == pin
                             dictionary.append(userAuth2)
                             print("Congratulations! Your Debit card pin has been changed!")
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
                   print("Welcome ", username, "!")
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

Ulang()

    
        














    

