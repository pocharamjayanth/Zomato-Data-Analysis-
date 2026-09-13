# Zomato Bangalore Data Analytics Portfolio Project

An end-to-end data analytics pipeline evaluating restaurant ratings, online order adoption, pricing distributions, and location dynamics across Bangalore.

## Project Architecture & Directory Structure
- **data/**: Houses raw datasets, SQLite databases (zomato.db), and processed/cleaned CSVs.
- **python/**: Contains modular scripts for data ingestion, cleaning (data_cleaning.py), EDA, SQL loading, and Excel pivoting.
- **sql/**: Relational database queries for data exploration and metric extraction.
- **excel/**: Pivot table summaries generated for business reporting.
- **images/charts/**: Visualizations exported from the analysis phase.
- **eports/**: Final analytical summaries and documentation.

## Tech Stack
- **Python**: Pandas, NumPy, Matplotlib, Seaborn, SQLite3
- **SQL**: SQLite relational database querying
- **Excel**: Pivot tables and multi-variable summary aggregation
- **Power BI**: Interactive business intelligence dashboarding

## Key Insights
1. **Online Ordering Trends**: High adoption rates observed across major restaurant formats, heavily influencing customer reach and vote counts.
2. **Pricing vs. Rating**: Fine dining and pubs command higher average costs for two people ($>1500$), while maintaining competitive ratings in high-density hubs like Koramangala and Indiranagar.
