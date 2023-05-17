#cordinate_rotation_program
#Minhaz, Tejaswini, and Natheeswar
#The program accepts inputs for different cordinates and allows the user to rotate them
#around different axes. 

import math
import time 
import tkinter

#Creating a function which converts degrees to radians
#This is needed in lots of the trig functions since they take 
#radians not degrees
def deg_to_rad(deg):

    rad = (deg/360)*2*math.pi
    return rad

rad_30 = deg_to_rad(30)

#Creatinga which rotates the cordinates around the y axis
#Takes in 2 arguments: the list containing the original cordinates
#then the amount in degrees that the cordinates need to be rotated
#the function then returns a list containing the new cordiantes
def y_axis_rot(cord_list, x_angle):

    cord_list_copy = []
    for i in cord_list:

        cord_list_copy.append(i)

    x_cord = cord_list_copy[1]
    y_cord = cord_list_copy[2]
    z_cord = cord_list_copy[3]

    y_absolute = math.sqrt(x_cord**2 + z_cord**2) #this is the shortest distance from the axis to the cordinates

    #an issue with calculating arctan of a number is that it doesn't take into account
    #if one or more numbers are negative, it doesn't know which number is negative 
    #since when you divide the numbers they give you a number which is only negative or only positve

    #the if statements bellow help to correct that by determining which values are negatives and postives
    #and depending on the outcome it adds the nessesary angles then does the calculations
    if (x_cord == 0 and z_cord<0):

        angle_x = deg_to_rad(270)
    elif (x_cord == 0 and z_cord>0):

        angle_x = deg_to_rad(90)
    elif(x_cord == 0 and z_cord==0):

        angle_x = 0
    else:

        angle_x = math.atan(z_cord/x_cord)

    angle_x = angle_x + x_angle

    if(z_cord < 0 or x_cord < 0):

        if (z_cord < 0 and x_cord<0):

            angle_x = angle_x+ deg_to_rad(180)
        elif(z_cord < 0 and x_cord>=0):

           angle_x = angle_x * (-1)
           angle_x = deg_to_rad(360)-angle_x
        elif(z_cord >= 0 and x_cord < 0):

            angle_x = angle_x * (-1)
            angle_x = deg_to_rad(180)-angle_x

    new_x = y_absolute*math.cos(angle_x)
    new_z = y_absolute*math.sin(angle_x)


    new_x = round(new_x,10)
    new_z = round(new_z,10)


    cord_list_copy[1] = new_x
    cord_list_copy[3] = new_z

    return cord_list_copy
#Creatinga which rotates the cordinates around the x axis
#Takes in 2 arguments: the list containing the original cordinates
#then the amount in degrees that the cordinates need to be rotated
#the function then returns a list containing the new cordiantes
def x_axis_rot(cord_list, y_angle):

    cord_list_copy = []
    for i in cord_list:

        cord_list_copy.append(i)

    x_cord = cord_list_copy[1]
    y_cord = cord_list_copy[2]
    z_cord = cord_list_copy[3]

    x_absolute = math.sqrt(z_cord**2 + y_cord**2)#this is the shortest distance from the axis to the cordinates

    #an issue with calculating arctan of a number is that it doesn't take into account
    #if one or more numbers are negative, it doesn't know which number is negative 
    #since when you divide the numbers they give you a number which is only negative or only positve

    #the if statements bellow help to correct that by determining which values are negatives and postives
    #and depending on the outcome it adds the nessesary angles then does the calculations

    if (z_cord == 0 and y_cord<0):

        angle_y = deg_to_rad(180)
    elif (z_cord == 0 and y_cord>0):

        angle_y = deg_to_rad(90)
    elif(z_cord == 0 and y_cord==0):

        angle_y = 0
    else:

        angle_y = math.atan(y_cord/z_cord)

    angle_y = angle_y + y_angle

    if(y_cord < 0 or z_cord < 0):

        if (y_cord < 0 and z_cord<0):

            angle_y = angle_y+ deg_to_rad(180)
        elif(y_cord < 0 and z_cord>=0):

           angle_y = angle_y * (-1)
           angle_y = deg_to_rad(360)-angle_y
        elif(y_cord >= 0 and z_cord < 0):

            angle_y = angle_y * (-1)
            angle_y = deg_to_rad(180)-angle_y
    
    new_y = x_absolute*math.sin(angle_y)
    new_z = x_absolute*math.cos(angle_y)

    new_y = round(new_y,10)
    new_z = round(new_z,10)
    cord_list_copy[2] = new_y
    cord_list_copy[3] = new_z

    return cord_list_copy

#creating a function which draws a circle
#takes arguments for the location of the center of the circle, the radius, and the colour of the circle
def draw_circle(pixel_cord,radius,colour):

    global canvas

    x = pixel_cord[0]
    y = pixel_cord[1]

    x1 = x-radius
    x2 = x+radius

    y1 = y-radius
    y2 = y+radius

# circle = canvas.create_oval(x1,y1,x2,y2,fill=colour,outline = "white") was this
    circle = canvas.create_oval(x1,y1,x2,y2,fill=colour)

# def draw_line(cool):
#     cool = input("enter the stuff: ")
#     cool = cool + " "
#     output_list = []
#     l_double = []
#     name = ""

#     for i in cool:
#         if (i == "&"):
#             l_double.append(name)
#             name = ""
#         elif (i == " "):
#             l_double.append(name)
#             output_list.append(l_double)
#             name = ""
#             l_double = []
#         else:
#             name = name + i

    

#creating a function which converts the x location on a plane to 2 dimensional
#pixel cordinates
def to_pixel_cord_x(original_pixel_cord, x):

    d_p_f = 45
    x_p = original_pixel_cord[0]
    y_p = original_pixel_cord[1]

    x_n = x_p + x*math.cos(rad_30)*d_p_f
    y_n = y_p + x*math.sin(rad_30)*d_p_f

    pixel_cord = [x_n,y_n]

    return pixel_cord
#creating a function which converts the z location on a plane to 2 dimensional
#pixel cordinates
def to_pixel_cord_z(original_pixel_cord,z):

    d_p_f = 45
    x_p = original_pixel_cord[0]
    y_p = original_pixel_cord[1]

    x_n = x_p - z*math.cos(rad_30)*d_p_f
    y_n = y_p + z*math.sin(rad_30)*d_p_f


    pixel_cord = [x_n,y_n]

    return pixel_cord

#creating a function which converts the y location on a plane to 2 dimensional
#pixel cordinates
def to_pixel_cord_y(original_pixel_cord,y):

    d_p_f = 45
    y_p = original_pixel_cord[1]

    x_n = original_pixel_cord[0]
    y_n = y_p - y*d_p_f

    pixel_cord = [x_n,y_n]

    return pixel_cord

#creating a function which converts the 3dimensional location on a plane to 2 dimensional
#pixel cordinates
#this takes an argumnet of a list containing the x,y,z points and converts it to a new
#list describing where the cordinate are on the screen
def cord_to_pixel(a):

    x = a[1]
    y = a[2]
    z = a[3]
    original_pixel_cord = [500,500]
    #in order to create the new cordinates the prior individual pixel cord functions are used
    updated_pixel_cord = to_pixel_cord_x(original_pixel_cord,x)
    updated_pixel_cord = to_pixel_cord_z(updated_pixel_cord,z)
    updated_pixel_cord = to_pixel_cord_y(updated_pixel_cord,y)
    
    updated_pixel_cord[0] = round(updated_pixel_cord[0],0)
    updated_pixel_cord[1] = round(updated_pixel_cord[1],0)

    return updated_pixel_cord

#creating a function which converts a list of cordinates directly to a graphic
def cord_to_graphic(a):

    radius = 3
    global canvas,wd1
    canvas = tkinter.Canvas(wd1,height=1000,width=1000,bg = "black")

    #creating the cordinates for the different axis
    x_axis_top_v = ['filler',-10,0,0]
    x_axis_bottom_v = ['filler',10,0,0]

    y_axis_top_v_1 = ['filler',0,10,0]
    y_axis_bottom_v_1 = ['filler',0,0,0]

    y_axis_bottom_v_2 = ['filler',0,-10,0]

    z_axis_top_v = ['filler',0,0,10]
    z_axis_bottom_v = ['filler',0,0,-10]

    x_axis_top = cord_to_pixel(x_axis_top_v)
    x_axis_bottom = cord_to_pixel(x_axis_bottom_v)

    y_axis_top_1 = cord_to_pixel(y_axis_top_v_1)
    y_axis_bottom_1 = cord_to_pixel(y_axis_bottom_v_1)

    y_axis_bottom_2 = cord_to_pixel(y_axis_bottom_v_2)

    z_axis_top = cord_to_pixel(z_axis_top_v)
    z_axis_bottom = cord_to_pixel(z_axis_bottom_v) 

    if (a[0] != 0):

        for prior_8 in a[0]:

                pixel_point = cord_to_pixel(prior_8)
                draw_circle(pixel_point,radius,prior_8[4])

    if (a[1] != 0):

        for prior_7 in a[1]:

                pixel_point = cord_to_pixel(prior_7)
                draw_circle(pixel_point,radius,prior_7[4])

    if (a[2] != 0):

        for prior_6 in a[2]:

                pixel_point = cord_to_pixel(prior_6)
                draw_circle(pixel_point,radius,prior_6[4])

    #drawing top part of axis y
    ##y_axis_bottom = canvas.create_line(y_axis_bottom_1,y_axis_bottom_2,fill = "red", width = 2)

    if (a[3] != 0):

        for prior_5 in a[3]:

                pixel_point = cord_to_pixel(prior_5)
                draw_circle(pixel_point,radius,prior_5[4])

    #drawing axis x and z
    # # x_axis = canvas.create_line(x_axis_top,x_axis_bottom,fill = "green", width = 2)
    # # z_axis = canvas.create_line(z_axis_top,z_axis_bottom,fill = "blue", width = 2)

    if (a[4] != 0):

        for prior_4 in a[4]:

                pixel_point = cord_to_pixel(prior_4)
                draw_circle(pixel_point,radius,prior_4[4])

    #drawing top part of axis y
    # y_axis_top = canvas.create_line(y_axis_top_1,y_axis_bottom_1,fill = "red", width = 2)

    

    if (a[5] != 0):

        for prior_3 in a[5]:

                pixel_point = cord_to_pixel(prior_3)
                draw_circle(pixel_point,radius,prior_3[4])

    if (a[6] != 0):

        for prior_2 in a[6]:

                pixel_point = cord_to_pixel(prior_2)
                draw_circle(pixel_point,radius,prior_2[4])

    if (a[7] != 0):

        for prior_1 in a[7]:

                pixel_point = cord_to_pixel(prior_1)
                draw_circle(pixel_point,radius,prior_1[4])

#assigning priorities for each function
#depending on what quadrant a point is, it will have different priorities
#this will help to determine which point is drawn over which axis
def priority(cordinate):

    x = cordinate[1]
    y = cordinate[2]
    z = cordinate[3]

    #quick note: lower number priorities are considered a higher priority
    #1 is the highest priority while 8 is the lowest

    #Series of if statements are needed so that lower number priority takes priority
    #by overiting any other priority assigned prior
    priority = 8 #initializing the variable by assigning it the lowest priority

    if((y<=0) and (x<=0) and (z<=0)):

        priority = 8

    if((y<=0) and (x>=0) and (z<=0)):

        priority = 7

    if((y<=0) and (x<=0) and (z>=0)):

        priority = 6

    if((y<=0) and (x>=0) and (z>=0)):

        priority = 5

    if((y>=0) and (x<=0) and (z<=0)):

        priority = 4

    if((y>=0) and (x>=0) and (z<=0)):

        priority = 3

    if((y>=0) and (x<=0) and (z>=0)):

        priority = 2
        
    if((y>=0) and (x>=0) and (z>=0)):

        priority = 1

    return priority


#Creating a function which adds the priority a cordinate has by iterating through the list
def add_priorities(cords):

    for i in cords:

        i.append(priority(i))
    return cords

#Creating a function which calculates the distance
def distance(cord):

    x = cord[1]
    y = cord[2]
    z = cord[3]

    distance = (10-x)**2 + (10-y)**2 + (10-z)**2
    distance =  round(distance,1)

    return distance

#Creating a function which adds the distance a cordinate is from the camera by iterating through the list
def add_distance(cords):

    for i in cords:

        i.append(distance(i))

    return cords

#Creating a function which sorts a cordinates into a multiple lists dedicated for each priority
def priority_sorter(a):

    sorted_priority = []
    priority_8 = []
    priority_7 = []
    priority_6 = []
    priority_5 = []
    priority_4 = []
    priority_3 = []
    priority_2 = []
    priority_1 = []

    for i in a:

        if (i[5] == 1):
            
            priority_1.append(i)
        if (i[5] == 2):

            priority_2.append(i)
        if (i[5] == 3):

            priority_3.append(i)
        if (i[5] == 4):

            priority_4.append(i)
        if (i[5] == 5):

            priority_5.append(i)
        if (i[5] == 6):

            priority_6.append(i)
        if (i[5] == 7):

            priority_7.append(i)
        if (i[5] == 8):

            priority_8.append(i)

    sorted_priority.append(priority_8)
    sorted_priority.append(priority_7)
    sorted_priority.append(priority_6)
    sorted_priority.append(priority_5)
    sorted_priority.append(priority_4)
    sorted_priority.append(priority_3)
    sorted_priority.append(priority_2)
    sorted_priority.append(priority_1)

    a = sorted_priority

    return (a)

#function used later to sort lists inside a list
def sort_list(cordinate):

    return cordinate[6]

#function created in order to sort by distances from camera
def sort_by_distance(priority_list):

    priority_list.sort(key=sort_list,reverse=True)
    return priority_list

#Creating a function which goes into each list of priorities and sorts it by distances
def full_sort(a):

    counter = 0
    for i in a:

        if len(i)!=0:

            a[counter] = sort_by_distance(a[counter])
        counter +=1
    return a

#creating a function that makes a copy of a list and returns it
def copy_list(a):
    return_list = []
    for i in a:

        return_list.append(i)

    return return_list

#creating a function which creates a database to store the information for the points
#before and after rotations
def create_data_base(original_cord,y_rotation,cord_after_y,x_rotation,final_cord):
    prompt_message = ""

    file_out_name = "cordinate_database.txt"
    output_file = open(file_out_name,"w")

    seperator = "     "

    output_message = ""

    line_output = "The Original Points are located at:\n"

    for i in original_cord:

        line_output += i[0] + seperator
        line_output += "x: " + str(i[1]) + seperator
        line_output += "y: " + str(i[2]) + seperator
        line_output += "z: " + str(i[3]) + seperator
        line_output += i[4] + "\n"

    line_output += "\nThe y rotation is " + str(y_rotation) + " degrees\n"
    output_message+=line_output
    line_output = ""
    output_message+="The new Points after this rotation are located at:\n"

    for i in cord_after_y:

        line_output += i[0] + seperator
        line_output += "x: " + str(i[1]) + seperator
        line_output += "y: " + str(i[2]) + seperator
        line_output += "z: " + str(i[3]) + seperator
        line_output += i[4] + "\n"

    line_output += "\nThe x rotation is " + str(x_rotation) + " degrees\n"
    output_message+=line_output
    line_output = ""
    output_message+="The final Points after the y and x rotation are located at:\n"

    for i in final_cord:

        line_output += i[0] + seperator
        line_output += "x: " + str(i[1]) + seperator
        line_output += "y: " + str(i[2]) + seperator
        line_output += "z: " + str(i[3]) + seperator
        line_output += i[4] + "\n"

    output_message+=line_output

    for i in final_cord:

        prompt_message += i[0] + seperator
        prompt_message += "x: " + str(i[1]) + seperator
        prompt_message += "y: " + str(i[2]) + seperator
        prompt_message += "z: " + str(i[3]) + "\n"

    output_file.write(output_message)

    return prompt_message

#creating a function which checks if a number is a decimal and returns a string withought the decimal
#this is used in the validation function to determin whether a number is a proper decimal
def decimal_check(value,decimal_existance):

    output = False

    if (decimal_existance == True):

        numerator = ""

        counter = 0
        bool_sen = True

        while bool_sen == True:
        
            if value[counter] == ".":

                bool_sen = False

            counter += 1

        decimal_places = len(value) - counter

        counter = counter - 1

        numerator = ""
        for i in value:

            if (i != "."):

                numerator += i

        if(numerator.isdigit() == True):

            output = True

    return output

#validates a string to see if it is a rational number
def input_validation(unknown_input):
    unknown_input = str(unknown_input)

    output = False

    decimal_number = 0
    for i in unknown_input:

        if (i == "."):

            decimal_number = decimal_number + 1

    decimal_existance = False

    if (decimal_number == 1 ):

        decimal_existance = True

    if (decimal_check(unknown_input, decimal_existance) == True):

        output = True

    elif (unknown_input.isdigit() == True):

        output = True

    elif (unknown_input == ""):

        output = False

    elif (unknown_input[0] == "-"):

        input_integer = True
        check_string = ""

        for i in range (1,len(unknown_input)):

            check_string += unknown_input[i]
        
        if(check_string.isdigit() == True):

            output = True

        else:

            if (decimal_number == 1):

                if (decimal_check(check_string, True) == True):

                    output = True
                else:

                    output = False
                
            else:
                output = False

    else:

        output = False

    return output

#creating a function which iterates through a list to determine that the list is correctly ordered
def validation_check(list_input):

    validation = True
    elements = len(list_input)
    if (elements%6) != 0:

        validation = False
    
    else:

        for i in range(elements//6):

            if (list_input[i*6 + 0] == ""):

                validation = False
            if(list_input[i*6 + 1] != "("):

                validation = False
            if(input_validation(list_input[i*6 + 2]) != True):

                validation = False
            if(input_validation(list_input[i*6 + 3]) != True):

                validation = False
            if(input_validation(list_input[i*6 + 4]) != True):

                validation = False
            if(list_input[i*6 + 5] != ")"):

                validation = False

    return validation

#removes brackets in a list
def bracket_remove(a):

    brackets_removed = 0
    for i in range(len(a)):

        i -= brackets_removed
        if a[i] == "(" or a[i] == ")":

            a[i:i+1] = [] 
            brackets_removed += 1

#sorts a list so that each point has its own list
def mini_lists(input_list): 
    
    temp_list = [] 
    overall_list = []

    # bracket_remove(input_list)
    
    list_elements = len(input_list)

    for i in range(list_elements//6):

        temp_list.append(input_list[i*6])
        temp_list.append(float(input_list[i*6+2]))
        temp_list.append(float(input_list[i*6+3]))
        temp_list.append(float(input_list[i*6+4]))

        overall_list.append(temp_list)
        temp_list = []
    
    return overall_list

#assings colours to each list of cordinate
def colour_assignment(input_list):

    file = open("graphic_colours.txt", "r")
    file_b = open("graphic_colours.txt", "r")
    colours_list = []

    read_file = file.readline()

    while read_file != "":

        read_file = read_file.strip("\n")
        colours_list.append(read_file)
        read_file = file.readline()

    colours_index = 0
    list_index = 0

    while list_index in range(len(input_list)):

        if colours_index > len(colours_list):

            colours_index = 0
        else:

            input_list[list_index].append("#336CFF")
            colours_index += 1
            list_index += 1

    return input_list

#converts a string input to a list formate to be validated
def string_to_list(string_input):
    
    validation_list = []

    counter = 0 

    output_list = []

    while(counter < len(string_input)):

        combiner = ""
        for i in range(len(string_input)):

            character = string_input[i]

            if(character == "("):

                output_list.append(combiner)
                output_list.append("(")
                combiner = ""

            elif(character == ","):

                output_list.append(combiner)
                combiner = ""
            elif(character == ")"):

                output_list.append(combiner)
                output_list.append(")")
                combiner = ""
            else:
                
                combiner = combiner + character

            counter +=1

    return output_list

#opens a shapes text file and returns a list of cordinates stored in that file
def shapes_coordinates(shape_input):

    file = open(shape_input, "r")
    shapes_list = ""
    read_file = file.readline()

    while read_file != "":

        read_file = read_file.strip("\n")
        shapes_list += (read_file)
        read_file = file.readline()

    return shapes_list

def y_update_line_list(list_in,running_angle):
    list_out = []
    for connections in list_in:
        new_list = []
        for cord in connections:
            new_list.append(y_axis_rot(cord,deg_to_rad(running_angle)))
        list_out.append(new_list)

    return list_out

def x_update_line_list(list_in,running_angle):
    list_out = []
    for connections in list_in:
        new_list = []
        for cord in connections:
            new_list.append(x_axis_rot(cord,deg_to_rad(running_angle)))
        list_out.append(new_list)

    return list_out



#[[[0,0,0],[1,1,1]],[[1,1,1],[-1,-1,-1]],[[-1,-1,-1],[0,0,0]]]

# test =

def draw_lines(all_con):
    for connections in all_con:
        
        print(connections)

        first_list = cord_to_pixel(connections[0])
        second_list = cord_to_pixel(connections[1])

        print(first_list[0])
        print(first_list[1])
        print(second_list[0])
        print(second_list[1])
        line = canvas.create_line(first_list[0],first_list[1],second_list[0],second_list[1],fill = "white", width = 1)




#creating main function
#[[[1,1,-1],[-1,1,-1]],[[1,1,-1],[1,1,1]],[[1,1,1],[-1,1,1]],[[-1,1,1],[-1,1,-1]]]

##################################################################################################
def main():

    global wd1 #globalizing the tkinter window which is needed by functions to display graphics

    print("Hello, this program is designed to allow you to enter cordinates and then rotate them"+
" around the y and x axis.")
    print("Here are some key points to understand before using the program:")
    print("Assuming each axis was a vector pointing towards the postive end of the axis.\n"+
"The rotation would be counterclockwise in the perspective of the vector.\nThe x and y axes"+
" are the axes of rotation"+
"that each point revolves around.\nThe origin is the point where all the axes intercept.\nThe "+
"x axis is green, and the postive"+
"side of the x axis is bottom right of the origin.\nThe z axis is blue and the postive side"+
" of the z axis is bottom left from the origin.\n"+
"Lastly the y axis is red and positive side is upwards from the origin.\n\n")

    angle_y = 0
    angle_x = 0

    bool_sen = True
    while (bool_sen == True):

        print("Would you like to choose premade cordinates stored in a file or would you like to enter your own cordinates?")
        pre_or_custom = input( "Please enter (Premade or Custom): " )
        pre_or_custom = pre_or_custom.lower()

        if (pre_or_custom == "custom"):

            bool_sen = False

            print("\nYou have choosen Custom meaning that you can enter your own" , 
                "cordinates [the formate is the form of"
, "cordinate_name(x,y,z)cordinate_name2(x2,y2,z2)...]","(x,y, and z are values for the locations of the cordinates.\n",
"x,y, and z all have to be between -4 and 4, and all cordinates need to be entered in one string\n" +
"you can enter cordinates higher or lower, but it may not be displayed on the graphic" )

            bool_sen_2 = True
            while (bool_sen_2 == True):

                cordinates_input = input("Please enter the cordinates:\n")
                unvalidated_cordinates_list = string_to_list(cordinates_input)
                validation_var = validation_check(unvalidated_cordinates_list)


                if (validation_var == True):
                    bool_sen_2 = False

                    validated_list = mini_lists(unvalidated_cordinates_list)
                    cordinate_list = colour_assignment(validated_list)

                else:
                    print("Sorry but your cordinates are formated wrong please try again\n")
            #cord_connection_string = input("great job now please enter which cordinates you would like to connect:\n") #check for validation later



        elif (pre_or_custom == "premade"):

            bool_sen_3 = True
            while (bool_sen_3 == True):

                print("\nPlease select a shape in the following list:"
                ,"\nCube\nPyramid\nRectangular Prism")

                choosen_shape = input("\nPlease enter the shape: ")
                choosen_shape = choosen_shape.lower()

                if(choosen_shape == "cube"):

                    bool_sen_3 = False
                    shape_file = "cube.txt"
                elif(choosen_shape == "pyramid"):

                    bool_sen_3 = False
                    shape_file = "pyramid.txt"
                elif(choosen_shape == "rectangular prism"):

                    bool_sen_3 = False
                    shape_file = "rec_prism.txt"
                else:

                    print("Please enter a valid input")
            
            shape_string = shapes_coordinates(shape_file)
            shape_list = string_to_list(shape_string)
            
            if validation_check(shape_list) == True:

                bool_sen = False
                shape_list = mini_lists(shape_list)
                cordinate_list = colour_assignment(shape_list)

            else:

                print("Sorry the file named(" + shape_file + ") is formated incorrectly")

        else:

            print("Sorry but your choise is not correctly formated")

    print("\nPlease enter the rotation that you would like to perform")

    bool_sen_4 = True

    while bool_sen_4 == True:

        angle_y_input = input("Please enter y axis rotation in degrees: ")
        if (input_validation(angle_y_input) == True):

            bool_sen_4 = False
            angle_y = float(angle_y_input)
        else:

            print("Please check your input to make sure its a number")

    bool_sen_5 = True   

    while bool_sen_5 == True:

        angle_x_input = input("Please enter x axis rotation in degrees: ")
        if (input_validation(angle_x_input) == True):

            bool_sen_5 = False
            angle_x = float(angle_x_input)
        else:

            print("Please check your input to make sure its a number")
            
    #Rotation Control Variable
    angle = 2 
    #calculate the amount of loops needs for the graphics
    angle_y_loop = angle_y//angle
    angle_x_loop = angle_x//angle

    running_angle = 0

    new_y_cord_list = []


    test = [[['s', 0, 0, -1], ['s', 0, 0, -1]], [['s', 0.47, 0.47, -0.75], ['s', 0.0, 0.66, -0.75]], [['s', 0.0, 0.66, -0.75], ['s', -0.47, 0.47, -0.75]], [['s', -0.47, 0.47, -0.75], ['s', -0.66, 0.0, -0.75]], [['s', -0.66, 0.0, -0.75], ['s', -0.47, -0.47, -0.75]], [['s', -0.47, -0.47, -0.75], ['s', -0.0, -0.66, -0.75]], [['s', -0.0, -0.66, -0.75], ['s', 0.47, -0.47, -0.75]], [['s', 0.47, -0.47, -0.75], ['s', 0.66, -0.0, -0.75]], [['s', 0.66, -0.0, -0.75], ['s', 0.47, 0.47, -0.75]], [['s', 0.61, 0.61, -0.5], ['s', 0.0, 0.87, -0.5]], [['s', 0.0, 0.87, -0.5], ['s', -0.61, 0.61, -0.5]], [['s', -0.61, 0.61, -0.5], ['s', -0.87, 0.0, -0.5]], [['s', -0.87, 0.0, -0.5], ['s', -0.61, -0.61, -0.5]], [['s', -0.61, -0.61, -0.5], ['s', -0.0, -0.87, -0.5]], [['s', -0.0, -0.87, -0.5], ['s', 0.61, -0.61, -0.5]], [['s', 0.61, -0.61, -0.5], ['s', 0.87, -0.0, -0.5]], [['s', 0.87, -0.0, -0.5], ['s', 0.61, 0.61, -0.5]], [['s', 0.68, 0.68, -0.25], ['s', 0.0, 0.97, -0.25]], [['s', 0.0, 0.97, -0.25], ['s', -0.68, 0.68, -0.25]], [['s', -0.68, 0.68, -0.25], ['s', -0.97, 0.0, -0.25]], [['s', -0.97, 0.0, -0.25], ['s', -0.68, -0.68, -0.25]], [['s', -0.68, -0.68, -0.25], ['s', -0.0, -0.97, -0.25]], [['s', -0.0, -0.97, -0.25], ['s', 0.68, -0.68, -0.25]], [['s', 0.68, -0.68, -0.25], ['s', 0.97, -0.0, -0.25]], [['s', 0.97, -0.0, -0.25], ['s', 0.68, 0.68, -0.25]], [['s', 0.71, 0.71, 0], ['s', 0.0, 1.0, 0]], [['s', 0.0, 1.0, 0], ['s', -0.71, 0.71, 0]], [['s', -0.71, 0.71, 0], ['s', -1.0, 0.0, 0]], [['s', -1.0, 0.0, 0], ['s', -0.71, -0.71, 0]], [['s', -0.71, -0.71, 0], ['s', -0.0, -1.0, 0]], [['s', -0.0, -1.0, 0], ['s', 0.71, -0.71, 0]], [['s', 0.71, -0.71, 0], ['s', 1.0, -0.0, 0]], [['s', 1.0, -0.0, 0], ['s', 0.71, 0.71, 0]], [['s', 0.68, 0.68, 0.25], ['s', 0.0, 0.97, 0.25]], [['s', 0.0, 0.97, 0.25], ['s', -0.68, 0.68, 0.25]], [['s', -0.68, 0.68, 0.25], ['s', -0.97, 0.0, 0.25]], [['s', -0.97, 0.0, 0.25], ['s', -0.68, -0.68, 0.25]], [['s', -0.68, -0.68, 0.25], ['s', -0.0, -0.97, 0.25]], [['s', -0.0, -0.97, 0.25], ['s', 0.68, -0.68, 0.25]], [['s', 0.68, -0.68, 0.25], ['s', 0.97, -0.0, 0.25]], [['s', 0.97, -0.0, 0.25], ['s', 0.68, 0.68, 0.25]], [['s', 0.61, 0.61, 0.5], ['s', 0.0, 0.87, 0.5]], [['s', 0.0, 0.87, 0.5], ['s', -0.61, 0.61, 0.5]], [['s', -0.61, 0.61, 0.5], ['s', -0.87, 0.0, 0.5]], [['s', -0.87, 0.0, 0.5], ['s', -0.61, -0.61, 0.5]], [['s', -0.61, -0.61, 0.5], ['s', -0.0, -0.87, 0.5]], [['s', -0.0, -0.87, 0.5], ['s', 0.61, -0.61, 0.5]], [['s', 0.61, -0.61, 0.5], ['s', 0.87, -0.0, 0.5]], [['s', 0.87, -0.0, 0.5], ['s', 0.61, 0.61, 0.5]], [['s', 0.47, 0.47, 0.75], ['s', 0.0, 0.66, 0.75]], [['s', 0.0, 0.66, 0.75], ['s', -0.47, 0.47, 0.75]], [['s', -0.47, 0.47, 0.75], ['s', -0.66, 0.0, 0.75]], [['s', -0.66, 0.0, 0.75], ['s', -0.47, -0.47, 0.75]], [['s', -0.47, -0.47, 0.75], ['s', -0.0, -0.66, 0.75]], [['s', -0.0, -0.66, 0.75], ['s', 0.47, -0.47, 0.75]], [['s', 0.47, -0.47, 0.75], ['s', 0.66, -0.0, 0.75]], [['s', 0.66, -0.0, 0.75], ['s', 0.47, 0.47, 0.75]], [['s', 0, 0, 1], ['s', 0, 0, 1]], [['s', 0.47, 0.47, -0.75], ['s', 0, 0, -1]], [['s', 0.0, 0.66, -0.75], ['s', 0, 0, -1]], [['s', -0.47, 0.47, -0.75], ['s', 0, 0, -1]], [['s', -0.66, 0.0, -0.75], ['s', 0, 0, -1]], [['s', -0.47, -0.47, -0.75], ['s', 0, 0, -1]], [['s', -0.0, -0.66, -0.75], ['s', 0, 0, -1]], [['s', 0.47, -0.47, -0.75], ['s', 0, 0, -1]], [['s', 0.66, -0.0, -0.75], ['s', 0, 0, -1]], [['s', 0.47, 0.47, -0.75], ['s', 0.61, 0.61, -0.5]], [['s', 0.0, 0.66, -0.75], ['s', 0.0, 0.87, -0.5]], [['s', -0.47, 0.47, -0.75], ['s', -0.61, 0.61, -0.5]], [['s', -0.66, 0.0, -0.75], ['s', -0.87, 0.0, -0.5]], [['s', -0.47, -0.47, -0.75], ['s', -0.61, -0.61, -0.5]], [['s', -0.0, -0.66, -0.75], ['s', -0.0, -0.87, -0.5]], [['s', 0.47, -0.47, -0.75], ['s', 0.61, -0.61, -0.5]], [['s', 0.66, -0.0, -0.75], ['s', 0.87, -0.0, -0.5]], [['s', 0.61, 0.61, -0.5], ['s', 0.68, 0.68, -0.25]], [['s', 0.0, 0.87, -0.5], ['s', 0.0, 0.97, -0.25]], [['s', -0.61, 0.61, -0.5], ['s', -0.68, 0.68, -0.25]], [['s', -0.87, 0.0, -0.5], ['s', -0.97, 0.0, -0.25]], [['s', -0.61, -0.61, -0.5], ['s', -0.68, -0.68, -0.25]], [['s', -0.0, -0.87, -0.5], ['s', -0.0, -0.97, -0.25]], [['s', 0.61, -0.61, -0.5], ['s', 0.68, -0.68, -0.25]], [['s', 0.87, -0.0, -0.5], ['s', 0.97, -0.0, -0.25]], [['s', 0.68, 0.68, -0.25], ['s', 0.71, 0.71, 0]], [['s', 0.0, 0.97, -0.25], ['s', 0.0, 1.0, 0]], [['s', -0.68, 0.68, -0.25], ['s', -0.71, 0.71, 0]], [['s', -0.97, 0.0, -0.25], ['s', -1.0, 0.0, 0]], [['s', -0.68, -0.68, -0.25], ['s', -0.71, -0.71, 0]], [['s', -0.0, -0.97, -0.25], ['s', -0.0, -1.0, 0]], [['s', 0.68, -0.68, -0.25], ['s', 0.71, -0.71, 0]], [['s', 0.97, -0.0, -0.25], ['s', 1.0, -0.0, 0]], [['s', 0.71, 0.71, 0], ['s', 0.68, 0.68, 0.25]], [['s', 0.0, 1.0, 0], ['s', 0.0, 0.97, 0.25]], [['s', -0.71, 0.71, 0], ['s', -0.68, 0.68, 0.25]], [['s', -1.0, 0.0, 0], ['s', -0.97, 0.0, 0.25]], [['s', -0.71, -0.71, 0], ['s', -0.68, -0.68, 0.25]], [['s', -0.0, -1.0, 0], ['s', -0.0, -0.97, 0.25]], [['s', 0.71, -0.71, 0], ['s', 0.68, -0.68, 0.25]], [['s', 1.0, -0.0, 0], ['s', 0.97, -0.0, 0.25]], [['s', 0.68, 0.68, 0.25], ['s', 0.61, 0.61, 0.5]], [['s', 0.0, 0.97, 0.25], ['s', 0.0, 0.87, 0.5]], [['s', -0.68, 0.68, 0.25], ['s', -0.61, 0.61, 0.5]], [['s', -0.97, 0.0, 0.25], ['s', -0.87, 0.0, 0.5]], [['s', -0.68, -0.68, 0.25], ['s', -0.61, -0.61, 0.5]], [['s', -0.0, -0.97, 0.25], ['s', -0.0, -0.87, 0.5]], [['s', 0.68, -0.68, 0.25], ['s', 0.61, -0.61, 0.5]], [['s', 0.97, -0.0, 0.25], ['s', 0.87, -0.0, 0.5]], [['s', 0.61, 0.61, 0.5], ['s', 0.47, 0.47, 0.75]], [['s', 0.0, 0.87, 0.5], ['s', 0.0, 0.66, 0.75]], [['s', -0.61, 0.61, 0.5], ['s', -0.47, 0.47, 0.75]], [['s', -0.87, 0.0, 0.5], ['s', -0.66, 0.0, 0.75]], [['s', -0.61, -0.61, 0.5], ['s', -0.47, -0.47, 0.75]], [['s', -0.0, -0.87, 0.5], ['s', -0.0, -0.66, 0.75]], [['s', 0.61, -0.61, 0.5], ['s', 0.47, -0.47, 0.75]], [['s', 0.87, -0.0, 0.5], ['s', 0.66, -0.0, 0.75]], [['s', 0.47, 0.47, 0.75], ['s', 0, 0, 1]], [['s', 0.0, 0.66, 0.75], ['s', 0, 0, 1]], [['s', -0.47, 0.47, 0.75], ['s', 0, 0, 1]], [['s', -0.66, 0.0, 0.75], ['s', 0, 0, 1]], [['s', -0.47, -0.47, 0.75], ['s', 0, 0, 1]], [['s', -0.0, -0.66, 0.75], ['s', 0, 0, 1]], [['s', 0.47, -0.47, 0.75], ['s', 0, 0, 1]], [['s', 0.66, -0.0, 0.75], ['s', 0, 0, 1]]]
    wd1 = tkinter.Tk()
    wd1.geometry("1000x1000")
    wd1.title("Graphics")

    original_cord = copy_list(cordinate_list)
    # Y value rotations------------------------
    if(angle_y < 0):

        angle = angle * -1

    print(cordinate_list)

    for i in range(int(abs(angle_y_loop))+2):

        for individual_cord in cordinate_list:

            new_cord = y_axis_rot(individual_cord,deg_to_rad(running_angle))
            new_y_cord_list.append(new_cord)

        test = y_update_line_list(test,angle)

        graphics_list = add_priorities(new_y_cord_list)
        graphics_list = add_distance(graphics_list)
        graphics_list = priority_sorter(graphics_list)
        graphics_list = full_sort(graphics_list)
        cord_to_graphic(graphics_list)
        draw_lines(test)

 

        # # # draw_lines(test)
        ########################################################################
        ########################################################################
        ########################################################################
        ########################################################################
        #line = canvas.create_line(500,200,300,400,fill="white",width=4)

        running_angle = i*angle
        canvas.pack()
        canvas.update()
        time.sleep(.015)
        canvas.destroy()

        new_y_cord_list = []

    #if there is no remainder there is no need to do further calculations
    #since all values are calculated in the loop
    #the code bellow determines if there is a remainder or not
    if (angle_y % angle != 0):

        for individual_cord in cordinate_list:

            new_cord = y_axis_rot(individual_cord,deg_to_rad(angle_y))
            new_y_cord_list.append(new_cord)

        graphics_list = add_priorities(new_y_cord_list)
        graphics_list = add_distance(graphics_list)
        graphics_list = priority_sorter(graphics_list)
        graphics_list = full_sort(graphics_list)
        cord_to_graphic(graphics_list)
        draw_lines(test)
        ########################################################################
        ########################################################################
        ########################################################################
        ########################################################################

        running_angle = i*angle
        canvas.pack()
        canvas.update()
        canvas.destroy()

        new_y_cord_list = []

    #X value rotations ---------------------------
    angle = 2

    if(angle_x < 0):

        angle = angle * -1

    time.sleep(2)

    #reseting variables for the new calculations
    finished_y_rotation_list = []
    new_cord = 0
    running_angle = 0

    #generating a list of the new cordinates after all y rotations are complete
    #this is required as the input for the x rotations
    for individual_cord in cordinate_list:

        new_cord = y_axis_rot(individual_cord,deg_to_rad(angle_y))
        finished_y_rotation_list.append(new_cord)

    after_y_rotation_list = copy_list(finished_y_rotation_list)
    
    new_x_cord_list = []
    
    for i in range(int(abs(angle_x_loop))+2):

        for individual_cord in finished_y_rotation_list:

            new_cord = x_axis_rot(individual_cord,deg_to_rad(running_angle))

            new_x_cord_list.append(new_cord)

        test = x_update_line_list(test,angle)
        graphics_list = add_priorities(new_x_cord_list)
        graphics_list = add_distance(graphics_list)
        graphics_list = priority_sorter(graphics_list)
        graphics_list = full_sort(graphics_list)
        cord_to_graphic(graphics_list)
        draw_lines(test)
        running_angle = i*angle
        canvas.pack()
        canvas.update()
        time.sleep(.015)
        canvas.destroy()
        new_x_cord_list = []


    #Generating the final frame for the finished destination of the cordinates
    for individual_cord in finished_y_rotation_list:
        
        new_cord = x_axis_rot(individual_cord,deg_to_rad(angle_x))
        new_x_cord_list.append(new_cord)
    # print("----------------------------")
    # print(new_list)
    # print("----------------------------")

    graphics_list = add_priorities(new_x_cord_list)
    graphics_list = add_distance(graphics_list)
    graphics_list = priority_sorter(graphics_list)
    graphics_list = full_sort(graphics_list)
    cord_to_graphic(graphics_list)


    running_angle = i*angle
    canvas.pack()
    canvas.update()
    time.sleep(3)
    canvas.destroy()
    new_x_cord_list = []

    ###############################################
    
    wd1.mainloop()
    
    #if there is no remainder there is no need to do further calculations
    #since all values are calculated in the loop
    #the code bellow determines if there is a remainder or not
    new_x_cord_list = []

    for individual_cord in finished_y_rotation_list:

        new_cord = x_axis_rot(individual_cord,deg_to_rad(angle_x))
        new_x_cord_list.append(new_cord)

    final_list = copy_list(new_x_cord_list)

    new_cord_promt = create_data_base(original_cord,angle_y,after_y_rotation_list,angle_x,final_list)

    print("Thank you for using the program")
    print("Your new points are located:\n")
    print(new_cord_promt)
    print("\nPlease access the cordinate_database.txt file for more indepth explanations")
    print(cordinate_list)
main() #opening main function