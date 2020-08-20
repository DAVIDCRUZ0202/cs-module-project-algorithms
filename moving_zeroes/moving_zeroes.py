'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    for i in arr:
        if i == 0:
            arr.remove(i)
            arr.append(i)
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

    # UPER

## Understand, Plan, Execute  , Reflect


### To Understand
# Re-phrase the problem.
# Make sure to fully grasp what is being asked
# If you understand what success looks like, you understand the problem


""" 

Understand!

Given an array of ints

move each non-zero to the left, and return the updated array

"""

### To Plan
# Gather info nonstop
# get rid of repeat info 


"""
check each element of the arr

if the element is 0, pop it and append it

once the loop is done, return the updated array
"""



### Execute
# Execute the plan!
"""
execution was a success
"""

### Reflect on the results of the execution
"""
This function, instead of checking for non-zeros, hacks the question by identifying 0's

If we can identify each 0, we can remove it from the array and simply append it to the end
"""
