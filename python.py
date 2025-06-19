# banking programme 
# banking program

def show_balance():
    print(f"Your current balance is ₹{balance}")

def deposits():
    global balance
    amount = float(input("Enter amount to deposit: ₹"))
    if amount > 0:
        balance += amount
        print(f"₹{amount} deposited successfully.")
    else:
        print("Invalid amount.")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: ₹"))
    if 0 < amount <= balance:
        balance -= amount
        print(f"₹{amount} withdrawn successfully.")
    else:
        print("Invalid or insufficient funds.")

balance = 0
is_running = True
while is_running :
    print("\n--------------------------------------------")
    print("WELCOME TO V BANK")
    print("--------------------------------------------\n")
    x = ["1. Show Balance", "2. Deposit", "3. Withdraw", "4. Exit"]
    for y in x :
       
        print(y)
        
    
    choice = input("Select the service (1-4): ").strip()

    if choice == "1":
        show_balance()
    elif choice == "2":
        deposits()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        print("Thank you for banking with us!")
        is_running = False
    else:
        print("Invalid input. Please choose 1-4.")
