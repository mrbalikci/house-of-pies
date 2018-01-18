
# Part 1

# Created an order form that will display a list of pies to the user in the following way:

# 
# Welcome to the House of Pies! Here are our pies:
print("Welcome ot the House of Pies! Here are our pies")
# ---------------------------------------------------------------------
# (1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee,  (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek,  (9) Tamale, (10) Steak
# ```
pie_list = ['Pecan', 'Apple Crisp', 'Bean', 'Banoffee',  'Black Bun', 'Blueberry', 'Buko', 'Burek',  'Tamale', 'Steak']

for pie in pie_list:
    # print('[' + str(pie_list.index(pie)) + ']'+ pie)
    # or 
    print(f"[{pie_list.index(pie)}] {pie}")

# * Then prompt the user to select which pie they'd like to order via number.
shopping = 'y'
pie_cart = []

while shopping == 'y':
    pie_input = input("Which pie would you like to order? ")

    for pies in pie_input:
        pie_cart.append(pie_list[int(pies)])
        # print(pie_cart)

        print(f"Great! We'll have that {pie_cart} right out for you. ")

        shopping = input("Would you like to make another order? 'Yes' or 'No' ")

# Immediately after, follow the order with `Great! We'll have that <PIE NAME> right out for you.` and then ask if they would like to make another order. If so, repeat the process.

# Once the user is done purchasing pies, print the total number of pies ordered.


# Part 2

# Modify the application once again, this time conclude the user's purchases by listing out the total pie count broken by *each* pie.


# Create an order form that will display a list of pies to the user in the following way:

# ```
# Welcome to the House of Pies! Here are our pies:
print("Welcome ot the House of Pies! Here are our pies")
# ---------------------------------------------------------------------
# (1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee,  (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek,  (9) Tamale, (10) Steak
# ```
pie_list = ['Pecan', 'Apple Crisp', 'Bean', 'Banoffee',  'Black Bun', 'Blueberry', 'Buko', 'Burek',  'Tamale', 'Steak']

for pie in pie_list:
    # print('[' + str(pie_list.index(pie)) + ']'+ pie)
    # or 
    print(f"[{pie_list.index(pie)}] {pie}")

# Then prompt the user to select which pie they'd like to order via number.
shopping = 'y'
pie_cart = []

count = [0,0,0,0,0,0,0,0,0,0]

while shopping == 'y':
    pie_input = input("Which pie would you like to order? ")

    count[int(pie_input)-1] = count[int(pie_input)-1] + 1

    for pies in pie_input:
        pie_cart.append(pie_list[int(pies)])
        # print(pie_cart)

        print(f"Great! We'll have that {pie_cart} right out for you. ")

        print(f"[{count}] {pie_cart}")


        shopping = input("Would you like to make another order? 'Yes' or 'No' ")

        

# Immediately after, follow the order with `Great! We'll have that <PIE NAME> right out for you.` and then ask if they would like to make another order. If so, repeat the process.

# Once the user is done purchasing pies, print the total number of pies ordered.