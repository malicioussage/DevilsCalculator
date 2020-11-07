import shutil
import time

def Devil():
  print(""" 
            ^         ^
           ( (_______) )            
           [ <->   <-> ]
            \         /  
             \   V   /
              \  _  /
               \   /
                 V
                              """) 
  print("HELL AWAITS!!!!")
      
def add():
  num1 = int(input("Enter a number: "))
  num2 = int(input("Enter another number: "))
  num3 = num1 + num2
  print(num3)
  if num3 == 666:
    Devil()
    
    #shutil.rmtree(path, ignore_errors=False, onerror=None)
    
  else:
    main()

def subtract():
  num1 = int(input("Enter a number: "))
  num2 = int(input("Enter another number: "))
  num3 = print(num1 - num2)
  if num3 == 666:
    Devil()
    
    #shutil.rmtree(path, ignore_errors=False, onerror=None)
    
  else:
    main()


def divide():
  num1 = int(input("Enter a number: "))
  num2 = int(input("Enter another number: "))
  num3 = print(num1 / num2)
  if num3 == 666:
    Devil()
    
    #shutil.rmtree(path, ignore_errors=False, onerror=None)
    
  else:
    main()


def multiply():
  num1 = int(input("Enter a number: "))
  num2 = int(input("Enter another number: "))
  num3 = print(num1 * num2)
  if num3 == 666:
    Devil()
    
    #shutil.rmtree(path, ignore_errors=False, onerror=None)
    
  else:
    main()




  
def main():
  print("Options")
  print("[1] addition")
  print("[2] subtraction")
  print("[3] division")
  print("[4] multiplication")
  option = int(input("select option: "))
  
  if option == 1:
    add()
  elif option == 2:
    subtract()
  elif option == 3:
    divide()
  elif option == 4:
    multiply()
  else:
    quit()
    
    
main() 
