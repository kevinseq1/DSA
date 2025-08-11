# Time Complexity: O(N^2)
# Space Complexity: O(1)

def three_sum(nums):

    # Sort the input array in ascending order (n log n)
    nums.sort()

    # Create an empty array to store the unique triplets
    results = []

    # Store the length of the array in a variable
    n = len(nums)

    # Iterate over the array till n - 2
    for i in range(n - 2):
        
        # If the current number is greater 0, break the loop
        if n[i] > 0:
            break
        
        # The current element is either the first element or not a duplicate of the previous element
        if i == 0 or nums[i] != nums[i - 1]:

            # Initialize two pointers
            low = i + 1
            high = n - 1

            # Run the loop as long a low is less than high
            while low < high:

                # Calculate the sum of the triplets
                sum = nums[i] + nums[low] + nums[high]

                # If the sum is less than 0, move the low pointer forward
                if sum < 0:
                    low += 1

                # If the sum is greater than 0, move the high pointer backward
                elif sum > 0:
                    hight -= 1
                else:
                    # Add the triplet to the result as this triplet sums to 0
                    results.append([nums[i], nums[low], nums[high]])

                    # Move both pointers to the next distinct values to avoid dupicate triplets
                    low += 1
                    high -= 1
                    
                    # Keep moving left forward as long as low < high and low is not equal to low - 1 
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                    
                    # Keep moving right backward as long as low < high and right is not equal to right + 1
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1

            
    
    # Return result, which contains all unique triplets that sum to zero
    return results