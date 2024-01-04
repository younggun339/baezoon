t = int(input());
i = 0;
s = "";
list = [];
while i < t :
    stra = str(input());
    s = stra[0] + stra[len(stra)-1];
    list.append(s);
    i = i + 1;

for li in list :
    print(li);