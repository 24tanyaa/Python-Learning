# example
#
indian=('samosa','daal','chawal')
chinese=('noodles','fried rice','dimsum')
italian=('pizza','pasta','lasagna')

dish=input("enter a dish name: ")

if dish in indian:
        print('indian')
elif dish in chinese:
        print('chinese')
elif dish in italian:
        print('italian')
else:
    print('based on little knowledge I have I dont know which cuisine', dish)



# EXERCISE 1.1
# Using following list of cities per country,
# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]
# Write a program that asks user to enter a city name and it should tell which country the city belongs to


india=["mumbai","banglore","chennai","delhi"]
pakistan=["lahore","karachi","islamabad"]
bangladesh=["dhaka","khulna","rangpur"]

city=input("Enter the city name: ")

if city in india:
    print('india')
elif city in pakistan:
    print('pakistan')
elif city in bangladesh:
    print('bangladesh')
else:
    print(" it does't belong to any of the listed countries","india,","pakistan,","bangladesh.")


# exercise 1.2
# Using following list of cities per country,
# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]
#
# Write a program that asks user to enter two cities and it tells you if they both are in same country
# or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but
# if I enter mumbai and dhaka it should print "They don't belong to same country"


india=["mumbai","banglore","chennai","delhi"]
pakistan=["lahore","karachi","islamabad"]
bangladesh=["dhaka","khulna","rangpur"]

city1=input("Enter the name of city1: ")
city2=input("Enter the name of city2: ")

if city1 in india and city2 in india:
    print('both cities are in india')
elif city1 in pakistan and city2 in pakistan:
    print('both cities are in pakistan')
elif city1 in bangladesh and city2 in bangladesh:
    print('both cities are in bangladesh')
else:
    print("they don't belong to same country.")



# exercise 2
# Write a python program that can tell you if your sugar is normal or not. Normal fasting levelsugar range is 80 to 100.
# Ask user to enter his fasting sugar level
# If it is below 80 to 100 range then print that sugar is low
# If it is above 100 then print that it is high otherwise print that it is normal

sugar=input('Enter the fasting sugar level: ')
sugar=int(sugar)

if sugar<80:
    print("your sugar level is low.")
elif sugar>100:
    print("your sugar level is high.")
else:
    print("your sugar level is normal.")