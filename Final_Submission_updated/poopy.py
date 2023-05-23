#creating a function which converts a list of cordinates directly to a graphic
    def cord_to_graphic(self,a,):

        

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