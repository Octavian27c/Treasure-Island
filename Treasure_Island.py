print('''
            .-._   _ _ _ _ _ _ _ _
 .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
'.___ '    .   .--_'-' '-' '-' _'-' '._
 V: V 'vv-'   '_   '.       .'  _..' '.'.
   '=.____.=_.--'   :_.__.__:_   '.   : :
           (((____.-'        '-.  /   : :
 snd                         (((-'\ .' /
                           _____..'  .'
                          '-._____.-'
                          
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("You're at a crossroad, where do you want to go? Type 'left' or 'right'.\n").lower()

if choice1 == "left":
  #continue the game.
  choice2 = input("You\'ve come to a lake. There is an island in the middle of the lake. Type \'wait' to wait for a boat. Type \'swim' to swim across.\n").lower()
  if choice2 =="wait":
     #continue the game.
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
    
else:
  print("You fell into a hole. Game Over.")