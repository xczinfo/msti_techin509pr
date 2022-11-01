from typing import List

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]


def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """
    # Implement your code here.

    width = len(board)
    height = len(board[0])

    if x > width or y > height:
        return []

    output_board = input_board[:]

    def dfs_4Neighbor(x: int, y: int):
        if 0 <= x < width and 0 <= y < height and output_board[x][y] == old and output_board[x][y] != new:
            output_board[x] = paint_color(output_board, x, y, new)
            dfs_4Neighbor(x + 1, y)
            dfs_4Neighbor(x - 1, y)
            dfs_4Neighbor(x, y + 1)
            dfs_4Neighbor(x, y - 1)
        else:
            return

    dfs_4Neighbor(x, y)
    return output_board


def paint_color(input: List[str], x: int, y: int, new: str) -> List[str]:
    output_line = input[x][:y] + new + input[x][y + 1:]
    return output_line

# Main function
modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)
for a in modified_board:
    print(a)

# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....