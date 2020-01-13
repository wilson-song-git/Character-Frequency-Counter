#Wilson Song
#afternoon1
#23466407

#notes:
#add the try to the entry - done
#add the if n>54 do something about it - done
#the rest of numbers probability is not working - done - working
#white spaces
#all special characters must be in 1

##=non-working code

"""
could not get the program to work correctly with whitespaces and putting all special characters into 1
program will have a different probability for each special character
white spaces such as \n and \t and " " are represented as nothing in the piechart when it is being labeled
everything else is working as expected
"""


from tkinter import*
from turtle import Turtle,Screen #importing turtle module
from itertools import cycle

master=Tk()
master.title('Frequent Letters Program')#name the gui
Label(master, text='Number of Letters:').grid(row=0)
e1=Entry(master)
e1.grid(row=0,column=1)

#
##each_letter.isalpha() or each_letter=='' or each_letter=='\n' or each_letter=='\t') and each_letter not in existing_letters
#opens a file but used a specific path where the words.txt is on the desktop
file = open('/Users/wilsong/Desktop/Words.txt', 'r')
existing_letters = {} #dictionary to hold existing letters and their number of occurences
the_frequent_characters = []#list to hold the n most frequent letters - need a loop to extract the max
for line in file:  # iterating through each line in file
    for each_letter in line:  # iterating through each character in line
       ## if (each_letter=='\n' or each_letter=='\t' or each_letter==' ') and each_letter in existing_letters:
        ##    if each_letter==' ':
         ##       existing_letters['Space']+=1
          ##  else:
           ##     existing_letters[each_letter]+=1
        ##elif(each_letter == '\n' or each_letter == '\t' or each_letter == ' ') and each_letter not in existing_letters:
         ##   if each_letter=='\n':
          ##      existing_letters={'\n':1}
           ## elif each_letter=='\t':
            ##    existing_letters={'\t':1}
            ##elif each_letter==' ':
             ##   existing_letters={'Space':1}
        if each_letter in existing_letters:  # if character is already in dictionary
            existing_letters[each_letter] += 1 #if the current letter already exist in the dictionary then add 1
        elif each_letter not in existing_letters:
            existing_letters[each_letter] = 1 #if the current letter does not exist in the dictionary then set it = to 1 to start
        ##elif each_letter in existing_letters:  # if character is already in dictionary
         ##   existing_letters['Special'] += 1
        ##elif each_letter not in existing_letters:  # if character is already in dictionary
           ## existing_letters['Special'] += 1

file.close()

def callback(user_inputed_entry):
    #use a try and accept to make sure we take in an integer or just destroy program
    string_entry = user_inputed_entry.get()
    try:
        n = int(string_entry)#n is the number that the user entered for the n most frequent numbers
    except ValueError:
        print("Please only enter a integer value!")
        master.destroy()
    except:
        print("Something has gone wrong1")
        master.destroy()

    if n>54:
        print("Entered value is too large (greater than 54)")
        master.destroy()

    print('You have selected to draw a pie chart of the',n,'most frequent letters')

    for i in range(0, n):  # iterating loop n times to find n most frequent numbers
        current_max = -1  # max
        for j in existing_letters:  # iterating through each key in dictionary
            if (existing_letters[j] > current_max and j not in the_frequent_characters):  # if value of the key is greater than max and is not already in the_max_character list
                temp = j
                current_max = existing_letters[j]
        the_frequent_characters.append(temp)  # adding key to list

    total_of_all_characters=0
    for i in existing_letters:
        total_of_all_characters+=existing_letters[i]

    total_of_frequent = 0
    for i in the_frequent_characters:
        total_of_frequent += existing_letters[i]  # counting total

    rest_of_characters=total_of_all_characters-total_of_frequent

    radius = 200  # radius of pie chart
    label_radius = radius*1.13 # radius of labels

    col = cycle(['green', 'red', 'white', 'blue', 'yellow', 'pink','orange','brown'])  # color cycle
    turtle_object = Turtle()  # object

    #change turtle speed based on the amount of frequent letters chosen
    if n>25:
        turtle_object.speed(7)#max speed is 10
    if n>45:
        turtle_object.speed(10)

    turtle_object.penup()  #the turtles tail so that it doesn't draw
    turtle_object.sety(-radius) #move the y point to the button to start drawing from
    turtle_object.pendown()  #the turtle tail so it draws
    for i in the_frequent_characters:  # iterates through each tuple in fre list
        turtle_object.fillcolor(next(col))  # filling color in pie chart
        turtle_object.begin_fill()
        turtle_object.circle(radius, existing_letters[i] * 360 / total_of_all_characters)  # segment of area to fill color
        position = turtle_object.position()
        turtle_object.goto(0, 0)  # moves the turtle to position
        turtle_object.end_fill()
        turtle_object.setposition(position)

    #this part will draw the rest of the letters part of the pie chart
    turtle_object.fillcolor(next(col))  # filling color in pie chart
    turtle_object.begin_fill()
    turtle_object.circle(radius, rest_of_characters * 360 / total_of_all_characters)  # segment of area to fill color
    position = turtle_object.position()
    turtle_object.goto(0, 0)  # moves the turtle to position
    turtle_object.end_fill()
    turtle_object.setposition(position)

    # label
    turtle_object.speed(0) #i wanted to make the labeling of each segment of the piechart almost instant after drawing so i set speed to 0
    turtle_object.penup()


    #of the charcaters later
    # for loop to draw the labels around each part of the pie chart
    for i in the_frequent_characters:
        turtle_object.circle(radius, existing_letters[i] * 360 / total_of_all_characters/2)  # segment - goes halfway and then finishes the other half after
        #create a string as a label by combining the chatacter in the frequent_character list and a str of the rounded probaility
        label_as_string = i +', '+ str(round(float(existing_letters[i]/total_of_all_characters),4)) # label
        turtle_object.write(label_as_string, align="center", font=18)  # writing label
        turtle_object.circle(radius, existing_letters[i] * 360 / total_of_all_characters / 2)
        position = turtle_object.position()
        turtle_object.goto(0, 0)  # moves the turtle to position
        turtle_object.setposition(position)
        #turtle_object.circle(LABEL_RADIUS, existing_letters[i] * 180 / total_of_all_characters )

    #this part will calculate the probability of the rest of the characters
    total_prob=0
    for i in the_frequent_characters:
        total_prob += float(existing_letters[i]/total_of_all_characters)
    rest_prob=1-total_prob

    #this part will label the rest of the letters part of the pie chart
    turtle_object.circle(label_radius, rest_of_characters * 360 / total_of_all_characters / 2)  # segment
    label_as_string = 'All other letters, '+str(round(float(rest_prob),4)) # label - plus the probability of 1-total probability of the frequent letters
    turtle_object.write(label_as_string, align="center", font=11)  # writing label
    turtle_object.circle(label_radius, rest_of_characters * 360 / total_of_all_characters / 2)

    turtle_object.hideturtle()

    screen = Screen()
    screen.exitonclick()


#need to use lambda:callback(arg) to pass argument to the callback so that the
#button isn't pressed right when the program is ran
#clicking button will invoke callback to start the piechart drawing
start_button=Button(master,text="Create Pie Chart!",command=lambda:callback(e1))
start_button.grid(row=1,column=1)

#add button to end the program early or just in general if needed
#trying with just command=master.destroy() ends the mainloop when program is ran
#so needed to create a lambda function that you can then pass the command
end_program_button=Button(master,text="End Program/Close Window", command=lambda:master.destroy())
end_program_button.grid(row=2,column=1)


master.mainloop()


