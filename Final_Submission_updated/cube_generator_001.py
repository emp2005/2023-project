#this code is to make cordinates for a sphere
import math

PI = math.pi
overall_list = []
floor_list = []
######################
rounding_digit = 2
rotations = 6
p=8
r=2
########################
r_sub = 0
z_increments = r/p
radiants = 0
distance_value = .6
#middle calculation [x,y,z]
for i in range(p-1):
    z_val = (i+1)*z_increments
    r_sub = math.sqrt(r*r-z_val*z_val)
    for t in range(rotations):
        radians = (t+1)*PI*2/rotations
        floor_list.append([round(r_sub*math.cos(radians),rounding_digit),round(r_sub*math.sin(radians),rounding_digit),round(z_val,rounding_digit)])
    overall_list.append(floor_list)
    floor_list = []

for i in range(p-1):
    z_val = (i+1)*z_increments
    r_sub = math.sqrt(r*r-z_val*z_val)
    for t in range(rotations):
        radians = (t+1)*PI*2/rotations
        floor_list.append([round(r_sub*math.cos(radians),rounding_digit),round(r_sub*math.sin(radians),rounding_digit),-round(z_val,rounding_digit)])
    overall_list.append(floor_list)
    floor_list = []

overall_list.append([[0,0,r]])
overall_list.append([[0,0,-r]])

#a(1,2,3)
#c[1,1,1]c[1,1,-1]c[1,-1,1]c[-1,1,1]c[-1,-1,1]c[-1,1,-1]c[1,-1,-1]c[-1,-1,-1]

string_printout = ""


# for floors in range(z_repitition_value):
counter = 0

for floor0 in overall_list:
    for cordinate0 in floor0:

        counter += 1
        string_printout += str("s") + "("
        string_printout += str(cordinate0[0])
        string_printout += ","
        string_printout += str(cordinate0[1])
        string_printout += ","
        string_printout += str(cordinate0[2])
        string_printout += ")"

for p in overall_list:
    print(p)
    print("\n\n\n")

print("\n\n\n\n\n")
print(string_printout)
#a(1,2,3)

