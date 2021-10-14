
# WITHDRAWAL AND BALANCE UPDATE FUNCTION
def withdrawUpdate():
    # DISPLAY FUNCTION MESSAGE
    print ('########################################### ATM WITHDRAWAL #####################################################\n \n')
    print (('Tech Seals Banking App\n \n Please follow the instructions for a successful transaction').upper())

    # SET A MINIMUM BALANCE LIMIT
    minimumBalance = 50

    # SET A MAXIMUM WITHDRAWAL LIMIT
    maxWithdrawal = 5000

    # TAKE USER INPUTS ON WITHDRAWAL SPECIFICS
    def withdrawRequest():
       # TAKE CURRENCY INPUT 
        while True:
            print (' \n******************************************* CURRENCY *****************************************************\n \n')
            currency = str(input('Withdraw from USD or GHS account (Type D for USD / G for GHS):\n').upper())

            # IF THE USER INPUT IS INCORRECT RESTART FUNCTION
            if currency not in ('D', 'G'):
                print (' \n_______________________________________________________________________________\n  \n')
                print("Invalid choice. Please try again")
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
                amount = int(input('Please enter the amount you want to withdraw:\n'))

                # IF THE WITHDRAWAL AMOUNT IS MORE THAN THE USERS BALANCE DO THIS
                if amount >= userBalance[currency]:
                    
                    # ALLOW USER TO DECIDE TO TR AGAIN OR RETURN TO MAIN MENU
                    while True:
                        stopContinue = str(input("Insufficient Funds\n \nWould you like to try again or return to the main Menu? \n Type 'Y' to try agin or Type 'N' to return to the main Menu: \n")).upper()

                        # IF THE USER INPUT IS INCORRECT ASK FOR CORRECT INPUT
                        if stopContinue not in ('Y', 'N'):
                            print ('Invalid Input, try again.')
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
                        print ('Insufficient remaining balance after withdrawal.\n You must have a minimum balance of '+ currency + ' ' +str(minimumBalance) +'. Try Again: \n')
                        print (' \n_______________________________________________________________________________\n  \n')
                        continue

                    # CHECK IF WITHDRAWAL AMOUNT IS GREATER THAN MAXIMUM WITHDRAWAL LIMIT AND ASK USER TO TRY AGAIN
                    elif amount > maxWithdrawal:
                        print (' \n_______________________________________________________________________________\n  \n')
                        print ('Sorry. You can not withdraw more than '+ currency + ' ' + str(maxWithdrawal) +'. Try Again: \n')
                        print (' \n_______________________________________________________________________________\n  \n')
                        continue

                    else:
                        break
                

            # IF THE USER DOES NOT INPUT WHOLE NUMBERS ASK USER TO TRY AGAIN
            except ValueError:
                print (' \n_______________________________________________________________________________\n  \n')
                print ('Invalid input. Please enter a number')
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
        confirmation = str(input('Please confirm withdrawal amount: ' + currency + ' '+ str(amount) + '\n Y to continue / N to change amount: ').upper())
        
        # IF THE USER INPUT IS INCORRECT ASK FOR CORRECT INPUT
        if confirmation not in ('Y', 'N'):
            print (' \n_______________________________________________________________________________\n  \n')
            print ("Sorry I didn't understand that. Please start again.")
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
    print ('Successful Withdrawal of '+ currencyWithdrawn +' '+ str(amountWithdrawn))

    # DISPLAY USERS PREVIOUS BALANCE
    print ('Previous Balance: '+ currencyWithdrawn +' '+ str(userBalance[currency]))
    # SUBTRACT WITHDRAWN AMOUNT FROM USERS CURRENT BALANCE AND SAVE IT TO newBalance VARIABLE
    newBalance = userBalance[currency] - amountWithdrawn
    
    # UPDATE USERS BALANCE TO WITH NEW BALANCE
    userBalance[currency] = newBalance
    # DISPLAY USERS UPDATED BALANCE
    print ('New Balance: '+ currencyWithdrawn +' '+ str(userBalance[currency]))
    print (' \n_______________________________________________________________________________\n  \n')
    print ('Thank You For Banking With Us!')
    print (' \n_______________________________________________________________________________\n  \n')

    # HOLD USERS SPECIFIED CURENCY, AMOUNT AND CURRENT BALANCE AFTER WITHDRAWAL
    return currencyWithdrawn, amountWithdrawn, newBalance
