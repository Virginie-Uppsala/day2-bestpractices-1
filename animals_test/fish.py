class Fish:
 def __init__(self):
  self.members=['Salmon','Tuna','Goldfish','Jellyfish','Shark']
#  self.harmless=['Salmon','Tuna','Goldfish']
#  self.dangerous=['Jellyfish','Shark']
  
  
 def printMembers(self):
  print('Printing animals of the Fish class')
  for member in self.members:
   print('\t%s ' % member)
   
 def dangerous(self):
  print('Printing animals of the Fish class')
  for member in self.members:
   print('\t%s ' % member)
