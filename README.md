# Streamlit-Data-App
# Water Quality Dashboard 

## Overview
This project is an interactive Streamlit web application that visualizes and explores
water quality data from Biscayne Bay. The dashboard allows users to view descriptive
statistics, generate 2D and 3D plots, and view NASA's Astronomy Picture of the Day (APOD)
using a public API.

The goal of this project is to demonstrate internship-ready software development skills,
including data visualization, API integration, and public deployment.

---

## Dataset
**Source:** Biscayne Bay Water Quality Dataset  
**File:** biscayneBay_waterquality (3).csv  

The dataset includes variables such as:
- Temperature (°C)
- pH
- Dissolved Oxygen (ODO mg/L)
- Longitude / Latitude
- Total Water Column (m)
- Time

---

## Features
### Tab 1 – Descriptive Statistics
- View raw dataset
- Dropdown to select a numeric variable
- Displays descriptive statistics for the selected variable

### Tab 2 – 2D Plots
- Line plot of temperature over time
- Scatter plot of dissolved oxygen vs temperature, colored by pH

### Tab 3 – 3D Plots
- 3D scatter plot of geographic coordinates and water depth

### Tab 4 – NASA APOD
- Displays NASA’s Astronomy Picture of the Day
- Uses NASA public API with secure key storage

---

## How to Run Locally

1. Clone the repository:
```bash
git clone https://github.com/yourusername/water-quality-dashboard.git
cd water-quality-dashboard

