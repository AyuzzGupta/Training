import ctypes#List khud se banane ke liye 
class FirstList:
    def __init__(self):#cunstructor
        self.size=1
        self.n=0
        self.A=self.__make_array(self.size)
    def __make_array(self,capacity):
        return(capacity*ctypes.py_object)()
    def __str__(self):
        result=''
        for i in range(self.n):
            result +=str(self.A[i])+','
        return ('['+result[:-1]+']')
    def append(self,item):
        if self.n==self.size:
            self.resize(2*self.size)#naya array bada size aur purane element copy kardiya aur nam purana kardiya 
        self.A[self.n]=item#last mein insert karta hai
        self.n +=1
    def resize(self,new_capacity):
        B=self.__make_array(new_capacity)
        self.size=new_capacity
        for i in range (self.n):
            B[i]=self.A[i]
        self.A=B
    def pop(self):
        if self.n==0:
            return "Empty"
        print(self.A[self.n-1])
        self.n-=1
    def insert(self,index,item):
        if self.n==self.size:
            self.resize(2*self.size)
        for i in range(self.n, index, -1):
            self.A[i] = self.A[i - 1]
        self.A[index] = item

        self.n += 1  
    def cleariing(self):
        self.size = 1
        self.n = 0  
    def finding(self,item):
        for i in range(self.n):
            if(self.A[i]==item):
                return i
        return ValueError
    def __len__(self):
        return self.n
    def __getitem__(self, index):
        if 0<=index<self.n:
            return self.A[index]
        else:
            raise IndexError('Index Aukat ke bahar hai ')
    
l=FirstList()
l.append(1)
l.append("Ele")
print(l)