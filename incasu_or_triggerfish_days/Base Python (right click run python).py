import random

class ClassTester:
    # dinge hier sal geld vir ALLE instances van die ClassTester en is class_level so kan nie verander word nie (static values)
    # dinge binne def geld apart vir elke instance en kan verander word

    def EmptyMethod(self):
        pass # As jy die method leeg wil los vir eers

    def __init__(self):
        self.number = 10
        self.MagicNumbers = [3, 7]

    # print(Tester.AgeInSeconds())
    def AgeInSeconds(self):
        return "You have lived for {age} seconds. This corresponds to {years} years".format(age = int(self.number) * 365 * 24 * 60 * 60, years = self.number)

    # Tester.InMagicNumbers()
    def InMagicNumbers(self):
        if int(self.number) in self.MagicNumbers: print('You guessed correctly!')
        if int(self.number) not in self.MagicNumbers: print('You guessed wrong :(')

    # If & Sum
    def IfAndSum(self):
        print(sum([1, 5, 6]))
        self.Marks = {"Student_Marks" : [1, 7, 3]}
        print(sum(self.Marks["Student_Marks"]))
        
        if len(self.Marks["Student_Marks"]) > 2:
            print("Marks length is longer than 2")
        else:
            print("Marks length is NOT longer than 2")
        #elif : x == x (tel as n else if)
  
    # Tester.LoopUsingRange()
    def LoopUsingRange(self):
        self.TheRange = 3
        for index in range(self.TheRange):
            print(str(index) + ". Random number: " + str(random.randint(0, 10)))

    # Tester.ArraysANDLists()
    def ArraysANDLists(self):
        # Split string at "," points
        self.NumbersString = "5, 16, 25, 3, 4, 1"
        print(self.NumbersString.split(","))

        # Create list from array
        self.NumbersArray = [1, 6, 3, 7, 2]
        print([number for number in self.NumbersArray])
        print([number*2 for number in self.NumbersArray])

        # Sets
        self.NewEmptySet = set() # Jy kan nie n empty set so create nie = {}
        self.UniqueSet = {3, 5, 3, 7, 5, 1, 5}
        print(self.UniqueSet) # Sets sal altyd unique wees en die ander delete
        self.List1 = {3, 6, 8, 2}
        self.List2 = {6, 7, 3, 1}
        print(self.List1.intersection(self.List2))
        print(len(self.List2))

        # Advanced Dictionary
        self.Dictionary = {"student": ["Francois"],
                            "marks": {
                                "midterm": 50,
                                "final": [70, 50, 64, 21, 16]
                            }}
        print(self.Dictionary["marks"]["final"][2])
        self.Dictionary["student"].append("Deon")
        print(self.Dictionary["student"])

# Create instance van class
Tester = ClassTester()

print("#############################################################") # Code vir displaying
# Tester.function()

# Tester.number = input('Enter a number: ')

#Tester.InMagicNumbers()
Tester.ArraysANDLists()
Tester.IfAndSum()