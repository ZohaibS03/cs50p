user_var = input("camelCase: ")
final_var = []

for i in range(len(user_var) - 1):
    if user_var[i].isupper() == True:
        final_var.append("_{}".format(user_var[i].lower()))
    elif user_var[i].isalpha() or user_var[i].isalnum():
        final_var.append(user_var[i])
    else:
        continue

for i in range(len(final_var)-1):
    print(final_var[i], end = " ")
        
    
