#Sistema Bancário v0.1

import textwrap

def menu():
    menu = """
    ================ BANCO D.I.O ================
    [1] DEPOSITAR
    [2] SACAR
    [3] EXTRATO
    [4] NOVA CONTA
    [5] LISTAR CONTAS
    [6] NOVO USUÁRIO
    [0] Sair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor_deposito, extrato, /):

    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! Insira um valor válido para depósito...")

    return saldo, extrato

def sacar(*, saldo, valor_saque, extrato, limite, numero_saques, limite_saques):

    if valor_saque > saldo:
        print("Saldo insuficiente!")

    elif valor_saque > limite:
        print(f"Limite de R$ {limite} por saque excedido!")

    elif numero_saques >= limite_saques:
        print("Limite de três saques por dia excedido!")

    elif valor_saque > 0:
        saldo -= valor_saque
        extrato += f"Saque: R$ {valor_saque:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")

    else:
        print("Operação falhou! Insira um valor válido para saque...")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=========================================")

def criar_usuario(usuarios):

    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):

    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):

    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado! Fluxo de criação de conta encerrado...")

def listar_contas(contas):

    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 10)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        match menu():
            case "1":
                valor_deposito = float(input("Informe o valor do depósito: "))

                saldo, extrato = depositar(saldo, valor_deposito, extrato)

            case "2":
                valor_saque = float(input("Informe o valor do saque: "))

                saldo, extrato = sacar(
                saldo=saldo,
                valor_saque=valor_saque,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
                )
            
            case "3":
                exibir_extrato(saldo, extrato=extrato)
            
            case "4":
                numero_conta = len(contas) + 1
                conta = criar_conta(AGENCIA, numero_conta, usuarios)

                if conta:
                    contas.append(conta)
            
            case "5":
                listar_contas(contas)

            case "6":
                criar_usuario(usuarios)
            
            case "0":
                 break
            
            case _:
                 print("Operação inválida! Selecione uma operação válida...")

main()