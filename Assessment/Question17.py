""" Complete the calc_average() method that has an integer list parameter and returns the average value of the elements in the array as a double.

Ex: If the input array is:

1 2 3 4 5

then the returned average will be:

3.0

 """
def calc_average(nums):
    total = 0
    average = 0
    for num in nums:
        total += num
    average = total / len(nums)
    return average
    
if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    print(calc_average(nums))   # calc_average() should return 3.0