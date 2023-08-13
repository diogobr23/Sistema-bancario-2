# Otimização do Projeto do Sistema Bancário
import textwrap

def menu():
    menu = """
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNovo cliente
    [5]\tNova conta
    [6]\tListar contas
    [7]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\t{valor:.2f}\n"
        print(f"\nVocê depositou R$ {valor:.2f}\n") 
    else:
        print ('\nA operação falhou! Informe um valor positivo.\n')
    return saldo, extrato
    

def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):

    if valor > saldo:
        print("\n*** Operação falhou! Você não tem saldo suficiente. ***")

    elif valor > limite:
        print("\n*** Operação falhou! O valor do saque excede o limite. ***")

    elif numero_saques > LIMITE_SAQUES:
        print("\n*** Operação falhou! Número máximo de saques excedido. ***")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n*** Saque realizado com sucesso! ***")

    else:
        print("\n*** Operação falhou! O valor informado é inválido. ***")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\nEXTRATO:\n")
    print("Nenhuma movimentação foi efetuada." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}\n")

def novo_cliente(clientes):
    cpf = input("Informe o CPF (somente números): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\nCPF já cadastrado!\n")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa):")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\nCliente cadastrado com sucesso!\n")


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def criar_conta(agencia, numero_conta, clientes):
    cpf = input("Informe o CPF (somente números): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\nConta criada com sucesso!\n")  
        return {"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente}

    print("\nUsuário não encontrado, fluxo de criação de conta encerrado!\n")  
    return None

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:\t{conta['agencia']}
            CC: \t\t{conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
        """
        print("="*100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    clientes = []
    contas = []
    numero_conta = 1



    while True:

        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES,
                )
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "4":
            novo_cliente(clientes)

        elif opcao == "5":
            conta = criar_conta(AGENCIA, numero_conta, clientes)

            if conta:
                contas.append(conta)
                numero_conta += 1
        
        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "7":
            break

        else:
            print("Opção inválida, por favor, insira a conta novamente.")



main()