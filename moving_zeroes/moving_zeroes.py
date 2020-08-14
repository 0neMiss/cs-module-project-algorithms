'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    for i in range(len(arr)- 1):
        # if the value is 0
        if arr[i] == 0:
            #remove the value and append 0 at the end of the array
            arr.pop(i)
            arr.append(0)
        else:
            #if the value is not 0 add it to the front of the array, and then pop the original value
            arr.insert(0, arr[i])
            arr.pop(i + 1)
    return arr



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
