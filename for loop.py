# example

# exp=[160,200,320,190,250]
# total=0
# for item in exp:
#     total=total+item
#     print(total)

# example
#
# for i in range(1,11):
#     print(i**3)


# exercise 1
# After flipping a coin 10 times you got this result,
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# Using for loop figure out how many times you got heads


result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count=0

for item in result:
    if item == "heads":
        count+=1
print("frequency of heads:", count)


# exercise 2
# Print square of all numbers between 1 to 10 except even numbers


for i in range(1,11):
    print(i**2)

# except even numbers

for i in range(1,11):
    if i%2==0:
        continue
    print(i**2)


# exercise 3
# Your monthly expense list (from Jan to May) looks like this,
# expense_list = [2340, 2500, 2100, 3100, 2980]
# Write a program that asks you to enter an expense amount and program should tell you in which month that expense
# occurred. If expense is not found then it should print that as well.


monthly_exp=[2340, 2500, 2100, 3100, 2980]
months=["january","february","march","april","may"]
exp=input("Enter an expense amount:")
exp=int(exp)

month=-1
for i in range(len(monthly_exp)):
    if exp == monthly_exp[i]:
        month = i
        break

if month != -1:
    print(f'You spent {exp} in {months[month]}')
else:
    print(f'You didn\'t spend {exp} in any month')


# exercise 4
# Lets say you are running a 5 km race. Write a program that,
#
# Upon completing each 1 km asks you "are you tired?"
# If you reply "yes" then it should break and print "you didn't finish the race"
# If you reply "no" then it should continue and ask "are you tired" on every km
# If you finish all 5 km then it should print congratulations message


for i in range(5):
    print(f"you ran {i + 1} miles")
    ask = input("are you tired? ")
    if ask == 'yes':
        break

if i == 4:
    print("Congratulations! you just completed the 5km race.")
else:
    print("You didn't finish 5 km race but hey congrats anyways! You still ran {i+1} miles")


# exercise 5
# Write a program that prints following shape
#
# *
# **
# ***
# ****
# *****

for i in range(1,6):
    s=''
    for j in range(i):
        s += '*'
    print(s)



