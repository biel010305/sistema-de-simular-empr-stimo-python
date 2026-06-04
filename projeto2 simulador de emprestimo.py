nome = input("Digite seu nome: ")
valor = float(input("Digite o valor do empréstimo: "))
parcelas = int(input("Digite a quantidade de parcelas: "))

juros = 0.03

valor_com_juros = valor + (valor * juros * parcelas)
valor_parcela = valor_com_juros / parcelas

print("------ RESULTADO ------")
print("Cliente:", nome)
print("Valor solicitado: R$", valor)
print("Quantidade de parcelas:", parcelas)
print("Valor total com juros: R$", round(valor_com_juros, 2))
print("Valor de cada parcela: R$", round(valor_parcela, 2))