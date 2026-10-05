import os
import time
os.system("cls")

saldo_atual=1000

while True:

    print(f"Seu saldo atual é de {saldo_atual}")
    time.sleep(2)
    os.system("cls")

    opcao = int(input ("Digite a operação desejada - [1] Sacar [2] Sair [3] Consultar Saldo: "))

    if opcao == 1:
        valorSaque=float(input(f"Qual valor deseja sacar? "))

        saldoFinal=(saldo_atual-valorSaque - 2.5)
                                          #-2,50 de taxa

        time.sleep(2)
        os.system("cls")

        limiteDiario=2000

        if valorSaque>limiteDiario:
            print("Limite excedido.")
            time.sleep(2)
            quit()
        elif valorSaque<=0:
            print("Valor inválido.")
            time.sleep(2)
            quit()
        elif valorSaque % 10 !=0:
            print("Valor indisponível.")
            time.sleep(2)
            quit()
        elif valorSaque>saldo_atual:
            print("Saldo insuficiente.")
            time.sleep(2)
            quit()   
        else:
            print('''Operação realizada com sucesso.
Uma taxa de serviço no valor de R$ 2,50 foi cobrada dessa transação.''')
            saldo_atual = saldoFinal
            time.sleep(5)
            os.system("cls")

    elif opcao == 2:
        os.system("cls")
        print ("Saindo do Sistema.")
        time.sleep (3)
        break

    elif opcao == 3:
        print (f"Seu saldo atual é: {saldo_atual}")
        time.sleep (3)
        os.system("cls")

    else:
        print ("Por Favor, digite uma opção válida.")
        time.sleep (3)
        os.system("cls")


