from conta import Conta

def main():
    # Criando uma instância da classe Conta
    minha_conta = Conta()

    # Depositar dinheiro
    try:
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        minha_conta.depositar(valor_deposito)
    except ValueError as ve:
        print(ve)

    # Sacar dinheiro
    try:
        valor_saque = float(input("Digite o valor a ser sacado: "))
        minha_conta.sacar(valor_saque)
    except ValueError as ve:
        print(ve)

    # Consultar saldo
    saldo_atual = minha_conta.consultar_saldo()
    print(f"Saldo disponível: {saldo_atual}")

    # Ativar e desativar conta
    ativar = input("Deseja ativar a conta? (S/N): ").lower()
    if ativar == "s":
        minha_conta.ativar_conta()
    elif ativar == "n":
        minha_conta.desativar_conta()
    else:
        raise ValueError("Opcao invalida")

    # Consultar se a conta está ativa
    if minha_conta.is_conta_ativa():
        print("A conta está ativa.")
    else:
        print("A conta está desativada.")

if __name__ == "__main__":
    main()
