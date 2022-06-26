# takuzu.py: Template para implementacao do projeto de Inteligencia Artificial 2021/2022.
# Devem alterar as classes e funcoes neste ficheiro de acordo com as instrucoes do enunciado.
# Alem das funcoes e classes ja definidas, podem acrescentar outras que considerem pertinentes.

# Grupo 030:
# 89627 Gustavo Pinto
# 98876 Tomas Cayatte

import sys
from search import (
    Problem,
    Node,
    astar_search,
    breadth_first_tree_search,
    depth_first_tree_search,
    greedy_search,
    recursive_best_first_search,
)

class TakuzuState:
    state_id = 0

    def __init__(self, board):
        self.board = board
        self.id = TakuzuState.state_id
        TakuzuState.state_id += 1

    def __lt__(self, other):
        return self.id < other.id
    
    def getBoard(self):
        return self.board

    # TODO: outros metodos da classe

class Board:
    """Representação interna de um tabuleiro de Takuzu."""
    def __init__(self):
        stdin = Board.parse_instance_from_stdin()
        self.board = []

        self.size = stdin[1]
        for line in stdin[0]:
            row = []
            for char in line:
                if char != ' ':
                    row.append(int(char))
            
            self.board.append(row)

    def get_number(self, row: int, col: int) -> int:
        """Devolve o valor na respetiva posição do tabuleiro."""

        return self.board[row - 1][col - 1]

    def adjacent_vertical_numbers(self, row: int, col: int) -> (int, int):
        """Devolve os valores imediatamente abaixo e acima,
        respectivamente."""

        if (row - 2 < 0):
            sup_lim = None
        else:
            sup_lim = self.board[row - 2][col - 1]

        if (row >= self.size):
            inf_lim = None
        else:
            inf_lim = self.board[row][col - 1]
        
        return (inf_lim, sup_lim)        

    def adjacent_horizontal_numbers(self, row: int, col: int) -> (int, int):
        """Devolve os valores imediatamente a esquerda e a direita,
        respectivamente."""
        
        if (col - 2 < 0):
            inf_lim = None
        else:
            inf_lim = self.board[row - 1][col - 2]

        if (col >= self.size):
            sup_lim = None
        else:
            sup_lim = self.board[row - 1][col]
        
        return (inf_lim, sup_lim)  

    def double_adjacent_up(self, row: int, col: int):
        """ Devolve os dois valores imediatamente acima """
        if (row + 1 >= self.size):
            up_adj = None
        else:
            up_adj = self.board[row + 1][col]
        if (row + 2 >= self.size):
            up_next_adj = None
        else:
            up_next_adj = self.board[row + 2][col]
        return (up_adj, up_next_adj)

    def double_adjacent_down(self, row: int, col: int):
        """ Devolve os dois valores imediatamente abaixo """
        if (row - 1 < 0):
            down_adj = None
        else:
            down_adj = self.board[row - 1][col]
        if (row - 2 < 0 ):
            down_next_adj = None
        else:
            down_next_adj = self.board[row - 2][col]
        return (down_adj, down_next_adj)

    def double_adjacent_right(self, row: int, col: int):
        """ Devolve os dois valores imediatamente a direita """
        if (col + 1 >= self.size):
            right_adj = None
        else:
            right_adj = self.board[row][col + 1]
        if (col + 2 >= self.size):
            right_next_adj = None
        else:
            right_next_adj = self.board[row][col + 2]
        return (right_adj, right_next_adj)
    
    def double_adjacent_left(self, row: int, col: int):
        """ Devolve os dois valores imediatamente a esquerda """
        if (col - 1 < 0):
            left_adj = None
        else:
            left_adj = self.board[row][col - 1]
        if (col - 2 < 0):
            left_next_adj = None
        else:
            left_next_adj = self.board[row][col - 2]
        return (left_adj, left_next_adj)
        

    @staticmethod
    def parse_instance_from_stdin():
        """Le o test do standard input (stdin) que e passado como argumento
        e retorna uma instância da classe Board.
        
        Por exemplo:
            $ python3 takuzu.py < input_T01

            > from sys import stdin
            > stdin.readline()
        """
        
        file = open('input.txt', 'r')
        lines = [line.rstrip() for line in file.readlines()]

        size = int(lines[0])
        lines = lines[1:]
        
        return (lines, size)

    # TODO: outros metodos da classe
    def print_board(self):
        i = 0
        while i < self.size:
            print('\t'.join(map(str, self.board[i])))
            
            i += 1
            if i < self.size:
                print('\n')


class Takuzu(Problem):
    def __init__(self, board: Board):
        """O construtor especifica o estado inicial."""
        self.initial = Board(board)
        pass

    def actions(self, state: TakuzuState):
        """Retorna uma lista de acoes que podem ser executadas a
        partir do estado passado como argumento."""
        # TODO
        for row in range(state.board.size):
            for col in range(state.board.size):
                if state.board.get_number(row, col) != 2:
                    continue
                pass
        

    def result(self, state: TakuzuState, action):
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A acao a executar deve ser uma
        das presentes na lista obtida pela execucao de
        self.actions(state)."""
        # TODO
        pass

    def goal_test(self, state: TakuzuState):
        """Retorna True se e só se o estado passado como argumento e
        um estado objetivo. Deve verificar se todas as posicoes do tabuleiro
        estao preenchidas com uma sequencia de números adjacentes."""
        # TODO
        pass

    def h(self, node: Node):
        """Funcao heuristica utilizada para a procura A*."""
        # TODO
        pass

    # TODO: outros metodos da classe


if __name__ == "__main__":
    # TODO:
    # Ler o ficheiro do standard input,
    # Usar uma tecnica de procura para resolver a instância,
    # Retirar a solucao a partir do nó resultante,
    # Imprimir para o standard output no formato indicado.
    pass
