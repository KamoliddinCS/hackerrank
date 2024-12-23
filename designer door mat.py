# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
#
# Mat size must be X. ( is an odd natural number, and  is  times .)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.
# Sample Designs
#
#     Size: 7 x 21
#     ---------.|.---------
#     ------.|..|..|.------
#     ---.|..|..|..|..|.---
#     -------WELCOME-------
#     ---.|..|..|..|..|.---
#     ------.|..|..|.------
#     ---------.|.---------
#
#     Size: 11 x 33
#     ---------------.|.---------------
#     ------------.|..|..|.------------
#     ---------.|..|..|..|..|.---------
#     ------.|..|..|..|..|..|..|.------
#     ---.|..|..|..|..|..|..|..|..|.---
#     -------------WELCOME-------------
#     ---.|..|..|..|..|..|..|..|..|.---
#     ------.|..|..|..|..|..|..|.------
#     ---------.|..|..|..|..|.---------
#     ------------.|..|..|.------------
#     ---------------.|.---------------
# Input Format
#
# A single line containing the space separated values of  and .
#
# Constraints
#
# Output Format
#
# Output the design pattern.
#
# Sample Input
#
# 9 27
# Sample Output
#
# ------------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---
# ----------WELCOME----------
# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------

n, m = list(map(int, input().split()))

e1 = ".|."
e2 = "-"

for i in range(1, int(n/2)+1):
    print(e1.center(m, e2))
    e1 += '.|.'*2

print('WELCOME'.center(m, e2))
e1 = ".|."

for i in range(n-2, 0, -2):
    print((e1*i).center(m, e2))
