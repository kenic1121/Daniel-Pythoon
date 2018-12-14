def pets () :


    myPet1 = petClass("Dog","John","Boxer")
    print(myPet1.pname)
    print(myPet1.ptype)
    myPet1.whatIsIt()



    myPet2 = petClass("Cat","Charles","Calico")
    print(myPet2.pname)
    print(myPet2.ptype)
    myPet2.whatIsIt()


    myCage1 = cageClass("crocodile","True")
    print(myCage1.cType)
    print(myCage1.ptype)
    myCage1.whatDanger()



    myCage2 = cageClass("mouse","False")
    print(myCage2.cType)
    print(myCage2.petType)
    myCage2.whatDanger()





class petClass () :
    type = 'cage free pet'
    def __init__ (self, type , name , breed) :
        self.ptype = type
        self.pname = name
        self.pbreed = breed

    def WhatItIs (self) :
        print(self.ptype, self.pname, self.pbreed)


class cageClass () :
    type = 'caged pet'

    def __init__ (self , type, danger):
         self.ctype = type
         self.cdanger = danger
    def WhatDanger (self) :
        if self.cdanger == 'true' :
            print ('DANGEROUS')
        if self.cdanger == 'false' :
            print ('Not Dangerous')

pets()
