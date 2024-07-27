class ContaBancaria:
    
    def __init__(self, banco, saldo):
        self.banco = banco
        self.saldo = saldo
        
    def depositar(self, deposito):
        deposito = float(deposito)
        if deposito > 0:
            self.saldo += deposito
            print(f"Depositei {deposito}. Novo saldo: {self.saldo}")
    
    def sacar(self, saque):
        saque = float(saque)
        if saque > self.saldo:
            print("Saque excedeu o limite")
        elif saque > 0:
            self.saldo -= saque
            print(f"Foi retirado {saque}. Novo saldo: {self.saldo}")
        
    def verificar_saldo(self):
        print(f"Saldo disponível: {self.saldo}")
    
    def __str__(self):
        return f"Conta no banco {self.banco} com saldo {self.saldo}"
    

class Cliente:
    
    def __init__(self, nome):
        self.nome = nome
        self.contas = []
        
    def adicionar_conta(self, conta):
        self.contas.append(conta)
    
    def transferir(self, conta_origem, conta_destino, valor):
        if conta_origem in self.contas and conta_destino in self.contas:
            if valor > 0 and conta_origem.saldo >= valor:
                conta_origem.sacar(valor)
                conta_destino.depositar(valor)
                print(f"Transferência de {valor} realizada com sucesso")
            else:
                print("Transferência não realizada: saldo insuficiente ou valor inválido")
        else:
            print("Contas inválidas")     
               
    def __str__(self):
        return f"Cliente {self.nome}"
    
# Exemplo de uso
cliente1 = Cliente('Juliana')
conta1 = ContaBancaria('Sabank', 5000)
cliente1.adicionar_conta(conta1)
print(f"{cliente1} realizou ação")

cliente2 = Cliente('Luís')
conta2 = ContaBancaria('Sabank', 3000)
cliente2.adicionar_conta(conta2)
print(f"{cliente2} realizou ação")

conta1.depositar(200.55)
conta1.sacar(210.33)
conta1.verificar_saldo()

cliente1.transferir(conta1, conta2, 1000)
