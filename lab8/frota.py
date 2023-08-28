from veiculo import Veiculo

class Frota(Veiculo):
    def __init__(self):
        self.__frota = []

    def inserir_veiculo(self, veiculo):
        self.__frota.append(veiculo)

    def buscar_veiculo(self, placa):
        for veiculo in self.__frota:
            if veiculo.getPlacaVeiculo() == placa:
                return True
        return False
    
    def listar_veiculos(self):
        ordem = {"Carro": 1, "Moto": 2, "Bicicleta": 3}
        for index in range(1, 4):
            for veiculo in self.__frota:
                if ordem[veiculo.__class__.__name__] == index:
                    print(f"Placa: {veiculo.getPlacaVeiculo()}, Marca: {veiculo.getFabricanteVeiculo()}")   

    def remover_veiculo(self, placa):
        for veiculo in self.__frota:
            if veiculo.getPlacaVeiculo() == placa:
                if veiculo:      
                    self.__frota.remove(veiculo)  
                    print(f"Veículo {veiculo.getPlacaVeiculo()} {veiculo.getFabricanteVeiculo()} removido.")
                else:
                    print("Veículo não encontrado.")
