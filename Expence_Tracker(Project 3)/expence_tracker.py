open("EXPENCE_Tracker.txt", "w").close() 
while True:
       amount = input("Enter Your Expence (Type Done When Complete): ")
       if amount.lower() == "done":
           break
       else:
           with open ("EXPENCE_Tracker.txt", "a") as f:
               f.write(amount+ "\n")

with open ("EXPENCE_Tracker.txt", "r") as f:
            lines =  f.readlines()
            Total = 0 
            for line in lines:
                Total = Total + int(line.strip())
            print(f"Total Expence = {Total}")