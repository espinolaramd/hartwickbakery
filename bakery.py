#Diego Espinola
#10.14.19
# project for Thursday

cookies = []
candy = []

def cookie_input():
    for i in range(0,6):
        cookies.append(int(input(">")))

def candy_input():
    for i in range (0,6):
        candy.append(int(input(">")))

def average_sales1():
    return print(f"\nYour average monthly  sales of cookies is: {total1/6}")

def average_sales2():
    return print(f"\nYour average monthly  sales of candy is {total2/6}")

def maximum_cookies():
    return print(f"The maximum of cookies is:{max(cookies)}")

def maximum_candy():
    return print(f"The maximum of cookies is:{max(candy)}")



print("Type your sales of cookies from the last 6 months")
cookie_input()
total1 = int(sum(cookies))
average_sales1()
maximum_cookies()

print("Type your sales of candy from the last 6 months")
candy_input()
total2= int(sum(candy))
average_sales2()
maximum_candy()

print("\nCandy is more popular at the bakery")

