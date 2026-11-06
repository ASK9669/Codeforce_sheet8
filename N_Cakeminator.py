rows, columns = map(int, input().split())
grid = [input().strip() for _ in range(rows)]

empty_rows = [all(cell != "S" for cell in row) for row in grid]
empty_columns = [
    all(grid[row][column] != "S" for row in range(rows))
    for column in range(columns)
]

eaten = sum(columns for is_empty in empty_rows if is_empty)
eaten += sum(
    1
    for row in range(rows)
    for column in range(columns)
    if not empty_rows[row] and empty_columns[column]
)

print(eaten)