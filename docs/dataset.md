# Dataset Documentation

## Overview

**Dataset Name:** Zomato Delivery Operations Analytics Dataset  
**Source:** Public dataset available on Kaggle and Hugging Face  
**Primary Use:** Business operations analysis and root-cause investigation  
**Row Count:** 38,964 delivery records  
**Column Count:** 22 operational and engineered fields  

## Data Provenance

### Original Source
- **Platform:** Kaggle
- **Dataset:** Zomato Delivery Operations Analytics Dataset (by Saurabh Badole)
- **URL:** https://www.kaggle.com/datasets/saurabhbadole/zomato-delivery-operations-analytics-dataset

### Mirror/Secondary Source
- **Platform:** Hugging Face
- **Repository:** allenborochin/zomato_delivery_EDA
- **URL:** https://huggingface.co/datasets/allenborochin/zomato_delivery_EDA

### License
- **Type:** Public domain / Open data
- **Usage:** Research, educational, and portfolio demonstration purposes
- **Restrictions:** None specified for non-commercial analytical use

## Important Disclaimer

This is a **publicly available, anonymized dataset** distributed through Kaggle and mirrored on Hugging Face. It is **NOT** proprietary internal Zomato data. The dataset should be treated as a realistic operational dataset for demonstration, educational, and portfolio purposes.

## Schema Description

### Core Fields

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| `id` | String | Unique delivery identifier | "0xcdcd" |
| `delivery_person_id` | String | Delivery personnel identifier | "HYDRES04DEL02" |
| `delivery_person_age` | Float | Age of delivery person | 30.0 |
| `delivery_person_ratings` | Float | Rating of delivery person (1-5) | 4.7 |
| `restaurant_latitude` | Float | Restaurant GPS latitude | 18.9234 |
| `restaurant_longitude` | Float | Restaurant GPS longitude | 76.9123 |
| `delivery_location_latitude` | Float | Delivery GPS latitude | 18.9834 |
| `delivery_location_longitude` | Float | Delivery GPS longitude | 76.9823 |
| `order_date` | Datetime | Date of order (YYYY-MM-DD) | 2022-03-15 |
| `time_orderd` | String | Time order was placed (HH:MM) | "17:55" |
| `time_order_picked` | String | Time order was picked up (HH:MM) | "18:10" |
| `weather_conditions` | String | Weather condition category | "Fog", "Stormy", "Sunny" |
| `road_traffic_density` | String | Traffic density level | "Low", "Medium", "High", "Jam" |
| `vehicle_condition` | Int | Vehicle condition rating (0-2) | 1 |
| `type_of_order` | String | Order type | "Snack", "Meal", "Drinks", "Buffet" |
| `type_of_vehicle` | String | Vehicle type | "motorcycle", "scooter", "electric_scooter" |
| `multiple_deliveries` | Float | Number of additional stops in the trip | 0, 1, 2, 3 |
| `festival` | String | Whether a festival was active | "Yes", "No" |
| `city` | String | City classification | "Metropolitan", "Urban", "Semi-Urban" |
| `time_taken_min` | Int | Total delivery time in minutes | 26 |
| `distance_km` | Float | *(Engineered)* Haversine distance in km | 9.77 |
| `delivery_speed` | String | *(Engineered)* Speed category | "Fast", "Average", "Slow" |

## Data Characteristics

### Temporal Coverage
- **Date Range:** February 11, 2022 – April 6, 2022 (55 days)
- **Time Granularity:** Individual delivery records
- **Frequency:** Multiple deliveries per day across various time-of-day segments

### Geographical Coverage
- **Locations:** Multiple cities in India
- **Coordinate System:** WGS84 (standard GPS coordinates)
- **Coverage Area:** Point-to-point from Restaurant to Delivery Location

### Operational Factors Captured
- Delivery personnel characteristics (age, ratings)
- Environmental conditions (weather, traffic)
- Vehicle information (type, condition)
- Order characteristics (type, timing, multiple drops)
- Location data (GPS coordinates, derived distance)
- Contextual factors (festivals, city classification)

## Known Limitations

1. **Observational Data:** This is observational data, not experimental. Causal claims require careful interpretation and are explicitly avoided by the AI agent.
2. **Missing Business Context:** The dataset does not include revenue, order value, customer IDs, restaurant preparation time, SLA commitments, or cancellation reasons.
3. **Anonymized Entities:** Delivery person IDs and GPS coordinates are anonymized/hashed.
4. **Temporal Limitation:** The dataset only covers an 8-week window, limiting long-term seasonal trend analysis.
5. **Class Imbalance:** "Semi-Urban" deliveries represent only ~0.37% of the dataset, making statistical conclusions about this segment less robust.

## Preprocessing Performed

### Raw Data Preservation
- Original dataset preserved in `data/raw/zomato_delivery_raw.csv`.
- No modifications made to raw data.
- All transformations are documented and reversible.

### Cleaning & Engineering (Silver/Gold Layer)
- Standardized column names to lowercase with underscores.
- Corrected `order_date` parsing using `dayfirst=True`.
- Imputed missing `delivery_person_age` and `delivery_person_ratings` with medians.
- Created `time_orderd_missing` boolean flag.
- Calculated `pickup_delay_minutes` and `order_hour`.
- Standardized categorical values (e.g., fixed "Metropolitian" typo).
- Saved final analytical dataset to `data/processed/zomato_cleaned_analytical.csv`.

## Usage Guidelines

### Appropriate Uses
- Operational performance analysis and root-cause investigation.
- Trend analysis and segmentation studies.
- Demonstrating AI-driven analytical reasoning (as done in this project).

### Inappropriate Uses
- Making definitive causal claims without proper methodology.
- Extrapolating findings to represent all global food delivery operations.
- Using for production business decisions without validating against live internal data.

## Data Quality Tracking

All data quality issues and cleaning decisions are tracked in:
- `docs/data_quality.md` - Detailed quality report
- `notebooks/01_data_profiling.ipynb` - Profiling analysis
- `notebooks/02_data_cleaning.ipynb` - Cleaning decisions

## Version Control

- **Raw Data Version:** 1.0 (original download)
- **Last Updated:** September 2026
- **Checksum (MD5):** `166cda3c214c1d85ad0cd11d3b39fa02`

## Contact and Support

- **Original Source:** Check Kaggle dataset discussion page.
- **Project Issues:** See project `README.md`.
- **Data Quality Concerns:** See `docs/data_quality.md`.