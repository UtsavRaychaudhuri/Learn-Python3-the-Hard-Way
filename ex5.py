name='Zed A. Shaw'
age=35 # not a lie
height= 74 #inches
weight= 180
eyes= 'Blue'
teeth='White'
hair='Brown'
height_in_centimeters=height*2.54
weight_in_kilograms=weight*0.453592
print(f"Let's talk about {name}.")
print(f"He's {height_in_centimeters} centimeters tall.")
print(f"He's {weight_in_kilograms} kilograms heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky try to get it exactly right
total = age+height_in_centimeters+weight_in_kilograms
print(f"If i add {height_in_centimeters}, {weight_in_kilograms}, {age} I get {total}.")