# **House Rocket – Projeto de Insights**

![Imagem](https://user-images.githubusercontent.com/80589529/183155590-de7f2d73-a749-4623-91d6-8b5aed3aedd7.png)

## 1.	Pergunta de negócios

A House Rocket é uma empresa fictícia cujo modelo de negócio é a compra e venda de imóveis utilizando tecnologia. Sua principal estratégia é comprar boas casas em ótimas localizações a preços baixos e depois revendê-las a preços mais altos. Quanto maior a diferença entre comprar e vender, maior o lucro da empresa e, portanto, maior sua receita. Seu CEO em uma busca para maximizar seu lucro está procurando uma análise em seu conjunto de dados para encontrar os melhores negócios disponíveis para eles, comprando a um preço baixo, reformando e vendendo a um preço mais alto, ele também quer saber qual é o melhor preço que poderiam vender para obter o maior lucro possível. Ele quer a resposta para duas perguntas:

* Qual é o imóvel que a House Rocket deve comprar e a que preço?
* Uma vez comprado o imóvel, qual é o melhor momento para vender e a que preço?

## 2.	Premissas de Negócios

Todas as suposições de dados, insights e hipóteses são baseadas no conjunto de dados disponível.

## 3.	Estratégia de solução

1.	Qual é o imóvel que a House Rocket deve comprar e a que preço?
- Agrupei o CEP dos dados e calculei o preço médio de cada imóvel.
- Mescle esses dados com o conjunto de dados inicial.
- Criei um novo atributo 'status' que indica se o imóvel está bom para compra ou não, através dos seguintes critérios: preço abaixo da média e condição acima de 3 é bom para compra.

2.	Uma vez comprado o imóvel, qual é o melhor momento para vender e a que preço?
- adicionou um novo atributo 'temporada' no conjunto de dados.
- Agrupei por CEP e temporada e peguei os preços médios.
- novo atributo 'price_sale': o preço acima da média aumenta em 30%, abaixo da média aumenta apenas em 10%.
- O atributo 'profit' é calculado pela diferença entre 'price' e 'price_sale'.

## 4.	Insights obtidos

* O crescimento de preço ano a ano tem um aumento de 0,52.
* Imóveis sem porão na mediana são quase 1,45% maiores do que imóveis com.
* Os estados com vista para o mar são 212,64% mais caros, em média.

## 5.	Resultados de negócios

Através da análise dos dados foi possível obter os seguintes resultados do lucro nas safras.

| SEASON | PROFIT |
| ----- | ------ |
| Fall | 120,982.75 |
| Spring | 125,389.88 |
| Summer | 124,251.96 |
| Winter | 117,868.11 |

## 6.	Conclusão

Com base na análise dos dados, é possível afirmar que a melhor época de compra para uma empresa é o inverno, por outro lado, a época de maior venda é a primavera.

## 7.	Links:
* source: https://www.kaggle.com/shivachandel/kc-house-data
* webapp: https://ds-project-rocket.herokuapp.com/

