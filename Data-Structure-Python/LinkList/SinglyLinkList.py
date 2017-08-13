######### Created By ##########
#                             #
#           Md Hasan          #
#                             #
######### Doubly LinkList #####

class Node:
    def __init__(self,value):
        self.value = value
        self.next = next

class Linklist:

######### Create Head Node ##########
    def __init__(self):
        self.head =None

######### Add at the front of the link list ##########
    def addToFront(self,value):

        temp = Node(value)
        temp.next=self.head
        self.head=temp

    def addToLast(self,value):
        temp = Node(value)
        temp.next = None
        if self.head==None:
            self.head=temp
        else:
            current=self.head
            while (current.next != None):
                current = current.next

            current.next=temp

    def Display(self):
        temp = self.head
        while(temp != None):
            print(temp.value)
            temp=temp.next


if __name__=="__main__":

    list = Linklist()

    n = int(input("how much value you want to add?"))
    for i in range(n):
        k=int(input(">> "))
        list.addToLast(k)
    list.Display()




