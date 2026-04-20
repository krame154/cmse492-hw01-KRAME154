# CMSE 492 HW01

## Overview
This project analyzes sales-related CSV data and produces summary statistics by region. The main script reads the input data, cleans and combines it, and generates both a CSV summary and visualizations.

## Data
The input data is stored in the `data/` folder.

Main files used:
- `data/datafiles/customer_lookup.csv`
- `data/datafiles/sales_jan.csv`

Additional sample data:
- `data/random_data/weather_small.csv`

## Project Structure
- `src/` contains the main analysis code
- `data/` contains the input datasets
- `results/outputs/` contains generated outputs
- `notebooks/` contains example notebooks

## Personal Analysis

For my personal modification, I added a new metric called `revenue_per_unit`, which calculates how much revenue was earned per unit sold for each region and category group. I also added a new visualization using the `seaborn` package to show the average revenue per unit by region. This improves the analysis by showing not just total revenue, but also how efficiently regions generate revenue from each unit sold.

## How to Run Locally
Run the project with:

```bash
python3 src/analysis.py
