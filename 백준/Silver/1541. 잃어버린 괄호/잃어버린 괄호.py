



import sys

seq = []
input_data = sys.stdin.readline().strip()
seq = [str(x) for x in input_data.split('-')]

# print(seq)

result = 0
i = 0

for seqeunce in seq:
    number_list = seqeunce.split('+')
    int_list = list(map(int, number_list))
    sum_num = sum(int_list)

    if i == 0 :
        result += sum_num
        i += 1
    else :
        result -= sum_num

print(result)