import math

class cord_adjustments():
    def __init__(self,original_cordinates):
        self.cord_system = original_cordinates


    def deg_to_rad(self,deg):
        rad = (deg/360)*2*math.pi
        return rad

    def y_axis_rot(self, x_angle):

        cord_list_copy = []
        for i in self.cord_system:

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
            angle_x = self.deg_to_rad(270)
        elif (x_cord == 0 and z_cord>0):
            angle_x = self.deg_to_rad(90)

        elif(x_cord == 0 and z_cord==0):
            angle_x = 0

        else:
            angle_x = math.atan(z_cord/x_cord)

        angle_x = angle_x + x_angle

        if(z_cord < 0 or x_cord < 0):
            if (z_cord < 0 and x_cord<0):
                angle_x = angle_x+ self.deg_to_rad(180)

            elif(z_cord < 0 and x_cord>=0):
                angle_x = angle_x * (-1)
                angle_x = self.deg_to_rad(360)-angle_x

            elif(z_cord >= 0 and x_cord < 0):

                angle_x = angle_x * (-1)
                angle_x = self.deg_to_rad(180)-angle_x

        new_x = y_absolute*math.cos(angle_x)
        new_z = y_absolute*math.sin(angle_x)


        new_x = round(new_x,10)
        new_z = round(new_z,10)


        cord_list_copy[1] = new_x
        cord_list_copy[3] = new_z

        self.cord_system = cord_list_copy
    
    #Creatinga which rotates the cordinates around the x axis
    #Takes in 2 arguments: the list containing the original cordinates
    #then the amount in degrees that the cordinates need to be rotated
    #the function then returns a list containing the new cordiantes
    def x_axis_rot(self, y_angle):

        cord_list_copy = []
        for i in self.cord_system:

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

            angle_y = self.deg_to_rad(180)
        elif (z_cord == 0 and y_cord>0):

            angle_y = self.deg_to_rad(90)
        elif(z_cord == 0 and y_cord==0):

            angle_y = 0
        else:

            angle_y = math.atan(y_cord/z_cord)

        angle_y = angle_y + y_angle

        if(y_cord < 0 or z_cord < 0):

            if (y_cord < 0 and z_cord<0):
                angle_y = angle_y+ self.deg_to_rad(180)

            elif(y_cord < 0 and z_cord>=0):
                angle_y = angle_y * (-1)
                angle_y = self.deg_to_rad(360)-angle_y

            elif(y_cord >= 0 and z_cord < 0):

                angle_y = angle_y * (-1)
                angle_y = self.deg_to_rad(180)-angle_y
        
        new_y = x_absolute*math.sin(angle_y)
        new_z = x_absolute*math.cos(angle_y)

        new_y = round(new_y,10)
        new_z = round(new_z,10)
        cord_list_copy[2] = new_y
        cord_list_copy[3] = new_z

        self.cord_system = cord_list_copy

    def update_cords(self, cord_in):
        self.cord_system = cord_in