## Question

# In a university, your attendance determines whether you will be
# allowed to attend your graduation ceremony.
# You are not allowed to miss classes for four or more consecutive days.
# Your graduation ceremony is on the last day of the academic year,
# which is the Nth day.

# Your task is to determine the following:
# 1. The number of ways to attend classes over N days. () 
# 2. The probability that you will miss your graduation ceremony.

# Represent the solution in the string format as "Answer of (2) / Answer of (1)", 
# don't actually divide or reduce the fraction to decimal

# Test cases:
# for 5 days: 14/29
# for 10 days: 372/773

def draduation_ceremony(number):
    if number < 1:
        return "Invalid Input"
    
    if number < 4:
        # No restriction on 4 consecutive days, 
        # 1 So 2^number to attend classes
        # 2 missed graduation 2^(number-1)
        return str(2**(number-1))+"/"+str(2**number)
    
    invalid = [0 for _ in range(number + 1)]
    invalid[0] = None # none for zero
    invalid[4] = 1    

    for i in range(5, number + 1):
        invalid[i] = (2 ** (i - 4)) + invalid[i - 4] + invalid[i - 3] + invalid[i - 2] + invalid[i - 1]
    #print(invalid)

    allowed = [0 for _ in range(number + 1)]
    allowed[0] = None
    for i in range(1, number + 1):
        allowed[i] = (2 ** i) - invalid[i]

    # probability = total_ways_to_miss - invalid_consecutive_days
    probability = allowed[number] - allowed[number - 1]
    return str(probability) + "/" + str(allowed[number])

#Test cases
print(draduation_ceremony(5))
print(draduation_ceremony(10))
print(draduation_ceremony(3))