# password manager 
def add_account() :
    account_name = input('Enter your account name')

def view_account() :
    pass

def saerch_by_username():
    pass

def remove_account() :
    pass

is_running =True

while is_running :
    print("------------------------")
    print("        Welcome         ")
    print("------------------------")
    print('1. add account' \
    '2. view saved accounts' \
    '3. Search by user_name ' \
    '4. Remove account' \
    '5. Exit')
    service = input("please enter a service (1-5) : ")

    if service == '5':
        is_running =False
        break 
    if service == '1' :
        add_account()

print('Thank you for viusiting ')