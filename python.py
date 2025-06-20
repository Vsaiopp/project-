# password manager 
def add_account(vault):
    account_name = input('Enter your account name: ')
    user_name = input('Enter a user name: ')
    password = input('Enter a password: ')

    if account_name in vault:
        print("⚠️ Account already exists!")
    else:
        vault[account_name] = {
            'user name': user_name,
            'password': password
        }
        print("✅ Account added successfully!\n")

def view_account(vault):
    if not vault:
        print("📂 No accounts saved.\n")
    else:
        print("📘 Saved Accounts:")
        for acc in vault:
            print(f"- {acc}")
        print()

def search_by_username(vault):
    name = input("🔍 Enter the account name to search: ")
    if name in vault:
        print(f"👤 Username: {vault[name]['user name']}")
        print(f"🔑 Password: {vault[name]['password']}\n")
    else:
        print("❌ Account not found.\n")

def remove_account(vault):
    name = input("🗑️ Enter the account name to remove: ")
    if name in vault:
        del vault[name]
        print("✅ Account removed.\n")
    else:
        print("❌ Account not found.\n")

# Main Program
vault = {}
is_running = True

while is_running:
    print("------------------------")
    print("🔐 Password Vault Menu")
    print("------------------------")
    print("1. Add account")
    print("2. View saved accounts")
    print("3. Search by username")
    print("4. Remove account")
    print("5. Exit")

    service = input("👉 Choose an option (1–5): ")

    if service == '1':
        add_account(vault)
    elif service == '2':
        view_account(vault)
    elif service == '3':
        search_by_username(vault)
    elif service == '4':
        remove_account(vault)
    elif service == '5':
        is_running = False
    else:
        print("⚠️ Invalid input. Please try again.\n")

print("👋 Thank you for using Password Vault!")
