#DOC 333 Course work
import random
import sys
import os

#creating variables

color_num=[]
color_num=random.randrange(1,7)

guess_limit=8
attempt=guess_limit
color_num1=random.randrange(1,7)
color_num2=random.randrange(1,7)
color_num3=random.randrange(1,7)
color_num4=random.randrange(1,7)

print("////////////////////GAMEINT//////////////////")
print("")
start=input("would you like to start this game:[yes/no]\n")
if start=="yes" :
 name=input("Enter your name")

 print("")
 print('           '"Hi",name,'  '"Welcome to GAMEINT")
 print("")
 print("MENU")
 print("colour mapping")
 print("1-White, 2-Blue, 3-Red, 4-Yellow, 5-Green, 6-Purple")
 print("The guessed color is not in the correct place =0")
 print("The guessed color is in the correct place =1")
 print("The guessed color is wrong and not in the correct place='-'")
 keep_playing="true"
 re=[]
 while keep_playing=="true":
     
     guess1 = input("guess the first number")
     guess2 = input("guess the second number")
     guess3 = input("guess the third number")
     guess4 = input("guess the fourth number")
     guess1 = int(guess1)
     guess2 = int(guess2)
     guess3 = int(guess3)
     guess4 = int(guess4)
     guess_limit=guess_limit-1
     
     if guess1 == color_num1:
        re.append('1')
        guess2 == color_num2
        re.append('1')
        guess3 == color_num3
        re.append('1')
        guess4 == color_num4
        re.append('1')
        print("yes! you won")
        keep_playing="false"
        os.system('cls')
        print("  attempt                      guess                      result              {attempt}          {guess}                 {re[0]},{re[1]},{re[2]},{re[3]}")
        print("----------------------------------------------------------------------")
        print("/ncongtatz you win")
        print("ypur score{score}% points")
     
     else:
         guess1 != color_num1
         re.append('0')
         guess2 != color_num2
         re.append('0')
         guess3 != color_num3
         re.append('0')
         guess4 != color_num4
         re.append('0')
         print("try again")


     if guess_limit == 0:
            print ("You are out of tries! ")
            sys.exit()
            
            

     



