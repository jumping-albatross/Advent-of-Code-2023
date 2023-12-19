# Python3 implementation of the approach
# https://www.geeksforgeeks.org/flood-fill-algorithm/

def hello():
    print('hello')

# FloodFill function
def flood_fill(screen, r, c, prev_c, new_c):
    """Accepts grid screen as 2-d array, starting row and column as r, c, and the
    previous colour and new colour values"""

    queue = []
    m = len(screen)
    n = len(screen[0])

    # Append the position of starting 
    # pixel of the component
    queue.append([r, c])

    # Color the pixel with the new color
    screen[r][c] = new_c

    # While the queue is not empty
    while queue:

        # Dequeue the front node
        curr_pixel = queue.pop()

        pos_r, pos_c = curr_pixel

        # Check if the adjacent
        # pixels are valid
        for dr, dc in ((1,0),(0,1),(-1,0),(0,-1)):
            if 0 <= pos_r + dr < n and 0 <= pos_c + dc < m:
              if screen[pos_r + dr][pos_c + dc] == prev_c:
    
                  # Color with newC
                  # if valid and enqueue
                  screen[pos_r + dr][pos_c + dc] = new_c
                  queue.append([pos_r + dr, pos_c + dc])
    

def main():
    # Driver code
    o_screen =[
    [1, 1, 1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1, 0, 0], 
    [1, 0, 0, 1, 1, 0, 1, 1], 
    [1, 2, 2, 2, 2, 0, 1, 0], 
    [1, 1, 1, 2, 2, 0, 1, 0], 
    [1, 1, 1, 2, 2, 2, 2, 0], 
    [1, 1, 1, 1, 1, 2, 1, 1], 
    [1, 1, 1, 1, 1, 2, 2, 1], 
        ]
    
    # Row of the display
    m = len(o_screen)
    
    # Column of the display
    n = len(o_screen[0])
    
    # Co-ordinate provided by the user
    r = 4
    c = 4
    
    # Current color at that co-ordinate
    prev_c = o_screen[r][c]
    
    # New color that has to be filled
    new_c = "■"
    
    flood_fill(o_screen, r, c, prev_c, new_c)
    
    
    # Printing the updated screen
    for i in range(m):
        for j in range(n):
            print(o_screen[i][j], end =' ')
        print()

if __name__ == "__main__":
    main()