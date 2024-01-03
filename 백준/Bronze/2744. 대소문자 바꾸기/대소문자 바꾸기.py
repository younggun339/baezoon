sequence = str(input());
convertsequence = "";
for i in sequence :
    i = str(i);
    if i.isupper() :
        convert = i.lower();
        convertsequence = convertsequence + convert;
    else :
        convert = i.upper();
        convertsequence = convertsequence + convert;

print(convertsequence);