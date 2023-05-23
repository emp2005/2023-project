#this code is to make cordinates for a sphere
import math

PI = math.pi
overall_list = []
floor_list = []
cordinate_list = []

r=1
r_sub = 0
p=8
z_increments = r/p

distance_value = .6

#middle calculation [x,y,z]
floor_list.append([r,0,0])
for i in range(math.floor(2*PI*r/distance_value)):
    i=i+1
    floor_list.append([round(math.cos(distance_value*i),2),round(math.sin(distance_value*i),2),0])

cordinate_list.append(floor_list)

#posisitive z values
for i in range(p):
    floor_list = []
    z_val = (i+1)*z_increments
    r_sub = math.sqrt(r*r-z_val*z_val)
    for m in range(math.floor(2*PI*r_sub/distance_value)):
        radiant_angle = m*distance_value/r_sub
        floor_list.append([r_sub*math.cos(radiant_angle),r_sub*math.sin(radiant_angle),z_val])
        
    cordinate_list.append(floor_list)

for i in range(p):
    floor_list = []
    z_val = (i+1)*z_increments
    r_sub = math.sqrt(r*r-z_val*z_val)
    for m in range(math.floor(2*PI*r_sub/distance_value)):
        radiant_angle = m*distance_value/r_sub
        floor_list.append([r_sub*math.cos(radiant_angle),r_sub*math.sin(radiant_angle),-z_val])
        
    cordinate_list.append(floor_list)

cordinate_list.append([[0,0,r]])
cordinate_list.append([[0,0,-r]])


string_printout = ""


# for floors in range(z_repitition_value):
counter = 0

for floor0 in cordinate_list:
    for cordinate0 in floor0:

        counter += 1
        string_printout += str("s") + "("
        string_printout += str(cordinate0[0])
        string_printout += ","
        string_printout += str(cordinate0[1])
        string_printout += ","
        string_printout += str(cordinate0[2])
        string_printout += ")"

for p in cordinate_list:
    print(p)
    print("\n\n\n")

print("\n\n\n\n\n")
print(string_printout)
#a(1,2,3)

