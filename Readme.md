# Assignment 45 
### Machine Learning
### Linear Least Squares (LLS) 



# 1.Tehran House Price 🏠


### I used 60 Tomans to update the dollar price in this dataset

<img src="Output\Dollar_update.png" width="550">


### 5 most expensive houses in Tehran

|               |       Area     |       Room     |       Parking     |       Warehouse     |      Elevator     |      Address     |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 1      | 420 | 4 | have | have | have | Zaferanieh || ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 2      | 705 | 5 | have | have | don`t have | Abazar || ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 3      | 400 | 5 | have | have | don`t have | Lavasan || ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 4      | 680 | 5 | have | have | don`t have | Ekhtiarieh || ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 5      | 350 | 4 | have | have | have | Niavaran |

<img src="Output\Address.png" width="550">

### Compare my model with Scikit-Learn

|        Model       |       MAE     |       MSE     |      RMSE     |
| ------------- | ------------- | ------------- | ------------- |
| My LLS Model  | 3283843917.195741 | 4.228054165728168e+19 | 6502348933.830119 || ------------- | ------------- | ------------- | ------------- |
| Sklearn LinearRegression    | 3063125616.2289405 | 3.942122695718726e+19 | 6278632570.646833 || ------------- | ------------- | ------------- | ------------- |
| Sklearn RidgeCV     | 3062539132.375875 | 3.94159888399221e+19 | 278215418.406898 |


___
### Why the MSE metric is a very large number?
* Because the numbers of the differences have been raised to the power of 2 to get out of the negative state, but at the end, no root has been taken from them.

## How to Install
Run following commend :
```
pip install -r requirments.txt
```

## How to Run
```
Run Tehran-House-Price.ipynb file in jupyter notebook
```
-----------------------------------------

# 2.Dollar Rial Price 💰

#  Highest vs  Lowest Dollar Price

* Show the highest dollar and the lowest price in Ahmadinejad, Rouhani and Raisi's presidency respectively

| President | Highest Price | Lowest Price|
| ------------- | ------------- | ------------- |
| Ahmadinejad | 39,700 | 13,350 || ------------- | ------------- | ------------- | ------------- |
| Rouhani | 320,060 | 12,850 || ------------- | ------------- | ------------- | ------------- |
| Raiesi | 555,600 | 251,250 |


### MAE loss:
- MAE of ahmadinejad is **2.0110322469723354e+24**.
- MAE of rohani is **1.6516357696253647e+26**.
- MAE of raisi is **1.498722684643541e+27**.

## How to Install
Run following commend :
```
pip install -r requirments.txt
```

## How to Run
```
Run Dollar_Rial_Price.ipynb file in jupyter notebook
```
-----------------------------------------