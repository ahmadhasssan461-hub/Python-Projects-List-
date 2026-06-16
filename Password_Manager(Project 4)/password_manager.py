class Passwordmanager:
    def __init__(self):
        self.passwords = {}
    
    def add_password(self):
        with open("pm.txt", "a") as f:
            site = input("Enter Your Site Name: ")
            password = input("Enter Your Password For This Site: ")
            f.write(f"{site},{password}\n")
            print("Password is saved.")
    
    def show_password(self):
        with open("pm.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
               data = line.strip().split(",")  # comma se split ✅
            print(f"Site: {data[0]}\nPassword: {data[1]}")

pm = Passwordmanager()
while True:
    choice = input("\n1. Add\n2. Show\n3. Exit\nChoice: ")

    if choice == "1":
        pm.add_password()
    elif choice == "2":
        pm.show_password()
    elif choice == "3":
        break