''' TOday I am going to rool the dice
 firstly for the dice symbols we need to have get the symbols

 print this line and the symbols will appear 
 the line "print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")"
'''
import random
'''print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")''' # ● ┌ ─ ┐ │ └ ┘
choice = {
  1: ("┌───────────┐" ,
      "│           │", 
      "│     ●     │",
      "│           │",
      "└───────────┘"),

  2: ("┌───────────┐",
      "│       ●   │", 
      "│           │",
      "│  ●        │",
      "└───────────┘") ,

  3: ("┌───────────┐",
      "│        ●  │", 
      "│     ●     │",
      "│ ●         │",
      "└───────────┘") ,

  4: ("┌───────────┐",
      "│  ●     ●  │", 
      "│           │",
      "│  ●     ●  │",
      "└───────────┘") ,

  5: ("┌───────────┐",
      "│  ●     ●  │", 
      "│     ●     │",
      "│  ●     ●  │",
      "└───────────┘") ,

  6: ("┌───────────┐",
      "│  ●     ●  │", 
      "│  ●     ●  │",
      "│  ●     ●  │",
      "└───────────┘") ,

 }
print('You rolled!')
for line in choice.get(random.randint(1,6)):
    print(line)
