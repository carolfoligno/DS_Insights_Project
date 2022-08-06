# **House Rocket – Insight Project**

![Imagem](https://user-images.githubusercontent.com/80589529/183155590-de7f2d73-a749-4623-91d6-8b5aed3aedd7.png)

## 1.	Business Question

House Rocket is a fictitious company whose business model is the purchase and sale of real estate using technology. Their main strategy is to buy good homes in great locations at low prices and then resell them later at higher prices. The greater the difference between buying and selling, the greater the company's profit and therefore the greater its revenue. Their CEO in a pursue to maximize their profit are looking for an analysis in their dataset to find the best businesses available to them, buying at a low price, renovate and sell it to a higher price, he also want to know what is the best price they could sell to make the most profit possible. He wants the answer for two questions:

* Which is the real state that House Rocket should buy and at what price?
* Once bought the real state, when is the best moment to sell and at what price?

## 2.	Business Assumptions

All the data assumptions, insights and hypotehsis are based on available dataset.

## 3.	Solution Strategy

1.	Which is the real state that House Rocket should buy and at what price?
- I grouped the zip code of the data and calculated the average price of each property.
- Merge this data with the initial dataset.
- I created a new attribute 'status' that indicates if the property is good for purchase or not, through the following criteria: price below average and condition above 3 is good for purchase.

2.	Once bought the real state, when is the best moment to sell and at what price?
- added a new 'season' attribute in the dataset.
- I grouped by zipcode and season and got the average prices.
- new attribute 'price_sale': above average price increases by 30%, less than average only increases by 10%.
- 'profit' attribute is calculated by the difference between 'price' and 'price_sale'.

## 4.	Insights gained

* The price growth YoY has an increase of 0.52 YoY.
* Properties without basement in median are almost 1.45% larger than properties with.
* State with waterfront view are 212.64% more expensive at average.

## 5.	Business Results

Through the analysis of the data it was possible to obtain the following results of the profit in the seasons.

| SEASON | PROFIT |
| ----- | ------ |
| Fall | 120,982.75 |
| Spring | 125,389.88 |
| Summer | 124,251.96 |
| Winter | 117,868.11 |

## 6.	Conclusion

Based on data analysis, it is possible to say that the best buying season for a company is winter, on the other hand, the best selling season is spring.

## 7.	Links:
* source: https://www.kaggle.com/shivachandel/kc-house-data
* webapp: https://ds-project-rocket.herokuapp.com/

