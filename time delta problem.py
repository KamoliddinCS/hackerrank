# When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.
#
# Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:
#
# Day dd Mon yyyy hh:mm:ss +xxxx
#
# Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.
#
# Input Format
#
# The first line contains , the number of testcases.
# Each testcase contains  lines, representing time  and time .
#
# Constraints
#
# Input contains only valid timestamps
# .
# Output Format
#
# Print the absolute difference  in seconds.
#
# Sample Input 0
#
# 2
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000
# Sample Output 0
#
# 25200
# 88200
# Explanation 0
#
# In the first query, when we compare the time in UTC for both the time stamps, we see a difference of 7 hours. which is  seconds or  seconds.
#
# Similarly, in the second query, time difference is 5 hours and 30 minutes for time zone adjusting for that we have a difference of 1 day and 30 minutes. Or

import math
import os
import random
import re
import sys
import datetime


# Complete the time_delta function below.
def time_delta(t1, t2):
    s1 = t1
    s2 = t2

    fmt = '%a %d %b %Y %H:%M:%S  %z'

    dt1 = datetime.datetime.strptime(s1, fmt)
    dt2 = datetime.datetime.strptime(s2, fmt)

    day_difference = dt1.day - dt2.day
    hr_difference = dt1.hour - dt2.hour
    min_difference = dt1.minute - dt2.minute
    sec_difference = dt1.second - dt2.second

    print(day_difference, hr_difference)

    total_difference_seconds = day_difference*24*60**2 + hr_difference*60**2 + min_difference*60 + sec_difference

    dt1_hrs = int(dt1.timetz().strftime("%z")[0:3])
    dt2_hrs = int(dt2.timetz().strftime("%z")[0:3])
    dt1_mins = int(dt1.timetz().strftime("%z")[3:])
    dt2_mins = int(dt2.timetz().strftime("%z")[3:])
    dt1_sec = dt1_hrs * 60**2 + dt1_mins * 60 if dt1_hrs >= 0 else dt1_hrs * 60**2 - dt1_mins * 60
    dt2_sec = dt2_hrs * 60**2 + dt2_mins * 60 if dt2_hrs >= 0 else dt2_hrs * 60**2 - dt2_mins * 60
    print(dt1_hrs, dt1_mins, dt1_sec)
    td = abs(total_difference_seconds - abs(dt2_sec - dt1_sec))

    print(td)

t1 = input()
t2 = input()

time_delta(t1, t2)



# Sample Input 0
#
# 2
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000
# Sample Output 0
#
# 25200
# 88200



# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     t = int(input())
#
#     for t_itr in range(t):
#         t1 = input()
#
#         t2 = input()
#
#         delta = time_delta(t1, t2)
#
#         fptr.write(delta + '\n')
#
#     fptr.close()