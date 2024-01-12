nine = []
while True:
    try:
        input_data = input()
        # if input_data == "":
        #     break
        # else:
        nine.append(int(input_data))
    except:
        break

register = 0;

for num in nine :
    if register == 0 :
        register = num
    else :
        if num > register :
            register = num
    

i = 1
for a in nine :
    if register == a :
        break
    else :
        i = i +1;


print(register)
print(i)