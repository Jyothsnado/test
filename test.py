print("----------------MENU---------------")
print("press 1 to creat details of postal ")
print("press 2 to read details of postal ")
print("press 3 to update details of postal ")
print("press 4 to retrive particular record")
print("press 5 to delete details of postal ")
print("press 6 to exit")
class Postman:
            def getpostdetails(self):
                self.postid=int(input("Enter post ID: "))
                self.postname = input("Enter postname : ")
                self.pincode =int(input("Enter pincode : "))
            def printResult(self):
                print('post ID :' ,self.postid)
                print('post name: ',self.postname)
                print('pincode: ',self.pincode)
            def get_id(self):
                return self.postid
temp=[]
def find(val):
    for i in temp:
        if(i.get_id()==val):
            return i
def retirve():
    for i in temp:
        i.printResult()
def delete(val):
    for i in temp:
        if(i.get_id()==val):
            temp.remove(i)
def modify(val):
    print("----------------MENU---------------")
    print("1.postid")
    print("2.postaname")
    print("3.pincode")
    n=int(input("enter field id  to modify :"))
    for i in temp:
         if(i.get_id()==val):
            new=input("enter new value : ")
            if(n==1):
                i.postid=int(new)
            elif(n==2):
                i.postname=new
            else:
                i.pincode=int(new)
            break
for i in range (1,100):
    a=int(input("enter the choice:-"))
    S1=Postman()           
    if a==1:
        S1.getpostdetails()
        temp.append(S1)
    elif a==2:
            retirve()
    elif a==3:
        val=int(input("enter record id to modify :"))
        modify(val)
    elif a==4:
        val=int(input('enter record id : '))
        st=find(val)
        st.printResult()
    elif a==5:
        val=int(input("enter record id to delete :"))
        delete(val)
    else:
        break
