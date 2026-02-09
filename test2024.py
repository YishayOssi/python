import random

# 1
# def randomNum():
#     listOfNum = []
#     for i in range(50):
#        num = random.randint(100,999)
#        listOfNum.append(num)
    
#     print(min(listOfNum))
    
# randomNum()


# 2
# def checkString():
#     bool = True
#     while(bool):
#       countA = 0
#       countDouble = 0
#       string = input("give me a string: ")

#       if string[0] == string[-1]:
#         bool = False

#       for str in string:
#          if str == "A":
#             countA+=1
#       print("Count of A:", countA)    
      
#       if len(string)%2 == 0:
#          countDouble+=1
#     print("Count of double string:", countDouble)


# checkString()

3
def is_balanced(arr):
   listEven = 0
   listOdd = 0
   for i, num in enumerate(arr):
      if i%2==0:
         listEven+=num
      else:
         listOdd+=num
   if listEven == listOdd:
      return True
   else:
      return False


listi = [12, 3, 7, 15, 5, 12, 6]
check_arr = is_balanced(listi)
print(check_arr)

def fill_return(size, x, y):
   if size > 2:
      listOfNum = []
      for i in range(size-1):
         num = random.randint(x,y)
         listOfNum.append(num)
         
      listEven = 0
      listOdd = 0
      for i, num in enumerate(listOfNum):
        if i%2==0:
          listEven+=num
        else:
          listOdd+=num
   print(listEven, listOdd)
      
fill_return(7,3,9)