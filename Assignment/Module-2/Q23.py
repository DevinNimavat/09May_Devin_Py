a=input("Enter a first String: ")

add_str=input("Enter a second string: ")

x=a.find(" ")

new_str=a[:x] + " " + add_str + " " + a[x+1: ]

print(new_str)