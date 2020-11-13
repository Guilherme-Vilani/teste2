
# def Colaboradores(id, nome, cargo, qualificacao, cargaHoraria):
#     print('id:', id, '\nNome:', nome, '\nCargo:', cargo, '\nQualificacao:', qualificacao, '\nCarga Horaria:', cargaHoraria)

colaboradores = open("D:\PROJETOS\PYTHON\Hello\colaboradores.csv", "w")
colaborador1 = colaboradores.write("1 Guilherme Entregador Superior 3")
colaborador2 = colaboradores.write("\n2 Pedro Entregador Superior 5")
colaborador3 = colaboradores.write("\n3 Joao Entregador PosGrad 5")
colaborador4 = colaboradores.write("\n4 Alexsandro Entregador Superior 11")
colaboradores.close()

print("----------------------------------------------------------------------------------")

qualificacao = open("D:\PROJETOS\PYTHON\Hello\colaboradores.csv", "r")
for linha in qualificacao:
    salario = 100
    dadosqualificacao = linha.split()
    if(dadosqualificacao[3] == "Superior"):
        salario += (salario * 0.03)
        print(salario)
    else:
        salario += (salario * 0.07)
        print(salario)

print("----------------------------------------------------------------------------------")

bonus = open("D:\PROJETOS\PYTHON\Hello\colaboradores.csv", "r")
for linha in bonus:
    dadosbonus = linha.split()
    if(int (dadosbonus[4]) < 5):
        print("ganhou 10% de bonus")
    elif(int (dadosbonus[4])  >=5 and int (dadosbonus[4]) <= 9 ):
        print("ganhou 5% de bonus")
    else:
        print("Não ganhou nada")


# vec1 = ["fiat", "2007", "esportivo"]
# vec2 = ["chevrolet", "2007", "sedan"]

# veiculos = [vec1, vec2]

# a = veiculos[0][0]
# print(a)
