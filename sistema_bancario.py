# SISTEMA BANCARIO PYTHON

menu = '''
*  *  *  *  *  *  *  *  *  *  *
*  Digite a opção desejada:   *
*                             *
*  [d] - Depósito             *
*  [s] - Saque                *
*  [e] - Extrato              *
*  [q] - Quit/Sair            *
*                             *
*  O Banco que apoia você!    *
*  *  *  *  *  *  *  *  *  *  *
'''
saldo = 1000
limite = 500
LIMITE_SAQUES = 3
saque_count = 0
extrato = ""

while True:

    opcao = input(menu)
    # sistema de deposito >
    if opcao == "d":

        deposito = int(input("Insira um valor para depósito: "))

        if deposito > 0:
            saldo = saldo + deposito
            print(f"Você depositou um valor de R${deposito:.2f}\n...")
            extrato += f"Deposito R${deposito:.2f}\n"

        elif deposito == 0:
            print("O valor inserido não altera o saldo. A operação foi cancelada.\n...")
            
        else:
            print("Por favor, digite um valor numérico positivo para depósito.\nA operação foi cancelada, tente novamente.\n...")
            
        
    elif opcao == "s":

        # sistema de saque >
        saque = int(input("Insira um valor para saque: "))  

        if saque > 0 : #saque de valores positivos

            if saque_count != LIMITE_SAQUES: # contador de saques

                if saque <= limite:
                    saldo = saldo - saque
                    saque_count = saque_count + 1
                    print(f"\nVocê sacou um valor de R${saque:.2f}\n...")
                    extrato += f"Saque R${saque:.2f}\n"
                else:
                    print("\nValor excede o limite máximo.\nA operação foi cancelada.\n...")

            else:
                print("\nVocê excedeu o numero de saques diários.\n...")

        elif deposito == 0:
            print("\nO valor inserido não altera o saldo. \nA operação foi cancelada.\n...")

        else:
            print("\nPor favor, digite um valor numérico positivo para depósito.\nA operação foi cancelada, tente novamente.\n...")

    elif opcao == "e":
        print("== EXTRATO ==================\n")# sistema de extrato >        
        print("Não há nenhum registro de operações!\n" if not extrato else extrato) 
        print(f"Saldo: R$ {saldo:.2f}")
        print("=============================")# sistema de extrato >
    

    elif opcao == "q":
        print("---\n\nObrigado por utilizar o nosso Banco!\n\n---")
        break
    
    else:
        print("---\n\nOpção inexistente. Tente novamente.\n\n---")