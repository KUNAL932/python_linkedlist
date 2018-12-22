Python 3.5.2 (default, Nov 12 2018, 13:43:14) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
class Node:
	def __init__(self,dataval=None):
		self.dataval=dataval
		self.nextval=None

		
>>> class SLinkedList:
	def __init__(self):
		self.headval=None
	def listprint(self):
		printval=self.headval
		while printval is not None:
			print(printval.dataval)
			printval=printval.nextval

			
>>> list=SLinkedList()
>>> list.headval=Node("MON")
>>> e2=Node('TUESDAY')
>>> e3=Node('WEDNESDAY')
>>> 
>>> list.headval.nextval=e2
>>> e2.nextval=e3
>>> list.listprint()
MON
TUESDAY
WEDNESDAY
>>> 
