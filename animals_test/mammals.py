class Mammals:
 def __init__(self):
  self.members=['Tiger','Elephant','Wild Cat']
  
  
 def printMembers(self):
  print('Printing animals of the Mammals class')
  for member in self.members:
   print('\t%s ' % member)
