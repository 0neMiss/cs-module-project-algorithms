'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):

    if len(arr) < 2:
        return 'There needs to be more than one number in the array.'
    #creates a list filled with the number of None values equal to the lenghtn of the array
    arr_of_products =  [None] * len(arr)
    print(f'array of products: {arr_of_products}')
    #sets variable to change the current iteration value to 1 in order to remove it from the toal product
    current_product = 1
 #fills the arr_of_products with every value in the array, except for the one in the iteration, that is changed to 1
    for i in range(len(arr)):
        #sets current index to 1 so that it does not add anything to the total product
        arr_of_products[i] = current_product
        print(f'array of products[i] line 15: {arr_of_products[i]}')
        # multiply and update current_product with each item in the array
        current_product *= arr[i]
        print(f'current_product line 17: {current_product}')
        print(f'arr_of_products line 18: {arr_of_products}')
    #reset current product to 1
    current_product = 1
    for i in range(len(arr) - 1, -1, -1):
        #
        arr_of_products[i] *= current_product
        print(f'arr_of_products: {arr_of_products[i]}')
        current_product *= arr[i]
        print(f'arr_of_products: {current_product}')
    return arr_of_products


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
