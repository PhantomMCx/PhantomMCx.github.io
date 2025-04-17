#Let's start a coffee shop together!! We're going to build a coffee shop using some new Python Programming concepts!!

#Let's build a robot Barista!!

print("Hello, welcome to vvi_ny Coffee!!!!!!!!!!!!!")

name = input("May I start off with your name please?\n")

if name == "Amy" or name == "Khanh":
  evil_status = input("Are you evil?\n")
  good_deeds = int(input("How many good deeds have you done today?\n"))
  if evil_status == "Yes" and good_deeds < 4:
    print("You are not welcome here " + name + "!! Get out of my shop!!")
    exit()
  else:
    print("Oh, I am so sorry for the misunderstanding. Come on in!!\n\n\n")
else:
  print("Hello "+ name + ", thank you so much for coming in today!!!\n\n\n")

#Coffee Menu
menu = "Americano, Espresso, Matcha Latte, Cappucino, Frappuccino"

order_1 = input(name + ", what would you like from our menu today?\n" "Here is what we are serving.\n" + menu + "\n" + "Also, today's special is Dirty Matcha.\n")

#Prices for each coffee
if order_1 == "Frappuccino":
  price = 7.99
elif order_1 == "Americano":
  price = 3.99
elif order_1 == "Espresso":
  price = 3.99
elif order_1 == "Matcha Latte":
  price = 6.99
elif order_1 == "Cappucino":
  price = 5.99
elif order_1 == "Dirty Matcha":
  price = 5
else:
  order_1 = input("Sorry, we don't have that here. Anything else from the menu?\n")

if order_1 == "Frappuccino":
  price = 7.99
elif order_1 == "Americano":
  price = 3.99
elif order_1 == "Espresso":
  price = 3.99
elif order_1 == "Matcha Latte":
  price = 6.99
elif order_1 == "Cappucino":
  price = 5.99
elif order_1 == "Dirty Matcha":
  price = 5

#Create a variable name "price"
#Program barista to ask how many coffees they would like
#Program barista to give total

quantity_1 = input("\n\n\nHow many coffees would you like?\n")

total = price * float(quantity_1)

more = input("Anything else?\n")

#If customer wants more items
if more == "Yes":
  order_2 = input("What else would you like?\n")
  
  if order_2 == "Frappuccino":
    price = 7.99
  elif order_2 == "Americano":
    price = 3.99
  elif order_2 == "Espresso":
    price = 3.99
  elif order_2 == "Matcha Latte":
    price = 6.99
  elif order_2 == "Cappucino":
    price = 5.99
  elif order_2 == "Dirty Matcha":
    price = 5

  quantity_2 = input("How many coffees would you like?\n")

  total += price * float(quantity_2)

  input("\n\n\nSounds good " + name + "\nYour total is: $" + str(round(total,2)) + "\nWould that be cash or card?\n")

  print("\n\n\nGreat! Your " + quantity_1 + " " + order_1 + " and " + quantity_2 + " " + order_2 + " will be ready for you in a moment.\n" "Please wait on the side until I call your name.\n" "Thank you!")
else:
  input("\n\n\nSounds good " + name + "\nYour total is: $" + str(round(total,2)) + "\nWould that be cash or card?\n")

  print("\n\n\nGreat! Your " + quantity_1 + " " + order_1 + " will be ready for you in a moment.\n" "Please wait on the side until I call your name.\n" "Thank you!")