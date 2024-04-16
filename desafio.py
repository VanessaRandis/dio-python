menu = """
    [Q] Sair
    [S] Saque
    [D] Deposito
    [E] Extrato

"""

saldo = 200
limite = 500
extrato = ""
numero_saques = 0 
LIMITE_DAQUE = 3



while True:

    opcao = input(menu).upper()
    

    if opcao == "Q":
        print("Obrigada!")
        break
    elif opcao == "S":
        valor_saque = float(input("Informe o valor de saque: "))
        if(saldo - valor_saque < 0 or numero_saques > 3 or valor_saque > 500):
            print(f"Operação não pode ser efetuada com valor R$ {saldo:.2f} e quantidade de saques {numero_saques} ")
        else:
            saldo -= valor_saque
            numero_saques += 1
            extrato += f""" | Saque realizado de R$ {valor_saque} seu saldo atual R$ {saldo:.2f} |"""
    elif opcao == "D":
        valor_deposito = float(input("Informe o valor de deposito: "))
        if(valor_deposito <= 0):
            print("Operação não pode ser reaizada com valor menor que 0")
        else:
            saldo += float(valor_deposito)
            extrato += f"""| Depósito realizado de R$ {valor_deposito} seu saldo atual R$ {saldo:.2f} |"""
    elif opcao == "E":
         print(extrato)
    else:
         print("Opção inválida, refaça a operação: ")


         



