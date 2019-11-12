# Taiwan-Preferred-Stock-IRR(台灣特別股IRR即時報價程式)
Project by [廖芳毅](https://github.com/gontue5959)

## Table of Contents
+ [About](#about)
+ [Dependencies](#dependencies)
+ [Reference](#reference)
+ [To run real time demo](#to-run-real-time-demo)

## About
Taiwan-Preferred-Stock-IRR是一個針對於台灣特別股所設計的一個即時計算內部報酬率的程式，方便投資人即時了解以現在的價格買進特別股，持有到期(重設日)時的內部報酬率。盤中股價即時資訊取自於[twstock](https://github.com/mlouielu/twstock)，資料來源為[台灣證券交易所](https://www.twse.com.tw/zh/)、[證券櫃台買賣中心](https://www.tpex.org.tw/web/index.php?l=zh-tw)。

## Dependencies
* twstock 1.3.1
* pandas 0.25.3
* Python 3.6.5
### install package
```
> pip install twstock
> pip install pandas
```

## Reference
* [XIRR](https://github.com/dkensinger/python/blob/master/XIRR.py)

## To run real time demo
```
> python IRR_Demo.py
```
<img src="https://github.com/gontue5959/Preferred-Stock-IRR/blob/master/Demo/demo.png" width="400"> 
