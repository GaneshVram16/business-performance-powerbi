# Project walkthrough

## Problem
Design an executive business-performance reporting model that supports revenue, profitability and operational analysis.

## Workflow
1. Create one fact table and four dimension tables.
2. Build a star schema using one-to-many relationships.
3. Define DAX measures for revenue, profit, margin, AOV, SLA compliance and YoY growth.
4. Design three report pages for executive, regional/channel and product analysis.
5. Validate headline KPIs against source-data summaries.

## What to explain in a discussion
- Why a star schema is preferable to one large flat table for BI.
- Difference between a calculated column and a measure.
- Why DIVIDE is safer than the / operator in DAX.
- How SAMEPERIODLASTYEAR supports YoY comparisons.
- Why filters and slicers should support a clear analytical question.

## Limitation
The repository is a reproducible Power BI build pack based on synthetic data. The final Desktop visual layout can be rebuilt locally from the included model and measures.
