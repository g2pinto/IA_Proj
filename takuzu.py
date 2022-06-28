# takuzu.py: Template para implementacao do projeto de Inteligencia Artificial 2021/2022.
# Devem alterar as classes e funcoes neste ficheiro de acordo com as instrucoes do enunciado.
# Alem das funcoes e classes ja definidas, podem acrescentar outras que considerem pertinentes.

# Grupo 030:
# 89627 Gustavo Pinto
# 98876 Tomas Cayatte

import time
import copy
import sys
from search import (
    Node, 
    Problem, 
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
    """Representação interna de um tabuleiro de Takuzu."""
    def __init__(self, board):
        self.board = board
        self.size = len(board[0])
        
        empties = [self.get_number(i, j) for i in range(self.size) for j in range(self.size) if self.get_number(i, j) == 2]
        self.toFill = len(empties)

    def get_size(self):
        return self.size

    def get_number(self, row: int, col: int) -> int:
        """Devolve o valor na respetiva posição do tabuleiro."""
        return self.board[row][col]

    def adjacent_vertical_numbers(self, row: int, col: int):
        """Devolve os valores imediatamente abaixo e acima,
        respectivamente."""
        if (row - 1 < 0):
            up_adj = None
        else:
            up_adj = self.get_number(row - 1, col)

        if (row >= self.size - 1):
            down_adj = None
        else:
            down_adj = self.get_number(row + 1, col)
        
        return (down_adj, up_adj)        

    def adjacent_horizontal_numbers(self, row: int, col: int):
        """Devolve os valores imediatamente a esquerda e a direita, respectivamente."""
        if (col - 1 < 0):
            down_adj = None
        else:
            down_adj = self.get_number(row, col - 1)

        if (col >= self.size - 1):
            up_adj = None
        else:
            up_adj = self.get_number(row, col + 1)
        
        return (down_adj, up_adj)  

    @staticmethod
    def parse_instance_from_stdin():
        """Le o test do standard input (stdin) que e passado como argumento
        e retorna uma instância da classe Board.
        
        Por exemplo:
            $ python3 takuzu.py < input_T01

            > from sys import stdin
            > stdin.readline()
        """

        size = int(sys.stdin.readline())
        lines = []
        for i in range(size):
            lines.append(sys.stdin.readline().rstrip())
                    
        board = []
        for line in lines:
            row = []
            for char in line:
                if char != ' ' and char != '\t':
                    row.append(int(char))
            
            board.append(row)
        
        return Board(board)

# TODO: outros metodos da classe
    def change_value(self, row: int, col: int, value: int):
        self.board[row][col] = value
        self.toFill -= 1
    
    def double_adjacent_up(self, row: int, col: int):
        """ Devolve os dois valores imediatamente acima """
        if (row + 1 >= self.size):
            up_adj = None
        else:
            up_adj = self.get_number(row + 1, col)
            
        if (row + 2 >= self.size):
            up_next_adj = None
        else:
            up_next_adj = self.get_number(row + 2, col)
            
        return (up_adj, up_next_adj)

    def double_adjacent_down(self, row: int, col: int):
        """ Devolve os dois valores imediatamente abaixo """
        if (row - 1 < 0):
            down_adj = None
        else:
            down_adj = self.get_number(row - 1, col)
            
        if (row - 2 < 0 ):
            down_next_adj = None
        else:
            down_next_adj = self.get_number(row - 2, col)
            
        return (down_adj, down_next_adj)

    def double_adjacent_right(self, row: int, col: int):
        """ Devolve os dois valores imediatamente a direita """
        if (col + 1 >= self.size):
            right_adj = None
        else:
            right_adj = self.get_number(row, col + 1)
            
        if (col + 2 >= self.size):
            right_next_adj = None
        else:
            right_next_adj = self.get_number(row, col + 2)
        
        return (right_adj, right_next_adj)
    
    def double_adjacent_left(self, row: int, col: int):
        """ Devolve os dois valores imediatamente a esquerda """
        if (col - 1 < 0):
            left_adj = None
        else:
            left_adj = self.get_number(row, col - 1)
        if (col - 2 < 0):
            left_next_adj = None
        else:
            left_next_adj = self.get_number(row, col - 2) 
        return (left_adj, left_next_adj)
        
    def describe_row(self, row):
        """ devolve (num_zeros, num_uns, num_dois) """
        count_0 = 0
        count_1 = 0
        count_2 = 0
        for i in range(self.size):
            val = self.get_number(row, i) 
            if (val == 0):
                count_0 += 1
            elif (val == 1):
                count_1 += 1
            elif (val == 2):
                count_2 += 1
        return (count_0, count_1, count_2)
    
    def describe_col(self, col):
        """ devolve (num_zeros, num_uns, num_dois) """
        count_0 = 0
        count_1 = 0
        count_2 = 0
        for i in range(self.size):
            val = self.get_number(i, col) 
            if (val == 0):
                count_0 += 1
            elif (val == 1):
                count_1 += 1
            elif (val == 2):
                count_2 += 1

        return (count_0, count_1, count_2)

    def get_row(self, row):
        return self.board[row]

    def equal_row(self, row):
        for i in range(self.size):
            if self.get_row(i) == row:
                return True
    
    def get_col(self, col_num):
        return [self.get_number(i, col_num) for i in range(self.size)]

        
    def equal_col(self, col):
        for i in range(self.size):
            if (self.get_col(i) == col):
                return True
            
    def print_board(self):
        i = 0
        while i < self.size:
            print('\t'.join(map(str, self.get_row(i))))            
            i += 1




class Takuzu(Problem):
    def __init__(self, board: Board):
        """O construtor especifica o estado inicial."""
        self.initial = TakuzuState(board)
        pass

    def still_possible(self, list):
        return list[0] or list[1]

    def actions(self, state: TakuzuState):
        """Retorna uma lista de acoes que podem ser executadas a
        partir do estado passado como argumento."""
        if state.board.toFill == 0:
            return []
        
        actions = []
        for row in range(state.board.size):
            for col in range(state.board.size):
                # SKIP ALREADY FILLED POSITIONS
                if state.board.get_number(row, col) != 2:
                    continue

                # THE NUMBER OF ONES AND ZEROS (IN THE COL) SHOULD BE SIZE/2
                _tuple = state.board.describe_col(col) #(0s, 1s, 2s)
                if state.board.size%2 == 0:                    
                    if (_tuple[0] >= state.board.size/2):
                        #actions.append((row, col, 1))
                        #if (row, col) == (5, 8):
                            #print("erro 1")
                        #print([(row, col, 1)])
                        return [(row, col, 1)]
                    if (_tuple[1] >= state.board.size/2):
                        #actions.append((row, col, 0))
                        #if (row, col) == (5, 8):
                            #print("erro 2")
                        #print([(row, col, 0)])
                        return [(row, col, 0)]
                        
                else:                   
                    if (_tuple[0] >= state.board.size//2 + 1):
                        #actions.append((row, col, 1))
                        #if (row, col) == (5, 8):
                            #print("erro 3")
                        #print([(row, col, 1)])
                        return [(row, col, 1)]
                    if (_tuple[1] >= state.board.size//2 + 1):
                        #actions.append((row, col, 0))
                        #if (row, col) == (5, 8):
                            #print("erro 4")
                        #print([(row, col, 0)])
                        return [(row, col, 0)]
                
                # VERIFICAR COLUNAS IGUAIS
                if (_tuple[2] == 1):
                    possible_col = state.board.get_col(col)[:]
                    possible_col[row] = 0
                    if (state.board.equal_col(possible_col)):
                        #actions.append((row, col, 1))
                        #if (row, col) == (5, 8):
                            #print("erro 5")
                        #print([(row, col, 1)])
                        return [(row, col, 1)]
                    possible_col[row] = 1
                    if (state.board.equal_col(possible_col)):
                        #actions.append((row, col, 0))
                        #if (row, col) == (5, 8):
                            #print("erro 6")
                        #print([(row, col, 0)])
                        return [(row, col, 0)]

                # TODO - se numero de zeros = size/2 meter um 1 é sempre acao (?)
                # TODO - se numero de uns = size/2 meter um 0 é sempre acao (?)
                # só necessário para problemas de tempo, i think

                # THE NUMBER OF ONES AND ZEROS (IN THE ROW) SHOULD BE SIZE/2
                _tuple = state.board.describe_row(row)
                if state.board.size%2 == 0:                    
                    if (_tuple[0] >= state.board.size/2):
                        #actions.append((row, col, 1))
                        #print([(row, col, 1)])
                        return [(row, col, 1)]
                    if (_tuple[1] >= state.board.size/2):
                        #actions.append((row, col, 0))
                        #print([(row, col, 0)])
                        return [(row, col, 0)]  
                    
                else:                   
                    if (_tuple[0] >= state.board.size//2 + 1):
                        #actions.append((row, col, 1))
                        #print([(row, col, 1)])
                        return [(row, col, 1)]
                    if (_tuple[1] >= state.board.size//2 + 1):
                        #actions.append((row, col, 0))
                        #print([(row, col, 0)])
                        return [(row, col, 0)]
                    
                # VERIFICAR LINHAS IGUAIS
                if (_tuple[2] == 1):
                    possible_row = state.board.get_row(row)[:]
                    possible_row[col] = 0
                    if (state.board.equal_row(possible_row)):
                        #actions.append((row, col, 1))
                        #print([(row, col, 1)])
                        return [(row, col, 1)]
                    possible_row[col] = 1
                    if (state.board.equal_row(possible_row)):
                        #actions.append((row, col, 0))
                        #print([(row, col, 0)])
                        return [(row, col, 0)]
                        

                # CHECK IF ADJACENT VERTICAL VALUES ARE ALREADY THE SAME
                _tuple = state.board.adjacent_vertical_numbers(row, col)
                if (_tuple[0] == _tuple[1]):
                    if (_tuple[0] == 0):
                        #actions.append((row, col, 1))
                        #print([(row, col, 1)])
                        return [(row, col, 1)]
                    elif (_tuple[0] == 1):
                        #actions.append((row, col, 0))
                        #print([(row, col, 0)])
                        return [(row, col, 0)]
                
                # CHECK IF ADJACENT HORIZONTAL VALUES ARE ALREADY THE SAME
                _tuple = state.board.adjacent_horizontal_numbers(row, col)
                if (_tuple[0] == _tuple[1]):
                    if (_tuple[0] == 0):
                        #actions.append((row, col, 1))
                        #print([(row, col, 1)])
                        return [(row, col, 1)]
                    elif (_tuple[0] == 1):
                        #actions.append((row, col, 0))
                        #print([(row, col, 0)])
                        return [(row, col, 0)]

                # CHECK IF DOWN VALUES ARE ALREADY DOUBLED
                _tuple = state.board.double_adjacent_down(row, col)
                if (_tuple[0] == _tuple[1]):
                    if (_tuple[0] == 0):
                        #actions.append((row, col, 1))
                        #print([(row, col, 1)])
                        return [(row, col, 1)]
                    elif (_tuple[0] == 1):
                        #actions.append((row, col, 0))
                        #print([(row, col, 0)])
                        return [(row, col, 0)]

                # CHECK IF UP VALUES ARE ALREADY DOUBLED
                _tuple = state.board.double_adjacent_up(row, col)
                if (_tuple[0] == _tuple[1]):
                    if (_tuple[0] == 0):
                        #actions.append((row, col, 1))
                        #print([(row, col, 1)])
                        return [(row, col, 1)]
                    elif (_tuple[0] == 1):
                        #actions.append((row, col, 0))
                        #print([(row, col, 0)])
                        return [(row, col, 0)]
                
                # CHECK IF RIGHT VALUES ARE ALREADY DOUBLED
                _tuple = state.board.double_adjacent_right(row, col)
                if (_tuple[0] == _tuple[1]):
                    if (_tuple[0] == 0):
                        #actions.append((row, col, 1))
                        #print([(row, col, 1)])
                        return [(row, col, 1)]
                    elif (_tuple[0] == 1):
                        #actions.append((row, col, 0))
                        #print([(row, col, 0)])
                        return [(row, col, 0)]
                
                # CHECK IF LEFT VALUES ARE ALREADY DOUBLED
                _tuple = state.board.double_adjacent_left(row, col)
                if (_tuple[0] == _tuple[1]):
                    if (_tuple[0] == 0):
                        #actions.append((row, col, 1))
                        #print([(row, col, 1)])
                        return [(row, col, 1)]
                    elif (_tuple[0] == 1):
                        #actions.append((row, col, 0))
                        #print([(row, col, 0)])
                        return [(row, col, 0)]

                # ADICIONA ACOES POSSIVEIS
                actions.append((row, col, 0))
                actions.append((row, col, 1))
                
        #print(actions)
        return actions

    def result(self, state: TakuzuState, action):
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A acao a executar deve ser uma
        das presentes na lista obtida pela execucao de
        self.actions(state)."""
        result_state = copy.deepcopy(state)
        result_state.board.change_value(action[0], action[1], action[2])
        
        
        return result_state

    def goal_test(self, state: TakuzuState):
        """Retorna True se e só se o estado passado como argumento e
        um estado objetivo. Deve verificar se todas as posicoes do tabuleiro
        estao preenchidas com uma sequencia de números adjacentes."""
        for i in range(state.board.size):
            for j in range(state.board.size):
                num = state.board.get_number(i, j)
                a_h_num = state.board.adjacent_horizontal_numbers(i, j)
                a_v_num = state.board.adjacent_vertical_numbers(i, j)
                
                if a_h_num[0] == num == a_h_num[1] or a_v_num[0] == num == a_v_num[1]:
                    return False
                    
                if j > i:
                    if state.board.get_row(i) == state.board.get_row(j) or state.board.get_col(i) == state.board.get_col(j):
                        return False
        
            row_desc = state.board.describe_row(i)
            if state.board.size%2 == 0:
                if not (state.board.size/2 == row_desc[0] == row_desc[1]):
                    return False
            else:
                if not (state.board.size//2 == row_desc[0] and row_desc[0] == row_desc[1]-1 or state.board.size//2 == row_desc[1] and row_desc[1] == row_desc[0]-1):
                    return False
            
        return True                  
              
    def h(self, node: Node):
        """Funcao heuristica utilizada para a procura A*."""
        h = 0
        for i in range(node.state.board.size):
            desc_row = node.state.board.describe_row(i)
            desc_col = node.state.board.describe_col(i)
            h += desc_row[2] * 15
            h += abs(desc_row[0] - desc_row[1]) * 5
            h += abs(desc_col[0] - desc_col[1]) * 5
            
        return h

# TODO: outros metodos da classe





if __name__ == "__main__":
    # TODO:
    # Ler o ficheiro do standard input,
    # Usar uma tecnica de procura para resolver a instância,
    # Retirar a solucao a partir do nó resultante,
    # Imprimir para o standard output no formato indicado. 
        
    #start_time = time.time() 
    
    board = Board.parse_instance_from_stdin()
    problem = Takuzu(board)
    
    goal_node = depth_first_tree_search(problem)
    
    goal_node.state.board.print_board()
    
    #print(time.time() - start_time, "seconds")
    
    
    


#para testar, em vez de printar actions, printar as posicoes com 2

#nas actions verificar se linha vai ficar igual

#guardar posicoes por preencher