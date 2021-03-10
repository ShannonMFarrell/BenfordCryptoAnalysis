# BenfordCryptoAnalysis
Statistical analysis and Hypothesis testing of historical Bitcoin prices 


This script takes daily bitcoin prices in USD($) and stock volumes and attempts to investigate possible manipulation of bitcoin cryptocurrency prices between 2014 and 2021.
 
This is made possible using Benford's law, which states the first leading digit (1-9) of natural, unbounded numbers of a large sample size are not distributed uniformly as expected but follow a power-law distribution. 

Features :

1. Benford's law analysis : Performing benford analysis on the dataset of open, close, volume prices of BTC per year.s


2. Statistical testing and 'Goodness of fit' : Hypothesis testing using Chi-squared and visual representation of benford analysis for evaluation purposes

3. Painting the tape analysis : Using the posted daily volume of each stock, examine and test dataset for "Painting the tape" manipulation. This is where the price of a stock is manipulated by inflating volume on that day. This is characterised by rapid changes in volume over a period of time.

V2 Planned features :

- Benfords analysis of second leading digit
