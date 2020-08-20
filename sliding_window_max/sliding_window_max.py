'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

def sliding_window_max(nums, k):
    arrayLength = len(nums)
    maxs = []
    m = 0
    while k <= arrayLength:
        
        window = nums[m:k]

        localMax = max(window)

        m += 1
        k += 1

        maxs.append(localMax)

    return maxs

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

# UPER

## Understand, Plan, Execute  , Reflect


### To Understand
# Re-phrase the problem.
# Make sure to fully grasp what is being asked
# If you understand what success looks like, you understand the problem
"""
Given an array(arr) indefinitely long

create a sub-array of a given size(k)

which will traverse the entire array one element at a time

and will return the greatest element of the sub-array each time it moves forward
"""


### To Plan
# Gather info nonstop
# get rid of repeat info 

"""
the array is called arr

the sub array is defined by length k

sub array must be of size k, and advance through arr 1 index position at a time
this can be i+1

get the max of the sub-array and append it to some result array before moving onto
the next sub array
"""


### Execute
# Execute the plan!

### Reflect on the results of the execution

