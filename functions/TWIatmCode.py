import getpass
import random


#Database of user accounts
userArray=[{'username':'aba', 'pin':2121, 'balance':{'GHS':100000, 'USD':80000} },
{'username':'akosua', 'pin':4000, 'balance':{'GHS':280, 'USD':450} },
{'username':'eben', 'pin':5461, 'balance':{'GHS':800, 'USD':300} },
{'username':'bet', 'pin':3197, 'balance':{'GHS':995000, 'USD':980000} },
{'username':'david', 'pin':3216, 'balance':{'GHS':789, 'USD':250} },
{'username':'dna', 'pin':1234, 'balance':{'GHS':25000, 'USD':15000} },
{'username':'dave', 'pin':1034, 'balance':{'GHS':250, 'USD':8000} },
{'username':'esinam', 'pin':1110, 'balance':{'GHS':5000, 'USD':20000} },
{'username':'emmanuel', 'pin':2145, 'balance':{'GHS':8943, 'USD':2153} },
{'username':'van', 'pin':2111, 'balance':{'GHS':15000, 'USD':80000} },
{'username':'bagna', 'pin':7438, 'balance':{'GHS':555000, 'USD':300000} } ]


# LANDING MESSAGE
print ('########################################### TECH SEALS SIKAKORABIA #####################################\n \n')
print ('Me pa wo kyew bo woahyensode\n \n')


# Main Interaction Menu after Successful LogIn       
def atmMenu():

    # DISPLAY WELCOME MESSAGE
    print (' \n_______________________________________________________________________________\n  \n')
    print (('TECH SEALS SIKAKORABIA\n \nDi saa nhyeshe3 yi so na watumi ayi sika no').upper())
    print (' \n_______________________________________________________________________________\n  \n')
    print ("Akwaaba " + str(userName.upper()) + "\n \nD3n na wo p3s3 wo y3 3nn3?\n \n")
    
    # CHECK USER TRANSACTION SELECTION
    while True:
        # REQUEST USER TRANSACTION SELECTION
        print ("Mia n)ma a wop3 s3 wode y3 adwuma no na mia (ENTER): ")
        print (' \n_______________________________________________________________________________\n  \n')   
            
        try:
            transaction = int(input("1) Sika a aka  2) Yi sika  3) Mobile Money  99) Gyae / Log Out\n \n"))

            # CHECK IF USER WANTS TO CHECK BALANCE AND RUN
            if transaction == 1:
                # RUN THE BALANCE CHECK FUNCTION
                crntBalance()
                pause = input('\n Mia (ENTER) na ko (MAIN MENU)')
                continue
                
            # CHECK IF USER WANTS TO MAKE A WITHDRAWAL AND RUN
            elif transaction == 2:
                # RUN THE WITHDRAWAL FUNCTION AND SAVE ALL OUTPUTS TO THE VARIABLE
                withdrawn = withdrawUpdate()
                # RUN THE RECEIPT REQUEST FUNCTION
                rcptPrint(withdrawn)
                break
            
            # CHECK IF USER WANTS TO MAKE A MOBILE MONEY WITHDRAWAL
            elif transaction == 3:
                # RUN THE MOBILE MONEY FUNCTION
                momo()
                break
            
            # CHECK IF USER WANTS QUIT OR LOG OFF
            elif transaction == 99:
                while True:
                    # REQUEST INPUT FROM USER
                    print (' \n_______________________________________________________________________________\n  \n')
                    quitConfirm = str(input('\n \nWop3 s3 wogyae? Mia (Y) ma aane /anaa (N) ma daabi:  ')).upper()
                    print (' \n_______________________________________________________________________________\n  \n')

                    # IF USER SAYS YES END PROGRAM
                    if quitConfirm == 'Y':
                        print("""
                            -----------------------------------------
                            |    TECH SEALS SIKAKORABIA da woase.    |
                            |            San Bra bio.!               |
                            -----------------------------------------
                        """)
                        exit()

                    # IF USER SAYS NO RELOAD THE MAIN MENU
                    elif quitConfirm == 'N':
                        break
                    
                    # IF USER RESPONSE IS INVALID ASK FOR A VALID INPUT
                    else:
                        print (' \n_______________________________________________________________________________\n  \n')
                        print ('Any3 yie, san bo bio')
                        print (' \n_______________________________________________________________________________\n  \n')
                        continue

                continue

            else:
                print (' \n_______________________________________________________________________________\n  \n')
                print ('Any3 yie, san bo bio')
                print (' \n_______________________________________________________________________________\n  \n')
                continue
        
        except ValueError:
            print (' \n_______________________________________________________________________________\n  \n')
            print ('Any3 yie, san bo bio')
            print (' \n_______________________________________________________________________________\n  \n')
            continue


    # CHECK IF USER WOULD LIKE TO PERFORM ANOTHER TRANSACTION
    while True:
        # REQUEST INPUT FROM USER
        print (' \n_______________________________________________________________________________\n  \n')
        backtoMain = str(input('Wop3 s3 woy3 biribi foforo bio? Mia (Y) ma aane /anaa (N) ma daabi :  ')).upper()
        print (' \n_______________________________________________________________________________\n  \n')

        # IF USER SAYS YES RELOAD THE MAIN MENU
        if  backtoMain == 'Y':
            return atmMenu()
        
        # IF USER SAYS NO END PROGRAM
        elif  backtoMain == 'N':
            print("""
                -----------------------------------------
                |    TECH SEALS SIKAKORABIA da woase.    |
                |        San Bra bio.!                   |
                -----------------------------------------
            """)
            exit()

        # IF USER RESPONSE IS INVALID ASK FOR A VALID INPUT
        else:
            print ('Any3 yie, san bo bio')
            continue


# WITHDRAWAL AND BALANCE UPDATE FUNCTION
def withdrawUpdate():
    # DISPLAY FUNCTION MESSAGE
    print ('########################################### ATM WITHDRAWAL #####################################################\n \n')
    print (('TECH SEALS SIKAKORABIA\n \nDi saa nhyeshe3 yi so').upper())

    # SET A MINIMUM BALANCE LIMIT
    minimumBalance = 50

    # SET A MAXIMUM WITHDRAWAL LIMIT
    maxWithdrawal = 5000

    # TAKE USER INPUTS ON WITHDRAWAL SPECIFICS
    def withdrawRequest():
       # TAKE CURRENCY INPUT 
        while True:
            print (' \n******************************************* CURRENCY *****************************************************\n \n')
            currency = str(input('Yi fri CEDIS anaa D)LA account mu (Mia (G) ma CEDIS /anaa (D) ma D)LA):\n').upper())

            # IF THE USER INPUT IS INCORRECT RESTART FUNCTION
            if currency not in ('D', 'G'):
                print (' \n_______________________________________________________________________________\n  \n')
                print("Any3 yie, san bo bio")
                print (' \n_______________________________________________________________________________\n  \n')
                continue
            
            # IF THE USER INPUT IS CORRECT ASSIGN THE SELECTED CURRENCY TO THE VARIABLE CURRENCY
            elif currency == 'D':
                currency = 'USD'
                break
            elif currency == 'G':
                currency = 'GHS'
                break
        
        # TAKE AMOUNT INPUT
        while True:
            print (' \n******************************************* AMOUNT *********************************************************\n \n')

            # CHECK THE AMOUNT VALUE INPUTTED
            try:
                amount = int(input('B) sika dodow a wop3 s3 woyi:\n'))

                # IF THE WITHDRAWAL AMOUNT IS MORE THAN THE USERS BALANCE DO THIS
                if amount >= userBalance[currency]:
                    
                    # ALLOW USER TO DECIDE TO TR AGAIN OR RETURN TO MAIN MENU
                    while True:
                        stopContinue = str(input("Sika no 3nso\n \nWop3 s3 wo san y3 bio anaa wob3k) ahy3ase3?\n \n Mia (Y) na san y3 bio / anaa Mia (N) na ko ahy3ase3" )).upper()

                        # IF THE USER INPUT IS INCORRECT ASK FOR CORRECT INPUT
                        if stopContinue not in ('Y', 'N'):
                            print ('Any3 yie, san bo bio.')
                            continue
                        
                        # IF USER SAYS YES RESTART FUNCTION AND TAKE CORRECT AMOUNT INPUT
                        elif stopContinue == 'Y':
                            break

                        # IF USER SAYS NO RETURN TO THE MAIN MENU
                        elif stopContinue == 'N':
                            return atmMenu()
                            
                    continue

                # IF THE WITHDRAWAL AMOUNT IS LESS THAN THE USERS BALANCE MOVE TO THE NEXT STEP
                elif amount < userBalance[currency]:
                    # CHECK USER BALANCE AFTER SPECIFIED WITHDRAWAL AMOUNT IS WITHDRAWN
                    balanceAfterWithdraw = userBalance[currency] - amount
                    
                    # CHECK IF BALANCE AFTER WITHDRAWAL IS LESS THAN MINIMUM ALLOWED BALANCE AND ASK USER TO TRY AGAIN
                    if balanceAfterWithdraw < minimumBalance:
                        print (' \n_______________________________________________________________________________\n  \n')
                        print ('Sika no nso bere a woyi wie no.\n Ewose wo sika so kyen '+ currency + ' ' +str(minimumBalance) +'. San bo bio: \n')
                        print (' \n_______________________________________________________________________________\n  \n')
                        continue

                    # CHECK IF WITHDRAWAL AMOUNT IS GREATER THAN MAXIMUM WITHDRAWAL LIMIT AND ASK USER TO TRY AGAIN
                    elif amount > maxWithdrawal:
                        print (' \n_______________________________________________________________________________\n  \n')
                        print ('Meser3wo, wontumi nnyi sika '+ currency + ' ' + str(maxWithdrawal) +'. San bo bio: \n')
                        print (' \n_______________________________________________________________________________\n  \n')
                        continue

                    else:
                        break
                

            # IF THE USER DOES NOT INPUT WHOLE NUMBERS ASK USER TO TRY AGAIN
            except ValueError:
                print (' \n_______________________________________________________________________________\n  \n')
                print ('Any3 yie, san bo bio')
                print (' \n_______________________________________________________________________________\n  \n')
                continue
        
        # HOLD CURRENCY AND AMOUNT SPECIFIED BY USER
        return currency,amount
            
    
    # RUN THE WITHDRAWAL REQUEST FUNCTION
    while True: 
        # SAVE CURRENCY AND AMOUNT SPECIFIED BY USER INTO THE VARIABLE
        withdrawalValues = withdrawRequest()
        # SAVE CURRENCY SPECIFIED BY USER INTO THE VARIABLE
        currency = withdrawalValues[0]
        # SAVE AMOUNT SPECIFIED BY USER INTO THE VARIABLE
        amount = withdrawalValues[1]
        
        # PROMPT USER TO CONFIRM WITHDRAWAL AMOUNT
        print (' \n******************************************* CONFIRM WITHDRAWAL AMOUNT *********************************************************\n \n')
        confirmation = str(input('Mepaky3w hw3 s3 sika no aso: ' + currency + ' '+ str(amount) + '\n Mia (Y) na toaso / anaa mia (N) na sesa no: ').upper())
        
        # IF THE USER INPUT IS INCORRECT ASK FOR CORRECT INPUT
        if confirmation not in ('Y', 'N'):
            print (' \n_______________________________________________________________________________\n  \n')
            print ("Any3 yie, san bo bio.")
            print (' \n_______________________________________________________________________________\n  \n')
            continue

        # IF THE USER SAYS NO ALLOW USER CHANGE VALUES
        elif confirmation == 'N':
            continue

        # IF THE USER SAYS YES CONFIRM SUCCESSFUL WITHDRAWAL IN NEXT STEP
        elif confirmation == 'Y':
            break
    
    # DISPLAY SUCCESSFUL WITHDRAWAL MESSAGE
    print (' \n******************************************* SUCCESSFUL WITHDRAWAL *********************************************************\n \n')
    print ('SUCCESS!')

    # SAVE THE WITHDRAWN AMOUNT AND CURRENCY
    amountWithdrawn = amount
    currencyWithdrawn = currency

    # DISPLAY AMOUNT WITHDRAWN TO USER
    print (' \n_______________________________________________________________________________\n  \n')
    print ('Watumi ayi '+ currencyWithdrawn +' '+ str(amountWithdrawn))

    # DISPLAY USERS PREVIOUS BALANCE
    print ('Sika a na wo w): '+ currencyWithdrawn +' '+ str(userBalance[currency]))
    # SUBTRACT WITHDRAWN AMOUNT FROM USERS CURRENT BALANCE AND SAVE IT TO newBalance VARIABLE
    newBalance = userBalance[currency] - amountWithdrawn
    
    # UPDATE USERS BALANCE TO WITH NEW BALANCE
    userBalance[currency] = newBalance
    # DISPLAY USERS UPDATED BALANCE
    print ('Sika a aka: '+ currencyWithdrawn +' '+ str(userBalance[currency]))
    print (' \n_______________________________________________________________________________\n  \n')
    print ('TECH SEALS SIKAKORABIA da woase!')
    print (' \n_______________________________________________________________________________\n  \n')

    # HOLD USERS SPECIFIED CURENCY, AMOUNT AND CURRENT BALANCE AFTER WITHDRAWAL
    return currencyWithdrawn, amountWithdrawn, newBalance


def momo():
        print ('########################################### MOBILE MONEY WITHDRAWAL #####################################################\n \n')
        print("Wo p3 Network ben?\n1) MTN\n2) Vodafone\n3) AirtelTigo \n \n")
        while True:
            try:
                userService = str(input("Mia 1, 2, 3: "))
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
                    print("Any3 yie, san bo bio")
                    print (' \n_______________________________________________________________________________\n  \n')
                    continue
            
            except ValueError:
                print (' \n_______________________________________________________________________________\n  \n')
                print("Any3 yie, san bo bio")
                print (' \n_______________________________________________________________________________\n  \n')
                continue
        
        
        while True:
            print (' \n_______________________________________________________________________________\n  \n')
            print("Y3amane TRANSACTION CODE no w) wo fon no so")
            transactionCode = random.randint(100000,999999)
            print ("Transaction Code: "+ str(transactionCode))
            
            try:
                print (' \n_______________________________________________________________________________\n  \n')
                userTransactionCode = int(input("B) wo TRANSACTION CODE no w) ha: "))
                if userTransactionCode == transactionCode:
                    while True:
                        print (' \n_______________________________________________________________________________\n  \n')
                        print("B) sika dodow a wop3 s3 woyi?")
                        try:
                            momoAmount = int(input("B) sika no: "))

                            if momoAmount <= 2000:
                                print (' \n_______________________________________________________________________________\n  \n')
                                print ("Mepaky3w hw3 s3 sika no y3 GHS "+ str(momoAmount))
                                while True:
                                    momoConfirm = str(input("MIA (Y) na toaso /anaa 'N' na san y3:  ")).upper()

                                    if momoConfirm not in ('Y', 'N'):
                                        print (' \n_______________________________________________________________________________\n  \n')
                                        print ("Any3 yie, san bo bio.")
                                        print (' \n_______________________________________________________________________________\n  \n')
                                        continue
                                    
                                    elif momoConfirm == 'Y':
                                        while True:
                                            momoPin = random.randint(1000,9999)
                                            print (' \n_______________________________________________________________________________\n  \n')
                                            print (" B) wo momo pin no")
                                            print ("MOMO PIN = "+ str(momoPin))
                                            print (' \n_______________________________________________________________________________\n  \n')
                                            momoPinValid = int(getpass.getpass(" B) wo Momo Pin: "))
                                            
                                            if momoPinValid == momoPin:
                                                print (' \n_______________________________________________________________________________\n  \n')
                                                print("Mo! Watumi ayi sika no")
                                                print (' \n_______________________________________________________________________________\n  \n')
                                                pause = input('Mia (ENTER) na ko (MAIN MENU) ')
                                                return atmMenu()
                                

                                            elif momoPinValid != momoPin:
                                                print (' \n_______________________________________________________________________________\n  \n')
                                                print('Any3 yie, san bo bio.')
                                                print (' \n_______________________________________________________________________________\n  \n')
                                                continue
                                    
                                    elif momoConfirm == 'N':
                                        break

                                    else:
                                        print (' \n_______________________________________________________________________________\n  \n')
                                        print ("Any3 yie, san b) bio.")
                                        print (' \n_______________________________________________________________________________\n  \n')
                                        continue
                                
                                break

                            elif momoAmount > 2000:
                                while True:
                                    print (' \n_______________________________________________________________________________\n  \n')
                                    momoContinue = str(input("Any3 yie! Wontumi enyi ky3n GHS 2000\n \nWo p3s3 wony3 bio a mia (Y) / anaa Wo p3s3 wo san hy3 ase mia (N): ")).upper()
                                    print (' \n_______________________________________________________________________________\n  \n')

                                    # IF THE USER INPUT IS INCORRECT ASK FOR CORRECT INPUT
                                    if momoContinue not in ('Y', 'N'):
                                        print (' \n_______________________________________________________________________________\n  \n')
                                        print ('Any3 yie, san b) bio.')
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
                            print ('Any3 yie, san b) bio')
                            print (' \n_______________________________________________________________________________\n  \n')
                            continue

                    break 
                else:
                    print (' \n_______________________________________________________________________________\n  \n')
                    print("Any3 yie, san b) bio")
                    print (' \n_______________________________________________________________________________\n  \n')
                    continue

            except ValueError:
                print (' \n_______________________________________________________________________________\n  \n')
                print("Any3 yie, san b) bio")
                print (' \n_______________________________________________________________________________\n  \n')
                continue
        

# PRINT RECEIPT FUNCTION
def rcptPrint(withdrawn):
    # CHECK IF USER WOULD LIKE TO PRINT A RECEIPT FOR THE TRANSACTION
    while True:
        optn = input("Mepaky3w wop3 RECEIPT anaa?? (Y/N):  ").upper()
        
        # CHECK IF THE USER SAYS YES AND PRINT A RECEIPT FOR THE TRANSACTION i.e DISPLAY SPECIFICS OF THE TRANSACTION
        if optn == "Y":
            print(("\n \n.........TRANSACTION RECEIPT............\n").upper())
            print("******************************************\n \n")
            print(("Wo awie wo dwumadie no.\n").upper())                       
            print("Transaction n)ma: "+str(random.randint(100000000000,999999999999))+"\n")
            print("Account din: "+str(session['username']).upper()+"\n") 
            print("Sika a woyii y3: "+str(withdrawn[0])+" "+str(withdrawn[1])+"\n")      
            print("Sika a aka: "+str(withdrawn[2])+"\n \n")                 
            print("*******************************************\n \n")
            print("TECH SEALS SIKAKORABIA da woase!\n \n")
            print("*******************************************\n \n")
            break
        
        # CHECK IF THE USER SAYS NO STOP THE LOOP
        elif optn == "N":
            break   

        # CHECK IF THE USER INPUT IS INCORRECT AND ASK FOR THE CORRECT INPUT
        else:
            print("Any3 yie, san bo bio. Mia (Y) ma aane /anaa (N) ma daabi.\n")
            continue
    return


# CHECK CURRENT BALANCE FUNCTION
def crntBalance():    

    while True:
        print ('########################################### BALANCE CHECK #####################################################\n \n')
        currency = str(input("Account b3n na wop3 s3 wohw3: \nMia (G) ma GHS /anaa (D) ma USD: ")).upper()
        if currency == 'G':
            currency = 'GHS'
            break                    

        elif currency == 'D':
            currency = 'USD'
            break

        else:
            print (' \n_______________________________________________________________________________\n  \n')
            print("Any3 yie, san bo bio. Mia 'G' ma GHS or /anaa (D) ma USD")        
            print (' \n_______________________________________________________________________________\n  \n')    
            continue


    availableBalance = userBalance[currency]
    print (' \n_______________________________________________________________________________\n  \n')
    print (('Sika wo w) wo '+ currency +' account y3:\n \n').upper())
    print (currency +' '+ str(availableBalance ))
    print (' \n_______________________________________________________________________________\n  \n')
  

# USER LOGIN IDENTITY VERIFICATION FUNCTION
def userLogin(userName):

    for userdata in userArray:

        sessiondata = {'username':'unknown', 'pin':0000, 'balance':{'GHS':0, 'USD':0} } 

        # Checks for user existence and says a welcome message

        if userName == userdata['username']:
            found = True
            sessiondata = userdata #Transfers the found users bank info in to sessiondata variable
            break  
            
        else:
            found = False
            pass          

    
    return sessiondata # Returns the value of sessiondata after userLogin() is run,  so we can use in the continuing code 


def updatePin():
        
    #user inputs pin
    print("Y3amane CODE no w) wo fon no so")
    
    verificationCode = random.randint(1000,9999)

    print(verificationCode)
    
    #after the user has been verified, he/she proceeds with the change
    while True:
        
        codeVerify = int(input("B) wo CODE no w) ha: "))
        
        if codeVerify == verificationCode:
            while True:
                newPin = int(getpass.getpass(" B) PIN foforo: "))
                newPinConfirm = int(getpass.getpass(" San b) PIN foforo nu: "))
                
                if newPin == newPinConfirm:
                    print("Mo! Wo PIN asasesa!")
                    session['pin'] = newPin
                    pause = input('Mia 3nta na hy3 ase3 foforo. ')
                    break

                elif newPin != newPinConfirm:
                    print('PIN no anfa. San b) PIN no bio.')
                    continue
            break

        elif codeVerify != verificationCode:
            print("CODE no anfa. San b) CODE no bio")
            continue
    
    return
    

# USER LOGIN PIN VERIFICATION FUNCTION
def pinVerify(userPin):
    
    def pinChangeRequest():
        while True:
            pinChange = str(input('Woafiri wo pin anaa? Mia (Y) ma aane /anaa (N) ma daabi (Y/N): ')).upper()

            if pinChange == 'Y':
                updatePin()
                return atmMenu()

            elif pinChange == 'N':
                print("""
                    -----------------------------------------
                    |    TECH SEALS SIKAKORABIA da woase    |
                    |            San bra bio!               |
                    -----------------------------------------
                """)
                exit()

            else:
                print ('Any3 yie, san b) PIN no bio')
                continue

    
    valid = False
    
    for attempt in range(4):
        print ("\n \n B) wo PIN no na toaso\n")
            
        pin = str(getpass.getpass("B) wo PIN no: "))
        
        if userPin == pin :
            valid = True
            break

        else:
            print (' \n_______________________________________________________________________________\n  \n')
            print ('Any3 yie, san b) PIN no bio')
            print (' \n_______________________________________________________________________________\n  \n')
            continue
    
    if attempt == 3:
        pinChangeRequest()
    
    
            
    return atmMenu() 


# STORE USER'S USERNAME INPUT TO SPECIFIED VARIABLE
userName = str(input("Account din: ")).lower()


# RETRIEVE SPECIFIED USER DETAILS FROM DICTIONARY TO SPECIFIED VARIABLE
session = userLogin(userName)


# RETRIEVE SPECIFIED USER PIN AND STORE TO VARIABLE
userPin = str(session['pin'])


# RETRIEVE SPECIFIED USER BALANCE AND STORE TO VARIABLE
userBalance = session['balance']


# RUN PIN VERIFICATION FUNCTION
pinVerify(userPin)