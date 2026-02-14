# SmartLoad: AI-Powered Building Energy Estimator

SmartLoad is a modern web application that leverages **Machine Learning** to predict a building's energy footprint. This project was built as a "Mini Project" to solidify my understanding of **Linear Regression** and end-to-end model deployment.



## Project Overview
As a second-year student, I developed this tool to bridge the gap between theoretical regression analysis and practical, user-facing applications. The app calculates both **Heating Load** and **Cooling Load** (in kWh) based on eight specific architectural parameters.

## Tech Stack
* **Backend:** Flask (Python)
* **Machine Learning:** Linear Regression via Scikit-Learn
* **Model Persistence:** Pickle
* **Frontend:** HTML5, CSS3 (Glassmorphism), JavaScript (ES6+)
* **Deployment:** Designed for deployment on platforms like Render

## Key Features
* **Glassmorphism UI:** A premium, modern interface featuring frosted glass effects, vibrant background animations, and responsive hover states.
* **Real-time Analysis:** An interactive JavaScript-driven frontend that provides immediate visual feedback during the prediction process.
* **Multi-Output Prediction:** A single model trained to estimate two distinct energy metrics simultaneously.
* **Step-by-Step UX:** A dedicated "How It Works" section to guide users through the data entry process.

## The Science
The project uses the **ENB2012** dataset to train a regression model. It takes the following inputs:
1. Relative Compactness (X1)
2. Surface Area (X2)
3. Wall Area (X3)
4. Roof Area (X4)
5. Overall Height (X5)
6. Orientation (X6)
7. Glazing Area (X7)
8. Glazing Area Distribution (X8)


### Prerequisites
* Python 3.x
* Flask
* NumPy
* Scikit-Learn

