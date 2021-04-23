"""
source
https://www.py4e.com/lessons/loops#
by Charles Severance
"""

count = 0
sum = 0
print('Befor', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum/count)
