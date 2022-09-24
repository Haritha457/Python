def movesToChessboard(board):

	n = len(board)

	# Loop to check whether the board
	# can be made valid or not
	for r in range(0, n):
		for c in range(0, n):
			if (board[0][0] ^ board[r][0] ^ board[0][r] ^ board[r][r] == 1):
				return -1

	rowsum = 0
	colsum = 0
	rowswap = 0
	colswap = 0

	# Loop to calculate sum and swap
	for i in range(0, n):
		rowsum += board[i][0]
		colsum += board[0][i]
		rowswap += board[i][0] == i % 2
		colswap += board[0][i] == i % 2

	# If there are more white or more black
	if (rowsum != n // 2 and rowsum != (n + 1) // 2):
		return -1
	if (colsum != n // 2 and colsum != (n + 1) // 2):
		return -1

	# If n is odd
	if (n % 2):
		if (rowswap % 2):
			rowswap = n - rowswap
		if (colswap % 2):
			colswap = n - colswap

	# If n is even
	else:
		rowswap = min(rowswap, n - rowswap)
		colswap = min(colswap, n - colswap)

	# Return the ans
	return (rowswap + colswap) // 2



arr = [[0, 1, 1, 0],[0, 1, 1, 0],[1, 0, 0, 1],[1, 0, 0, 1]]

minswap = movesToChessboard(arr)

print(arr)
if (minswap == -1):
	print("Impossible")
else:
	print(minswap)
