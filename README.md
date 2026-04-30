# FitSync - Health Analytics Platform 📊

*A comprehensive solution for personal health tracking and insights.*

## Project Overview
FitSync is a cutting-edge personal health analytics dashboard designed to empower individuals with detailed insights into their health data. Leveraging the power of Python and Streamlit, this three-page application offers a user-friendly interface that displays key performance indicators, interactive charts, and in-depth trend analyses. The platform seamlessly integrates various data metrics, providing users with the ability to track their health progress over time. Designed with scalability in mind, FitSync is an ideal tool for personal wellness tracking or as a demonstration of advanced data visualization capabilities.

## 🚀 Key Features

* **Unified Dashboard:** A real-time overview of physical activity vs. mental reflections.
* **Trend Analysis:** Deep-dive correlations (Heatmaps) showing how sleep and steps directly impact mood.
* **The "Storyteller" Engine:** A custom logic layer that simulates realistic health correlations for demonstration purposes.
* **Dynamic Data Import:** Supports session-based CSV uploads for Apple Health and Daylio exports.
* **Responsive UI:** A clean, modern interface built with Streamlit.


## Tech Stack
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0-red)
![Pandas](https://img.shields.io/badge/Pandas-latest-blue)
![Plotly](https://img.shields.io/badge/Plotly-latest-orange)
![Continue Agent](https://img.shields.io/badge/Continue_Agent-implemented-success)
![GitHub Codespaces](https://img.shields.io/badge/GitHub_Codespaces-configured-brightgreen)

## 📁 Project Structure

```text
fitsync/
├── Home.py              # Landing page & entry point
├── data/                # Local CSV storage (Apple/Daylio exports)
├── modules/
│   ├── processor.py     # ETL pipeline (Data cleaning & merging)
│   ├── demo_story.py    # Logic for correlation adjustments (delete out when real data is incorporated)
│   └── interface.py     # Global UI components (Sidebar/Uploader)
└── pages/
    ├── 1_Dashboard.py   # Daily metrics & health overview
    └── 2_Trends.py      # Correlation matrix & weekly patterns
```

---

## How to Run
To get started with FitSync, follow these simple steps:

1. **Clone the repository**:
 ```bash
   git clone [https://github.com/Saras-AI-Institute/fitsync-project-Kapish-Garg.git](https://github.com/Saras-AI-Institute/fitsync-project-Kapish-Garg.git)
   cd fitsync-project-Kapish-Garg
Install Dependencies

Bash
pip install -r requirements.txt
Launch the Dashboard

Bash
streamlit run main.py

---

## 🧠 The Philosophy
The core of FitSync is the **Recovery Score**. This is a proprietary calculation that weights heart rate, sleep duration, and daily mood to tell the user not just how much they moved, but how ready they are for the day ahead.

---

## 🤖 AI Collaboration Statement
This project was developed using a "Human-in-the-Loop" AI workflow. While AI was utilized to streamline the building process, the core system architecture and data logic were human-led.

System Architecture: I designed the multi-page Streamlit framework and the dynamic state-management logic that allows the app to switch seamlessly between Demo Mode and Live Mode.

Proprietary Logic: I architected the Recovery Score Algorithm, defining how heart rate, sleep duration, and mood data are weighted and normalized to create a single actionable metric.

Data Engineering: I directed the development of the ETL pipeline, specifically the logic required to merge disparate schemas from Apple Health (XML/CSV) and Daylio (CSV) into a unified data structure.

AI as a Force Multiplier: Tools like Google Gemini and GitHub Copilot were used as pair-programmers to accelerate boilerplate generation, assist in complex Plotly visualization debugging, and ensure code PEP-8 compliance.

### 👩‍💻 Author
**Kapish Garg**
*Software Development Student | Saras AI Institute*

---