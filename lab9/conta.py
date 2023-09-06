class Conta:
    def __init__(self):
        tentativas = 0
        while tentativas < 3:
            try:
                self.__nome_correntista = input("Digite o nome do correntista: ")
                if not self.__nome_correntista:
                    raise ValueError("Nome do correntista não pode estar vazio.")
                if self.__nome_correntista.isnumeric():
                    raise ValueError("Nome do correntista não pode ser um número.")

                self.__numero_conta = input("Digite o número da conta: ")
                if not self.__numero_conta.isnumeric() or int(self.__numero_conta) <= 0:
                    raise ValueError("Número da conta inválido.")

                self.__saldo_disponivel = 0
                self.__conta_ativa = True
                break
            except ValueError as ve:
                tentativas += 1
                print(f"Tentativa {tentativas} de 3 - Erro no cadastro da conta: {ve}")

        if tentativas == 3:
            print("Número máximo de tentativas excedido. Conta bloqueada.")



    def depositar(self, valor):
        if valor > 0:
            self.__saldo_disponivel += valor
            print(f"Depósito de {valor} realizado com sucesso. Novo saldo: {self.__saldo_disponivel}")
        else:
            raise ValueError("Valor de depósito inválido.")

    def sacar(self, valor):
        if not self.__conta_ativa:
            raise ValueError("Conta desativada. Não é possível fazer saques.")

        if valor > 0 and valor <= self.__saldo_disponivel:
            self.__saldo_disponivel -= valor
            print(f"Saque de {valor} realizado com sucesso. Novo saldo: {self.__saldo_disponivel}")
        else:
            raise ValueError("Saldo insuficiente para saque.")

    def consultar_saldo(self):
        return self.__saldo_disponivel

    def ativar_conta(self):
        self.__conta_ativa = True
        print("Conta ativada.")

    def desativar_conta(self):
        self.__conta_ativa = False
        print("Conta desativada.")

    def get_nome_correntista(self):
        return self.__nome_correntista

    def set_nome_correntista(self, nome):
        if nome:
            self.__nome_correntista = nome
        else:
            raise ValueError("Nome do correntista não pode ser vazio.")

    def get_numero_conta(self):
        return self.__numero_conta

    def set_numero_conta(self, numero):
        if numero:
            self.__numero_conta = numero
        else:
            raise ValueError("Número da conta não pode ser vazio.")

    def is_conta_ativa(self):
        return self.__conta_ativa


