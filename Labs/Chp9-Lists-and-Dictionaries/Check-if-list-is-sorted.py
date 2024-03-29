""" Write the in_order() function, which has a list of integers as a parameter, and returns True if the integers are sorted (in order from low to high) or False otherwise. The program outputs "In order" if the list is sorted, or "Not in order" if the list is not sorted.

Ex: If the list passed to the in_order() function is [5, 6, 7, 8, 3], then the function returns False and the program outputs:

Not in order

Ex: If the list passed to the in_order() function is [5, 6, 7, 8, 10], then the function returns True and the program outputs:

In order

Note: Use a for loop. DO NOT use sorted() or sort().
 """
def in_order(nums):
    a = [nums[i-1] <= nums[i] for i in range(1, len(nums))]
    return all(x == a[0] for x in a)
    
if __name__ == '__main__':
    # Test out-of-order example
    nums1 = [5, 6, 7, 8, 3]
    if in_order(nums1):
        print('In order')
    else:
        print('Not in order')
        
    # Test in-order example
    nums2 = [5, 6, 7, 8, 10]
    if in_order(nums2):
        print('In order')
    else:
        print('Not in order')