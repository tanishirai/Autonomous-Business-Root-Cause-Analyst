# Autonomous Business Root-Cause Analyst

An AI-powered analytics investigation system that automatically investigates business problems, identifies root causes using data, provides quantitative evidence, and recommends actions.

> **Traditional BI tells businesses WHAT happened. This system investigates WHY it happened and WHAT should be done next.**

---

## Project Status

### Phase 1: Dataset Foundation ✅ IN PROGRESS

**Completed:**
- ✅ Project structure setup
- ✅ Dataset acquisition script
- ✅ Data profiling notebook
- ✅ Dataset documentation
- ✅ Data quality framework

**Next:**
- ⏳ Complete data profiling
- ⏳ Document all quality issues
- ⏳ Proceed to Phase 2: Data Engineering

---

## Quick Start

### Prerequisites
- Python 3.9+
- pip

### Setup

```bash
# Clone repository
git clone [repository-url]
cd autonomous-business-root-cause-analyst

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download dataset
python scripts/download_dataset.py

# Run profiling
cd notebooks
jupyter notebook
# Open 01_data_profiling.ipynb and run all cells

Project Phases
Phase 1: Dataset Foundation (Current)
Dataset acquisition
Data profiling
Quality documentation
Phase 2: Data Engineering
Data cleaning
Feature engineering
Analytical model building
Phase 3: Analytics
Metric implementation
Statistical analysis
Comparison frameworks
Phase 4: Power BI
Semantic model
Dashboard creation
DAX measures
Phase 5: AI Agent
Question understanding
Hypothesis generation
Tool implementation
Phase 6: Investigation Engine
Evidence collection
Root-cause ranking
Recommendation generation
Phase 7: FastAPI Backend
API endpoints
Service layer
Integration
Phase 8: React Frontend
Investigation UI
Evidence visualization
User experience
Phase 9: Evaluation
Benchmark creation
Performance testing
Comparison with baseline
Phase 10: Deployment
Production setup
Monitoring
Documentation
Architecture Overview

12345678910111213
Dataset
Source: Zomato Delivery Operations Dataset (Public)
Records: ~45,584 deliveries
Fields: 20 operational variables
Coverage: Multiple Indian cities
See docs/dataset.md for complete documentation.
Documentation
docs/dataset.md - Dataset provenance and schema
docs/data_quality.md - Data quality report
docs/metric_dictionary.md - Business metrics (Phase 3)
docs/architecture.md - System architecture (Phase 7)
docs/investigation_methodology.md - Investigation approach (Phase 6)
Development
Current Phase: 1 - Dataset Foundation
Files:
scripts/download_dataset.py - Dataset acquisition
notebooks/01_data_profiling.ipynb - Data profiling
docs/dataset.md - Dataset documentation
docs/data_quality.md - Quality framework
Status: Profiling in progress
License
This project is for educational and portfolio purposes.
Dataset is publicly available from Kaggle/Hugging Face.
Contact
For questions about this project, please open an issue on GitHub.


---

## Summary of Phase 1 Deliverables

✅ **Project Structure:** Complete directory hierarchy  
✅ **Dependencies:** All required packages specified  
✅ **Dataset Acquisition:** Automated download with verification  
✅ **Data Profiling:** Comprehensive analysis notebook  
✅ **Documentation:** Dataset and quality frameworks  
✅ **README:** Project overview and setup instructions  

---

## Next Steps

After completing Phase 1:

1. **Review profiling results** - Examine all identified issues
2. **Complete data quality report** - Fill in all findings
3. **Validate dataset** - Ensure data is suitable for analysis
4. **Proceed to Phase 2** - Begin data cleaning and feature engineering

---

## Common Issues and Solutions

### Issue: Dataset download fails
**Solution:** Download manually from Hugging Face and place in `data/raw/`

### Issue: Missing dependencies
**Solution:** Ensure virtual environment is activated and run `pip install -r requirements.txt`

### Issue: Jupyter notebook won't start
**Solution:** Install Jupyter with `pip install jupyter` and ensure kernel is installed

### Issue: Memory errors during profiling
**Solution:** The dataset is ~45K rows, should fit in memory. If issues persist, profile in chunks.

---

**Phase 1 is now ready to execute.** Run the profiling notebook, review the findings, and we'll proceed to Phase 2: Data Engineering where we'll clean the data and build the analytical foundation.

Would you like me to proceed with Phase 2, or do you have any questions about Phase 1?