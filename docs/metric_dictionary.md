# Business Metric Dictionary

This document defines the authoritative business metrics for the Autonomous Business Root-Cause Analyst. The AI Agent and Power BI Semantic Model strictly adhere to these definitions to ensure consistency and prevent hallucination.

## 1. Delivery Performance Metrics

### Total Deliveries
- **Definition:** Count of all valid delivery records in the dataset.
- **Grain:** Delivery (`id`)
- **Filters:** None (includes all records).
- **Business Interpretation:** Overall operational volume.

### Average Delivery Time
- **Definition:** Mean of `time_taken_min`.
- **Grain:** Delivery
- **Filters:** Exclude records where `time_taken_min` is null or <= 0.
- **Business Interpretation:** The average operational time from order placement to delivery completion.

### Median Delivery Time
- **Definition:** 50th percentile of `time_taken_min`.
- **Business Interpretation:** The typical delivery time, robust to extreme outliers (e.g., extreme traffic jams).

### P90 Delivery Time
- **Definition:** 90th percentile of `time_taken_min`.
- **Business Interpretation:** The time within which 90% of deliveries are completed. Used to measure worst-case performance and SLA compliance.

### Average Pickup Delay
- **Definition:** Mean of `pickup_delay_minutes` (calculated as `time_order_picked` - `time_orderd`).
- **Grain:** Delivery
- **Filters:** Exclude records where `time_orderd_missing == True`.
- **Business Interpretation:** Average time taken by the delivery person to reach the restaurant and pick up the order after it was placed.

## 2. Operational Condition Metrics

### High Traffic Percentage
- **Definition:** Percentage of deliveries occurring under adverse traffic conditions.
- **Formula:** `(Count(road_traffic_density IN ['High', 'Jam']) / Total Deliveries) * 100`
- **Business Interpretation:** Exposure to traffic-related delays.

### Multiple Deliveries Percentage
- **Definition:** Percentage of deliveries where the driver is handling more than one order simultaneously.
- **Formula:** `(Count(multiple_deliveries > 0) / Total Deliveries) * 100`
- **Business Interpretation:** Indicator of route optimization and potential batching delays.

### Poor Vehicle Condition Percentage
- **Definition:** Percentage of deliveries made with vehicles rated at the lowest condition tier.
- **Formula:** `(Count(vehicle_condition == 0) / Total Deliveries) * 100`
- **Business Interpretation:** Potential risk factor for breakdowns or slower travel speeds.

## 3. Dimensional Attributes (Used for Segmentation)

The AI Agent uses these dimensions to slice and dice metrics during root-cause hypothesis testing:

- **City:** `Metropolitan`, `Urban`, `Semi-Urban`
- **Weather:** `Sunny`, `Cloudy`, `Fog`, `Stormy`, `Windy`, `Sandstorms`
- **Traffic:** `Low`, `Medium`, `High`, `Jam`
- **Vehicle Type:** `Motorcycle`, `Scooter`, `Electric_scooter`
- **Order Type:** `Snack`, `Meal`, `Drinks`, `Buffet`
- **Time of Day:** `Morning` (06-11), `Afternoon` (12-16), `Evening` (17-20), `Night` (21-05)
- **Festival:** `Yes`, `No`

## 4. Data Quality Metrics

### Missing Order Time Count
- **Definition:** Count of deliveries where `time_orderd` is null or empty.
- **Business Interpretation:** Tracks data pipeline health. These records cannot be used for pickup delay analysis.