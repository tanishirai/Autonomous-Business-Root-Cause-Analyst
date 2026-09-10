# Data Quality Report

## Executive Summary

**Dataset:** Zomato Delivery Operations (Hugging Face Mirror)  
**Total Records:** 38,964  
**Total Columns:** 22  
**Critical Issues:** 0 (All resolved conservatively during ETL)  
**Data Quality Score:** High (99.6% cell completeness)  

## Quality Dimensions Assessed

### 1. Completeness
- **Overall missing value rate:** 0.34% of total cells (2,909 missing cells out of 857,208)
- **Columns with missing values:** `Delivery_person_Ratings`, `Delivery_person_Age`, `Time_Orderd`
- **Rows with any missing value:** ~2,500 (some rows have multiple missing fields)

### 2. Uniqueness
- **Exact duplicate rows:** 0
- **Duplicate based on key columns (`ID`, `Delivery_person_ID`, `Order_Date`, `Time_Orderd`):** 0
- **Duplicate percentage:** 0.00%

### 3. Validity
- **Invalid ages:** 0 (All values logically fall between 20 and 39)
- **Invalid ratings:** 0 (All values logically fall between 2.5 and 5.0)
- **Invalid coordinates:** 0 (All lat/long values fall within valid Indian geographic bounds; no zero-coordinates)
- **Invalid timestamps:** 0 (Initially appeared as 20,809 due to MM-DD vs DD-MM parsing, fully resolved with `dayfirst=True`)
- **Invalid delivery times:** 0 (Range is 10 to 54 minutes; no zeros or negatives)

### 4. Consistency
- **Format inconsistencies:** `Order_Date` required explicit `dayfirst=True` parsing in Pandas.
- **Categorical value variations:** `City` contained a typo ("Metropolitian" instead of "Metropolitan").
- **Logical inconsistencies:** None detected post-cleaning.

### 5. Accuracy
- **Geographic plausibility:** High. Coordinates align with major Indian metropolitan and semi-urban regions.
- **Temporal plausibility:** High. Data spans a realistic 55-day operational window (Feb 11, 2022 – Apr 6, 2022).
- **Value range plausibility:** High. Delivery times (10–54 mins) and distances (1.4–20.9 km) are operationally realistic.

## Detailed Findings

### Missing Values Analysis

| Column | Missing Count | Missing % | Severity |
|--------|---------------|-----------|----------|
| Delivery_person_Ratings | 1,055 | 2.71% | Low |
| Delivery_person_Age | 1,019 | 2.62% | Low |
| Time_Orderd | 835 | 2.14% | Medium |

### Duplicate Records

**Exact Duplicates:** 0  
**Key-based Duplicates:** 0  

**Decision:** No deduplication required.  
**Reason:** The dataset is inherently unique at the delivery record level.

### Coordinate Quality

**Zero Coordinates:** 0  
**Out-of-Range Coordinates:** 0  
**Impossible Distances:** 0  

**Impact:** None. Geospatial features (`distance_km`) are highly reliable.  
**Decision:** Retain all records for spatial analysis.

### Timestamp Quality

**Invalid Date Formats:** 0 (Resolved via `dayfirst=True`)  
**Impossible Timestamps:** 0  
**Missing Timestamps:** 835 (`Time_Orderd`)  

**Decision:** Created a boolean flag `time_orderd_missing`. Records with missing order times are excluded from `pickup_delay_minutes` calculations but retained for overall delivery time analysis.

### Categorical Data Quality

**Whitespace Issues:** Resolved via `.str.strip()` on all categorical columns.  
**Inconsistent Values:** "Metropolitian" (30,036 rows).  
**Invalid Categories:** None.  

**Decision:** Standardized "Metropolitian" to "Metropolitan" to ensure accurate grouping in BI and AI layers.

## Data Quality Issues Requiring Attention

### Critical Issues
*None remaining after ETL processing.*

### Moderate Issues
1. **Missing Order Time (`Time_Orderd`)**
   - **Impact:** Prevents accurate calculation of `pickup_delay_minutes` for a subset of data.
   - **Proposed Solution:** Flagged via `time_orderd_missing` column. Excluded from pickup delay aggregations.
   - **Rows Affected:** 835

### Minor Issues
1. **Missing Demographic Data (Age/Ratings)**
   - **Impact:** Minor loss of granularity for delivery-person segmentation.
   - **Proposed Solution:** Imputed with dataset medians (Age: 30.0, Ratings: 4.7) to preserve row count for downstream ML/analytical tasks.
   - **Rows Affected:** 1,019 (Age), 1,055 (Ratings)

## Cleaning Principles

1. **Conservative Approach:** Do not delete rows unless absolutely necessary.
2. **Documentation:** Every cleaning decision is documented and reversible.
3. **Reversibility:** Maintain ability to trace back to the raw data layer.
4. **Transparency:** Report the impact of each cleaning decision explicitly.
5. **Preservation:** The raw data layer (`data/raw/`) remains completely untouched.

## Cleaning Decisions Log

| Issue | Detection Method | Decision | Reason | Rows Affected | Impact |
|-------|------------------|----------|--------|---------------|--------|
| Date Parsing Error | Pandas `to_datetime` default behavior | Applied `dayfirst=True` | Dates are DD-MM-YYYY, not MM-DD-YYYY | 38,964 | Enabled accurate temporal feature engineering |
| Missing Age/Ratings | Null count analysis | Median Imputation | Preserves row count; median is robust to outliers | 2,074 total | Allows continuous use of demographic columns |
| City Typo | Value counts inspection | String replacement | "Metropolitian" is a misspelling of "Metropolitan" | 30,036 | Ensures correct aggregation in Power BI and AI tools |
| Missing Order Time | Null count analysis | Created boolean flag | Cannot calculate pickup delay without start time | 835 | Prevents silent errors in delay calculations |

## Recommendations

1. **For Future Data Collection:** Implement frontend validation to prevent blank `Time_Orderd` entries at the point of order creation.
2. **For Analytical Use:** Always filter by `time_orderd_missing == False` when analyzing `pickup_delay_minutes`.
3. **For AI Agent:** The agent should be prompted to acknowledge the 8-week temporal limitation of this dataset when making trend-based recommendations.

## Next Steps

1. ✅ Complete detailed profiling in notebook.
2. ✅ Document all findings.
3. ✅ Make cleaning decisions.
4. ✅ Implement cleaning in `02_data_cleaning.ipynb`.
5. ✅ Validate cleaned data and proceed to Analytics layer.