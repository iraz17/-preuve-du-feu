import sys

def load_board(file_path):
    try:
        with open(file_path, 'r') as file:
            return [list(line.strip()) for line in file]
    except FileNotFoundError:
        sys.exit(f"Erreur : Le fichier {file_path} n'existe pas.")

def load_shape(file_path):
    try:
        with open(file_path, 'r') as file:
            return [list(line.strip()) for line in file]
    except FileNotFoundError:
        sys.exit(f"Erreur : Le fichier {file_path} n'existe pas.")

def find_shape(board, shape):
    shape_height = len(shape)
    shape_width = len(shape[0])

    for i in range(len(board) - shape_height + 1):
        for j in range(len(board[0]) - shape_width + 1):
            found = True
            for si in range(shape_height):
                for sj in range(shape_width):
                    if board[i + si][j + sj] != shape[si][sj]:
                        found = False
                        break
                if not found:
                    break
            if found:
                return i + 1, j + 1  # Ajuster les coordonnées pour commencer à partir de 1
    return None

def print_result(result):
    if result:
        i, j = result
        print("Trouvé !")
        print(f"Coordonnées : {i},{j}")
        print("----")
        for row in board:
            print("".join(row))
    else:
        print("Introuvable")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage : python exo.py board_file.txt shape_file.txt")

    board_file_path = sys.argv[1]
    shape_file_path = sys.argv[2]

    board = load_board(board_file_path)
    shape = load_shape(shape_file_path)

    result_board = find_shape(board, shape)
    print_result(result_board)

