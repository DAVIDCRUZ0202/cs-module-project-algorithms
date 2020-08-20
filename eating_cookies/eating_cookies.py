'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    if n < 0:
        return 0
    if n == 0:
        return 1

    else:
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")


# UPER

## Understand, Plan, Execute  , Reflect

"""
# given a number
# how many ways can you reach 0 from that number

# example : given 3
# (given 3) - 1 - 1 - 1 = 0
# (given 3) - 2 - 1 = 0
# (given 3) - 1 - 2 = 0
# (given 3) - 3 = 0
# you can reach 0 in 4 ways given 3

### To Understand
# Re-phrase the problem.
"""

# Make sure to fully grasp what is being asked
# If you understand what success looks like, you understand the problem


### To Plan
# Gather info nonstop
# get rid of repeat info 
"""
This question is asking for permutations.

Given a number (n)


"""
### Execute
# Execute the plan!

### Reflect on the results of the execution


