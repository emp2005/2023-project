import tkinter
import math

class draw():
    def __init__(self,original_cordinates):
        self.cord_system = original_cordinates
        ###
        self.wd1 = tkinter.Tk()
        self.wd1.geometry("1000x1000")
        self.wd1.title("Graphics")
        ###
        self.original_pixel_cord = [500,500]
        self.rad_30 = (30/360)*2*math.pi
        self.canvas = tkinter.Canvas(self.wd1,height=1000, width=1000, bg = "black")

    def draw_circle(self,pixel_cord,radius,colour):
        canvas = self.canvas
        x = pixel_cord[0] 
        y = pixel_cord[1]

        x1 = x-radius
        x2 = x+radius

        y1 = y-radius
        y2 = y+radius

        #circle = canvas.create_oval(x1,y1,x2,y2,fill=colour,outline = "white") was this
        circle = canvas.create_oval(x1,y1,x2,y2,fill=colour)

    def to_pixel_cord_x(self, x):
        original_pixel_cord = self.original_pixel_cord
        rad_30 = self.rad_30
        d_p_f = 45
        x_p = original_pixel_cord[0]
        y_p = original_pixel_cord[1]

        x_n = x_p + x*math.cos(rad_30)*d_p_f
        y_n = y_p + x*math.sin(rad_30)*d_p_f

        pixel_cord = [x_n,y_n]

        return pixel_cord
#creating a function which converts the z location on a plane to 2 dimensional
#pixel cordinates
    def to_pixel_cord_z(self,z):
        original_pixel_cord = self.original_pixel_cord
        rad_30 = self.rad_30

        d_p_f = 45
        x_p = original_pixel_cord[0]
        y_p = original_pixel_cord[1]

        x_n = x_p - z*math.cos(rad_30)*d_p_f
        y_n = y_p + z*math.sin(rad_30)*d_p_f


        pixel_cord = [x_n,y_n]

        return pixel_cord

    #creating a function which converts the y location on a plane to 2 dimensional
    #pixel cordinates
    def to_pixel_cord_y(self,y):
        original_pixel_cord = self.original_pixel_cord

        d_p_f = 45
        y_p = original_pixel_cord[1]

        x_n = original_pixel_cord[0]
        y_n = y_p - y*d_p_f

        pixel_cord = [x_n,y_n]

        return pixel_cord

    def cord_to_pixel(self,a):

        x = a[1]
        y = a[2]
        z = a[3]
        original_pixel_cord = [500,500]
        #in order to create the new cordinates the prior individual pixel cord functions are used
        updated_pixel_cord = self.to_pixel_cord_x(x)
        updated_pixel_cord = self.to_pixel_cord_z(z)
        updated_pixel_cord = self.to_pixel_cord_y(y)
        
        updated_pixel_cord[0] = round(updated_pixel_cord[0],0)
        updated_pixel_cord[1] = round(updated_pixel_cord[1],0)

        return updated_pixel_cord

    #creating a function which converts a list of cordinates directly to a graphic
    def cord_to_graphic(self):
        a = self.cord_system
        

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

        x_axis_top = self.cord_to_pixel(x_axis_top_v)
        x_axis_bottom = self.cord_to_pixel(x_axis_bottom_v)

        y_axis_top_1 = self.cord_to_pixel(y_axis_top_v_1)
        y_axis_bottom_1 = self.cord_to_pixel(y_axis_bottom_v_1)

        y_axis_bottom_2 = self.cord_to_pixel(y_axis_bottom_v_2)

        z_axis_top = self.cord_to_pixel(z_axis_top_v)
        z_axis_bottom = self.cord_to_pixel(z_axis_bottom_v) 

        if (a[0] != 0):

            for prior_8 in a[0]:

                    pixel_point = self.cord_to_pixel(prior_8)
                    self.draw_circle(pixel_point,radius,prior_8[4])

        if (a[1] != 0):

            for prior_7 in a[1]:

                    pixel_point = self.cord_to_pixel(prior_7)
                    self.draw_circle(pixel_point,radius,prior_7[4])

        if (a[2] != 0):

            for prior_6 in a[2]:

                    pixel_point = self.cord_to_pixel(prior_6)
                    self.draw_circle(pixel_point,radius,prior_6[4])

        #drawing top part of axis y
        ##y_axis_bottom = canvas.create_line(y_axis_bottom_1,y_axis_bottom_2,fill = "red", width = 2)

        if (a[3] != 0):

            for prior_5 in a[3]:

                    pixel_point = self.cord_to_pixel(prior_5)
                    self.draw_circle(pixel_point,radius,prior_5[4])

        #drawing axis x and z
        # # x_axis = canvas.create_line(x_axis_top,x_axis_bottom,fill = "green", width = 2)
        # # z_axis = canvas.create_line(z_axis_top,z_axis_bottom,fill = "blue", width = 2)

        if (a[4] != 0):

            for prior_4 in a[4]:

                    pixel_point = self.cord_to_pixel(prior_4)
                    self.draw_circle(pixel_point,radius,prior_4[4])

        #drawing top part of axis y
        # y_axis_top = canvas.create_line(y_axis_top_1,y_axis_bottom_1,fill = "red", width = 2)

        

        if (a[5] != 0):

            for prior_3 in a[5]:

                    pixel_point = self.cord_to_pixel(prior_3)
                    self.draw_circle(pixel_point,radius,prior_3[4])

        if (a[6] != 0):

            for prior_2 in a[6]:

                    pixel_point = self.cord_to_pixel(prior_2)
                    self.draw_circle(pixel_point,radius,prior_2[4])

        if (a[7] != 0):

            for prior_1 in a[7]:

                    pixel_point = self.cord_to_pixel(prior_1)
                    self.draw_circle(pixel_point,radius,prior_1[4])

    #assigning priorities for each function
    #depending on what quadrant a point is, it will have different priorities
    #this will help to determine which point is drawn over which axis

    def update_cords(self, cord_in):
        self.cord_system = cord_in

    def canvas_display(self):
        canvas = self.canvas
        canvas.pack()
        canvas.update()

    def canvas_destroy(self):
        canvas = self.canvas
        wd1 = self.wd1 = tkinter.Tk()
        canvas.destroy()
        wd1.mainloop()
            