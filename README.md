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
## Takeaways
In Homework 1, I took a basic starter repository and reorganized it into a more professional  project. One of the biggest improvements was restructuring the project into clear folders such as `src`, `data`, `results`, and `notebooks`. This made it much easier to understand where everything belongs and how the project is organized. I also improved the README to clearly explain what the project does, how to run it, and what outputs to expect, which is important for anyone else trying to understand my project.

To improve consistency, I used both `requirements.txt` and `environment.yml` to define the environment dependencies. I also created a Dockerfile, which was especially useful Because it ensures consistent performance across all environments(ex local).Docker complements environment tools by isolating the entire environment, preventing issues with missing packages or version conflicts.

For my personal modification, I added a new metric called `revenue_per_unit`, which calculates how much revenue is generated per unit sold. I also added a new visualization using the `seaborn` package to show this metric by region. This demonstrates my understanding of the code because I was able to extend the existing analysis pipeline, modify the summary table, and add a new output while keeping everything integrated.

One challenge I delt with was debugging errors, especially with Docker and Python. However, I fixed this issue by  testing my code step by step. If I were handing this project to an intern or employer, my main priority would be making sure they fully understand the data and assumptions behind the analysis. Overall, this assignment helped me understand how important structure, documentation, and consistency are in real-world data science work.


## How to Run Locally
Run the project with:

```bash
python3 src/analysis.py
