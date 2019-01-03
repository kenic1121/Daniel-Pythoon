class petClass () :
    type = 'cage free pet'
    def whatIsIt (self) :
        print(self.ptype, self.pname, self.pbreed, self.cagefreepet)
    def __init__ (self, type , name , breed , CFP) :
        self.ptype = type
        self.pname = name
        self.pbreed = breed
        self.cagefreepet = CFP

class cageClass () :
    type = 'caged pet'
    def WhatDanger (self) :
        if self.cdanger == 'true' :
            print ('DANGEROUS')
        if self.cdanger == 'false' :
            print ('Not Dangerous')

    def __init__ (self , type, danger):
         self.cType = type
         self.cdanger = danger


def pets () :
    myPet1 = petClass("Dog","John","Boxer","Cage Free Pet")
    print(myPet1.pname)
    print(myPet1.ptype)
    print(myPet1.cagefreepet)
    myPet1.whatIsIt()

    input('Pause')

    myPet2 = petClass("Cat","Charles","Calico","Cage Free Pet")
    print(myPet2.pname)
    print(myPet2.ptype)
    print(myPet1.cagefreepet)
    myPet2.whatIsIt()

    input('pause')

    myCage1 = cageClass("snake","true")
    print(myCage1.cType)
    myCage1.WhatDanger()

    input('pause')

    myCage2 = cageClass("rat","false")
    print(myCage2.cType)
    myCage2.WhatDanger()







pets()
