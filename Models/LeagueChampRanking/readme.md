## Model: 
League Champion Ranking
## Description: 
The way this model works is pretty simple and served as one of those relaxing, fun, and shallow experiment. The goal is to find out which league of Legends champion is the best performer on paper. All that was required was to create a seperate column name `Composite Score` where the score would be located. Each row in this column has the score label for the champion. 
To calculate the score, all that is needed is a standard scaler applied to each column to ensure each feature would contribute to the model equally. Simply add up the scaled values for each column in that row and you get the `Composite Score` for that row. The highest wins. Simply sort in descending order and take the first row, in this case the winner was... `pyke`!