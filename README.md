# Delivery Delay Analysis 

## Overview
This project analyzes e-commerce delivery performance using SQL for data extraction and Python for data visualization. The objective is to identify delivery delay patterns across time, geography, product categories, and payment methods.

## Problem Statement
Late deliveries affect customer satisfaction and operational efficiency in e-commerce. This project investigates where and when delays happen most often and highlights the business dimensions associated with higher delivery risk.

## Objectives
- Measure the overall level of delivery delays.
- Track monthly delivery delay trends.
- Identify states and cities with the highest delay percentages.
- Analyze product categories associated with higher delays.
- Compare delay rates across payment types.

## Tools and Technologies
- MySQL
- Python
- Pandas
- Matplotlib
- Jupyter Notebook
- Git and GitHub

## Repository Structure
```bash
delivery-delay-analysis/
│── charts/
│── exports/
│── dashboard/
│── src/
│── notebooks/
│── data/
│── sql/
│── README.md
```

## Workflow
1. Load and clean the dataset.
2. Run SQL queries to calculate total orders, delayed orders, and delay percentages.
3. Export final query outputs as CSV files.
4. Use Python to create PNG charts from the exported files.
5. Summarize the findings in the README and dashboard.

## SQL Analysis Areas
The SQL analysis was performed across the following business dimensions:
- Overall summary of delayed orders
- Month-wise delivery delay trend
- State-wise delay analysis
- City-wise delay analysis
- Product category delay analysis
- Payment type delay analysis

## Visual Analysis

### 1. Monthly Delivery Delay Trend
![Monthly Delay Trend](./charts/delay_by_month.png)


This chart shows how delivery delays changed over time and helps identify months with relatively higher operational stress. Peaks in the line indicate periods where delay percentages increased, which may reflect seasonal demand, logistics bottlenecks, or fulfillment inefficiencies.

### 2. Delivery Delay by State
![Delay by State](./charts/delay_by_state.png)

This chart compares delay percentages across states and highlights the regions with weaker delivery performance. States with higher delay percentages may require closer investigation into courier performance, distance-related issues, or regional supply chain constraints.

### 3. Delivery Delay by City
![Delay by City](./charts/delay_by_city.png)

This chart highlights the top cities with the highest delivery delay percentages. City-level analysis helps narrow the problem further and can reveal urban logistics issues, local infrastructure limitations, or last-mile delivery challenges.

### 4. Delivery Delay by Product Category
![Delay by Category](./charts/delay_by_category.png)

This chart compares product categories by delay percentage and helps identify which categories are more prone to delayed delivery. Higher delays in certain categories may be linked to product handling complexity, seller distribution, packaging time, or shipping difficulty.

### 5. Delivery Delay by Payment Type
![Delay by Payment Type](./charts/delay_by_payment.png)

This chart shows whether payment method has any relationship with delivery delays. If the differences are small, payment type likely has limited operational impact; if differences are larger, it may indicate indirect links between payment workflow and order processing speed.

## Key Insights
- Delivery delays do not occur uniformly and vary across different months.
- Some states and cities experience noticeably higher delay percentages than others.
- Product category appears to influence delivery performance in several cases.
- Payment type may have a smaller effect compared to geography and category, depending on the observed differences in the chart outputs.
- Geographic and category-based analysis provides stronger operational insight than looking only at overall totals.

## Project Outputs
- SQL query results exported as CSV files
- Python-generated PNG charts
- Organized repository structure for analysis and presentation
- README documentation with findings and visuals

## How to Reproduce
1. Import the dataset into MySQL.
2. Run the SQL queries from the `sql/` folder.
3. Export the final query outputs into the `exports/` folder as CSV files.
4. Run the Python scripts or notebooks from `src/` or `notebooks/` to generate charts.
5. Save the generated chart images in the `charts/` folder.

## Business Value
This analysis helps identify delivery bottlenecks and provides data-backed insight into where logistics improvements may be needed. The findings can support better inventory planning, courier strategy, regional monitoring, and customer experience improvement.

## Future Improvements
- Build an interactive dashboard for dynamic filtering.
- Add seller-level and courier-level delay analysis.
- Compare delivered-on-time vs delayed orders more deeply.
- Include predictive modeling for delivery delay risk.

## Conclusion
This project demonstrates how SQL and Python can be combined to perform operational analytics on e-commerce delivery data. It transforms raw order data into meaningful business insights through structured querying and visual analysis.