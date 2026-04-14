import random
import time
import os

# Variables to pre-determine the options of the ATM
deposit = "D"
withdraw = "W"
quit = "Q"
balance = random.randint(-1000, 10000)

count = 2

while count > 0:

  # ATM Select Menu
  print(f"""****************************************
        PIXELL RIVER FINANCIAL
            ATM Simulator

  Your current balance is: ${balance:2,}

              Deposit: D
              Withdraw: W
                Quit: Q
****************************************""")

  # some values that might be repented
  transaction = "Enter the transaction amount: "
  insufficient_funds = """
****************************************
      INSUFFICIENT FUNDS
****************************************"""

  # asked for an input
  selection = input("Enter your selection: ")

  # DEPOSIT
  # if statement to see if the input is deposit
  ## add more numeric value to the balance
  if selection.upper() == deposit:
    amount = input(transaction)
    
    if int(amount) < 0: 
      print(insufficient_funds) 
      # end loop
      count = 0

      # Pause the script for the specified number of second
      time.sleep(3)

      # Clear the screen
      os.system('cls' if os.name == 'nt' else 'clear')
      break

    balance = balance + int(amount)    
    print(f"""
***************************************
  Your current balance is: ${balance:2,}
***************************************""")
    
  # WITHDRAW
  # check if the user input is withdraw
  elif selection.upper() == withdraw:
    amount = input(transaction)

    # check if the input isn't negative
    if int(amount) < 0:
      print(insufficient_funds)
      # end loop
      count = 0

      # Pause the script for the specified number of second
      time.sleep(3)

      # Clear the screen
      os.system('cls' if os.name == 'nt' else 'clear')
      break

    # checking if the user input is insufficient from the balance
    elif int(amount) > balance:
      print(insufficient_funds)
      # Pause the script for the specified number of second
      time.sleep(3)

      # Clear the screen
      os.system('cls' if os.name == 'nt' else 'clear')
      break

    # subtract the current balance to withdraw
    else:
      balance = balance - int(amount)
      print(f"""
***************************************
  Your current balance is: ${balance:2,}
***************************************""")

  # QUIT
  # quit a transaction
  elif selection.upper() == quit:
    # Pause the script for the specified number of seconds
    time.sleep(3)

    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    exit()

  # check if the value is invalid in the 
  # selection menu of the ATM before transaction
  else:
    print("""
****************************************
          INVALID SELECTION
****************************************""")

  # AFTER-TRANSACTION
  # to ensure the loop count goes down
  count = count - 1

  # to ensure the loop stays finite
  if count > 2:
    break
  
  # Pause the script for the specified number of second
  time.sleep(3)

  # Clear the screen
  os.system('cls' if os.name == 'nt' else 'clear')