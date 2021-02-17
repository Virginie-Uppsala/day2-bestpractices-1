class dangerous:
 def __init__(self):
  self.members=['Fish','Birds']

 class Fish:
  def __init__(self):
   self.members=['Jellyfish','Shark']
  
  def printMembers(self):
   print('Printing animals of the dangerous Fish class')
   for member in self.members:
    print('\t%s ' % member)
    
 class Birds:
  def __init__(self):
   self.members=['Sparrow']
  
  def printMembers(self):
   print('Printing animals of the dangerous Bird class')
   for member in self.members:
    print('\t%s ' % member)


class harmless:
 def __init__(self):
  self.members=['Fish','Birds']
  
 class Fish:
  def __init__(self):
   self.members=['Salmon','Tuna','Goldfish']
  
  def printMembers(self):
   print('Printing animals of the harmless Fish class')
   for member in self.members:
    print('\t%s ' % member)
    
 class Birds:
  def __init__(self):
   self.members=['Robin','Duck']
  
  def printMembers(self):
   print('Printing animals of the harmless Bird class')
   for member in self.members:
    print('\t%s ' % member)
  
 
