"""
找出100~999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
如: 153 = 1**3 + 5**3 + 3**3

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""

for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)


        
     //另一种方法   
 for x in range(1,10):
    for y in range(0,10):
        for z in range(0,10):
            m = x**3 + y**3 +z**3
            n = x*100 + y*10 + z
            if m == n:
                print(m)
