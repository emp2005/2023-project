import math

def deg_to_rad(deg):

    rad = (deg/360)*2*math.pi
    return rad

rad_30 = deg_to_rad(30)

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

def draw_lines(all_con):
    for connections in all_con:

        print(cord_to_pixel(connections[0])[0])
        print(cord_to_pixel(connections[0])[1])
        print(cord_to_pixel(connections[1])[0])
        print(cord_to_pixel(connections[1])[1])
        print("----------------")

test = [[['1',-3,0,0],['1',1,-1,1]],[['1',1,0,1],['1',-1,-1,-1]],[['1',-1,-1,-1],['1',0,0,0]]]
#draw_lines([[['1',0,0,0],['1',1,-1,1]],[['1',1,1,1],['1',-1,-1,-1]],[['1',-1,-1,-1],['1',0,0,0]]])
draw_lines(test)