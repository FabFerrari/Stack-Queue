#Fabrizio Ferrari Roela de Oliveira Cesar - 166685
#Luis Felipe Pires Gomes - 165601

import queue

def adicionar_operacao(fila_operacoes):
    print("Operacoes disponíveis:")
    print("1 - Adicao")
    print("2 - Subtracao")
    print("3 - Multiplicacao")
    print("4 - Divisao")
    
    # entrada de ususario
    operacao = input("Selecione uma operacao: ")
    valores = input("Digite os valores a serem operados (x,y): ")
    
     # valores na fila
    fila_operacoes.put((int(operacao), [int(v) for v in valores.split(",")]))

def executar_proxima_operacao(fila_operacoes):
    if fila_operacoes.empty():
        print("Nenhuma operação na fila.")
        return
    
    operacao, valores = fila_operacoes.get()
    
    if operacao == 1:
        resultado = sum(valores)
    elif operacao == 2:
        resultado = valores[0] - sum(valores[1:])
    elif operacao == 3:
        resultado = 1
        for v in valores:
            resultado *= v
    elif operacao == 4:
        resultado = valores[0] / valores[1]
    
    print(f"Operação: {operacao}, Valores: {valores}, Resultado: {resultado}")

def executar_todas_operacoes(fila_operacoes):
    if fila_operacoes.empty():
        print("Nenhuma operação na fila.")
        return
    
    while not fila_operacoes.empty():
        executar_proxima_operacao(fila_operacoes)

def validar_expressao():
    expressao = input("Digite uma expressão matemática: ")
    
    pilha = []
    for c in expressao:
        if c in ["(", "{", "["]:
            pilha.append(c)
        elif c in [")", "}", "]"]:
            if len(pilha) == 0:
                print("INVALIDO")
                return
            elif c == ")" and pilha[-1] == "(" or \
                 c == "}" and pilha[-1] == "{" or \
                 c == "]" and pilha[-1] == "[":
                pilha.pop()
            else:
                print("INVALIDO")
                return
    #fila vazia --->
    if len(pilha) == 0:
        print("VALIDO")
    else:
        print("INVALIDO")

def main():
    # criar fila de operações VAZIA!
    fila_operacoes = queue.Queue()
    
    # MENU
    while True:
        print("Menu principal:")
        print("1 - Operacoes")
        print("2 - Expressao")
        print("0 - Encerrar programa")
        opcao = input("Selecione uma opcao: ")
        
        if opcao == "1":
            while True:
                print("Menu de operacoes:")
                print("1 - Adicionar operação a fila")
                print("2 - Executar proxima operação da fila")
                print("3 - Executar todas as operacoes da fila")
                print("0 - Voltar ao menu principal")
                op_opcao = input("Selecione uma opcao: ")
                
                if op_opcao == "1":
                    adicionar_operacao(fila_operacoes)
                elif op_opcao == "2":
                    executar_proxima_operacao(fila_operacoes)
                elif op_opcao == "3":
                    executar_todas_operacoes(fila_operacoes)
                elif op_opcao == "0":
                    break
                else:
                    print("Opção invalida.")
        elif opcao == "2":
            validar_expressao()
        elif opcao == "0":
            return
        else:
            print("Opção invalida.")


main()
