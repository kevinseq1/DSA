# Time Complexity: O(N)
# Space Complexity: O(1)

def sort_colors(colors: int):

    start = 0
    current = 0
    end = len(colors) - 1

    while current <= end:
        
        # Color is red 
        if colors[current] == 0:

            # Move the red color to the location of the start pointer
            colors[start], colors[current] = colors[current], colors[start]

            # Update the pointers
            start += 1
            current += 1

        # Color is white
        elif colors[current] == 1:
            current += 1

        # Color is blue
        else:

            # Move the blue color to the location of the end pointer
            colors[current], colors[end] = colors[end], colors[current]
            
            # Update only the end pointer
            end -= 1
    
    return colors
            