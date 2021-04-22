"""
source
https://www.py4e.com/lessons/loops#
by Charles Severance
"""

zork = 0
sum = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing
    print(zork, thing)
print('After', zork)
