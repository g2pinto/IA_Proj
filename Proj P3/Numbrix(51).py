#!/usr/bin/env python
# coding: utf-8

# In[7]:


# numbrix.py: Template para implementação do projeto de Inteligência Artificial 2021/2022.
# Devem alterar as classes e funções neste ficheiro de acordo com as instruções do enunciado.
# Além das funções e classes já definidas, podem acrescentar outras que considerem pertinentes.

# Grupo al040:
# 95748 João Melo
# 95746 Isabel Nogueira

import sys
from search import Problem, Node, astar_search, breadth_first_tree_search, depth_first_tree_search, greedy_search, recursive_best_first_search
import time

##start = time.time()
class NumbrixState:
    state_id = 0

    def __init__(self, board):
        self.board = board
        self.id = NumbrixState.state_id
        NumbrixState.state_id += 1

    def __lt__(self, other):
        return self.id < other.id
        
    # TODO: outros metodos da classe


class Board:
    """ Representação interna de um tabuleiro de Numbrix. """
    
    def __init__(self,board1):
        self.board = board1[:]
        self.leng=len(board1[0])
        self.numbs=[]
        self.zeros=[]
        for i in range(len(board1)):
            l=0
            for j in range(len(board1[i])):
                if board1[i][j]!=0:
                    self.numbs.append((board1[i][j],i,j))
                else:
                    l+=1
            self.zeros.append([l])
        self.numbs.sort()
        
        
    
    def get_number(self, row: int, col: int) -> int:
        """ Devolve o valor na respetiva posição do tabuleiro. """
        if row<0 or row>=self.leng or col < 0 or col>=self.leng:
            return None
        else:
            return self.board[row][col]
        pass
    
    def adjacent_vertical_numbers(self, row: int, col: int) -> (int, int):
        """ Devolve os valores imediatamente abaixo e acima, 
        respectivamente. """
        if 0<=row<self.leng and 0<=col<self.leng:
            x1=Board.get_number(self,row+1,col)
            x2=Board.get_number(self,row-1,col)
        return(x1,x2)
    
    def adjacent_horizontal_numbers(self, row: int, col: int) -> (int, int):
        """ Devolve os valores imediatamente à esquerda e à direita, 
        respectivamente. """
        if 0<=row<self.leng and 0<=col<self.leng:
            x1=Board.get_number(self,row,col+1)
            x2=Board.get_number(self,row,col-1)
        return(x2,x1)
        pass
        pass
    
    def insert_number(self, row: int, col: int,numb: int ):
        ## Devolve o talbuleiro com o número numb na linha row e coluna col.
        a=self.board[:]
        aux=a[row][:]
        aux[col]=numb
        a[row]=aux[:]
        return Board(a)
    
    ##def find_number(self,numb: int):
        ## Dado um número numb, devolve a linha e coluna onde esse número se encontra no tabuleiro.
        ##k=(None,None)
        ##for i in range(self.leng):
            ##for j in range(self.leng):
                ##if Board.get_number(self,i,j)== numb:
                    ##k=(i,j)
        ##return k
                
        
    
    @staticmethod    
    def parse_instance(filename: str):
        """ Lê o ficheiro cujo caminho é passado como argumento e retorna
        uma instância da classe Board. """
        pythontext= open(filename,"r")
        k=pythontext.read()
        m=[]
        for r in k.split():  
            if r.isdigit()== True:
                m+=[r]
        m2=[]
        i=0
        while i < len(m): 
            m2+=[int(m[i])]
            i=i+1 
        board=[[0 for j in range(m2[0])] for i in range(m2[0])]
        l=1     
        for u in range(len(board)):
            for w in range(len(board[u])):
                       board[u][w]= m2[l]
                       l+=1
        return Board(board)

    def to_string(self):
        k=''
        for i in range(self.leng):
            for j in range(self.leng-1):
                k+=str(self.board[i][j])+'\t'
            if i==self.leng-1:
                k+=str(self.board[i][-1])
            else:
                k+=str(self.board[i][-1])+'\n'
        return k
        
        
    # TODO: outros metodos da classe


class Numbrix(Problem):
    def __init__(self, board: Board):
        """ O construtor especifica o estado inicial. """
        self.initial = NumbrixState(board)
        pass

    def actions(self, state: NumbrixState):
        """ Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento. """
        k=[]
        if (state.board.leng)**2 == len(state.board.numbs):
            return k
        
                        
        if len(state.board.numbs)>1:
            for i in range(len(state.board.numbs)-1):
                    nume=state.board.numbs[i][0]
                    nnume=state.board.numbs[i+1][0]
                    npos=(state.board.numbs[i][1],state.board.numbs[i][2])
                    ahn=Board.adjacent_horizontal_numbers(state.board,npos[0],npos[1])
                    avn=Board.adjacent_vertical_numbers(state.board,npos[0],npos[1])
                    dif=nnume - nume
                    if dif==  1:
                        if nnume ==ahn[0] or  nnume ==ahn[1]  or nnume==avn[0] or  nnume==avn[1] :
                               k=k
                        else:
                               return k
                    if dif>1:
                        nnpos=(state.board.numbs[i+1][1],state.board.numbs[i+1][2])
                        if abs(npos[0]-nnpos[0]) + abs(npos[1] - nnpos[1]) > dif: 
                            return k
                        
                        if dif==2:
                            if state.board.leng<7:  
                                if nnpos[0]== npos[0] and nnpos[1]> npos[1] :
                                    if Board.get_number(state.board,npos[0],npos[1] +1)==0:
                                        k+=[(nume +1,npos[0],npos[1]+1)]
                                    return k 
                                if nnpos[0]== npos[0] and nnpos[1]< npos[1]:
                                    if Board.get_number(state.board,npos[0],npos[1] -1)==0:
                                        k+=[(nume +1,npos[0],npos[1]-1)]
                                    return k 
                                if nnpos[1]== npos[1] and nnpos[0]> npos[0] :
                                    if Board.get_number(state.board,npos[0]+1,npos[1] )==0:
                                        k+=[(nume +1,npos[0]+1,npos[1])]
                                    return k
                                if nnpos[1]== npos[1] and nnpos[0]< npos[0]:
                                    if Board.get_number(state.board,npos[0]-1,npos[1])==0:
                                        k+=[(nume +1,npos[0]-1,npos[1])]
                                    return k 
                                if nnpos[1] > npos[1] and nnpos[0] < npos[0]:
                                    if Board.adjacent_horizontal_numbers(state.board,npos[0]-1,npos[1])[0]==None and Board.adjacent_vertical_numbers(state.board,npos[0]-1,npos[1])[1]== None:
                                        if Board.get_number(state.board,npos[0]-1,npos[1] ) == 0:
                                            k+=[(nume+1,npos[0]-1,npos[1])]
                                        return k
                                    if Board.adjacent_horizontal_numbers(state.board,npos[0],npos[1]+1)[1]==None and Board.adjacent_vertical_numbers(state.board,npos[0],npos[1]+1)[0]== None:
                                        if Board.get_number(state.board,npos[0],npos[1]+1 ) == 0:
                                            k+=[(nume+1,npos[0],npos[1]+1)]
                                        return k
                                    else:
                                        if Board.get_number(state.board,npos[0]-1,npos[1] ) == 0:
                                            k+=[(nume+1,npos[0]-1,npos[1])]
                                        if Board.get_number(state.board,npos[0],npos[1] +1 ) == 0:
                                            k+=[(nume+1,npos[0],npos[1]+1)]
                                        return k 
                                if nnpos[1] > npos[1] and nnpos[0] > npos[0]:
                                    if Board.adjacent_horizontal_numbers(state.board,npos[0]+1,npos[1])[0]==None and Board.adjacent_vertical_numbers(state.board,npos[0]+1,npos[1])[0]== None:
                                        if Board.get_number(state.board,npos[0]+1,npos[1] ) == 0:
                                            k+=[(nume+1,npos[0]+1,npos[1])]
                                        return k
                                    if Board.adjacent_horizontal_numbers(state.board,npos[0],npos[1]+1)[1]==None and Board.adjacent_vertical_numbers(state.board,npos[0],npos[1]+1)[1]== None:
                                        if Board.get_number(state.board,npos[0],npos[1]+1 ) == 0:
                                            k+=[(nume+1,npos[0],npos[1]+1)]
                                        return k
                                    else:
                                        if Board.get_number(state.board,npos[0]+1,npos[1] ) == 0:
                                            k+=[(nume+1,npos[0]+1,npos[1])]
                                        if Board.get_number(state.board,npos[0],npos[1] +1 ) == 0:
                                            k+=[(nume+1,npos[0],npos[1]+1)]
                                        return k 
                                if nnpos[1] < npos[1] and nnpos[0] < npos[0]:
                                    if Board.adjacent_horizontal_numbers(state.board,npos[0]-1,npos[1])[1]==None and Board.adjacent_vertical_numbers(state.board,npos[0]-1,npos[1])[1]== None:
                                        if Board.get_number(state.board,npos[0]-1,npos[1] ) == 0:
                                            k+=[(nume+1,npos[0]-1,npos[1])]
                                        return k
                                    if Board.adjacent_horizontal_numbers(state.board,npos[0],npos[1]-1)[0]==None and Board.adjacent_vertical_numbers(state.board,npos[0],npos[1]-1)[0]== None:
                                        if Board.get_number(state.board,npos[0],npos[1]-1 ) == 0:
                                            k+=[(nume+1,npos[0],npos[1]-1)]
                                        return k
                                    if Board.get_number(state.board,npos[0]-1,npos[1] ) == 0:
                                            k+=[(nume+1,npos[0]-1,npos[1])]
                                    if Board.get_number(state.board,npos[0],npos[1] -1 ) == 0:
                                            k+=[(nume+1,npos[0],npos[1]-1)]
                                    return k 
                                if nnpos[1] < npos[1] and nnpos[0] > npos[0]:
                                    if Board.adjacent_horizontal_numbers(state.board,npos[0]+1,npos[1])[1]==None and Board.adjacent_vertical_numbers(state.board,npos[0]+1,npos[1])[0]== None:
                                        if Board.get_number(state.board,npos[0]+1,npos[1] ) == 0:
                                            k+=[(nume+1,npos[0]+1,npos[1])]
                                        return k
                                    if Board.adjacent_horizontal_numbers(state.board,npos[0],npos[1]-1)[0]==None and Board.adjacent_vertical_numbers(state.board,npos[0],npos[1]-1)[1]== None:
                                        if Board.get_number(state.board,npos[0],npos[1]-1 ) == 0:
                                            k+=[(nume+1,npos[0],npos[1]-1)]
                                        return k
                                    if Board.get_number(state.board,npos[0]+1,npos[1] ) == 0:
                                            k+=[(nume+1,npos[0]+1,npos[1])]
                                    if Board.get_number(state.board,npos[0],npos[1] -1 ) == 0:
                                            k+=[(nume+1,npos[0],npos[1]-1)]
                                    return k 
            
            
        
        
        
        if state.board.numbs[0][0]!=1:
                l= (state.board.numbs[0][1],state.board.numbs[0][2])
                if Board.adjacent_vertical_numbers(state.board,l[0],l[1])[0] == 0:
                    k+=[(state.board.numbs[0][0]-1,l[0]+1,l[1])]
                if Board.adjacent_vertical_numbers(state.board,l[0],l[1])[1] == 0:
                    k+=[(state.board.numbs[0][0]-1,l[0]-1,l[1])]
                if Board.adjacent_horizontal_numbers(state.board,l[0],l[1])[0] == 0:
                    k+=[(state.board.numbs[0][0]-1,l[0],l[1]-1 )]
                if Board.adjacent_horizontal_numbers(state.board,l[0],l[1])[1] == 0:
                    k+=[(state.board.numbs[0][0]-1,l[0],l[1]+1)]
                return k 
                    
        r=0
        while r<len(state.board.numbs)-1:
                if state.board.numbs[r+1][0]!= state.board.numbs[r][0] + 1:
                    l1= (state.board.numbs[r][1],state.board.numbs[r][2])
                    if Board.adjacent_vertical_numbers(state.board,l1[0],l1[1])[0] == 0:
                        k+=[(state.board.numbs[r][0]+1,l1[0]+1,l1[1])]
                    if Board.adjacent_vertical_numbers(state.board,l1[0],l1[1])[1] == 0:
                        k+=[(state.board.numbs[r][0]+1,l1[0]-1,l1[1])]
                    if Board.adjacent_horizontal_numbers(state.board,l1[0],l1[1])[0] == 0:
                        k+=[(state.board.numbs[r][0]+1,l1[0],l1[1]-1 )]
                    if Board.adjacent_horizontal_numbers(state.board,l1[0],l1[1])[1] == 0:
                        k+=[(state.board.numbs[r][0]+1,l1[0],l1[1]+1)]
                    return k 
                r+=1
        l2=(state.board.numbs[-1][1],state.board.numbs[-1][2])
        if Board.adjacent_vertical_numbers(state.board,l2[0],l2[1])[0] == 0:
                k+=[(state.board.numbs[-1][0]+1,l2[0]+1,l2[1])]
        if Board.adjacent_vertical_numbers(state.board,l2[0],l2[1])[1] == 0:
                k+=[(state.board.numbs[-1][0]+1,l2[0]-1,l2[1])]
        if Board.adjacent_horizontal_numbers(state.board,l2[0],l2[1])[0] == 0:
                k+=[(state.board.numbs[-1][0]+1,l2[0],l2[1]-1 )]
        if Board.adjacent_horizontal_numbers(state.board,l2[0],l2[1])[1] == 0:
                k+=[(state.board.numbs[-1][0]+1,l2[0],l2[1]+1)]             
        return k            
                
            
            
        pass

    def result(self, state: NumbrixState, action):
        """ Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de 
        self.actions(state). """
        b=Board.insert_number(state.board,action[1],action[2],action[0])
        return NumbrixState(b)
        pass

    def goal_test(self, state: NumbrixState):
        """ Retorna True se e só se o estado passado como argumento é
        um estado objetivo. Deve verificar se todas as posições do tabuleiro 
        estão preenchidas com uma sequência de números adjacentes. """
        k=True
        if len(state.board.numbs)!=(state.board.leng)**2:
            k=False
        else:
            for i in range(state.board.leng):
                for j in range(state.board.leng):
                    gn=Board.get_number(state.board,i,j)
                    ahn=Board.adjacent_horizontal_numbers(state.board,i,j)
                    avn=Board.adjacent_vertical_numbers(state.board,i,j)
                    if gn + 1==ahn[0] or gn - 1==ahn[0] or gn + 1 ==ahn[1]  or gn-1==ahn[1]  or gn+1==avn[0] or gn-1==avn[0]  or gn +1==avn[1] or gn-1==avn[1]:
                        pass
                    else:
                        k=False
        return k
        pass

    def h(self, node: Node):
        """ Função heuristica utilizada para a procura A*. """
        def h(self, node: Node):
            k=0
            for i in range(len(node.state.board.numbs)-1):
                if i==0:
                    k+=node.state.board.numbs[0][0]-1
                    if node.state.board.numbs[1][0]-node.state.board.numbs[0][0]!=1:
                        k+=(node.state.board.numbs[1][0]-node.state.board.numbs[0][0])*5
                else:
                    if node.state.board.numbs[i+1][0]-node.state.board.numbs[i][0]!=1:
                        k+=(node.state.board.numbs[i+1][0]-node.state.board.numbs[i][0])*5

            k+=(node.state.board.leng**2-node.state.board.numbs[-1][0])*5


            for i in range(len(node.state.board.numbs)):
                pos=(node.state.board.numbs[i][1],node.state.board.numbs[i][2])
                k1=Board.adjacent_vertical_numbers(node.state.board,pos[0],pos[1])
                k2=Board.adjacent_horizontal_numbers(node.state.board,pos[0],pos[1])
                if k1[0]==0:
                    k+=15
                if k1[1]==0:
                    k+=15
                if k2[0]==0:
                    k+=15
                if k2[1]==0:
                    k+=15
            if node.state.board.leng**2/len(node.state.board.numbs)>(1/0.9):
                for i in range(1,len(node.state.board.zeros)-1):
                       if node.state.board.zeros[i]==0:
                            q1=False
                            q2=False
                            for j in range(i):
                                if node.state.board.zeros[j]!=0:
                                    q1=True
                            for t in range( i,node.state.board.leng):
                                    if node.state.board.zeros[t]!=0:
                                        q2=True
                            if q1 and q2:
                                k+=10
            return k 

    # TODO: outros metodos da classe


if __name__ == "__main__":
    # TODO:
    # Ler o ficheiro de input de sys.argv[1],
    # Usar uma técnica de procura para resolver a instância,
    # Retirar a solução a partir do nó resultante,
    # Imprimir para o standard output no formato indicado.
    file=sys.argv[1]
    tabuleiro=Board.parse_instance(file)
    problema=Numbrix(tabuleiro)
    print(Board.to_string(tabuleiro))
    ##instrumented_problem=InstrumentedProblem(problema)
    goal_node=depth_first_tree_search(problema)
    ##nodes=astar_search(instrumented_problem)
    print(Board.to_string(goal_node.state.board))
    ##print(nodes)
    pass

##end = time.time()
##total_time = end - start
##print("\n"+ str(total_time))


# In[ ]:




