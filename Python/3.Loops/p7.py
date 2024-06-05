# 7. Write a program to print 1 to 10 using the do-while loop statement.

"""
Python does not have a built-in do-while loop construct like some other programming languages (e.g., C, C++, Java). However, you can mimic the behavior of a do-while loop using a while loop. The key characteristic of a do-while loop is that the loop body executes at least once before the condition is tested.
"""

i = 0
while True:
    print(i)
    i+=1
    if i>10:
        break
