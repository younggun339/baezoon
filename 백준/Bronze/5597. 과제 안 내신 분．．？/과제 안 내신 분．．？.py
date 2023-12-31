i = 0;
report_list = [];
report_list = set(report_list);
while i <28 :
    i = i +1;
    number = int(input());
    report_list.add(number);

j = 0;
Comparison_list = [];
Comparison_list = set(Comparison_list);

while j <30 :
    j = j+1;
    Comparison_list.add(j);

result_list = list(Comparison_list - report_list);
result_list.sort();

print((result_list)[0]);
print((result_list)[1]);

# while len(report_list)<30 :
#     j = 0;
#     while j <30 :
#         j = j + 1;
#         report_list.add(j);
#         if len(report_list)>29 :
#             print(j);
#             break;
        



