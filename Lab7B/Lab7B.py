class pet:
    def __init__(self, name, breed):
        self.pname = name
        self.pbreed = breed

    def info(self):
        return(self.pname + " " + self.pbreed)

class dog(pet):
    def __init__(self, activity):
        self.activity = activity

    def info2(self):
        return (self.activity)

def Pets () :
    print("_________Pet #1_________")
    myPet1 = pet("Spot" , "dog")
    print(myPet1.info())

    print("_________Pet #2_________")
    myPet2 = dog("Runs")
    print(myPet1.info() , myPet2.info2 ())


Pets()
