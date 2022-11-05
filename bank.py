#parent class: User
#Holds details about a user
#has a function to show details
#stores details about the account balance
#stores details about the amount
#allows for deposits, withdraws, view_balance

#Parent Class
class User():
    def __init__(self,name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_user_details(self):
        print ("\n Personal Details:")
        print("")
        print("Name:",self.name)
        print("Age:", self.age)
        print("Gender:",self.gender)

#Child Class

class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 20

    def deposit(self,amount):
        self.balance = self.balance + amount
        print("Account balance has been updated: $", self.balance)

bankuser = Bank("usuario1", "33", "F")
bankuser.show_user_details()
bankuser.deposit(20)