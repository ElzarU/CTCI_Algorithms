class Solution:
    def zero_matrix(self, matrix):
        """
        If an element in an MxN matrix is 0, sets its entire row and column to 0.

        Parameters:
            matrix (List[List[int]]): A 2D list representing the matrix.

        Returns:
            None: Modifies the matrix in place.

        Approach:
            - First pass: identify rows and columns containing zeros.
            - Second pass: set identified rows and columns to zero.

        Example:
            Input:
                1 2 3
                4 0 6
                7 8 9
            Output:
                1 0 3
                0 0 0
                7 0 9
        """
        if not matrix or not matrix[0]:
            return

        rows = set()
        cols = set()

        # First pass: record rows and columns with zeros
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Second pass: zero out rows
        for i in rows:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0

        # Second pass: zero out columns
        for j in cols:
            for i in range(len(matrix)):
                matrix[i][j] = 0

matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]

Solution().zero_matrix(matrix)
for row in matrix:
    print(row)