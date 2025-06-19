# slot machine 
import random
def spin_row() :
    symbols =["🍉","🥥","🍊","🍎","🥝"]

    return [random.choice(symbols) for symbol in range(3)]

def print_row(row):
    print("".join(row))

def get_payout(row,bet):
   if row[0] == row[2] == row[1] :
       if row[0] =="🍉" :
           return bet*3
       elif row[0] =="🥥":
           return bet*2
       elif row[0] =="🍊":
           return bet*25
       elif row[0] =="🍎":
           return bet*5
       elif row[0] =="🥝":
           return bet*8
       else :
           return 0
       
def main():
    balance =100

    print("-------------------------")
    print("Welcome to the slot game ")
    print("symbols: 🍉🥥🥝🍊🍎")
    print("-------------------------")
    
    while balance > 0 :
        print(f"your current balance is ${balance}")
        bet = input("Enter a bet amount")
        
        if not bet.isdigit():
            print("ENTER A VALID AMOUNT")
            continue
        bet = int(bet)

        if bet > balance:
            print("INSUFFICIENT FUNDS")
            continue

        if bet<=0 :
            print("BET MUST BE GREATER THAN $0 ")
            continue
        balance-=bet

        print("Spinning the slot machine... 🎰")
        row = spin_row()
        print(" | ".join(row))

        payout = get_payout(row,bet)
        

        if payout > 0:
          print(f"you won ${payout}")

        else :
          print("YOU LOST AGAIN ")

        balance +=payout

        play_again = input("DO you want to play another game (Y/N)").upper()

        if play_again != "Y" :
            break


print("YOU ARE OUT OF MONEY")
if __name__=='__main__':
    main()
 