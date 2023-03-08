from contextlib import nullcontext
import tkinter as tk
import matplotlib.pyplot as plt
from countryinfo import CountryInfo
from matplotlib.widgets import Button
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sys

# Create the main window
root = tk.Tk()
root.title("Country Population")

# Create a label to prompt the user to input the first country
label1 = tk.Label(root, text="Enter a country's name:")
label1.pack()

# Create a text input field for the first country
input_box1 = tk.Entry(root)
input_box1.pack()

# Create a label to prompt the user to input the second country
label2 = tk.Label(root, text="Enter another country's name:")
label2.pack()

# Create a text input field for the second country
input_box2 = tk.Entry(root)
input_box2.pack()

c1=""
c2=""
data1=0
data2=0

def closeButton():
    root.destroy()
    sys.exit(0)

# Display the chart
def countryChart():
    plot_frame = tk.Frame(root)
    plot_frame.pack()
    fig, ax = plt.subplots()
    ax.bar([c1, c2], [data1, data2])
    # Add labels and title
    ax.set_xlabel('Country')
    ax.set_ylabel('Population')    
    ax.set_title("Current population of " + c1 + " and " + c2)
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()
    seeGraph.destroy()
    close_button = tk.Button(root, text="Close", command=closeButton)
    close_button.pack()
    

# Create a function to get the user's input and display the chart
def display_chart1():
     # Get the user's input for the first country
    global c1
    c1 = input_box1.get().title()
    # Creates instance of CountryInfo module for specific country
    country1 = CountryInfo(c1)

    # Calls API methods that requests country's population
    try:
        global data1
        data1 = country1.population()
    except:
        # Display an error message if the first country is not valid
        error_label = tk.Label(root, text="Error: First country name doesn't exist or contains a typo!", fg="red")
        error_label.pack()
        # Make the error label disappear after 3 seconds
        root.after(3000, error_label.destroy)
        return
    
    # Get the user's input for the second country
    global c2
    c2 = input_box2.get().title()

    # Creates instance of CountryInfo module for specific country
    country2 = CountryInfo(c2)

    # Calls API methods that requests country's population
    try:
        global data2
        data2 = country2.population()
    except:
        # Display an error message if the second country is not valid
        error_label = tk.Label(root, text="Error: Second country name doesn't exist or contains a typo!", fg="red")
        error_label.pack()
        # Make the error label disappear after 3 seconds
        root.after(3000, error_label.destroy)
        return
    
    if data2 and data1 != None:
        submit_button2.destroy()
        seeGraph.pack()

seeGraph = tk.Button(root, text="See Graph", command=countryChart)
submit_button2 = tk.Button(root, text="Submit", command=display_chart1)
submit_button2.pack()

root.mainloop()
