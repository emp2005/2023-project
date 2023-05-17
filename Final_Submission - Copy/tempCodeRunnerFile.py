def draw_line(cool):
    cool = input("enter the stuff: ")
    cool = cool + " "
    output_list = []
    l_double = []
    name = ""

    for i in cool:
        if (i == "&"):
            l_double.append(name)
            name = ""
        elif (i == " "):
            l_double.append(name)
            output_list.append(l_double)
            name = ""
            l_double = []
        else:
            name = name + i