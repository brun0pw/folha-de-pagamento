import os
from dataclasses import dataclass

def limpar_tela():
    os.system("cls || clear")

@dataclass
class PessoaFuncionario:
    nome: str
    sobrenome: str
    idade: int
    cpf: float
    sexo: str
    salario: float
    dependentes: int = 0
    vale_transporte: str = "n"
    vale_refeicao: float = 0.0

def calcular_desconto(salario):
    if salario <= 1100.01:
        return salario * 0.09
    elif salario <= 2203.48:
        return salario * 0.09
    elif salario <= 3305.22:
        return salario * 0.12
    elif salario <= 6433.57:
        return salario * 0.14
    return 0

def calcular_salario_liquido(funcionario: PessoaFuncionario):
    desconto_inss = calcular_desconto(funcionario.salario)
    vale_transporte = funcionario.salario * 0.06 if funcionario.vale_transporte == 's' else 0
    dependentes_deduzidos = funcionario.dependentes * 189.59
    salario_liquido = (funcionario.salario - desconto_inss - vale_transporte + dependentes_deduzidos - funcionario.vale_refeicao)
    return salario_liquido

limpar_tela()
matricula = int(input("Digite sua matrícula: "))
senha = input("Digite sua senha: ")

limpar_tela()

while True:
    print("""
            === BEM VINDO À RECEITA FEDERAL ===
           1 - Criar funcionário
           2 - Consultar dados
           3 - Sair
    """)
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nome = input("Digite o nome do funcionário: ")
        sobrenome = input("Digite o sobrenome: ")
        idade = int(input("Digite a idade: "))
        cpf = float(input("Digite o CPF: "))
        sexo = input("Digite o sexo: ")
        salario = float(input("Digite o salário: "))
        dependentes = int(input("Digite o número de dependentes: "))
        vale_transporte = input("Gostaria de receber auxílio transporte? (s/n): ").lower()
        vale_refeicao = float(input("Digite o valor do vale refeição: "))
        
        funcionario = PessoaFuncionario(nome, sobrenome, idade, cpf, sexo, salario, dependentes, vale_transporte, vale_refeicao)
        salario_liquido = calcular_salario_liquido(funcionario)
        print(f"Salário líquido do funcionário {nome}: R$ {salario_liquido:.2f}")
    
    elif opcao == "2":
        print("Consultar dados ainda não implementado.")
    
    elif opcao == "3":
        print("Saindo...")
        break
    
    else:
        print("Opção inválida. Tente novamente.")
