kilometre= ["km","cm","mm"]
t = True

while t :
    distance= float(input("entre une distance: "))
    unit= (input("entre une unité de mesure (km,cm,mm : "))
    mesure = unit in kilometre 

    if mesure == "km":
        metre= distance % 1000
        print(f"{distance} {unit} = {metre} m")
    elif mesure == "cm":
        metre= distance * 100
        print(f"{distance} {unit} = {metre} m")
    elif mesure == "mm":
        metre= distance * 1000
        print(f"{distance} {unit} = {metre} m")
    else :
        print("unité de mesure non reconnue")

        t = False
       
