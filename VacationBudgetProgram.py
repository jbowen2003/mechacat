#A program used to help the user save for a vacation by telling them how much money to save per month


def getUserInput(prompt):
    data=int(input(prompt))
    return data

def getAmount(budget, months):
    amount = budget/months
    return amount

def displayResult(budget, months, amount):
    print("You need to save $", amount, "per month to go on vacation. ")


budget= getUserInput("Enter cost of vacation: ")
months=getUserInput("How many months until vacation? ")
amount=getAmount(budget, months)
displayResult(budget, months, amount)

