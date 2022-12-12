#Qn.1 Create a program to produce a supermarket shopping list.
# The list should be saved to a pickled file so that it can be amended later.
# Create a menu to allow users to add items, delete items and view the whole list.



#Creating a program to produce a supermarket shopping list
import sys
import pickle

print("Welcome to shoplist.py, your favourite shopping list application")
shoplist=[]
add = input("Want to add something to your shopping list?Y or N?")
while add.lower() =="y":
     item= input("Enter your item to the list:")
     shoplist.append(item)
     add=input("Want to add to your shopping list? Y or N?")

     print()
     print("Here is your alphabetical shopping list.")
     shoplist.sort()
     for listitem in shoplist:
          print(listitem)
    
#Saving the list to pickled file


pickle_out=open("mydata.pkl","wb")
pickle.dump(shoplist,pickle_out)
pickle_out.close()

#Creating a menu to allow users to add items, delete items and view the whole list.

def Menu():
     while True:
               
          print()
          print('''  ### SHOPPING LIST ###

          Select a number for action that you would like to do:

          1. View shopping list
          2.Add item to shopping list
          3.Remove item from the shopping list
          4.exit
          '''
          )
          selection= input("Make your selection :")

          if selection=="1":
               view_list()

          elif selection=="2":
               add_item()

          elif selection=="3":
               delete_item()


          elif selection=="4":
               sys.exit()

          else:
               print("You didnot make a valid selection")

def view_list():
     print()
     print("*** SHOPPING LIST ***")
     for i in shoplist:
          print("* "+i)

def add_item():
     item= input("Enter the item you want to add to the shopping list :")
     shoplist.append(item)
     print(item + "  has beeen added to shopping list ")
     shoplist.sort()
     print(shoplist)

def delete_item():
     item= input("Enter the item you want to remove from the shopping list :")
     shoplist.remove(item)
     print(item + "  has beeen removed from the shopping list ")
     print(shoplist)

Menu()