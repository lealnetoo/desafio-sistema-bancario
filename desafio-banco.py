
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    if valor > saldo:
        print("Você não tem saldo suficiente.")
    elif valor > limite:
        print("O valor do saque excede o limite.")
    elif numero_saques >= limite_saques:
        print("Numero maximo de saques excedidos. ")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("O valor informado é invalido.")

    return saldo, extrato

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print('\nDepósito realizado com sucesso!')
    else:
        print('ERRO! O valor informado é inválido.')

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    
    cpf = input("Informe o CPF (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nERRO! Já existe usuário cadastrado com este CPF.")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("\n-- Usuário criado com sucesso. --")
    
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n-- Conta criada com sucesso --")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\nUsuário não encontrado.")
    return None

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuarios_filtrados = usuario
            return usuarios_filtrados
        else:
            return None


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
    print("=" * 100)
    print(linha)
    

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar usuario
[5] Criar conta
[6] Listar contas
[0] Sair

=> """

LIMITE_SAQUES = 3
AGENCIA = "0635-X"

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuarios = list()
contas = []

while True:

    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Informe um valor para depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)
    
    elif opcao == 2:
        valor = float(input("Informe o valor de saque: "))
        saldo, extrato = sacar(
            saldo = saldo, 
            valor = valor,
            extrato = extrato, 
            limite = limite,
            numero_saques = numero_saques, 
            limite_saques = LIMITE_SAQUES)    
    
    elif opcao == 3:
        exibir_extrato(saldo, extrato = extrato)
    
    elif opcao == 4:
        criar_usuario(usuarios)
    
    elif opcao == 5:

        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        
        if conta:
            contas.append(conta)
    
    elif opcao == 6:
        listar_contas(contas)

    elif opcao == 0:
        break

    else:
        print (" ")