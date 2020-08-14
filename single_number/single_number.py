'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):

    for i in arr:
        #set var for current value
        num = arr[i]
        # remove current index
        arr.pop(i)
        if num in arr:
            #if the number we are iterating on is in the array still add the number back
            arr.append(num)
        else:
            #otherwise return the number
            return num




if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
