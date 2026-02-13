"""
Seconds to Time converter

This programa takes a total number of seconds as input
and converts it into hours, minutes and seconds
"""
x = int(input("Enter total second"))
H = x // 3600
R = x % 3600
M = R // 60
S = R % 60
print("Hours", H)
print("Minuts", M)
print("Secound", S)
