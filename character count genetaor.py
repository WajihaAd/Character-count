# Character count Generator:
def checker(sent):
  list1=set()
  sent=sent.lower()
  for value in sent:
    if value !=' ' and value not in list1:
      j=sent.count(value.lower())
      print("The letter",value,"is repeated",j,"times")
      list1.add(value) 
      
sent=input("Enter a sentences: ") 

checker(sent)

