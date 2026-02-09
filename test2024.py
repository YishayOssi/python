import random

# 1
# def randomNum():
#     listOfNum = []
#     for i in range(50):
#        num = random.randint(100,999)
#        listOfNum.append(num)
    
#     print(min(listOfNum))
    
# randomNum()


2
def checkString():
    bool = True
    while(bool):
      countA = 0
      countDouble = 0
      string = input("give me a string: ")

      if string[0] == string[-1]:
        bool = False

      for str in string:
         if str == "A":
            countA+=1
      print("Count of A:", countA)    
      
      if len(string)%2 == 0:
         countDouble+=1
    print("Count of double string:", countDouble)


checkString()

