# Francielli dos Santos Andreghetto

import datetime

class Produto:
    def __init__ (self, codigo, nome, preco, custo):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.custo = custo
    def calculaMargem(self):
        return (self.custo/self.preco) * 100
    
class ProdutoPericivel(Produto):
    def __init__ (self, codigo, nome, preco, custo, dataValidade):
        super().__init__(codigo, nome, preco, custo)
        self.dataValidade = dataValidade
    def calculaValidade(self):
      data_atual = datetime.datetime.today()
      return (self.dataValidade - data_atual.date()).days
    
class ProdutoBazar(Produto):
    def __init__ (self, codigo, nome, preco, custo, tempoGarantia):
        super().__init__(codigo, nome, preco, custo)
        self.tempoGarantia = tempoGarantia
    
class ProdutoLimpeza(Produto):
    def __init__ (self, codigo, nome, preco, custo):
        super().__init__(codigo, nome, preco, custo)

listprod = []

while True:
    print("1 - Cadastrar produto")
    print("2 - Cadastrar produto pericivel")
    print("3 - Cadastrar produto bazar")
    print("4 - Cadastrar produto de limpeza")
    print("5 - Calcula margem")
    print("6 - Calcula validade")
    print("7 - Sair")
    funcao = int(input("Digite o número da função que deseja realizar: "))
    if funcao == 1:
        while True:
            cadasprod = input('Cadastrar produt? [S/N]: ')
            if cadasprod == 'S' or cadasprod == 's':
                codigo = int(input('Digite o código do produto: '))
                nome = input('Digite o nome do produto: ')
                preco = float(input('Digite o valor do produto: '))
                custo = float(input('Digite o custo do produto: '))
                produto = Produto(codigo, nome, preco, custo)
                listprod.append(produto)
            if cadasprod == 'N' or  cadasprod == 'n':
                break

    if funcao == 2:
        while True:
            prodper = input('Deseja cadastrar produto pericivel? [S/N]: ')
            if prodper == 'S' or prodper == 's':
                codigo = int(input('Digite o código do produto: '))
                nome = input('Digite o nome do produto: ')
                preco = float(input('Digite o valor do produto: '))
                custo = float(input('Digite o custo do produto: '))
                dia = int(input('Digite o dia da data de validade: '))
                mes = int(input("Digite o mês da data de validade: "))
                ano = int(input("Digite o ano da data de validade: "))
                dataval = datetime.date(day = dia, month = mes, year = ano)
                produtopericivel = ProdutoPericivel(codigo, nome, preco, custo, dataval)
                listprod.append(produtopericivel)
            if prodper == 'N' or prodper == 'n':
                break

    if funcao == 3:
        while True:
            probazar= input('Deseja cadastrar produto bazar? [S/N]: ')
            if probazar == 'S' or probazar == 's':
                codigo = int(input('Digite o código do produto: '))
                nome = input('Digite o nome do produto: ')
                preco = float(input('Digite o valor do produto: '))
                custo = float(input('Digite o custo do produto: '))
                tempoGarantia = int(input('Digite quantos anos de garantia o produto possui: '))
                produtobazar = ProdutoBazar(codigo, nome, preco, custo, tempoGarantia)
                listprod.append(produtobazar)
            if probazar == 'n' or probazar == 'N':
                break

    if funcao == 4:
        while True:
            prolimp= input('Deseja cadastrar produto limpeza? [S/N]: ')
            if prolimp == 'S' or prolimp == 's':
                codigo = int(input('Digite o código do produto: '))
                nome = input('Digite o nome do produto: ')
                preco = float(input('Digite o valor do produto: '))
                custo = float(input('Digite o custo do produto: '))
                produtolimpeza = ProdutoLimpeza(codigo, nome, preco, custo)
                listprod.append(produtolimpeza)
            if prolimp == 'n' or prolimp == 'N':
                break

    if funcao == 5:
        while True:
            margem = input('Deseja calcular a margem? [S/N: ')
            if margem == 's' or margem == 'S':
                prodcal = int(input('Digite o código do produto que deseja calcular a margem: '))
                for produto in listprod:
                  if produto.codigo == prodcal:
                    print(f'Margem do produto: {produto.calculaMargem()}')
            if margem == 'n' or margem == 'N':
                break

    if funcao == 6:
        while True:
            validade = input('Deseja calcular a validade do produto? [S/N]: ')
            if validade == 's' or validade == 'S':
                prodval = int(input("Digite o código do produto que deseja calcular a validade: "))
                for produto in listprod:
                  if produto.codigo == prodval:
                    print(f'Faltam {produto.calculaValidade()} dias para o produto vencer')
            if validade == 'n' or validade == 'N':
                break

    if funcao == 7:
        break