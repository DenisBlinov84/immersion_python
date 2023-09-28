#  Напишите функцию для транспонирования матрицы.

def create_matrix(rows: int = 4, cols: int = 5) -> list[list]:
    from random import randint

    result = [[randint(1, 10) for _ in range(cols)] for _ in range(rows)]

    return result


def transpose_matrix(matrix: list[list]) -> list[list]:
    result = [[matrix[r][c] for r in range(len(matrix))] for c in range(len(matrix[0]))]

    return result


def print_matrix(matrix: list[list], massage: str = 'Матрица') -> None:
    print(massage)

    for r in range(len(matrix)):
        print()
        for c in range(len(matrix[0])):
            print(matrix[r][c], end='\t')
        print('\n\n')


if __name__ == '__main__':
    original_matrix = create_matrix(4, 5)
    print_matrix(original_matrix, 'Исходная матрица:')
    transposed_matrix = transpose_matrix(original_matrix)
    print_matrix(transposed_matrix, 'Транспонированая матрица:')
