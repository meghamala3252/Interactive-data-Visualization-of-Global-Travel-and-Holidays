# Interactive-data-Visualization-of-Global-Travel-and-Holidays
# Global Tourism AI Platform

# 1.Project Statement & Outcomes
# Project: Global Holidays and Travel Data Visualization

This project aims to develop an interactive Power BI dashboard that visualizes travel trends, holiday patterns, and tourism statistics across countries and regions. It includes collecting, preprocessing, and structuring historical and current data on global holidays, tourist arrivals, travel expenditures, and popular destinations to enable effective visualization and analysis.

# Outcomes:

* A user-friendly Power BI dashboard embedded within a web application that allows users to analyze travel trends over time, monitor seasonal fluctuations, and compare tourism metrics across regions and countries.
* Interactive visualizations and filters to identify peak seasons, regional differences, and outliers.
* A hosted web application (Streamlit/Flask) that embeds the dashboard, enabling seamless interaction for travel professionals and the public.
* Comprehensive testing and documentation that detail data sources, preprocessing steps, dashboard features, and recommendations for future enhancements.

# 2. Modules to be Implemented
* Data Collection and Preprocessing - Acquire and clean holidays and tourism datasets.
* Data Structuring and Power BI Dashboard Development - Transform and model data for visualizations.
* Exploring and Streamlit Integration - Host and embed the Power BI dashboard inside a web app.
* Testing, Review, and Documentation - QA, user testing, and final documentation.

# 3. Week-wise Plan & High-Level Requirements
# Weeks 1–2: Data Collection & Preprocessing

* Collect historical and current global holiday data from government tourism websites, UNWTO, and public travel APIs.
* Gather travel metrics: tourist arrivals, expenditures, popular destinations, and seasonal indicators.
* Clean and preprocess: handle missing values, outliers, inconsistent country names, and time-zone/date format issues.
* Ensure datasets are balanced and representative across countries, regions, and time ranges.

# Weeks 3–4: Data Structuring, Transformation & Power BI Dashboard Development

* Design a data model optimized for Power BI (date tables, country/region hierarchies, normalized measures).
* Transform data: normalization, aggregation, feature engineering (season flags, holiday proximity, occupancy proxies).
* Build visuals: time-series trends, heatmaps, choropleth maps, top-destination tables, seasonality charts, and KPI cards.
* Add interactivity: filters, slicers, bookmarks, drill-through pages, and tooltips.
* Make the dashboard responsive and user-centered with clear legends and accessible color choices.

# Weeks 5–6: Web App & Power BI Integration

* Develop a web application (Flask/Streamlit) to host the dashboard and supporting UI.
* Embed the Power BI dashboard via secure embed or iframe (for prototypes) inside the web app.
* Implement user authentication and role-based access for dashboards and admin features.
* Support dashboard interactions tracking for analytics and personalized recommendations.

# Weeks 7–8: Testing, Review & Documentation

* Conduct functional, integration, and user-acceptance testing on the dashboard and web app.
* Review visualizations for clarity and domain relevance; refine with stakeholder feedback.
* Prepare full documentation: data lineage, preprocessing notebooks/scripts, dashboard guide, and API docs.
* Produce a final presentation and a packaged deliverable including exports (PDF/DOCX) and example reports.

## Key Features

* Interactive tourism dashboards and country comparisons
* AI-generated insights using OCR and analytics
* Smart travel itinerary planner
* Recommendation engine for dashboards
* User authentication with role-based access
* Gamification with badges and activity tracking
* Admin panel for user, dashboard, and feedback management

## Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS, JavaScript
* **Database:** SQLite / PostgreSQL
* **Libraries:** Pandas, Plotly, Flask-Login, Flask-JWT-Extended, OpenCV, PyTesseract

## Installation

1. Navigate to the project folder
2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```
3. Run the application:

   ```
   python run_stable.py
   ```
4. Open in browser:

   ```
    http://127.0.0.1:5000
   

