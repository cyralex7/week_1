##### ASSIGNMENT STARTS HERE #####


#%%
# First Assignment
'''
1: Please create a program which inputs two years and outputs the years as well as the difference
between them!

Your output should look like:

Year 1: 2025
Year 2: 2028
Difference: 3
'''

def yearDifference():
    year1 = int(input('Please enter a year: '))
    year2 = int(input('Please enter another year: '))
    difference = abs(year2 - year1)
    print("Year 1:", year1)
    print("Year 2:", year2)
    print("Difference:", difference)

yearDifference()

#%%
# Second Assignment

'''
2: Please create a program which collects an input as fahrenheit and outputs the 
temperature in celsius

Your output should look like:

Fahrenheit: 25
Celsius: -3.89
'''
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * (5 / 9)
print("Fahrenheit:", fahrenheit)
print("Celsius:", round(celsius, 2))

#%%
# Third Assignment

'''

3: Please create a program which collects an input as US Dollars and converts the output to Euros 
given the exchange rate on 1/19/25 as 1 USD = 0.97 Euro

Your output should look like:
USD: 1
EU: 0.97

'''

def convert():
    dollars = float(input("Enter amount in US Dollars: "))
    euros = dollars * .98
    print("USD:", dollars)
    print("EU:", euros, 2)
convert()

##### ASSIGNMENT ENDS HERE #####
