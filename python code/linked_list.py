#creating class node 

class Node:
    def __init__(self, item=None , next=None): 
        self.item=item 
        self.next= next 




# creating linkded list 
class SLL : 
    def __init__(self,start=None):
        self.start=start

 # checking list is empty or not 
    def is_empty(self):
        return self.start==None

# insert element in list first node 
    def insert_start(self, data):
        
        n=Node(data,self.start)
        self.start=n
    # insert element in last node 
    def insert_last(self,data):
        n=Node(data)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
                
            temp.next=n
        else:
            self.start=n
     # serach element in linked list        
    def search(self, data):
            temp=self.start
            while temp is not None:
                if temp.item ==data:
                    return temp
                temp=temp.next
            return None 
      # insert element after    
    def insert_after(self,temp,data):
            if temp is not None:
                n=Node(data,temp.next)
                temp.next=n
                
    def list_show(self):
            temp=self.start
            while temp is not None:
                print(temp.item , end=' ')
                temp=temp.next
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
        
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next = None 
    def delete_data(self, data):
        if self.start in None:
            pass 
        elif self.start.next is None:
            if self.start.item==data:
                self.start=None 
        else:
            temp=self.start
            if temp.item==data:
                self.start=temp.next
            else:
                while temp.next is not None:
                    if temp.next.item==data:
                        temp.next-temp.next.next
                        break
                    temp=temp.next
    def __iter__(self):
        return SSLIter(self.start)

class SSLIter:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self): 
        if not self.current:
             raise StopIteration         
        data=self.current.item
        self.current=self.current.next
        return data     
            
 
# drive code 
mylist =SLL()
mylist.insert_start(20)
mylist.insert_start(10)
mylist.insert_last(25)
mylist.insert_after(mylist.search(20),35)

mylist.list_show()      


            
         
        

 
        

