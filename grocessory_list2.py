#Qn.2 Edit the program created in Q1 to allow the user to specify the quantity of each item required.

import sys

def Menu():
     while True:
               
          print()
          print('''  ### SHOPPING LIST ###

          Select a number for action that you would like to do:

          1.Specify the quantity of each item required 
          2.exit
          '''
          )
          selection= input("Make your selection :")

          if selection=="1":
               quantity_req()
          elif selection=="2":
               sys.exit()

          else:
               print("You didnot make a valid selection")


def quantity_req():
     shoplist={}
     n=int(input("Number of products to be purchased :"))

     for i in range(n):
          item=input("item name:")
          quantity=input("quantity of an item:")
          print(f"{item}  of qunatity  {quantity} has beeen assigned for shopping list")
          shoplist.update({item:quantity})
          print(shoplist)


Menu()
