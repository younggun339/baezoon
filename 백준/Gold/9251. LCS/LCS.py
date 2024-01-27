
import sys


seq_row_basic = list(map(str,sys.stdin.readline().rstrip()))
seq_col_basic = list(map(str,sys.stdin.readline().rstrip()))


seq_row = ['0'] + seq_row_basic
seq_col = ['-1'] + seq_col_basic

# print(seq_row)

LCS = [ [0 for _ in range(len(seq_row))] for _ in range(len(seq_col))]

# print(LCS)

for j in range(1,len(seq_col)):
    for i in range(1,len(seq_row)):
        if seq_col[j] == seq_row[i]:
            LCS[j][i] = LCS[j-1][i-1] + 1
        elif seq_col[j] != seq_row[i]:
            LCS[j][i] = max(LCS[j-1][i], LCS[j][i-1])

print(LCS[len(seq_col)-1][len(seq_row)-1])
