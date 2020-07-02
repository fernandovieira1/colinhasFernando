#### DATA SCIENCE (PYTHON)
# Pandas (importação, dataframe e manipulação de dados) [https://pandas.pydata.org/]
# Numpy (álgebra) [https://numpy.org/]
# https://www.programiz.com/python-programming

## Anotações diversas
# Encondig Python: https://docs.python.org/2/library/codecs.html#standard-encodings
# Estudo Titanic: https://paulovasconcellos.com.br/o-que-o-naufr%C3%A1gio-do-titanic-nos-ensina-at%C3%A9-hoje-data-science-project-2fea8ff1c9b5
# Geral Pandas: https://medium.com/data-hackers/uma-introdu%C3%A7%C3%A3o-simples-ao-pandas-1e15eea37fa1
# Loc e iloc no pandas: https://medium.com/horadecodar/data-science-tips-02-como-usar-loc-e-iloc-no-pandas-fab58e214d87
# Markdown: 
#          - https://support.zendesk.com/hc/pt-br/articles/203691016-Formata%C3%A7%C3%A3o-de-texto-com-Markdown#topic_xqx_mvc_43__line_break
#          - https://blog.da2k.com.br/2015/02/08/aprenda-markdown/
#          - https://docs.pipz.com/central-de-ajuda/learning-center/guia-basico-de-markdown#open

#### 0. IMPORTAÇÃO DE PACOTES ####
## Configuração de ambiente (antes)
# Bibliotecas padrão: http://turing.com.br/pydoc/2.7/tutorial/stdlib.html
import os
os.chdir("/Users/fernandovieira/OneDrive/1. Educacao/INFO E ESTAT/Fernando DS - Python e R/Dados")
# os.chdir("C:/Users/70485992191/OneDrive/1. Educacao/INFO E ESTAT/Fernando DS - Python e R/Dados")
os.getcwd()
os.listdir()

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
# fig = plt.gcf()
# fig.set_size_inches(11, 6) # tamanho das plotagens plt
import random
import seaborn as sns
import scipy.stats as sps

# plt.rcdefaults() # seta os valores padrão de estilo d 
# print(plt.style.available) # estilos disponíveis
# plt.style.use("seaborn")  # estilo

# plt.savefig("/Users/fernandovieira/Desktop/test_dpi_500.png", dpi = 500) # Salvando como figura
# Definindo o tamanho da figura a ser salva: http://www.learningaboutelectronics.com/Articles/How-to-set-the-size-of-a-figure-in-matplotlib-with-Python.php

#### 1. IMPORTAÇÃO DOS DADOS ####
## CSV
zuru = pd.read_csv("DadosAulaZurubabel.csv", encoding = "utf_8", sep = ";") # Dados Zurubabel
zuru.head()

titan = pd.read_csv("titanic_data.csv") # Dados Titanic
titan.head()

bank = pd.read_csv("bank.csv", encoding="UTF-8", sep=";" ) # https://archive.ics.uci.edu/ml/datasets/Bank+Marketing
bank.head()

## Excel
babel = pd.read_excel("Dados_Excel_Zurubabel.xlsx")
babel.head()

## Datas e hora
# df = pd.read_csv("dados.csv", parse_dates=["data","hora"]) # Com datas, usar parse_dates (aqui não vai funcionar -- não existe esse arquivo)

## TXT
climaCba = pd.read_csv("temp_cuiaba.txt", sep = ";", header = 3) # Ler o arquivo txt
climaCba = climaCba[["Data", "TempMaxima", "TempMinima", "Temp Comp Media", "Umidade Relativa Media"]] # Selecionar as colunas úteis
climaCba.columns = climaCba.columns.str.replace(" ", "_") # Substituir espaços no nome das colunas
climaCba["Data"] = pd.to_datetime(climaCba["Data"])
print(climaCba) # Imprime todo o df

climaCba_limpo = climaCba.dropna()
climaCba_limpo

# medias
climaCba_med_media = climaCba[["Data", "Temp_Comp_Media"]].dropna()
climaCba_med_media["Ano"] = climaCba_med_media["Data"].dt.year
climaCba_med_media = climaCba_med_media[["Ano", "Temp_Comp_Media"]].groupby(["Ano"]).mean()
climaCba_med_media  # temperatura média da média das temperaturas
climaCba_med_media.head()
climaCba_med_media.tail()

climaCba_med_max = climaCba[["Data", "TempMaxima"]].dropna()
climaCba_med_max["Ano"] = climaCba_med_max["Data"].dt.year
climaCba_med_max = climaCba_med_max[["Ano", "TempMaxima"]].groupby(["Ano"]).mean()
climaCba_med_max  # temperatura média das temperaturas mais altas
climaCba_med_max.head()
climaCba_med_max.tail()

climaCba_med_min = climaCba[["Data", "TempMinima"]].dropna()
climaCba_med_min["Ano"] = climaCba_med_min["Data"].dt.year
climaCba_med_min = climaCba_med_min[["Ano", "TempMinima"]].groupby(["Ano"]).mean()
climaCba_med_min # temperatura média das temperaturas mais baixas
climaCba_med_min.head()
climaCba_med_min.tail()

# máximas
climaCba_max = climaCba[["Data", "TempMaxima"]].dropna()
climaCba_max["Ano"] = climaCba_max["Data"].dt.year
climaCba_max = climaCba_max[["Ano", "TempMaxima"]].groupby(["Ano"]).max()
climaCba_max  # temperatura média das temperaturas mais altas
climaCba_max.head()
climaCba_max.tail()

# mínimas
climaCba_min = climaCba[["Data", "TempMinima"]].dropna()
climaCba_min["Ano"] = climaCba_min["Data"].dt.year
climaCba_min = climaCba_min[["Ano", "TempMinima"]].groupby(["Ano"]).min()
climaCba_min  # temperatura média das temperaturas mais altas
climaCba_min.head()
climaCba_min.tail()

# df
climaCba_med_media = climaCba_med_media.rename(columns={"Temp_Comp_Media": "media_Media"})
climaCba_med_max = climaCba_med_max.rename(columns={"TempMaxima": "media_Maxima"})
climaCba_med_min = climaCba_med_min.rename(columns={"TempMinima": "media_Minima"})
climaCba_max = climaCba_max.rename(columns={"TempMaxima": "Maxima"})
climaCba_min = climaCba_min.rename(columns={"TempMinima": "Minima"})

climaCba_df = climaCba_med_media.join(climaCba_med_max["media_Maxima"])
climaCba_df = climaCba_df.join(climaCba_med_min["media_Minima"])
climaCba_df = climaCba_df.join(climaCba_max["Maxima"])
climaCba_df = climaCba_df.join(climaCba_min["Minima"])
climaCba_df
climaCba_df.head()
climaCba_df.tail()

## DADOS P/ GRÁFICOS
# Lista dos arquivos no diretório
os.listdir()

# prompt padrão (mac ou linux): descobrir o codec dos arquivos
# file slavevoyages.csv
# file amazon.csv

## Dados Escravidão
# https://www.slavevoyages.org/
escravos = pd.read_csv("slavevoyages.csv", encoding = "UTF-8", sep = ",")
escravos.columns
renEscravos = ["ID", "Embarcacao", "Local_Navio", "Local_Compra", "Local_Desembarque", "Ano", "Qtde_Escravos", "Capitao"]
escravos.columns = renEscravos # renomear colunas
escravos
escravos.info()
escravos.describe()

# Análise da coluna "Qtde_Escravos"
# escravos.iloc[:,6].sum() 
# escravos.iloc[:,6].max()
# escravos.iloc[:,6].mean()
# escravos.iloc[:,6].std()

## Dados de queimadas na Amazônia
# https://www.kaggle.com/gustavomodelli/forest-fires-in-brazil
amazonia = pd.read_csv("amazon.csv", encoding = "iso-8859-1", sep = ",")
renAmazonia = ["Ano", "Estado", "Mes", "Queimadas_Qtde", "Data"]
amazonia.columns = renAmazonia
amazonia
# amazonia.info()
# amazonia.describe()

## Dados Pokemon
pokemon = pd.read_csv("Pokemon.csv", encoding = "latin1", sep = ",", index_col = 0)
pokemon

#### 2. ORGANIZAÇÃO E TRANSFORMAÇÃO DOS DADOS ####

## Criar dataframe
cervejas = {
	"Cerveja": ["Heineken", "Brahma", "Amstel", "Original"],
    "Mililitros": [330, 270, 285, 330],
	"Custo": [32, 45, 67, 43],
	"Valor": [4, 2.5, 3, 3.5],
	"Qtde": [110, 90, 80, 87]
}
cervejas = pd.DataFrame(cervejas)
cervejas
ƒ
## Operações entre colunas
cervejas["Vendas"] = cervejas["Valor"] * cervejas["Qtde"]
cervejas["Acumulado"] = cervejas["Vendas"].cumsum()
cervejas["Preco_Litro"] = cervejas["Valor"] / cervejas["Mililitros"]
cervejas["Resultado"] = cervejas["Vendas"] - cervejas["Custo"]
cervejas


#### 2.1 Visão geral dos dados
titan.head() # Cabeçalho
titan.tail() # Rodapé
print(titan.to_string()) # Imprime todo o dataframe
len(titan) # Nr. de linhas
titan.columns # Nome das colunas
titan.shape # nr. linhas e nr. colunas
titan.info() # Visão resumida do df -- colunas, nr. linhas e nr. colunas
titan.count() # Contagem de dados não nulos (linhas), por coluna
titan.isna().sum() # Contagem de dados nulos (linhas), por coluna
titan.isna().mean().round(2) # % de dados nulos (linhas), por coluna
titan.describe() # Estatística descritiva do df
print(titan.describe()["Survived"]) # Estatística descritiva de apenas uma coluna
type(titan) # Tipo/classe do objeto
titan2 = titan.copy() # Cria uma cópia do df

titan = titan[["Survived", "Pclass", "Sex", "Age", "Fare", "Embarked"]]
renTitan = ["Sobreviventes", "Classe", "Sexo", "Idade", "Custo_Passagem", "Local_Embarque"]
titan.columns = renTitan

titan["Local_Embarque"] = titan["Local_Embarque"].astype("str") # Mudar o tipo da coluna para string (nome da coluna)
titan["Local_Embarque"] = titan["Local_Embarque"].str.replace("S", "Southampton") # Substituir o nome da variável (nome da coluna)
titan["Local_Embarque"] = titan["Local_Embarque"].str.replace("C", "Cherbourg") # Substituir o nome da variável (nome da coluna)
titan["Local_Embarque"] = titan["Local_Embarque"].str.replace("Q", "Queenstown") # Substituir o nome da variável (nome da coluna)
titan["Sexo"] = titan["Sexo"].str.replace("female", "mulheres") # Substituir as variáveis (linhas da coluna)
titan["Sexo"] = titan["Sexo"].str.replace("male", "homens") # Substituir as variáveis (linhas da coluna)

titan.info()
titan

#### 2.2 Separar, inserir e excluir colunas
## Separar colunas (subset)
ageSex = titan[["Age", "Sex"]]
ageSex.head() # Separar

## Inserir coluna
# Criar nova coluna (addCol) com nrs. aleatórios
import random
addCol = []
n = len(titan)

for x in range(1):
	linha = []
	for y in range(n):
		linha = random.randint(1,100)
		addCol.append(linha)
print(addCol)
len(addCol)

# Inserindo a nova coluna
ageSex["novaColuna"] = addCol # Modo padrão do Python
ageSex.insert(3, "newCol", sorted(addCol)) # Modo pandas
print(ageSex)

# Exemplo 2 de inserir coluna: criar um novo df
df = {
"País": ["Bélgica", "Índia", "Brasil","Índia"],
"Capital": ["Bruxelas", "Nova Delhi", "Brasília", "Nova Delhi"],
"População": [123465, 456789, 987654, 456789]
}
df = pd.DataFrame(data=df)
print(df)

df["Pobreza"] = ["não", "sim", "sim", "sim"] # Modo padrão do Python
df.insert(4, "PIB_bi_dlrs", [100.2, 240.7, 1000.4, 240.7]) # Modo pandas
print(df)

## Excluir coluna
del ageSex["novaColuna"] # Modo padrão do Python
ageSex.drop("newCol", axis=1, inplace=True) # Modo pandas
print(ageSex)

del df["Pobreza"]
df.drop("PIB_bi_dlrs", axis=1, inplace=True)
print(df)

#### 2.3 Renomear colunas
# https://www.geeksforgeeks.org/python-change-column-names-and-row-indexes-in-pandas-dataframe/
ageSex.columns
ageSex.rename(columns={"Age": "idade", "Sex": "sexo", "novaColuna": "coluna1", "newCol": "coluna2"}, inplace=True) # Modo 1

df.columns
novosNomes = ["Country", "Capital", "Population"]
df.columns = novosNomes # Modo 2

dados = [[1, 2, 3],
		 [4, 5, 6],
		 [7, 8, 9]]
print(dados)

colunas = ["coluna1", "coluna2", "coluna3"]
modo3 = pd.DataFrame(data = dados, columns = colunas) # Modo 3
print(modo3)

df.columns.str.replace(" ", "_") # Modo 4: substitui caracteres no nome das colunas (este não vai funcionar aqui pq o df atual não tem espaço -- apenas p/ ex.)

#### 2.4 Selecionar dados (linhas e colunas)
babel.head(10)
babel[["rowguid", "AddressID"]] # Seleciona colunas

# Usando o loc e iloc
# https://medium.com/horadecodar/data-science-tips-02-como-usar-loc-e-iloc-no-pandas-fab58e214d87
babel.loc[0] # Retorna a primeira linha
babel.loc[0:3,] # Retorna as quatro primeiras linhas
babel.loc[2:4] # Retorna das linha 3 a 5
babel.loc[2:4, ["AddressID", "rowguid"]] # Retorna das linha 3 a 5 de duas colunas selecionadas
babel.loc[2:4, "AddressID":"rowguid"] # Retorna das linha 3 a 5 ENTRE as duas colunas selecionadas

babel.iloc[0] # Retorna a primeira linha
babel.iloc[-1] # Retorna a última linha
babel.iloc[:,1] # Retorna todas as linhas da segunda coluna
babel.iloc[0:20,] # Retorna as 20 primeiras linhas de todas as colunas
babel.iloc[0:10, 1] # Retorna as 10 primeiras linhas de todas as colunas
babel.iloc[[0,3,5], [3,4,6]] # retorna a primeira, quarta e sexta linhas da quarta, quinta e sétima coluna
babel.iloc[3:8, [1, 3, 6]] # Retorna das linha 4 a 7 das colunas 4, 5 e 6

# Usando o filter
bank.head()
bank.filter(items=["job", "marital"])
bank.filter(like="ult") # Seleciona apenas as colunas que contenham "ult". Neste caso "default"

#### 2.5 Ordenar os dados
babel.sort_values("City")
babel.sort_values("City").head() # Ordena, mas não altera o df original

# Alterando o ordenamento
ordemBabel = babel.sort_values("City")
ordemBabel.head # Modo 1

babel.sort_values("City", inplace=True) # Modo 2
babel.head()

#### 2.6 Operadores lógicos
bank.head()
bank[bank.marital == "single"].head() # Seleciona apenas os solteiros
bank[(bank.marital == "single") & (bank.education == "primary")].head() # Seleciona apenas os solteiros e com educação primária
bank[(bank.marital == "married") & (bank.education == "tertiary")][["age", "job"]] # Seleciona apenas as colunas "age" e "job" dos casados E com educação superior
bank[(bank.marital == "married") & (bank.education == "tertiary") | (bank.education == "secondary")] # Seleciona apenas os casados com educação superior OU nível médio

#### 2.7 Operador isin
bank.head()
bank[(bank.marital == "married") & ((bank.education == "primary") | (bank.education == "secondary"))].shape # Modo 1: com operador lógico
bank[(bank.marital == "married") & (bank.education.isin(["primary", "secondary"]))].shape # Modo 2: com isin
filtroIs = bank.isin({"marital": ["married"], "education": ["primary", "secondary"]}) # Modo 3: Usando o isin p/ mais de um tipo de operação. Criando um filtro de valores 

# lógicos por meio de um dicionário
filtroIs.shape # Modo 3: 
bank[(filtroIs.marital) & (filtroIs.education)].shape # Modo 3

#### 2.8 Tabelas
## Pivot (sentido word/excel)
# https://www.vooo.pro/insights/pivot-table-em-pandas-explicado/
bank.head()
pd.pivot_table(bank, index=["contact", "education"]) # Média (o padrão do pivot no pandas) de cada variável quantitativa (age, balance, campaign...) por tipo de contato (celular, fixo ou desconhecido) e nível de escolaridade (primário, secundário, superior, desconhecido)
pd.pivot_table(bank, index=["contact", "education"], values=["age", "balance"], aggfunc=[np.sum, np.mean]) # Soma e média das variáveis age e balance por tipo de contato (celular, fixo ou desconhecido) e nível de escolaridade (primário, secundário, superior, desconhecido)

## Melt (sentido bancos de dados)
# https://app.getpocket.com/read/2985259411
bank_pivot = pd.pivot_table(bank, index=["contact", "education"], values=["age", "balance"], aggfunc=[np.sum, np.mean]) # Soma e média das variáveis age e balance por tipo de contato (celular, fixo ou desconhecido) e nível de escolaridade (primário, secundário, superior, desconhecido)
pd.melt(bank_pivot) # Desfaz a tabela (em sentido word/excel) e a transforma em tabela (sentido banco de dados)

## 2.9 Lidando com valores nulos no Pandas (null, NaN, NA)
# https://jakevdp.github.io/PythonDataScienceHandbook/03.04-missing-values.html

## 2.10 Gerando números aleatórios
import random

random.random() # um float entre 0 e 1
random.randint(1, 5) # um int no intervalo
random.uniform(1, 100) # um float no intervalo
random.seed() # Defina um nr. como o índice do "seed" (ex.: random.seed(12)) e ele vinculará a aleatoriedade a esta "semente", travando o(s) nr(s)
np.random.rand(40) # Numpy gera n nrs aleatórios entre 0 e 1

# Criar uma lista
alea = [] # 1º: começa com ela vazia

for i in range(0, 10):
	alea.append(random.randint(0, 100)) # 2º: faz o loop e as apensa na var da lista

print(alea) # 3º: confirme se deu certo

#### 3. ANÁLISE DOS DADOS ####

## 3.1 AED
bank.head()
bank.describe() # Estatística descritiva dos dados

# Apenas uma variável (age)
bank.age.min() # Valor mínimo
bank.age.max() # Valor máximo
bank.age.mean() # Média
bank.age.std() # Desvio padrão
bank.age.quantile(.75) # Terceiro quartil (pode-se inserir qualquer valor)

## Groupby
# Normal
bank[bank.marital == "single"].age.mean() # Média de idade das pessoas solteiras
bank[bank.marital == "married"].age.mean() # Média de idade das pessoas casadas
bank[bank.marital == "divorced"].age.mean() # Média de idade das pessoas divorciadas

# Usando o groupby
bank[["marital", "age"]].head()
bank[["marital", "age"]].groupby(["marital"]).mean() # O mesmo resultado do anterior (normal), mas agora agrupado

bank[["marital", "education", "age"]].groupby(["marital", "education"]).mean() # A média do status civil de acordo com o nível de escolaridade

# Exercício: Média do balanço das pessoas com idade entre 30 e 50 anos, casadas e separadas
colunas = ["balance", "marital"]
bank[((bank.age>=30) & (bank.age<50)) & (bank.marital.isin(["married", "divorced"]))].head()
bank[((bank.age>=30) & (bank.age<=50)) & (bank.marital.isin(["married", "divorced"]))].shape # Volta todas as colunas
bank[((bank.age>=30) & (bank.age<=50)) & (bank.marital.isin(["married", "divorced"]))][colunas].head() # Volta apenas as colunas balance e marital
bank[((bank.age>=30) & (bank.age<=50)) & (bank.marital.isin(["married", "divorced"]))][colunas].groupby("marital").mean() # Volta apenas as colunas balance e marital

#### 4. MODELAGEM ####
# Statsmodels:
#             - https://www.statsmodels.org/stable/index.html#
#             - https://mode.com/python-tutorial/libraries/statsmodels/

### 4.1 Regressão linear

### 4.2 Regressão logística

### 4.3 Séries temporais

# Regressão linear
# Regressão logística

#### 5. VISUALIZAÇÃO ####
## LINKS
# Matplolib: 
#           - https://matplotlib.org/
#           - https://matplotlib.org/3.1.1/gallery/index.html
#           - https://matplotlib.org/3.1.1/users/dflt_style_changes.html (estilos: cores, linhas, fontes)
#           - https://www.rapidtables.com/web/color/RGB_Color.html (tabela de cores)
#           - https://matplotlib.org/api/pyplot_summary.html (índice de todos os comandos)
#           - https://pythonspot.com/matplotlib-gallery/
#           - https://realpython.com/python-matplotlib-guide/
#           - https://king.host/blog/2018/03/visualizacao-de-dados-matplotlib/
# Seaborn: 
#          - https://seaborn.pydata.org/
#          - https://jakevdp.github.io/PythonDataScienceHandbook/04.14-visualization-with-seaborn.html
#          - https://seaborn.pydata.org/examples/index.html (** galeria de gráficos **)
#          - https://seaborn.pydata.org/api.html # (Comandos detalhados)
#          - https://seaborn.pydata.org/generated/seaborn.set_style.html#seaborn.set_style (estilos)
#          - https://seaborn.pydata.org/tutorial/color_palettes.html (paleta de cores)
#          - https://elitedatascience.com/python-seaborn-tutorial
# Outras bibliotecas:
#                     - Plotly: https://plotly.com/python/
#                     - Bokeh: https://docs.bokeh.org/en/latest/
#                     - ggplot (for Python): http://ggplot.yhathq.com/
# https://datavizproject.com/
# https://infogram.com/page/choose-the-right-chart-data-visualization

### 5.0 O básico do matplolib ###

## 5.0.1 Plotar um gráfico simples
plt.plot([1,2,3], [5,7,4])
plt.show() # O gráfico padrão do plt é o de linhas

## Legendas, títulos e rótulos
x = [1,2,3]
y = [5,7,4]

x2 = [1,2,3]
y2 = [10,14,12]

plt.plot(x, y, label = "Primeira linha")
plt.plot(x2, y2, label = "Segunda linha")

plt.xlabel("Eixo x sem sem nome")
plt.ylabel("Eixo y sem sem nome")
plt.title("Gráfico interessante\n dá uma olhada!")
plt.legend()

plt.show()

## 5.0.2 Estilos matplobib
# https://matplotlib.org/3.2.1/tutorials/introductory/customizing.html (configurações manuais)
# https://jakevdp.github.io/PythonDataScienceHandbook/04.11-settings-and-stylesheets.html (configurações manuais)
# https://medium.com/@andykashyap/top-5-tricks-to-make-plots-look-better-9f6e687c1e08 (configurações manuais)
# https://matplotlib.org/3.1.0/gallery/style_sheets/style_sheets_reference.html
# https://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html 

## 5.0.3 Estilos Seaborn
# https://seaborn.pydata.org/tutorial/aesthetics.html

###################################
### 5.1 GRÁFICOS DE COMPARAÇÃO ###
###################################
## 5.1.1 Barras/colunas (vertical e horizontal)
# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar
x = [1,3,5,7,9]
y = [5,2,7,8,2]

x2 = [2,4,6,8,10]
y2 = [8,6,2,5,6]

plt.bar(x, y, label = "Ex. G. Barras 1")
plt.bar(x2, y2, label = "Ex. G. Barras 2", color = "b") # Vertical

# plt.barh(x, y, label = "Ex. G. Barras 1")
# plt.barh(x2, y2, label = "Ex. G. Barras 2", color = "b") # Horizontal

plt.legend()
plt.xlabel("Nr. da barra")
plt.ylabel("Altura da barra")
plt.title("Gráfico de barras no plt\n Veja como funciona")

plt.show()

## Seanborn barras
titan

sns.catplot(x = "Classe", y = "Sobreviventes", hue = "Sexo", data = titan, height = 6, kind = "bar", ci = None)
plt.ylabel("Probabilidade de sobrevivência")
plt.show() # Vertical

sns.catplot(x = "Sobreviventes", y = "Classe", hue = "Sexo", data = titan, height = 6, kind = "bar", ci = None, orient = "horizontal")
plt.xlabel("Probabilidade de sobrevivência")
plt.show() # Horizontal

## 5.1.2 Linhas
# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
random.seed(1) 
x = []
y = []
for i in range(0, 10):
	x.append(random.randint(0, 100))
	y.append(random.randint(0, 100))
	x.sort() # p/ ordenar
	y.sort()
print("x =", x, "e", "y =", y)

plt.plot(x, label = "x")
plt.plot(y, label = "y")
plt.legend()
plt.show()

## Seanborn linhas
data = pd.to_datetime(climaCba["Data"])
temp = climaCba["TempMaxima"]
cba = pd.DataFrame(temp, data)
cba

sns.catplot(data = temp)
plt.show()

rs = np.random.RandomState(365)
values = rs.randn(365, 4).cumsum(axis=0)
values
dates = pd.date_range("1 1 2016", periods=365, freq="D")
dates
data = pd.DataFrame(values, dates, columns=["A", "B", "C", "D"])
data
data = data.rolling(7).mean()

sns.lineplot(data=data, palette="tab10", linewidth=2.5)
plt.show()

## Seanborn linhas 2
# https://seaborn.pydata.org/generated/seaborn.lineplot.html
sns.set_palette("deep")
plt.rcParams["xtick.labelsize"] = 9
plt.rcParams["ytick.labelsize"] = 9
sns.lineplot(data = climaCba_df, legend = False, dashes = False).set_title("TEMPERATURAS EM CUIABA (1961-2019)\nEm graus Celsius")
sns.despine(left = False, bottom= False, top = True, right = True)
plt.xlabel("")
plt.show()

## 5.1.3 Bolhas (três ou mais variáveis)
# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter
x = np.random.rand(40)
y = np.random.rand(40)
z = np.random.rand(40)
 
plt.scatter(x, y, s=z*1000, alpha=0.5)
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.show()

###################################
### 5.2 GRÁFICOS DE COMPOSIÇÃO ###
###################################
## 5.2.1 Setores (pizza)
# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.pie.html
bichos = ["Sapos", "Catetos", "Cachorros", "Gatos", "Galinhas", "Hipopótamos"]
tamanhos = [15, 30, 45, 10, 67, 44]
focus = (0, 0.1, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. "Hogs")

fig1, ax1 = plt.subplots()
ax1.pie(tamanhos, explode = focus, labels = bichos, autopct = "%1.1f%%", shadow = True, startangle = 90)
ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.suptitle("Bichos encontrados")
plt.title("") # https://python-graph-gallery.com/190-custom-matplotlib-title/

plt.show()

## 5.2.2 Mapa de árvore (treemap)
# https://matplotlib.org/api/pyplot_summary.html
import squarify

bichos = ["Sapos\n encontrados: 15", "Catetos\n encontrados: 30", "Cachorros\n encontrados: 45", 
          "Gatos\n encontrados: 10", "Galinhas\n encontrados: 67", "Hipopótamos\n encontrados: 44"]
tamanhos = [15, 30, 45, 10, 67, 44]
cores = ["#0f7216", "#b2790c", "#ffe9a3", "#f9d4d4", "#d35158", "#6A5ACD"]

plt.rc("font", size=10)
squarify.plot(sizes = tamanhos, label = bichos, color = cores, alpha=0.7)
plt.axis("off")

plt.show()

## 5.2.3 Gráfico de Waffles
# https://stackoverflow.com/questions/41400136/how-to-do-waffle-charts-in-python-square-piechart
#
from pywaffle import Waffle
from matplotlib import cm # https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html (colormaps (mapas de cor))

# df (tem que ser como dicionário)
dfBichos = {"Sapos": 15, "Catetos": 30, "Cachorros": 45, "Gatos": 10, "Galinhas": 67, "Hipopótamos": 44}
dfBichos

# Gráfico 1 (quadradinhos)
fig = plt.figure(
	FigureClass = Waffle, 
    rows = 7, 
    values = dfBichos, 
    colors = ("#008000", "#8B4513", "#B8860B", "#4169E1", "#DC143C", "#778899"),
    title = {"label": "Bichos encontrados", "loc": "left"},
    labels = ["{0} ({1})".format(k, v) for k, v in dfBichos.items()],
    legend={"loc": "lower left", "bbox_to_anchor": (0, -0.3), "ncol": len(dfBichos), "framealpha": 0}
	)
fig.gca().set_facecolor("#EEEEEE")
fig.set_facecolor("#EEEEEE")
plt.show()

# Gráfico 2 (bichos)
fig = plt.figure(
	FigureClass = Waffle, 
    rows = 7, 
    values = dfBichos, 
    colors = ("#008000", "#778899", "#B8860B", "#4169E1", "#DC143C", "#8B4513"),
	legend={"loc": "lower left", "bbox_to_anchor": (0, -0.2), "ncol": len(dfBichos), "framealpha": 0},
	icons = ["frog", "piggy-bank", "dog", "cat", "crow", "hippo"], # https://fontawesome.com/icons?d=gallery
    font_size = 14,
    icon_style = "solid",
	icon_legend = True,
	labels = ["{0} ({1})".format(k, v) for k, v in dfBichos.items()],
	title = {"label": "Bichos encontrados", "loc": "left", "fontsize": 14, "fontweight": "bold"}
)
fig.gca().set_facecolor("#EEEEEE")
fig.set_facecolor("#EEEEEE")
plt.show()

# Gráfico 3 (bolinhas)
fig = plt.figure(
	FigureClass = Waffle, 
    rows = 8, 
    values = dfBichos, 
    colors = ("#008000", "#8B4513", "#B8860B", "#4169E1", "#DC143C", "#778899"),
    title = {"label": "Bichos encontrados", "loc": "left"},
    labels = ["{0} ({1})".format(k, v) for k, v in dfBichos.items()],
    legend={"loc": "lower left", "bbox_to_anchor": (0, -0.2), "ncol": len(dfBichos), "framealpha": 0},
	icons = "circle", icon_size = 18, 
    icon_legend = True
	)
fig.gca().set_facecolor("#EEEEEE")
fig.set_facecolor("#EEEEEE")
plt.show()

## 5.2.4 Barras empilhadas
# https://matplotlib.org/3.2.1/gallery/lines_bars_and_markers/bar_stacked.html
rotulos = ["G1", "G2", "G3", "G4", "G5"]
mascMedia = [20, 35, 30, 35, 27]
femMedia = [25, 32, 34, 20, 25]
mascDP = [2, 3, 4, 1, 2] # DP: Desvio padrão
femDP= [3, 5, 2, 3, 3]
largura = 0.35

fig, ax = plt.subplots()
ax.bar(rotulos, mascMedia, largura, yerr = mascDP, label = "Homens")
ax.bar(rotulos, femMedia, largura, yerr = femDP, bottom = mascMedia, label = "Mulheres")
ax.set_ylabel("Pontuação")
ax.set_title("Pontuação por grupo e sexo")
ax.legend()

plt.show()

## 5.2.5 Cachoeira (waterfall)
# https://pbpython.com/waterfall-chart.html
# # Não sei se funcionou, mas não pretendo utilizar este gráfico. É muito confuso.
refri = ["Coca-cola", "Fanta", "Sprite", "Guaraná", "Refrigereco", "Kapo"]
entraSai = {"qtde": [350000, -30000, -7500,-25000,95000,-7000]}
estoque = pd.DataFrame(data = entraSai, index = refri)
saldo = estoque.cumsum() # calculando fac da coluna estoque
estoque.insert(1, "saldo", saldo) # inserindo a coluna no df
estoque

branco = estoque.qtde.cumsum().shift(1).fillna(0)
branco

total = estoque.sum().qtde
estoque.loc["liquido"] = total
branco.loc["liquido"] = total
branco.loc["liquido"] = 0
estoque
branco

passo = branco.reset_index(drop=True).repeat(3).shift(-1)
passo[1::3] = np.nan
passo

estoque.plot(kind = "bar", stacked = True, bottom = branco,legend = None, title = "Vendas de bebidas em 2014")
estoque.plot(kind = "kde")
plt.show() 

## 5.2.6 Área empilhada
# Versão simples
anos = np.arange(1980, 1985, 1) # x
dormindo = [7,8,6,11,7] # y
comendo =   [2,3,4,3,2] # y
trabalhando =  [7,8,7,2,2] # y
brincando =  [8,5,7,8,13] # y
cores = ["m", "c", "r", "k"]

plt.stackplot(anos, dormindo, comendo, trabalhando, brincando, colors = cores, )

plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.title("Gráfico de área simples\n Aprendendo no Python")

plt.show()

# Versão aperfeiçoada
anos = np.arange(1980, 1985,1) # x
dormindo = [7,8,6,11,7] # y
comendo =   [2,3,4,3,2] # y
trabalhando =  [7,8,7,2,2] # y
brincando =  [8,5,7,8,13] # y
cores = ["m", "c", "r", "k"]

plt.plot([],[],color = "m", label = "dormindo", linewidth = 5)
plt.plot([],[],color = "c", label = "comendo", linewidth = 5)
plt.plot([],[],color = "r", label = "trabalhando", linewidth = 5)
plt.plot([],[],color = "k", label = "brincando", linewidth = 5)

plt.stackplot(anos, dormindo, comendo, trabalhando, brincando, colors = cores)

plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.xlim(1980, 1985) # Especificando o limite do eixo
plt.title("Gráfico de área aperfeiçoado\n Aprendendo no Python")
plt.legend()

plt.show()

################################
### 5.3 GRÁFICOS DE RELAÇÃO ###
################################
## 5.3.1 Dispersão (duas variáveis)
x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]

plt.scatter(x, y, label = "Pontinhos", color = "k", marker = "o")

plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.title("Gráfico de dispersão\n Aprendendo no Python")
plt.legend()

plt.show()

## Seaborn dispesão
# https://seaborn.pydata.org/examples/anscombes_quartet.html
sns.lmplot(x = "Attack" , y = "Defense" , data = pokemon) # jeito simples
plt.show()

sns.lmplot(x = "Attack" , y = "Defense" , data = pokemon, fit_reg = False, hue = "Stage")
plt.ylim(0, None)
plt.xlim(0, None)
plt.show()

#####################################
### 5.4 GRÁFICOS DE DISTRIBUIÇÃO ###
#####################################
## 5.4.1 Histograma de barras
populacao = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(populacao, bins, histtype = "bar", rwidth = 0.8, color = "b", cumulative = False)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Gráfico bacaninha\nSubtítulo aqui")
plt.legend()
plt.show()

## 5.4.2 Histograma de linhas
# Parametrizar a distribuição em normal
d1 = sps.norm(0, 10)
d2 = sps.norm(60, 15)

# Amostra aleatória com base na distribuição
y1 = d1.rvs(300)
y2 = d2.rvs(200)

# Transformar em df
ys = np.concatenate([y1, y2])

# Histograma mostrando componentes individuais
plt.hist([y1, y2], 31, histtype = "barstacked", density = True, alpha = 0.4, edgecolor = "none")

# Pegar x limites e os fixe
mn, mx = plt.xlim()
plt.xlim(mn, mx)

# Adicionar nossa distribuição ao gráfico
x = np.linspace(mn, mx, 301)
plt.plot(x, d1.pdf(x) * (len(y1) / len(ys)), color = "C0", ls = "--", label = "d1")
plt.plot(x, d2.pdf(x) * (len(y2) / len(ys)), color = "C1", ls = "--", label = "d2")

# Estimar a densidade e plotar
kde = sps.gaussian_kde(ys)
plt.plot(x, kde.pdf(x), label = "kde")

# Terminando
plt.legend()
plt.ylabel("Densidade de probabilidade")
sns.despine()
plt.show()

## 5.4.3 Tabela de histograma

## 5.4.4 Boxplot
# https://matplotlib.org/gallery/pyplots/boxplot_demo_pyplot.html#sphx-glr-gallery-pyplots-boxplot-demo-pyplot-py
espalhar = np.random.rand(50) * 100
centralizar = np.ones(25) * 50
outlierMais = np.random.rand(10) * 100 + 100
outlierMenos = np.random.rand(10) * -100
dfBoxplot = np.concatenate((espalhar, centralizar, outlierMais, outlierMenos))

fig1, ax1 = plt.subplots()
ax1.set_title("Exemplo de boxplot")
ax1.boxplot(dfBoxplot)
plt.show()

## 5.4.5 Violino
# Ex. 1
espalhar = np.random.rand(50) * 100
centralizar = np.ones(25) * 50
outlierMais = np.random.rand(10) * 100 + 100
outlierMenos = np.random.rand(10) * -100
dfBoxplot = np.concatenate((espalhar, centralizar, outlierMais, outlierMenos))

fig1, ax1 = plt.subplots()
ax1.set_title("Exemplo de boxplot")
ax1.violinplot(dfBoxplot)
plt.show()

# Ex. 2: https://www.tutorialspoint.com/matplotlib/matplotlib_violin_plot.htm
np.random.seed(10)
collectn_1 = np.random.normal(100, 10, 200)
collectn_2 = np.random.normal(80, 30, 200)
collectn_3 = np.random.normal(90, 20, 200)
collectn_4 = np.random.normal(70, 25, 200)

data_to_plot = [collectn_1, collectn_2, collectn_3, collectn_4]
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

bp = ax.violinplot(data_to_plot)
plt.show()

# Ex. 3: Seaborn violino
# https://seaborn.pydata.org/examples/wide_form_violinplot.html
sns.set(style="whitegrid")

# Load the example dataset of brain network correlations
df = sns.load_dataset("brain_networks", header=[0, 1, 2], index_col=0)

# Pull out a specific subset of networks
used_networks = [1, 3, 4, 5, 6, 7, 8, 11, 12, 13, 16, 17]
used_columns = (df.columns.get_level_values("network")
                          .astype(int)
                          .isin(used_networks))
df = df.loc[:, used_columns]

# Compute the correlation matrix and average over networks
corr_df = df.corr().groupby(level="network").mean()
corr_df.index = corr_df.index.astype(int)
corr_df = corr_df.sort_index().T

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 6))

# Draw a violinplot with a narrower bandwidth than the default
sns.violinplot(data=corr_df, palette="Set3", bw=.2, cut=1, linewidth=1)

# Finalize the figure
ax.set(ylim=(-.7, 1.05))
sns.despine(left=True, bottom=True)
plt.show()

#######################################################
### 5.5 ESTRUTURAS DE TOPOLOGIA (relações e fluxos) ###
#######################################################
###  ###

## 5.5.1 Mapa de calor (heatmap)
sns.set()
uniform_data = np.random.rand(12, 12)
ax = sns.heatmap(uniform_data, vmin=0, vmax=1)
plt.show()

## Grafos
## Rede em árvore
## Diagrama de Venn
## Pirâmide

### 5.6 Tabelas estilizadas ###

### 5.7 Mapas ###

### 5.8 Nuvem de palavras (wordcloud)

#### 6. PROGRAMAÇÃO ####

### 6.1 Funções ###
# Uma função é um objeto que você pode "chamar".

# Ex. 1
def add (x, y):
	return(x + y)

add(1, 2)

# Ex. 2
def add(x, y = 1):
	return(x+y)

add(3)
add(3, 2)

## Ex. 3
def calc(x, y, type):
	if type == "add":
		return(x + y)
	elif type == "menos":
		return(x - y)
	elif type == "mult":
		return(x * y)
	elif type == "div":
		return(x / y)
	else:
		print("Operação não encontrada")

calc(2, 2, "add")
calc(2, 2, "menos")
calc(2, 2, "mult")
calc(2, 2, "div")
calc(2, 3, "nao")

# Ex. 4
def greet(*names):
	"""Essa função cumprimenta todas as pessoas
	com os nomes na tupla"""

	for i in names:
		print("Oi,", i)

greet("João", "Maria", "Pedro", "Lula", "Bolsonaro")

### 6.2 If Else ###
x = 1

if (x > 0):
	print("Número positivo!")
else:
	print("Número negativo!")

### 6.3 For Loops ###
# Básico: "para cada ITEM (i) em um VETOR (v), faça tal coisa com i"
x = ["a", "b", "c", "d", "e"]

for i in x:
	print("Letra", i)

for i in x: 
	print(i)

for i in range(1, 10):
	print(i)

### 6.4 While ###
# Ex. 1
x = 2
y = 10

while x < y:
	print(x)
	x += 1

# Ex. 2
counter = 0

while counter < 3:
	print("dentro do loop")
	counter += 1
else:
	print("dentro de else")

### 6.5 Break e Continue ###
for val in "string":
    if val == "i":
        break
    print(val)

# Continue
x = np.arange(1, 11)
y = 7

for i in x:
	if i == y:
		continue
	print(i)

### 7. OBJETOS E CLASSES ###

#### 8. ASSUNTOS DIVERSOS ####
### 8.1 Funcões lambda ###
# Função anônima
dobrar = lambda x: x * 2
dobrar(2)

### 8.2 map ###
### 8.3 Data e hora