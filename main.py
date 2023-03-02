import matplotlib.pyplot as plt
from countryinfo import CountryInfo

#I couldnt get packages to  work maybe add files or packages to github. 

# .title() allows for title case applied to string
c1 = input("Please enter a country's name: ").title()
c2 = input("Please enter another country's name: ").title()

c1.lower 
c2.lower
#Add this functioin to create a the input to lower case just incase the letters are cap or not

# Creates instance of CountryInfo module for specific country
country1 = CountryInfo(c1)
country2 = CountryInfo(c2)

# Calls API methods that requests country's population
try:
    data1 = country1.population()
except:
    print("First country name doesn't exist or contains a typo.")

try:
    data2 = country2.population()
except:
    print("Second country name doesn't exist or contains a typo.")

#I am unfimilar with the try and except commands...


# Create a Bar Chart
fig, ax = plt.subplots()
ax.bar([c1, c2], [data1, data2])

# Add labels and title
ax.set_xlabel('Country')
ax.set_ylabel('Population')
ax.set_title("Current population of " + c1+" and " + c2)

# Display the chart
plt.show()


#Put it in  a loop so when someone puts in the 
# wrong country it contniues or it asks you to chose another country.