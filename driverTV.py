import mainclassTV

def createList():
    list = []
    amount = 0
    while True:
        amountInput = int(input("Input the amount of items"))
        amount = amountInput
        if amount >= 1:
            amount = amountInput
            break
    for i in range(amount):
        itemInput = input("Input the food name and amount of food (in pounds), seperated by comma ").split(",")
        foodName = itemInput[0]
        foodAmount = float(itemInput[1])
        if foodAmount < 1:
            print("Invalid food amount")
            i -= 1
        else:
            foodObject = mainclassTV.MainClass(foodName, foodAmount)
            list.append(foodObject)
            

def displayList(list):
    for i in list:
        list[i].__str__()

def calculateTotalCost(list):
    total = 0
    for i in list:
        total += list[i].calculatePriceTV()
    return total

def main():
    list = createList()
    displayList(list)
    calculateTotalCost(list)

main()