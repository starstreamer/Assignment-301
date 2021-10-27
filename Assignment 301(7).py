
def sumodd():
    sum=0
    for num in range(100):
        if num%2==1:
            sum = sum+num
    return (sum)

def sumeven():
    sum=0
    for num in range(100):
        if num % 2 == 0:
            sum = sum + num
    return (sum)

def sum_oddeven():
    print("The Sum of all evens and sum of all odds from 0 to 100 is: ", sumodd()+sumeven())
    print("===========================================================")

for num_even in range(100):
    for num_odd in range(100):
        if num_odd%2 == 1:
            pass
    if num_even%2 == 0:
        pass

sum_oddeven()