import math
import os
import random
import re
import sys
from string import capwords


# Complete the solve function below.
def solve(s):
    return re.sub(r'\b(\d*[A-Za-z])', lambda mo: mo.group(0)[0].upper() + mo.group(0)[1:], s)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


