# takuzu.py: Template para implementacao do projeto de Inteligencia Artificial 2021/2022.
# Devem alterar as classes e funcoes neste ficheiro de acordo com as instrucoes do enunciado.
# Alem das funcoes e classes ja definidas, podem acrescentar outras que considerem pertinentes.

# Grupo 030:
# 89627 Gustavo Pinto
# 00000 Nome2

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

    # TODO: outros metodos da classe


class Board:
    """Representacao interna de um tabuleiro de Takuzu."""

    def __init__(self, board):
        self.board = board[:]
        self.size=len(board[0])
        self.toFill = 0
        for row in board:
            for number in board[row]:
                if (number == 2):
                    self.toFill += 1


    def get_number(self, row: int, col: int) -> int:
        """Devolve o valor na respetiva posicao do tabuleiro."""
        if row<0 or row>=self.size or col < 0 or col>=self.size:
            return None
        return self.board[row][col]
    
    def adjacent_vertical_numbers(self, row: int, col: int) -> (int, int):
        """Devolve os valores imediatamente abaixo e acima,
        respectivamente."""
        if 0<=row<self.size and 0<=col<self.size:
            x1=Board.get_number(self,row+1,col)
            x2=Board.get_number(self,row-1,col)
        return(x1,x2)

    def adjacent_horizontal_numbers(self, row: int, col: int) -> (int, int):
        """Devolve os valores imediatamente a esquerda e a direita,
        respectivamente."""
        if 0<=row<self.size and 0<=col<self.size:
            x1=Board.get_number(self,row,col+1)
            x2=Board.get_number(self,row,col-1)
        return(x2,x1)

    @staticmethod
    def parse_instance_from_stdin():
        """Le o test do standard input (stdin) que e passado como argumento
        e retorna uma instância da classe Board.

        Por exemplo:
            $ python3 takuzu.py < input_T01

            > from sys import stdin
            > stdin.readline()
        """
        # TODO
        pass

    # TODO: outros metodos da classe


class Takuzu(Problem):
    def __init__(self, board: Board):
        """O construtor especifica o estado inicial."""
        # TODO
        pass

    def actions(self, state: TakuzuState):
        """Retorna uma lista de acoes que podem ser executadas a
        partir do estado passado como argumento."""
        # TODO
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
