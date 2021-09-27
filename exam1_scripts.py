
# collecting info from a user
first_name = input("Please provide your name and 2 numbers. Your first name is: ")
last_name = input("Please give your last name now: ")
number = int(input("Now, please provide our number: "))

# performing calculation
result = float(number/7)

# reporting results to the user
print("Hi, {} {}. Your personal code is {}".format(
    first_name, last_name, result))

# storing results in a dictionary for reuse
key = first_name + last_name
kidsClub = {key:result}

# testing data storage
#print(kidsClub)


en_de = {"red" : "rot", "green" : "grün", "blue" : "blau", "yellow" : "gelb"}
# (a) What Python code do you have to type to answer the question "What is the German word for red?"
print("This is German for 'red': ", en_de['red'])

de_fr = {"rot" : "rouge", "grün" : "vert", "blau" : "bleu", "gelb" : "jaune"}

print("What is French for red? French for red is 'red'->'rot'->'{}': ".format(
    de_fr[en_de['red']]))


class Alien:
  def __init__(self, name, numArms, home):
    self.name = name
    self.numArms = numArms
    self.planet = home

  def __str__(self):
    return self.name +' '+self.planet+' '+str(self.numArms)

  def changeName(self,name):
    self.name = name

  def growArms(self):
    self.numArms = self.numArms +1

class SonicAlien(Alien):
  def __init__(self,name,numArms,home,spots):
    '''
    Constructor written appropriately 
    It handels name, numArms,home,spots
    '''
  def __str__(self):
    return self.name +' '+self.planet+' '+str(self.num_Arms)+' ' +str(self.spots)

  def growArms(self):
    self.numArms = self.numArms +3
    
alien1 = Alien("K00kie",3,"Mars") # create alien1 object
alien2 = Alien("L33tAlien",5,"Titan") # create alien2 object
alien3 = SonicAlien("Sonny",7,"Pluto",True) # SonicAlien has spots! (boolean)

print(alien3.name)
alien1.growArms() # Line 1
alien1.changeName('MarsK00kie') # Line 2
alien3.growArms() # Line 3
alien3.changeName('Sonnie') # Line 4
print(alien3.name)





bankDB = {'Michael':6494, 'Angela':2982, 'Sage':7771, 'Oliver':3612, "Aaa":0}

# a) (5 points) Let’s write a helper method to identify client names that begin with a vowel. 

    
def beginWithVowel(theKey):
  vowels = ['A', 'E', 'I', 'O', 'U'] # a list of vowels
  # if the first letter is a vowel, return true.
  if theKey[0] in vowels: 
      return True
  else: # else, return false
      return False


VowelNames = list(filter(beginWithVowel, bankDB))

for key in bankDB:
    if key in VowelNames:
        bankDB[key] += 500
        
print(bankDB)





class Horse():
    def __init__(self, name, owner, age, injuryList=[]):
        self.name = name
        self.owner = owner
        self.age = age
        self.injuryList = injuryList

h = Horse("AaAAA", "BBBB", 34, ['broken leg', 'marks'])
h.injuryList
h2 = Horse("Bob", "Mike", 33)
h2.injuryList
h2.name











try:
  name = input("Enter the name of a file: ")
  file = open(name, 'r') # try to open this file for reading
  special = input("Enter a special boolean input: ") # assume no casting if type(special) is not 
  #boolean:

except FileNotFoundError:   # specifically for file errors [BEFORE IOError!]
    print("** FileNotFoundError >> Cannot open file! **")
    name = input("Enter the name of a file to open: ") # w2filegrades.txt
    file = open(name, 'r')     

except IOError:  # for general IO errors
    print("** You caught a general IOError! **")
    name = input("Enter the name of a file to open: ") # w2filegrades.txt
    file = open(name, 'r')

except TypeError:
    print("** Wrong data type >> Special boolean input is expected **")
    special = input("Enter a special boolean input again : "

















