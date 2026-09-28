# Star schema

- DimDate[DateKey] 1:* FactSales[DateKey]
- DimProduct[ProductKey] 1:* FactSales[ProductKey]
- DimRegion[RegionKey] 1:* FactSales[RegionKey]
- DimChannel[ChannelKey] 1:* FactSales[ChannelKey]

Recommended report pages:
1. Executive Overview
2. Region & Channel Performance
3. Product & Category Performance
