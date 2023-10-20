# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 09:23:35 2023

@author: lena
"""

country_capitals = { "United States" : "Washington D.C.", "Italy" : "Rome", "England" : "London"}
print(country_capitals)
country_capitals["Italy"] = "Naples"
print(country_capitals)
country_capitals["Germany"] = "Berlin"
print(country_capitals)
del country_capitals["United States"]
print(country_capitals)
for country in country_capitals:
    print(country)
for country in country_capitals:
    capital = country_capitals[country]
    print(capital)
country_capitals.clear()
print(country_capitals)


my_dict = {1 : "Hello", (1,2) : "Hello Hi", 3 : [1, 2, 3]}
print(my_dict)

Dict = {}
print("Empty dictionnary : ")
print(Dict)

Dict = dict({1:'Geeks',2:'For',3:'Geeks'})
print(Dict)

Dict = dict([(1,'Geeks'),(2,'For')])
print(Dict)

Dict = {1: 'Geeks', 'abc': 'For', 3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
print(Dict)
print(Dict[1])
print(Dict['abc'])
print(Dict[3]['A'])


my_list ={1:"Hello","Hi":25,"Howdy":100}
print(1 in my_list)
print("Howdy" not in my_list)
print("Hello" in my_list)


dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}
print(dict1)

dict2 = dict1.copy()
print(dict2)

dict1.clear()
print(dict1)

print(dict2.get(1))


print(dict2.items())

print(dict2.keys())

dict2.pop(4)
print(dict2)

dict2.popitem()
print(dict2)

dict2.update({3:"Scala"})
print(dict2)

print(dict2.values())

cities = {'Paris', 'Athens', 'Madrid'}
continent = 'Europe'
my_dictionary = dict.fromkeys(cities, continent)
print(my_dictionary)

my_dictionary = dict.fromkeys(cities)
print(my_dictionary)

countries = {"France", "Greece", "Spain"}
my_dictionary = dict.fromkeys(cities,countries)
print(my_dictionary)

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
res_dict = dict(zip(keys,values))
print(res_dict)

dict1 = {"Ten" : 10, "Twenty" : 20, "Thirty" : 30}
dict2 = {"Thirty" : 30, "Fourty" : 40, "Fifty" : 50}
dict3 = {**dict1, **dict2}
print(dict3)
dict1.update(dict2)
print(dict1)

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict["class"]["student"]["marks"]["history"])

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developper', "salary": 8000}
dict1 = dict.fromkeys(employees, defaults)
print(dict1)

sample_dict = {
    'emp1' : {'name' : 'John', 'salary' : 7500},
    'emp2' : {'name' : 'Emma', 'salary' : 8000},
    'emp3' : {'name' : 'Brad', 'salary' : 500}
   }
sample_dict['emp3']['salary'] = 8500
print(sample_dict)



element_dictionnary = {
    "H": {"Element": "Hydrogen", "Atomic number": 1, "Melting point": 14, "Boiling point": 20},
    "He": {"Element": "Helium", "Atomic number": 2, "Melting point": 1, "Boiling point": 4},
    "Li": {"Element": "Lithium", "Atomic number": 3, "Melting point": 453, "Boiling point": 1603},
    "Be": {"Element": "Beryllium", "Atomic number": 4, "Melting point": 1560, "Boiling point": 2742},
    "B": {"Element": "Boron", "Atomic number": 5, "Melting point": 2349, "Boiling point": 4200},
    "C": {"Element": "Carbon", "Atomic number": 6, "Melting point": 3915, "Boiling point": 3915},
    "N": {"Element": "Nitrogen", "Atomic number": 7, "Melting point": 63, "Boiling point": 77},
    "O": {"Element": "Oxygen", "Atomic number": 8, "Melting point": 54, "Boiling point": 90},
    "F": {"Element": "Fluorine", "Atomic number": 9, "Melting point": 53, "Boiling point": 85},
    "Ne": {"Element": "Neon", "Atomic number": 10, "Melting point": 25, "Boiling point": 27},
}


def get_state(element_symbol, temperature):
    while element_symbol not in element_dictionnary:
        print(f"Element '{element_symbol}' not found in the dictionary.")
        element_symbol = input("Enter the symbol of the element : ")
        temperature = float(input("Enter the temperature of the element : "))
    element = element_dictionnary.get(element_symbol)
    element_name = element["Element"]
    atomic_number = element["Atomic number"]
    melting_point = element["Melting point"]
    boiling_point = element["Boiling point"]
    if temperature < melting_point:
        print(f"At {temperature} K, the element {element_name} of symbol {element_symbol} and atomic number {atomic_number} is a solid.")
    elif temperature >= boiling_point:
        print(f"At {temperature} K, the element {element_name} of symbol {element_symbol} and atomic number {atomic_number} is a gas.")
    else:
        print(f"At {temperature} K, the element {element_name} of symbol {element_symbol} and atomic number {atomic_number} is a liquid.")

        
element_symbol = input("Enter the symbol of the element : ")
temperature = float(input("Enter the temperature of the element : "))    
get_state(element_symbol, temperature)




interest_rates = {
    "ANZ": {"Years 1 & 2": 2.3, "Year 3 onwards": 4.1},
    "Bank of Australia": {"Years 1 & 2": 0.1, "Year 3 onwards": 5},
    "Commonwealth Bank": {"Years 1 & 2": 3.5, "Year 3 onwards": 3.8},
    "Westpac": {"Years 1 & 2": 3.7, "Year 3 onwards":3.7}
}

def calculate_mortgage(bank_name, P, n):
    payment = 0
    bank = interest_rates.get(bank_name)
    annual_rate_1 = bank["Years 1 & 2"]/100
    annual_rate_2 = bank["Year 3 onwards"]/100
    if n <= 24:
        r = annual_rate_1/12
        payment = P * (r * (1 + r) ** n)/(((1 + r) ** n) - 1)
        print("the monthly payment will be :" + str(payment))
    else:
        r1 = annual_rate_1/12
        payment1 = P * (r1 * (1 + r1) ** n)/(((1 + r1) ** n) - 1)
        r2 = annual_rate_2/12
        payment2 = P * (r2 * (1 + r2) ** n)/(((1 + r2) ** n) - 1)
        print("the monthly payment for the firt 24 months will be :" + str(payment1))
        print("the monthly payment for the remaining period will be  :" + str(payment2))


reply = "Y"
while reply.upper() == "Y":
    bank_name = input("Enter the name of the bank : ")
    while bank_name not in interest_rates:
        bank_name = input("bank not found. Enter the name of the bank : ")
    P = float(input("Enter the value of the principal (starting balance) of the loan : "))
    n = int(input("Enter the number of payments in total : "))  
    calculate_mortgage(bank_name, P, n)
    reply = input("Do you want to test another bank (Y/N) ?")    