# 1. Basic - Print all integers from 0 to 150.
for count in range(151):
    print (count)

# 2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for count in range(5, 1005, 5):
    print(count)

# 3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for x in range(1,101):
    if x % 5 == 0 and x % 10 != 0:
        print("Coding")
    elif x % 10 == 0:
        print("Coding Dojo")
    else:
        print(x)


# 4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for num in range (0, 500001):
    if num % 2 != 0:
        sum = sum + num
print(total)

# 5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for num in range(2018,-1, -4):
    num += 1
    print(num)

# 6. Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
mult = 3
highNum = 9
lowNum = 2
for count in range(lowNum, highNum + 1):
    if count % mult == 0:
        print(count)