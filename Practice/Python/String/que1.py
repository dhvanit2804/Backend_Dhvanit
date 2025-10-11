s = input("Enter a string: ")
print(s)

al = 0
nm = 0
sp = 0
uc = 0
lc = 0
sy = 0

for i in s:
    
    if i.isalpha() :
        al = al + 1
    elif i.isnumeric() :
        nm = nm + 1
    elif i.isspace():
        sp = sp + 1
    else:
        sy = sy +1
    if i.isupper():
        uc = uc + 1
    elif i.islower():
        lc = lc + 1

print(f"Total Alphabets : {al}")
print(f"Total numeric : {nm}")
print(f"Total spaces : {sp}")
print(f"Total Upper Case : {uc}")
print(f"Total lower Case : {lc}")
print(f"Total special case : {sy}")