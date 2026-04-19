# CMSE 492 HW01

## Overview
This project analyzes sales-related CSV data and produces summary statistics by region. The main script reads the input data, cleans and combines it, and generates both a CSV summary and a visualization.

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

## How to Run Locally
Run the project with:

```bash
python3 src/analysis.py
