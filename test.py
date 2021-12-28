# Sample Input :
#    5
# Sample Output :
#  5432*
#  543*1
#  54*21
#  5*321
#  *4321

n = int(input())
for i in range(1, n+1):
    for j in range(1, n+1):
        if i >= j:
            print(i, end='')
        else:
            print('*', end='')
    print()