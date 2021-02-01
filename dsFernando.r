#### DATA SCIENCE (R)
## Principais pacotes/bibliotecas
# - Tidyverse [https://www.tidyverse.org/]
#             - readr (importação de dados) [https://readr.tidyverse.org/]
#             - dplyr (manipulação de dados) [https://dplyr.tidyverse.org/]
#             - tibble (dataframe) [https://tibble.tidyverse.org/]
#             - tidyr (transformação de dataframe) [https://tidyr.tidyverse.org/]
#             - purr (programação funcional) [https://purrr.tidyverse.org/]
#             - ggplot (gráficos) [https://ggplot2.tidyverse.org/]
# http://material.curso-r.com/rbase/
# wsl 23122020
# Como usar o github no RStudio: https://beatrizmilz.github.io/RLadies-Git-RStudio-2019/#1

#### 0. IMPORTAÇÃO DE PACOTES ####
## Configuração de ambiente (antes)
setwd("/Users/fernandovieira/OneDrive/1. Educacao/INFO E ESTAT/RAIZ-colinhasFernando/colinhasFernando")
# setwd("C:/Users/70485992191/OneDrive/1. Educacao/INFO E ESTAT/Fernando DS - Python e R/Dados")
dir()
library(tidyverse)
library(xlsx)
library(lubridate)
library(ggthemes)

#### 1. IMPORTAÇÃO DOS DADOS ####
## CSV
url_zuru = 'https://raw.githubusercontent.com/fernandovieira1/colinhasFernando/master/DadosAulaZurubabel.csv'
zuru <- read.csv(url_zuru, fileEncoding = "UTF-8", sep = ";") # Dados Zurubabel
zuru <- as_tibble(zuru)
head(zuru)

url_titan = "https://raw.githubusercontent.com/fernandovieira1/colinhasFernando/master/titanic_data.csv"
titan <- read.csv(url_titan) # Dados Titanic
titan <- as_tibble(titan)
head(titan)

url_escravos = "https://raw.githubusercontent.com/fernandovieira1/colinhasFernando/master/slavevoyages.csv"
escravos <- read.csv(url_escravos, fileEncoding = "UTF-8", sep = ",")
escravos <- as_tibble(escravos)
escravos <- escravos %>% rename("ID" = "Identidade.da.viagem",
                                "Embarcacao" = "Vessel.name",
                                "Local_Navio" = "Voyage.itinerary.imputed.port.where.began..ptdepimp..place",
                                "Local_Compra" = "Voyage.itinerary.imputed.principal.place.of.slave.purchase..mjbyptimp.",
                                "Local_Desembarque" = "Voyage.itinerary.imputed.principal.port.of.slave.disembarkation..mjslptimp..place",
                                "Ano" = "Year.of.arrival.at.port.of.disembarkation",
                                "Qtde_Escravos" = "Slaves.arrived.at.1st.port",
                                "Capitao" = "Captain.s.name")
escravos

url_bank = "https://raw.githubusercontent.com/fernandovieira1/colinhasFernando/master/bank.csv"
bank <- read.csv(url_bank, encoding = "UTF-8", sep = ";") # https://archive.ics.uci.edu/ml/datasets/Bank+Marketing
bank <- as_tibble(bank)
head(bank)

## Excel
babel <- read.xlsx2("Dados_Excel_Zurubabel.xlsx", 1)
babel <- as_tibble(babel)
head(babel)

## TXT
temp_cuiaba = "https://raw.githubusercontent.com/fernandovieira1/colinhasFernando/master/temp_cuiaba.txt"
climaCba <- read.table(temp_cuiaba, sep = ";", dec = ",", header = TRUE) # Ler o arquivo txt
climaCba <- climaCba %>% select("Data", "TempMaxima", "TempMinima", "Temp.Comp.Media", "Umidade.Relativa.Media") # Selecionar as colunas úteis
climaCba <- as_tibble(climaCba)
climaCba$Data <- dmy(climaCba$Data) # transformar factor em date
climaCba$TempMaxima <- as.numeric(as.character(climaCba$TempMaxima)) # transformar factor em double
climaCba$TempMinima <- as.numeric(as.character(climaCba$TempMinima)) # transformar factor em double
climaCba$Temp.Comp.Media <- as.numeric(as.character(climaCba$Temp.Comp.Media)) # transformar factor em double
climaCba$Umidade.Relativa.Media <- as.numeric(as.character(climaCba$Umidade.Relativa.Media)) # transformar factor em double
climaCba
head(climaCba)
tail(climaCba)

climaCba_limpo <- climaCba %>% filter(!is.na(TempMaxima & TempMinima & Temp.Comp.Media & Umidade.Relativa.Media))
climaCba_limpo
head(climaCba_limpo)
tail(climaCba_limpo)

# medias
climaCba_med_media <- climaCba %>% select(Data, Temp.Comp.Media) %>% filter(!is.na(Temp.Comp.Media)) %>% mutate(ano = year(Data))
climaCba_med_media <- climaCba_med_media %>% group_by(ano) %>% summarise(media_Media = mean(Temp.Comp.Media))
climaCba_med_media$ano <- as.Date(as.character(climaCba_med_media$ano), format = "%Y")
climaCba_med_media # temperatura média da média das temperaturas
head(climaCba_med_media)
tail(climaCba_med_media)

climaCba_med_max <- climaCba %>% select(Data, TempMaxima) %>% filter(!is.na(TempMaxima)) %>% mutate(ano = year(Data))
climaCba_med_max <- climaCba_med_max %>% group_by(ano) %>% summarise(media_Maxima = mean(TempMaxima))
climaCba_med_max$ano <- as.Date(as.character(climaCba_med_max$ano), format = "%Y")
climaCba_med_max # temperatura média das temperaturas mais altas
head(climaCba_med_max)
tail(climaCba_med_max)

climaCba_med_min <- climaCba %>% select(Data, TempMinima) %>% filter(!is.na(TempMinima)) %>% mutate(ano = year(Data))
climaCba_med_min <- climaCba_med_min %>% group_by(ano) %>% summarise(media_Minima = mean(TempMinima))
climaCba_med_min$ano <- as.Date(as.character(climaCba_med_min$ano), format = "%Y")
climaCba_med_min # temperatura média das temperaturas mais baixas
climaCba_med_min
head(climaCba_med_min)
tail(climaCba_med_min)

# máximas
climaCba_max <- climaCba %>% select(Data, TempMaxima) %>% filter(!is.na(TempMaxima)) %>% mutate(ano = year(Data))
climaCba_max <- climaCba_max %>% group_by(ano) %>% summarise(Maxima = max(TempMaxima))
climaCba_max$ano <- as.Date(as.character(climaCba_max$ano), format = "%Y")
climaCba_max # temperatura média das temperaturas mais altas
head(climaCba_max)
tail(climaCba_max)

# mínimas
climaCba_min <- climaCba %>% select(Data, TempMinima) %>% filter(!is.na(TempMinima)) %>% mutate(ano = year(Data))
climaCba_min <- climaCba_min %>% group_by(ano) %>% summarise(Minima = min(TempMinima))
climaCba_min$ano <- as.Date(as.character(climaCba_min$ano), format = "%Y")
climaCba_min # temperatura média das temperaturas mais baixas
head(climaCba_min)
tail(climaCba_min)

# df
climaCba_df <- climaCba_med_media %>%
                mutate(media_Maxima = climaCba_med_max$media_Maxima,
                media_Minima = climaCba_med_min$media_Minima,
                Maxima = climaCba_max$Maxima,
                Minima = climaCba_min$Minima)
climaCba_df
head(climaCba_df)
tail(climaCba_df)

## RDS
imdb <- read_rds("imdb.rds")
head(imdb)
tail(imdb)

#### 2. ORGANIZAÇÃO E TRANSFORMAÇÃO DOS DADOS ####

## Criar dataframe
df <- data.frame(
    Cerveja = c("Heineken", "Brahma", "Amstel", "Original"),
    Mililitros = c(330, 270, 285, 330),
    stringsAsFactors = FALSE
)
df

### 2.1 Visão geral dos dados
head(titan) # Cabeçalho
tail(titan) # Rodapé
View(titan) # Imprime todo o dataframe
nrow(titan) # Nr. de linhas
length(titan) # Nr. elementos / itens
colnames(titan) # Nome das colunas
dim(titan) # nr. linhas e nr. colunas
length(titan) # Qtde de itens (tamanho do vetor)
print(titan) # Visão resumida do df -- colunas, nr. linhas e nr. colunas (como tibble, via tidyverse)

colSums(is.na(titan)) # Contagem de dados nulos (linhas), por coluna (CUIDADO: r não lida bem com NaN em variáveis categóricas. A coluna 'Cabin' tem 687 obs (77%) de missing data, mas r não considerou falta de nenhuma)
round(colMeans(is.na(titan)), 2)

## Valores ausentes 
a <- is.na(df)
a # Procurar por NAs
df[a] <- 0 # Substituir NAs por 0

df[complete.cases(df),] # mantém apenas as linhas sem NAs (https://statisticsglobe.com/complete-cases-in-r-example/)

summary(titan, digits = 2) # Estatística descritiva do df
class(titan) # Tipo/classe do objeto
titan2 <- titan # Cria uma cópia do df

### 2.2 Separar, inserir e excluir colunas
## Separar colunas (subset)
ageSex = select(titan, c("Age", "Sex"))
head(ageSex) # Separar

## Inserir coluna
# Criar nova coluna (addCol) com nrs. aleatórios
addCol <- as_tibble(runif(nrow(ageSex), min = 0, max = 100))

# Inserindo
ageSex <- ageSex %>% add_column(addCol)
colnames(ageSex)

# Exemplo 2 de inserir coluna: criar um novo df (no estilo tidyverse)
df <- tibble(
País = c('Bélgica', 'Índia', 'Brasil', 'Índia'),
Capital = c('Bruxelas', 'Nova Delhi', 'Brasília', 'Nova Delhi'),
População = c(123465, 456789, 987654, 456789)
)
print(df)

df <- df %>% add_column(Pobreza = c("não", "sim", "sim", "sim")) %>% add_column(PIB_bi_dlrs = c(100.2, 240.7, 1000.4, 240.7))
df

# Exemplo 3
dados <- matrix(seq(1:9), nrow = 3, ncol = 3)
print(dados)

modo3 <- data.frame(coluna1 = dados[1, 1:3], coluna2 = dados[2, 1:3], coluna3 = dados[3, 1:3])
print(modo3)

### 2.3 Renomear colunas
colnames(ageSex) <- c("Idade", "Sexo", "colunaNova")
ageSex

colnames(df) <- c("Country", "Capital", "Population", "Poverty", "PIB_Dolars")
df

ageSex

### 2.4 Selecionar dados (linhas e colunas)
head(babel)
babel %>% select("rowguid", "AddressID") # Seleciona colunas
babel[, 1] # Retorna a primeira linha
head(babel, 4) # Retorna as quatro primeiras linhas
print(babel[3:5,]) # Retorna das linha 3 a 5
print(babel[3:5, c("AddressID", "rowguid")]) # Retorna das linha 3 a 5 de duas colunas selecionadas
print(babel[4:8, c(2, 4, 7)]) # Retorna das linha 4 a 8 das colunas 4, 5 e 6

# Usando o select
head(bank)
bank %>% select("job", "marital")

# Usando o filter
# https://sebastiansauer.github.io/dplyr_filter/
bank %>% filter(grepl("primary", education))

### 2.5 Ordenar os dados
head(babel)
tail(babel)
head(arrange(babel, City))
tail(arrange(babel, City))

### 2.6 Operadores lógicos
head(bank)
head(filter(bank, marital == "single")) # Seleciona apenas os solteiros
head(filter(bank, marital == "single" & education == "primary")) # Seleciona apenas os solteiros e com educação primária
filter(bank, marital == "married" & education == "tertiary") %>% select(c("age", "job")) # Seleciona apenas as colunas "age" e "job" dos casados E com educação superior
filter(bank, marital == "married" & education == "tertiary" | education == "secondary")

library(stringr) #  https://sebastiansauer.github.io/dplyr_filter/
bank %>% filter(str_detect(default, "yes"))

### 2.7 Selecionando partes do texto
filter(bank, marital == "married" & education %in% c("primary", "secondary"))

### 2.8 Tabelas
# https://stackoverflow.com/questions/7980030/how-to-pivot-unpivot-cast-melt-data-frame
# https://tidyr.tidyverse.org/articles/pivot.html
head(bank)

### 2.9 Lidando com valores nulos no Tidyverse (tidyr) (NA)
# https://www.r-bloggers.com/handling-missing-values-in-r-using-tidyr/
# https://medium.com/coinmonks/dealing-with-missing-data-using-r-3ae428da2d17

#### 3. ANÁLISE DOS DADOS ####

## 3.1 AED
head(bank)
summary(bank) # Estatística descritiva dos dados

# Apenas uma variável (age)
min(bank$age) # Valor mínimo
max(bank$age) # Valor máximo
mean(bank$age) # Média
sd(bank$age) # Desvio padrão
quantile(bank$age, .75) # Terceiro quartil (pode-se inserir qualquer valor)

## Groupby
head(bank)
bank %>% group_by(marital) %>% summarise(mean = mean(age)) # Média de idade das pessoas divorciadas, casadas e solteiras
bank %>% group_by(marital, education) %>% summarise(mean = mean(age)) # A média do status civil de acordo com o nível de escolaridade

# Exercício: Média do balanço das pessoas com idade entre 30 e 50 anos, casadas e separadas
bank %>% filter(age >= 30 & age < 50) %>% filter(marital == "married" | marital == "divorced") %>% head()
bank %>% filter(age >= 30 & age < 50) %>% filter(marital == "married" | marital == "divorced") %>% dim() # deu diferença para o python (93 a menos)
bank %>% filter(age >= 30 & age < 50) %>% filter(marital == "married" | marital == "divorced") %>% group_by(marital) %>% summarise(mean = mean(balance)) # Volta apenas as colunas balance e marital

## Sapply
head(iris)
tail(iris)
sapply(iris[,1:4], mean)

#### 4. MODELAGEM ####
# https://medium.com/data-hackers/tutorial-ajuste-e-interpreta%C3%A7%C3%A3o-de-regress%C3%A3o-linear-com-r-5b23c4ddb72

### 4.1 Regressão linear

### 4.2 Regressão logística

### 4.3 Séries temporais

#### 5. VISUALIZAÇÃO ####
# ggplot: 
#        - https://www.curso-r.com/material/ggplot/
#        - https://www.r-graph-gallery.com/index.html (** galeria de gráficos **)
#        - https://ggplot2.tidyverse.org/reference/ggplot.html
#        - https://ggplot2.tidyverse.org/reference/ (o melhor)
#        - https://ggplot2.tidyverse.org/
#        - http://curso-r.github.io/posts/aula05.html
#        - http://sape.inf.usi.ch/quick-reference/ggplot2/colour (cores ggplot)
#        - https://garthtarr.github.io/meatR/ggplot_extensions.html (paletas de cores)
# https://datavizproject.com/
# https://infogram.com/page/choose-the-right-chart-data-visualization

### 5.0 O Básico de gráficos em R ###
## Base R
? plot
plot(bank$balance, bank$age, type = "p") # pontos (apenas uma variável -- repete os eixos)
plot(bank$balance, bank$age) #  Dispersão (eixos x e y)
boxplot(bank$age) # boxplot
plot(c(1:10), c((1:10) ** 2), type = "b", col = "red", xlab = "x", ylab = "y", pch = 19) # linhas simples
plot(c(1:10), c((1:10) ** 2), type = "b", col = "red", xlab = "x", ylab = "y", pch = 19) # linhas com pontos

## ggplot
# https://www.curso-r.com/material/ggplot/
# https://blog.revolutionanalytics.com/2009/01/10-tips-for-making-your-r-graphics-look-their-best.html (imprimir o graf. com melhor resolução)
# http://www.sthda.com/english/wiki/ggplot2-title-main-axis-and-legend-titles (formatar titulos, bordas e eixos)
# Esquema básico: ggplot(dataFrame) + formaGeométrica(aes(x, y), atributoEstético = variável) + outrosArgumentos
# 1) Data Frame: ggplot(dataFrame) +
# 2) Forma geométrica: geom_tipoGrafico()
# 3) Coordenadas (dentro de forma geométrica: aes): aes(x, y)
# 4) Atributos estéticos (fora de aes)
# 5) outros argumentos (nome dos eixos, legendas, anotações, temas etc.)
? ggplot

ggplot(imdb) + geom_point(aes(x = orcamento, y = receita)) # dispersão
ggplot(imdb) + geom_point(aes(x = orcamento, y = receita)) + geom_abline(intercept = 0, slope = 1, color = "red") # acima da linha: lucro; abaixo: prejuízo

imdb %>%
mutate(
    lucro = receita - orcamento, # cria a variável lucro
    lucro = ifelse(lucro <= 0, "não", "sim") # transforma os resultados em variável categórica
) %>%
filter(!is.na(lucro)) %>% # filtra e seleciona apenas as que não são 'na'
ggplot() +
geom_point(mapping = aes(x = orcamento, y = receita, color = lucro)) + # divide as cores de acordo com a variável categórica (color = lucro)
labs(x = "Orçamento", y = "Arrecadação", color = "Houve lucro?")

## 5.0.2 Estilos ggplot
# https://ggplot2.tidyverse.org/reference/ggtheme.html
ggplot(imdb) + geom_point(aes(x = orcamento, y = receita)) + geom_abline(intercept = 0, slope = 1, color = "red") + theme_gray()
ggplot(imdb) + geom_point(aes(x = orcamento, y = receita)) + geom_abline(intercept = 0, slope = 1, color = "red") + theme_bw()
ggplot(imdb) + geom_point(aes(x = orcamento, y = receita)) + geom_abline(intercept = 0, slope = 1, color = "red") + theme_linedraw()
ggplot(imdb) + geom_point(aes(x = orcamento, y = receita)) + geom_abline(intercept = 0, slope = 1, color = "red") + theme_light()
ggplot(imdb) + geom_point(aes(x = orcamento, y = receita)) + geom_abline(intercept = 0, slope = 1, color = "red") + theme_dark()
ggplot(imdb) + geom_point(aes(x = orcamento, y = receita)) + geom_abline(intercept = 0, slope = 1, color = "red") + theme_minimal()
ggplot(imdb) + geom_point(aes(x = orcamento, y = receita)) + geom_abline(intercept = 0, slope = 1, color = "red") + theme_classic()
ggplot(imdb) + geom_point(aes(x = orcamento, y = receita)) + geom_abline(intercept = 0, slope = 1, color = "red") + theme_void()
ggplot(imdb) + geom_point(aes(x = orcamento, y = receita)) + geom_abline(intercept = 0, slope = 1, color = "red") + theme_test()

theme_set(theme_dark()) # Setar o tema do ggplot

## 5.0.3 Estilos ggtheme
# https://mran.microsoft.com/snapshot/2017-02-04/web/packages/ggthemes/vignettes/ggthemes.html

###################################
### 5.1 GRÁFICOS DE COMPARAÇÃO ###
###################################
## 5.1.1 Barras/colunas (vertical e horizontal)
# https://ggplot2.tidyverse.org/reference/geom_bar.html
# https://www.r-bloggers.com/detailed-guide-to-the-bar-chart-in-r-with-ggplot/ (muito bom!)
# Há duas possibilidades:
# Na contagem de variáveis qualitativas (factor)
ggplot(bank) + geom_bar(aes(x = marital)) # sintaxe 1 (padrão)
ggplot(bank, aes(x = marital)) + geom_bar() # sintaxe 2 (alternativa) -- mesmo resultado

ggplot(bank, aes(y = marital)) + geom_bar(fill = "blue") # horizontal, com a cor azul

ggplot(bank) + geom_bar(aes(x = marital, fill = loan)) # adicionar diferenciação qualitativa (factor) entre as variáveis qualitativas contadas
ggplot(bank) + geom_bar(aes(y = marital, fill = loan)) + theme(legend.position = "top") # horizontal + legenda no topo

## 5.1.2 Linhas
# https://ggplot2.tidyverse.org/reference/geom_path.html
filmes <- imdb %>% select(ano, orcamento)
filmes$orcamento <- log(filmes$orcamento)
filmes # df1
economics # df2
economics_long # df3

filmes %>%
filter(!is.na(orcamento)) %>%
arrange(ano) %>%
ggplot(aes(x = ano, y = orcamento)) + geom_line() # Ex. 1: simples

ggplot(economics, aes(x = date, y = unemploy)) + geom_line() # Ex. 2: simples

ggplot(economics, aes(x = unemploy, y = date)) + geom_line(orientation = "y") # Ex. 2: eixo invertido

economics %>%
filter(date >= "2013-01-01") %>%
ggplot(aes(x = date, y = unemploy)) + geom_line() # Ex. 2: dados a partir de 2013

economics %>%
filter(date >= "2013-01-01") %>%
ggplot(aes(x = date, y = unemploy)) + geom_step() # Ex. 2: http://sape.inf.usi.ch/quick-reference/ggplot2/geom_step

ggplot(climaCba_df, aes(x = ano, y = Maxima)) + geom_line() # Ex. 3 simples

theme_set(theme_dark()) # Setar o tema do ggplot
p = ggplot(climaCba_df, aes(x = ano)) +
geom_line(aes(y = Maxima, colour = "Maxima"), size = .75) +
geom_line(aes(y = media_Maxima, colour = "media_Maxima"), size = .75) +
geom_line(aes(y = media_Media, colour = "media_Media"), size = .75) +
geom_line(aes(y = media_Minima, colour = "media_Minima"), size = .75) +
geom_line(aes(y = Minima, colour = "Minima"), size = .75) +
scale_colour_manual("",
                   breaks = c("Maxima", "media_Maxima", "media_Media", "media_Minima", "Minima"),
                   values = c("red3", "orange", "gray", "skyblue", "darkblue")) +
xlab("") +
ylab("") +
ggtitle("TEMPERATURAS EM CUIABA (1961-2019)\nEm graus Celsius") +
scale_x_date(date_labels = "%Y", date_breaks = "10 years") +
scale_y_continuous(breaks = seq(0, 45, by = 8)) +
annotate("text", x = as.Date("2019-06-11", "%Y-%m-%d"), y = max(climaCba_df[,2])-2, # media_Media
         label = "Media", size = 3, colour = "gray") +
annotate("text", x = as.Date("2019-06-11", "%Y-%m-%d"), y = max(climaCba_df[,3])-2, # media_Maxima
         label = "Media maxima", size = 3, colour = "orange") +
annotate("text", x = as.Date("2019-06-11", "%Y-%m-%d"), y = max(climaCba_df[,4])-3, # media_Minima 
         label = "Media minima", size = 3, colour = "skyblue") +
annotate("text", x = as.Date("2019-06-11", "%Y-%m-%d"), y = max(climaCba_df[,5])-3, # Maxima 
         label = "Maxima", size = 3, colour = "red3") +
annotate("text", x = as.Date("2019-06-11", "%Y-%m-%d"), y = max(climaCba_df[,6])-10, # Minima 
         label = "Minima", size = 3, colour = "darkblue")
p
p + theme(legend.position = "none")
p + theme(
    plot.title = element_text(colour = "gray25"),
    panel.border = element_blank(), # borda
    panel.grid.major = element_blank(), # linhas de grade verticais; element_blank() p/ deixar em branco
    panel.grid.minor = element_line(size = 0.5, linetype = 'solid', colour = "white"), # linhas de grade horizontais
    panel.background = element_rect(fill = "gray100", linetype = "solid"),
    axis.line = element_line(colour = "transparent"),
    legend.position = "none") # cor das linhas do eixo

## 5.1.3 Bolhas (três ou mais variáveis)

###################################
### 5.2 GRÁFICOS DE COMPOSIÇÃO ###
###################################
## 5.2.1 Setores (pizza)
# https://ggplot2.tidyverse.org/reference/coord_polar.html
bichos <- c("Sapos", "Catetos", "Cachorros", "Gatos", "Galinhas", "Hipopótamos")
tamanhos <- c(15, 30, 45, 10, 67, 44)
perc = paste(round(tamanhos/sum(tamanhos) * 100, 2), "%")
dfPie <- data.frame(bichos, tamanhos, perc)
dfPie <- dfPie %>%
  arrange(desc(bichos)) %>%
  mutate(prop = tamanhos / sum(dfPie$tamanhos) * 100) %>%
  mutate(ypos = cumsum(prop) - 0.5 * prop) %>%
  mutate(focus = c(0, 0.2, 0, 0, 0, 0)) # Organizando os dados
dfPie

ggplot(dfPie, aes(x = "", y = tamanhos, fill = bichos)) +
    geom_bar(stat="identity", width=1, color="white") + 
    coord_polar("y", start = 0) + 
    theme_void() + 
    theme(legend.position="none") # Exemplo 1 ("cru")

p = ggplot(dfPie, aes(x = "", y = prop, fill = bichos)) +
        geom_bar(stat = "identity", width = 1, color = "white") +
        theme(panel.background = element_blank(), plot.title = element_text(hjust=0.5)) + 
        geom_text(aes(y = ypos, label = perc), color = "black", size = 3) +
        scale_y_continuous(breaks = dfPie$ypos, labels = dfPie$bichos) +
        scale_fill_brewer(palette = "Spectral") +
        labs(fill = "", x = NULL, y = NULL, title = "Bichos encontrados") 
p + coord_polar("y", start = 1) # Exemplo 2 ("formatado")

## 5.2.2 Mapa de árvore (treemap)
# https://www.r-graph-gallery.com/236-custom-your-treemap.html
library(treemap)

bichos <- c("Sapos: 15", "Catetos: 30", "Cachorros: 45", 
          "Gatos: 10", "Galinhas: 67", "Hipopótamos: 44")
tamanhos <- c(15, 30, 45, 10, 67, 44)
dfMap <- data.frame(bichos, tamanhos)
dfMap
treemap(dfMap, index = "bichos", vSize = "tamanhos", type = "index", title="Animais encontrados", palette = "Pastel1", 
        fontsize.labels = c(9, 12), fontface.labels = c(1, 2))

## 5.2.3 Gráfico de Waffles
# https://github.com/liamgilbey/ggwaffle (muitos dados/linhas)
# https://github.com/hrbrmstr/waffle (poucos dados/linhas)
library(waffle)

# df (tem que ser como numeric)
dfBichos <- c("Sapos (15)" = 15, "Catetos (30)" = 30, "Cachorros (45)" = 45, "Gatos (10)" = 10, "Galinhas (67)" = 67, "Hipopótamos (44)" = 44)
dfBichos

# Gráfico 1 (quadradinhos)
waffle(dfBichos, rows = 8,  size = 1, colors = c("#008000", "#8B4513", "#B8860B", "#4169E1", "#DC143C", "#778899"), legend_pos = "bottom") +
    labs(title = "Bichos encontrados")

## 5.2.4 Barras empilhadas
library(reshape)
library(plyr)

# df
rotulos <- c("G1", "G2", "G3", "G4", "G5", "G1", "G2", "G3", "G4", "G5")
media <- c(20, 35, 30, 35, 27, 25, 32, 34, 20, 25)
sexo <- c(rep("Homens", 5), rep("Mulheres", 5))
dfBars <- data.frame(rotulos, media, sexo)
dfBars

aglut <- melt(dfBars, id.vars=c("rotulos", "sexo"))
aglut
media_media <- ddply(aglut, c("variable", "sexo"), summarise,
           mean = mean(value), sem = sd(value) / sqrt(length(value)))
media_media
media_sem <- transform(media_media, 
                       lower = mean - sem, 
                       upper = mean + sem)
media_sem

# Grafico 1
gg <- ggplot(dfBars, aes(x = rotulos, y = media, fill = sexo)) + 
      geom_bar(position = "stack", stat = "identity", width = 0.35) + 
      theme(legend.key = element_rect(colour = NA, fill = NA), 
            legend.title = element_blank(),
            legend.justification=c(1, -0.11), 
            legend.position=c(0.98, 0.85),  
            legend.background = element_blank(),
            plot.title = element_text(hjust = 0.5, size = 11)) + # https://www.datanovia.com/en/blog/ggplot-title-subtitle-and-caption/
      scale_fill_manual(values = c("#5F88BC", "#68B37D")) + 
      xlab("") +
      ylab("Pontuação") + 
      scale_y_continuous(expand = c(0,0), limit = c(0, 80)) + 
      scale_x_discrete(expand = c(0.1,0)) +
      ggtitle("Pontuação por grupo e sexo")
gg

# Grafico 2 (com erro padrão)
gg + geom_errorbar(data = media_sem, 
                   aes(ymax = upper,  
                       ymin = lower), 
                   position = "fill", 
                   width = 0.15)

## 5.2.5 Cachoeira (waterfall)
# https://analyticstraining.com/waterfall-charts-using-ggplot2-in-r/
# Não sei se funcionou, mas não pretendo utilizar este gráfico. É muito confuso.
refri <- c("Coca-cola", "Fanta", "Sprite", "Guaraná", "Refrigereco", "Kapo")
entraSai <- c(350000, -30000, -7500,-25000,95000,-7000)
estoque <- tibble(index = refri, data = entraSai)
estoque <- estoque %>% mutate(saldo = cumsum(estoque$data)) # calculando fac da coluna estoque
estoque <- estoque %>% mutate(fim = cumsum(saldo)) %>% mutate(fim = c(head(fim, -1), 0))
estoque <- estoque %>% mutate(inicio = c(0, head(fim, -1))) %>% mutate(id = seq(1, nrow(estoque)))
estoque <- estoque %>% select(id, index, data, inicio, fim, saldo)
estoque

ggplot(estoque, aes(index)) + 
    geom_rect(aes(x = index, xmin = id - 0.45, xmax = id + 0.45, ymin = fim, ymax = inicio))

## 5.2.6 Área empilhada
# https://pt.stackoverflow.com/questions/245538/gr%C3%A1fico-de-barras-empilhadas-r%C3%B3tulos-e-ordena%C3%A7%C3%A3o-ggplot
anos <- seq(1980, 1984, 1) # x
horas <- c(7, 8, 6, 11, 7, 2, 3, 4, 3, 2, 7, 8, 7, 2, 2, 8, 5, 7, 8, 13) # y
acao <- c(rep("dormindo", 5), rep("comendo", 5), rep("trabalhando", 5), rep("brincando", 5))
dfArea <- data.frame(anos, horas, acao)
dfArea

ggplot(dfArea, aes(x = anos, y = horas)) + 
    geom_area(aes(colour = acao, fill = acao)) +
    xlab("Eixo x") +
    ylab("Eixo y") +
    labs(title = "Gráfico de área aperfeiçoado\nAprendendo no R")
    
################################
### 5.3 GRÁFICOS DE RELAÇÃO ###
################################
## 5.3.1 Dispersão (duas variáveis)
x <- c(1, 2, 3, 4, 5, 6, 7, 8)
y <- c(5, 2, 4, 2, 1, 4, 5, 2)
df <- data.frame(x, y)
df

ggplot(df, aes(x, y)) +
    geom_point() +
    labs(title = "Gráfico de dispersão\nAprendendo no R")

#####################################
### 5.4 GRÁFICOS DE DISTRIBUIÇÃO ###
#####################################
## 5.4.1 Histograma de barras
populacao <- c(22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48)
bins <- c(0,10,20,30,40,50,60,70,80,90,100,110,120,130)
df <- data.frame(populacao, bins)
df

ggplot(df, aes(x = populacao), ) + geom_histogram()

## 5.4.2 Histograma de linhas
## 5.4.3 Tabela de histograma
## 5.4.4 Boxplot
espalhar <- rnorm(50) * 100
centralizar <- rep(50, 25)
outlierMais <- rnorm(10) * 100 + 100
outlierMenos <- rnorm(10) * 100 - 100
dfBoxplot <- c(espalhar, centralizar, outlierMais, outlierMenos)
dfBoxplot

ggplot(as.data.frame(dfBoxplot), aes(y = dfBoxplot)) + 
    geom_boxplot()

## 5.4.5 Violino
# http://www.sthda.com/english/wiki/ggplot2-violin-plot-quick-start-guide-r-software-and-data-visualization
espalhar <- rnorm(50) * 100
centralizar <- rep(50, 25)
grupos <- c(rep("1", 10), rep("2", 10), rep("3", 10), rep("4", 10), rep("5", 10))
outlierMais <- rnorm(10) * 100 + 100
outlierMenos <- rnorm(10) * 100 - 100
dfBoxplot <- data.frame(espalhar, grupos, centralizar, outlierMais, outlierMenos)
dfBoxplot

ggplot(dfBoxplot, aes(x = grupos, y = espalhar, fill = grupos)) + 
    geom_violin()

#######################################################
### 5.5 ESTRUTURAS DE TOPOLOGIA (relações e fluxos) ###
#######################################################

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
add <- function(x, y) {
    x + y
}
add(2, 2)
add(as.Date("2014-06-01"), 1)

# Ex. 2
add <- function(x, y = 1) {
    x + y
}
add(3)
add(3, 2)

## Ex. 3
calc <- function(x, y, type) {
    if (type == "add") {
       x + y
}   else if (type == "menos") {
    x - y
}   else if (type == "mult") {
    x * y
}   else if (type == "div") {
    x / y
}   else {
    print("Operação não encontrada")
}
}
calc(2, 2, "add")
calc(2, 2, "menos")
calc(2, 2, "mult")
calc(2, 2, "div")
calc(2, 3, "nao")

# Ex. 4
x <- 1:4

quadrado <- function(x) {
    return(x^2)
}

quadrado(x)

# Ex. 5
soma <- function(x, y){
    x+y
}

soma(2, 4)

# Ex. 6
y = seq(1, 20)

getLog <- function(x) {
    plot(log(x))

getLog(y)

# Ex. 7
opAlea <- function(x = 10) {
    y = runif(x)
    z = plot(y)
    print(c(y, z))
}
opAlea()

### 6.2 If Else ###
x <- 1

if (x > 0) {
   print("Número positivo!")
} else {
   print("Número negativo!")
}

### 6.3 For Loops ###
# Básico: "para cada ITEM (i) em um VETOR (v), faça tal coisa com i"
x <- paste("Letra ", c("a", "b", "c", "d", "e"), sep = "")
x

for(i in 1:length(x)) {
    print(x[i])
} # imprime os valores do vetor x, uma vez cada um, "i" vezes

for(i in 1:length(x)) {
    print(x)
} # imprime "i" vezes todo o vetor x

for(i in 1:length(x)) {
    print(i)
} # imprime a sequência de "i", que é limitada ao tamanho do vetor x (1:length(x))

### 6.4 While ###
# Ex. 1
x <- 2
y <- 10
while(x < y) {
    print(x)
    x <- x + 1
} # enquanto x for menor que y, ele imprime os valores

# Ex. 2
counter = 0

while (counter < 3) {
	print("dentro do loop")
	counter = counter + 1
} # R não aceita else dentro de while

### 6.5 Break e Next ###
#  Break
x =  1:10
for (val in x) {
if (val == 3) {
break
}
print(val)
}

for (val in "string") {
if (val == "t") {
break
}
print(val)
}

for (val in "string") {
if (val == "t") {
break
}
str_sub("string", 1, 1)
}

# Next
x <- 1:10
y <- 7
for(i in x) {
    if(i == y) {
        next
    }
    print(i)
} # imprime a sequência de "i", que é limitada ao tamanho do vetor x, exceto o valor y

### 7. OBJETOS E CLASSES ###

#### 8. ASSUNTOS DIVERSOS ####
### 8.1 Função anônima no R
dobrar = {function(x) x * 2}
dobrar(2)

### 8.2 map ###
### 8.3 Data e hora
### 8.4 Família apply