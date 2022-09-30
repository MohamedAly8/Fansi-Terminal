class Person:
  def __init__(self, name, age, mood):
    self.name = name
    self.age = age
    self.mood = mood

  def myfunc(self):
    """Gets greeting from Person"""
    print("Hello my name is " + self.name)

  def getName(self):
    """Gets Name of Person Object"""
    return self.name

  def getAge(self):
    """Gets Age of Person Object"""
    return self.age

  def getMood(self):
    """Gets Mood of Person Object"""
    return self.mood

  def increaseAge(self):
    """Iterates the Age of Person Object"""
    self.age += 1

  def setName(self, newName):
    """Changes Name of Person Object"""
    self.name = newName

  def setMood(self, newMood):
    """Changes Mood of Person Object"""
    self.mood = newMood

def talk(name, input):
  """This function talks to someone"""
  print(input + name + "!")
  
def this_is_a_function():
  """This is a function"""
  return "i am returning something"

