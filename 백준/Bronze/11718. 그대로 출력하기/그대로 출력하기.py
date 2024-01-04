sequence = "";
while True :
    try :
        a = str(input());
        if sequence == "" :
            sequence = a;
        else :   
            sequence = sequence + "\n" + a;
    except :
        print(sequence);
        break;

# a = "";
# b = str(input());
# if a == "" :
#     a = b;
# else :
#     a = a + "\n" + b;

# print(a);