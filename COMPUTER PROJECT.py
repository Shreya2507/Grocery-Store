import pickle
import os

def create_rec():
    f=open("Grocery items.dat","wb")
    ftxt=open("Snum.txt","w")
    ftxt.write('0')
    ftxt.close()
    snum=0
    while True:
        d={}
        snum+=1
        l=[]
        item_name=input("enter name of item: ")
        l.append(item_name)
        quantity=int(input("enter quantity: "))
        l.append(quantity)
        price=int(input("enter price: "))
        l.append(price)
        d[snum]=l
        print(d)
        pickle.dump(d,f)
        ch=input("do you want to enter more records(y/n): ")
        if ch=='n' or ch=='N':
            break
    f.close()
    ftxt=open("Snum.txt","w")
    ftxt.write(str(snum))
    ftxt.close()
    print()

def delete_name_rec():
    f1=open("student.dat","rb")
    f2=open("temp.dat","wb")
    nm=input("enter name no to delete")
    flag=0
    try:
        while True:
            d=pickle.load(f1)
            for i in d:
                x_name,y_phno=d[i]
                if x_name.lower()==nm.lower():
                    flag=1
                else:
                    pickle.dump(d,f2)
    except EOFError:
        if flag==0: 
            print("sorry name to delete was not there")
        else:
            print("deleted record")
    finally:
        f1.close()
        f2.close()
    os.remove("student.dat")
    os.rename("temp.dat","student.dat")
    print()

    
def append_rec():
    f=open("Grocery items.dat","ab")
    ftxt=open("Snum.txt","r+")
    snum=int(ftxt.read())
    
    while True:
        d={}
        snum+=1
        l=[]
        item_name=input("enter name of item: ")
        l.append(item_name)
        quantity=int(input("enter quantity: "))
        l.append(quantity)
        price=int(input("enter price: "))
        l.append(price)
        d[snum]=l
        print(d)
        pickle.dump(d,f)
        ch=input("do you want to enter more records(y/n): ")
        if ch=='n' or ch=='N':
            break
    f.close()
    ftxt.seek(0)
    ftxt.write(str(snum))
    ftxt.close()
    print()


def display_all_rec():
    f=open("Grocery items.dat","rb")
    try:
        while True:
            d=pickle.load(f)
            a=list(d.keys())
            print("Serial no. is",a[0],"Item Name is",d[a[0]][0],"Quantity is",d[a[0]][1],"Price is",d[a[0]][2])            
    except EOFError:
            pass
    finally:
            f.close()
    print()



def delete_snum_rec():
    f1=open("Grocery items.dat","rb")
    f2=open("temp.dat","wb")
    snum=int(input("Enter serial no. to delete : "))
    flag=0
    try:
        while True:
            d=pickle.load(f1)
            for i in d:
                if i==snum:
                        flag=1
                else:
                        pickle.dump(d,f2)#not matching record
    except EOFError:
            if flag==0:
                print("sorry serial no. to delete was not found")
    finally:
            f1.close()
            f2.close()
    os.remove("Grocery items.dat")
    os.rename("temp.dat","Grocery items.dat")
    print()


def delete_itemname_rec():
    f1=open("Grocery items.dat","rb")
    f2=open("temp.dat","wb")
    nm=input("enter Item name to delete")
    flag=0
    try:
        while True:
            d=pickle.load(f1)
            for i in d:
                x_name,y_quant,z_price=d[i]
                if x_name.lower()==nm.lower():
                    flag=1
                else:
                    pickle.dump(d,f2)
    except EOFError:
        if flag==0: 
            print("sorry Item name to delete was not found")
        else:
            print("deleted record")
    finally:
        f1.close()
        f2.close()
    os.remove("Grocery items.dat")
    os.rename("temp.dat","Grocery items.dat")
    print()



def modify_name_rec():
    f1=open("Grocery items.dat","rb")
    f2=open("temp.dat","wb")
    snum=int(input("enter serial number to search: "))
    nm=input("enter new item name: ")
    flag=0
    try:
        while True:
            d=pickle.load(f1)
            if snum in d:
                d[snum][0]=nm #update name in dictionary
                flag=1
                pickle.dump(d,f2)
            else:
                    pickle.dump(d,f2)
            print(d)
    except EOFError:
        if flag==0:
            print("sorry serial number whose name had to be changed was not found")
    finally:
        f1.close()
        f2.close()
    os.remove("Grocery items.dat")
    os.rename("temp.dat","Grocery items.dat")
    print()

def modify_quantity_rec():
    f1=open("Grocery items.dat","rb")
    f2=open("temp.dat","wb")
    snum=int(input("enter serial number to search: "))
    qt=input("enter new quantity: ")
    flag=0
    try:
        while True:
            d=pickle.load(f1)
            if snum in d:
                d[snum][2]=qt #update name in dictionary
                flag=1
                pickle.dump(d,f2)
            else:
                    pickle.dump(d,f2)
            print(d)
    except EOFError:
        if flag==0: print("sorry serial number whose quantity had to be changed was not found")
    finally:
        f1.close()
        f2.close()
    os.remove("Grocery items.dat")
    os.rename("temp.dat","Grocery items.dat")
    print()

def modify_price_rec():
    f1=open("Grocery items.dat","rb")
    f2=open("temp.dat","wb")
    snum=int(input("enter serial number to search: "))
    price=input("enter new price: ")
    flag=0
    try:
        while True:
            d=pickle.load(f1)
            if snum in d:
                d[snum][2]=price #update name in dictionary
                flag=1
                pickle.dump(d,f2)
            else:
                    pickle.dump(d,f2)
            print(d)
    except EOFError:
        if flag==0: print("sorry serial number whose price had to be changed was not found")
    finally:
        f1.close()
        f2.close()
    os.remove("Grocery items.dat")
    os.rename("temp.dat","Grocery items.dat")
    print()


def search_rec():
    if not os.path.isfile("Grocery items.dat"): #checking whether file exists or not
        print("sorry file not found")
    else:
        f=open("Grocery items.dat","rb")
        nm=input("enter item name")
        flag=0
        try:
            while True:
                d=pickle.load(f)
                for i in d:
                    if d[i][0]==nm:
                        flag=1
                        print("serial number is",i)
                        print("The item name is",d[i][0])
                        print("The quantity is",d[i][1])
                        print("The price is",d[i][2])
                
        except EOFError:
            if flag==0:
                print("sorry item not found in the database")
        finally:f.close()
        print()



def main():
    while True:
        print(" 1.Create\n 2.Append records\n 3.Display records\n 4.Delete by serial number")
        print(" 5.Delete by item name\n 6.Modify item name\n 7.Modify quantity\n 8.Modify price")
        print(" 9.search by item\n 10.Exit")
        ch=input("enter ur choice")
        if ch=='1':create_rec()
        elif ch=='2':append_rec()
        elif ch=='3':display_all_rec()
        elif ch=='4':delete_snum_rec()
        elif ch=='5':delete_itemname_rec()
        elif ch=='6':modify_name_rec()
        elif ch=='7':modify_quantity_rec()
        elif ch=='8':modify_price_rec()
        elif ch=='9':search_rec()
        elif ch=='10':break
        else:
            print("invalid choice")
        print()
           
main()
