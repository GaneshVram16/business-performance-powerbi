from pathlib import Path
import numpy as np
import pandas as pd

np.random.seed(42)
ROOT=Path(__file__).resolve().parent
DATA=ROOT/"data"
DATA.mkdir(exist_ok=True)

categories=["Electronics","Home","Fashion","Beauty","Sports","Books"]
date_pool=pd.date_range("2024-01-01","2025-12-31",freq="D")

dim_date=pd.DataFrame({"DateKey":date_pool})
dim_date["Year"]=dim_date["DateKey"].dt.year
dim_date["MonthNo"]=dim_date["DateKey"].dt.month
dim_date["Month"]=dim_date["DateKey"].dt.strftime("%b")
dim_date["YearMonth"]=dim_date["DateKey"].dt.strftime("%Y-%m")
dim_date["Quarter"]="Q"+dim_date["DateKey"].dt.quarter.astype(str)

products=[]
base_prices={"Electronics":9000,"Home":2600,"Fashion":1600,"Beauty":1000,"Sports":2000,"Books":650}
for i in range(1,61):
    cat=categories[(i-1)%6]
    price=max(200,np.random.normal(base_prices[cat],500))
    products.append([i,f"{cat} Item {i:02d}",cat,round(price,2)])
dim_product=pd.DataFrame(products,columns=["ProductKey","Product","Category","UnitPrice"])
dim_region=pd.DataFrame({"RegionKey":[1,2,3,4],"Region":["South","West","North","East"]})
dim_channel=pd.DataFrame({"ChannelKey":[1,2,3],"Channel":["Direct","Partner","Online"]})

n=18000
fact=pd.DataFrame({
    "OrderID":np.arange(1,n+1),
    "DateKey":np.random.choice(date_pool,n),
    "ProductKey":np.random.randint(1,61,n),
    "RegionKey":np.random.randint(1,5,n),
    "ChannelKey":np.random.randint(1,4,n),
    "Quantity":np.random.choice([1,2,3,4],n,p=[.55,.27,.13,.05]),
})
fact=fact.merge(dim_product[["ProductKey","UnitPrice"]],on="ProductKey",how="left")
fact["DiscountRate"]=np.random.choice([0,.05,.10,.15],n,p=[.5,.24,.18,.08])
fact["Revenue"]=np.round(fact["Quantity"]*fact["UnitPrice"]*(1-fact["DiscountRate"]),2)
fact["Cost"]=np.round(fact["Revenue"]*np.random.uniform(.57,.79,n),2)
fact["Profit"]=np.round(fact["Revenue"]-fact["Cost"],2)
fact["DeliveryDays"]=np.random.choice([1,2,3,4,5,6,7],n,p=[.08,.17,.25,.22,.14,.09,.05])
fact["SLACompliant"]=(fact["DeliveryDays"]<=4).astype(int)
fact=fact.drop(columns=["UnitPrice"])

for name,df in [("FactSales",fact),("DimDate",dim_date),("DimProduct",dim_product),("DimRegion",dim_region),("DimChannel",dim_channel)]:
    df.to_csv(DATA/f"{name}.csv",index=False)

print("Generated Power BI star-schema source tables.")