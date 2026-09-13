# Autonomous Business Root-Cause Analyst

> **Traditional BI tells businesses WHAT happened. This system investigates WHY it happened and WHAT should be done next.**

An AI-powered analytics investigation system that automatically investigates business problems, identifies likely root causes using data, provides quantitative evidence, and recommends actionable business strategies.

## 🚀 Live Demo
- **Frontend Application:** [https://autonomous-business-root-cause-anal.vercel.app/](https://autonomous-business-root-cause-anal.vercel.app/) *(Try asking: "Why is delivery time so high in Semi-Urban areas?")*
- **Backend API Docs:** [https://autonomous-business-root-cause-analyst.onrender.com/docs](https://autonomous-business-root-cause-analyst.onrender.com/docs)
- **Power BI Dashboard:** Download the `.pbix` file from the `powerbi/` directory and open it in Power BI Desktop to explore the interactive Star Schema, DAX measures, and Decomposition Tree.

---

## 💡 The Problem & The Solution

### The Problem
Traditional dashboards answer questions like *"What was the average delivery time?"* or *"Which city performed worst?"*. But when an operations manager asks, *"Why did delivery performance deteriorate last month?"*, a normal dashboard requires a human analyst to manually identify metrics, compare periods, generate hypotheses, query databases, and test alternative explanations.

### The Solution
This project is **not a generic Text-to-SQL chatbot**. It is an **Autonomous Analytics Investigator**. When given a business question, the system:
1. **Understands** the business intent and maps it to defined metrics.
2. **Generates** multiple testable hypotheses based on available data dimensions.
3. **Leverages Python analytics context** to ground its responses in actual quantitative evidence.
4. **Tests alternative explanations** to avoid false causal claims.
5. **Ranks root causes** by evidence strength and sample size.
6. **Recommends actionable business strategies** while explicitly stating data limitations.

---

## 🏗️ Architecture Overview

This project is built on a modern, layered data and AI architecture designed for scalability and explainability:

```text
                    ┌──────────────────┐
                    │   Business User  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  React + Vite    │ (Hosted on Vercel)
                    │  + Tailwind CSS  │
                    └────────┬─────────┘
                             │ (JSON API)
                             ▼
                    ┌──────────────────┐
                    │   FastAPI        │ (Hosted on Render)
                    │   Backend        │
                    └────────┬─────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
        ┌──────────┐  ┌────────────┐  ┌─────────────┐
        │ Gemini   │  │ Python     │  │ Power BI    │
        │ LLM      │  │ Analytics  │  │ Semantic    │
        │ (Context)│  │ Context    │  │ Model       │
        └────┬─────┘  └─────┬──────┘  └─────────────┘
             │              │
             └──────┬───────┘
                    ▼
             ┌──────────────┐
             │ Pandas / CSV │ (Processed Data Layer)
             └──────────────┘

```
---

## 🌟 Key Differentiators
- Unlike generic AI SQL generators, this system:
- Generates Hypotheses: It doesn't just query; it forms testable business hypotheses before looking at the data.
- Provides an Evidence Ledger: Every claim is backed by a quantitative value, sample size, and confidence level (High/Medium/Low).
- Acknowledges Limitations: It explicitly states what the observational data cannot prove, preventing AI hallucinations and false causal claims.
- Recommends Actions: It translates data findings into actionable, prioritized business strategies.
- Separation of Concerns: The LLM orchestrates the logic and formats the business response, while Python handles the underlying data processing, ensuring high analytical accuracy.

---

## 🛠️ Tech Stack

- **Data & Analytics:** Python, Pandas, NumPy, SciPy, Jupyter Notebooks
- **BI & Visualization:** Microsoft Power BI, DAX, Star Schema Modeling
- **Backend API:** FastAPI, Pydantic (Strict Structured I/O)
- **AI/LLM:** Google Gemini API (Structured JSON generation & Tool Calling)
- **Frontend:** React, Vite, Tailwind CSS, Lucide Icons
- **Deployment:** Vercel (Frontend), Render (Backend)

---

## 📂 Project Structure

```text
autonomous-business-root-cause-analyst/
│
├── .env.example                  # Template for API keys
├── .gitignore                    # Protects secrets and large raw files
├── requirements.txt              # Python dependencies
├── runtime.txt                   # Python version for Render deployment
├── README.md                     # This file
│
├── data/
│   ├── raw/                      # (Ignored by Git) Original untouched data
│   └── processed/                # Cleaned, feature-engineered analytical dataset
│
├── notebooks/
│   ├── 01_data_profiling.ipynb   # Initial data quality investigation
│   ├── 02_data_cleaning.ipynb    # Conservative cleaning & feature engineering
│   └── 03_analytics_testing.ipynb# Validation of analytics modules
│
├── analytics/
│   ├── metrics.py                # Core metric calculations (matches Power BI DAX)
│   └── comparisons.py            # Period comparison & effect size calculations
│
├── agent/
│   ├── tools.py                  # Controlled Python functions the AI can call
│   └── investigator.py           # Main AI orchestration & prompt logic
│
├── backend/
│   ├── main.py                   # FastAPI application & CORS setup
│   └── models.py                 # Pydantic schemas for strict JSON validation
│
├── frontend/                     # React + Vite + Tailwind application
│   ├── src/
│   │   ├── App.jsx               # Main investigation UI & progress tracking
│   │   └── index.css             # Tailwind configuration
│   └── tailwind.config.js
│
├── powerbi/
│   └── Zomato_Root_Cause_Analysis.pbix # Interactive dashboard file
│
├── docs/
│   ├── dataset.md                # Dataset provenance, schema, and limitations
│   ├── data_quality.md           # Detailed cleaning decisions and impact log
│   └── metric_dictionary.md      # Authoritative business metric definitions
│
└── scripts/
    └── download_dataset.py       # Automated dataset acquisition script
```
---

## 🚀 How to Run Locally

### Prerequisites
- Python 3.9+
- Node.js 16+
- A free Google Gemini API Key ([Get one here](https://aistudio.google.com/app/apikey))

### 1. Backend Setup
```bash
# Clone the repository
git clone https://github.com/tanishirai/autonomous-business-root-cause-analyst.git
cd autonomous-business-root-cause-analyst

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt

# Create .env file and add your API key
echo "GOOGLE_API_KEY=your_actual_api_key_here" > .env

# Start FastAPI server
uvicorn backend.main:app --reload

The API will be available at http://127.0.0.1:8000/docs
```

### 2. Frontend Setup
```bash
# Open a new terminal and run:

cd frontend
npm install
npm run dev

Open http://localhost:5173 in your browser to use the application.
```

### 3. Power BI Setup
```bash
Open powerbi/Zomato_Root_Cause_Analysis.pbix in Power BI Desktop to explore the semantic model, DAX measures, and interactive dashboards.
```

## 📊 Example Investigation

**User Question:** *"Why is delivery time so high in Semi-Urban areas compared to Metropolitan?"*

**System Response:**
- **Executive Summary:** Identifies larger average travel distances and lower delivery partner density as primary drivers.
- **Evidence Ledger:** Shows Semi-Urban avg time (49.7 min, n=146) vs Metropolitan (27.4 min, n=30,036) with High confidence.
- **Root Causes:** 
  1. Longer transit distances. 
  2. Lower partner density. 
  3. Limited multi-route infrastructure.
- **Recommendations:** Establish dynamic delivery radii tailored to Semi-Urban transit times; introduce regional micro-fulfillment centers.
- **Limitations:** Explicitly notes the small sample size (n=146) for Semi-Urban deliveries, preventing definitive causal claims.

---

## 📝 Documentation

Deep dives into the analytical methodology:
- [📊 Dataset Provenance & Schema](docs/dataset.md)
- [🧹 Data Quality Report & Cleaning Log](docs/data_quality.md)
- [📏 Business Metric Dictionary](docs/metric_dictionary.md)

---

## 🔮 Future Roadmap (Planned V2 Upgrades)

- **True Agentic Loop:** Implement iterative tool-calling where the LLM dynamically executes Python functions and decides to run deeper segmentation if initial evidence confidence is "Low".
- **RAG Integration:** Add Retrieval-Augmented Generation to ingest internal company SOPs, allowing the AI to align recommendations with specific business policies.
- **Advanced Causal Inference:** Integrate Python libraries like DoWhy or EconML to move from association-based evidence to true causal impact estimation.
- **CI/CD Pipeline:** Add GitHub Actions for automated testing of the analytics modules and Pydantic schema validation on every PR.

---

*Built as a comprehensive portfolio project demonstrating end-to-end AI Analytics Engineering, bridging the gap between raw data, business intelligence, and autonomous AI reasoning.*
