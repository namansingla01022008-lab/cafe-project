
print("Welcome to naman's cafe")
print("here's the menu:")
print("1.pizza: Rs 150\n" \
"2. Pasta: Rs 80\n" \
"3. Hot chocolate coffee: Rs 90\n" \
"4. Tea: Rs 20\n" \
"5. Burger: Rs 50\n" \
"6. Sandwich: Rs 30")
confirmation = input("please type 'yes' for placing further order and 'no' for final bill:")
sum = 0
finalsum = 0
while (confirmation == "yes"):
    order1 = int(input("enter the number from 1 to 6 corresponding to what you want to order:-"))
    if order1 == 1:
        print("your order is placed!!")
        sum += 150
    elif order1 == 2:
        print("your order is placed!!")
        sum += 80
    elif order1 == 3:
        print("your order is placed!!")
        sum+= 90
    elif order1 == 4:
        print("your order is placed!!")
        sum += 20
    elif order1 == 5:
        print("your order is placed!!")
        sum+= 50
    elif order1 == 6:
        print("your order is placed!!")
        sum += 30

    else:
        print("please visit any other branch for those orders!!") 
    finalsum = sum 
    confirmation = input("please type 'yes' for placing further order and 'no' for final bill:")
    if(confirmation == "no"):
        print("your final bill is:",finalsum)
    elif(confirmation != "yes"):
        print("sorry check your response and try again!!")



print("thankyou for coming!! please visit again")




