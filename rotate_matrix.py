class Solution:
    def rotate_matrix(self, matrix):
        """
        Rotates an NxN matrix by 90 degrees clockwise in-place.

        Each pixel in the image is represented as a 4-byte element, 
        but this implementation rotates using element indices, not size.

        Parameters:
            matrix (List[List[int]]): A square 2D list representing the image.

        Returns:
            None: Modifies the matrix in place.

        Approach:
            - Work layer by layer from outermost to innermost.
            - For each layer, perform a 4-way swap for the corresponding elements:
                - Top → Right
                - Right → Bottom
                - Bottom → Left
                - Left → Top

        Example:
            Input:
                1 2 3
                4 5 6
                7 8 9
            Output:
                7 4 1
                8 5 2
                9 6 3
        """
        n = len(matrix)
        for layer in range(n // 2):
            first = layer
            last = n - 1 - layer

            for i in range(first, last):
                offset = i - first

                # Save top
                top = matrix[first][i]

                # left → top
                matrix[first][i] = matrix[last - offset][first]

                # bottom → left
                matrix[last - offset][first] = matrix[last][last - offset]

                # right → bottom
                matrix[last][last - offset] = matrix[i][last]

                # top → right
                matrix[i][last] = top

# Testcase:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original matrix:")
for row in matrix:
    print(row)

print()
Solution().rotate_matrix(matrix)

print("Rotated matrix:")
for row in matrix:
    print(row)