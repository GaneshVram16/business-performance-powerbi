# Power BI Desktop build guide

1. Open Power BI Desktop.
2. Run `generate_data.py` to generate the five CSV tables.
3. Import the five CSV files from `data/`.
4. Create relationships exactly as documented in `model/model_design.md`.
5. Mark `DimDate` as the date table using `DateKey`.
6. Add each measure from `model/measures.dax`.
7. Build the three report pages described in `README.md`.
8. Save as a Power BI Project (`.pbip`) if Developer Mode is enabled.
9. Take screenshots of each report page and add them to `outputs/`.

Use the validated KPI values in the README as a cross-check.
