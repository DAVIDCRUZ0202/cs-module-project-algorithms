'''
Input: a List of integers
Returns: a List of integers
'''

import numpy as np

def product_of_all_other_numbers(arr):
    results = []

    for i in arr:
        q = i

        x = [i for i in arr]

        x.remove(q)

        results.append(np.prod(x))

    return results

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")


    # UPER

## Understand, Plan, Execute  , Reflect


### To Understand
# Re-phrase the problem.
# Make sure to fully grasp what is being asked
# If you understand what success looks like, you understand the problem
"""
Write a function that receives an array of integers

and returns an array of products

each product in the returned array should be the result of 
multiplying each value EXCEPT for the index value which was passed through
"""


### To Plan
# Gather info nonstop
# get rid of repeat info 
"""
Python prod() for multiplication

for loop to pass through each value

append the product of all values except for the one being passed through
to a new array to be returned
"""


### Execute
# Execute the plan!
"""
through some bug fixing the execution is a success
"""

### Reflect on the results of the execution
"""
Major Takeaways

 - Duplicates are tricky!
 -- When working with arrays of integers, be careful of list comprehension.
 --- Using "!=" which is the not equals operator will 
 ---- refine results to the point where all duplicate values will be removed
 ---- not just the original index value. This will alter the returned list by 
 ----- more than just one value.
"""



 
