"""print("Hello world")

print("Welcome to python programming")

#first variable

age = 23

car_brand = "Toyota"

university = "University of Nairobi"

AGE = 24
Age = 25

#The 3 ages(line 7,13&14) are different because of the case sensitivity of python

print(car_brand)
print(university)

#Arithmetic operators

#Addition operator is the symbol + in python

no_1 = 10
no_2 = 21
no_3 = "30"
no_4 = 40

first_summation = no_1 + no_2
print(first_summation)

print(no_1 + no_2 )

#print(no_3 + no_2)
print(type(no_3))
print(type(university)) #type is used to check the data type of the variable

no_5 = 10.5
print(type(no_1))
print(type(no_5))
datatype_bool = True

print(type(datatype_bool))

#subraction

#minus in python is represe`nted by the symbol -`

print(no_2 - no_1)

print(no_5 - no_1)

#multiplication operator is represented by the symbol *

print(no_1 * no_2)
print(no_1 * no_5)

#division operator is represented by the symbol /
 
print(no_2 / no_1)
print(no_5 / no_1)
print(no_4 / no_1)
print(no_5 / no_4)
print(no_4 / no_5)

#floor division operator is represented by the symbol //

print(no_4 // no_5)
print(no_5 // no_4)

#modulus operator is represented by the symbol %

print(no_4 % no_5)
print(no_5 % no_4)
print(7 / 2)
print(7 // 2)
print(7 % 2)

#exponentiation operator is represented by the symbol **
print(10**2)
print(2**10)
print(100 ** 0.5)
print(100 ** (1/3))"""
"""
parcels=["p001","p002","p003"]
print(parcels) #prints the list of parcels
parcels.append("p004") #adds p004 to the end of the list
print(parcels) #prints the list of parcels
parcels.insert(2,"p001B") #adds p001B at index 2
print(parcels) #prints the list of parcels
#parcels.remove("p002") #removes p002 from the list
print(parcels) #prints the list of parcels
parcels.sort() #sorts the list in alphabetical order
print(parcels) #prints the list of parcels
last = parcels.pop() #removes the last item from the list and stores it in the variable last
print(last) #prints the value of the variable last
print(len(parcels)) #prints the number of items in the list

#tuples are similar to lists but they are immutable, meaning they cannot be changed after they are created
capital_cities = ("New York", "Nairobi", "Dodoma", "Kampala", "Addis Ababa") #creates a tuple of capital cities
print(capital_cities) #prints the tuple of capital cities
print(len(capital_cities)) #prints the number of items in the tuple
print(capital_cities[0]) #prints the first item in the tuple
#print(capital_cities[9]) #prints the i
#capital_cities.append("Cairo") #this will raise an error because tuples are immutable

#sets are unordered collections of unique items

survey_A = {"Mombassa", "Nairobi", "Kisumu", "Nakuru", "Eldoret"} #creates a set of cities surveyed in survey A
survey_B = {"Nairobi", "Kisumu", "Nakuru", "Eldoret", "Thika"} #creates a set of cities surveyed in survey B

#union _all covered counties

print(survey_A|survey_B) #prints the union of survey A and survey B

#intersection _common counties

print(survey_A&survey_B) #prints the intersection of survey A and survey B

#difference _counties in survey A but not in survey B

print(survey_A-survey_B) #prints the difference of survey A and survey B

#.add() method adds an item to a set

survey_A.add("Thika") #adds Thika to survey A
print(survey_A) #prints the updated survey A

#dictionaries are collections of key-value pairs

student={"name": "Joy",
         "age":int(20),
         "course": "Computer Science",
         "year": 1,
         "nationality": "Kenyan"} #creates a dictionary of student information
print(student) #prints the dictionary of student information
print(student["name"]) #prints the value associated with the key "name" 


student_2={}
name_2=input("Enter your name:   ") #prompts the user to enter the name of the student and stores it in the variable name_2
student_2["name"]=name_2 #adds the key "name" and the value of name_2 to the student_2 dictionary
age_2=int(input("Enter your age:   ")) #prompts the user to enter the age of the student and stores it in the variable age_2
student_2["age"]=age_2 #adds the key "age" and the value of age_2 to the student_2 dictionary
course_2=input("Enter your course:   ") #prompts the user to enter the course of the student and stores it in the variable course_2
student_2["course"]=course_2 #adds the key "course" and the value   of course_2 to the student_2 dictionary
year_2=int(input("Enter your year of study:   ")) #prompts the user to enter the year of study of the student and stores it in the variable year_2
student_2["year"]=year_2 #adds the key "year" and the value of year_2 to the student_2 dictionary
nationality_2=input("Enter your nationality:  ")
student_2["nationality"]=nationality_2

print(student_2) #prints the student_2 dictionary
print(student.keys()) #returns a view object of the keys in the student dictionary
print(student.values()) #returns a view object of the values in the student dictionary
print(student.items()) #returns a view object of the key-value pairs in the student dictionary  
print(len(student)) #prints the number of key-value pairs in the student dictionary

#indexing and slicing 

fruits=["apple", "banana",  "mango", "pineapple"] #creates a list of fruits
print(fruits[0]) #prints the first item in the list
print(fruits[0:3]) #prints the first three items in the list
print(fruits[:3]) #prints the first three items in the list
print(fruits[-1]) #prints the last item in the list
print(fruits[1:3]) #prints the items at indices 1 and 2
print(fruits[1:]) #prints the items from index 1 to the end of the list
print(fruits[:2]) #prints every other item in the list starting from index 0
print(fruits[0:3:2]) #prints every other item in the list starting from index 0 to index 2
print(fruits[::-1]) #prints every other item in the list in reverse orders"""

"""bunches=(30)
cost_per_bunch=(25)
total_cost=bunches*cost_per_bunch
print(total_cost)
selling_price=(40)
total_revenue=bunches*selling_price
print(total_revenue)
profit=total_revenue-total_cost
print(profit)
profit_check=profit>300
print(bool(profit_check))

number=int(input("how many tomatoes did you buy?:  "))
price=int(input("what is the price per tomato?:  "))
total_cost=number*price
print("The total cost is:"  ,total_cost)

sacks=8
sacks_wieght="50"
print(type(sacks))
print(type(sacks_wieght))   
sacks_wieght=int(sacks_wieght)
total_wieght=sacks*sacks_wieght
print(total_wieght)
print(type(sacks_wieght))"""

#if-else statement

temperature=32
if temperature>30:
    print("It's a hot day!")
elif temperature>20: 
    print("Nice weather.")
else:
    print("It's a cold day!")  

temperature=int(input("Enter the temperature:  "))
if temperature>30:
    print("It's a hot day!") 
elif temperature>20:
    print("Nice weather.") 
else:
    print("It's a cold day!")


 

