# ==============================================================================
# SCRIPT: 03_exploratory_analysis.R
# PURPOSE: Parametric & Non-Parametric Exploratory Statistics & Group Profiling
# PROJECT: Week 4 Final Capstone - Comprehensive Data Analysis of Superstore Sales
# ==============================================================================

suppressPackageStartupMessages({
  library(dplyr)
  library(readr)
})

cat("[INFO] ------------------------------------------------------------\n")
cat("[INFO] STAGE 3: EXPLORATORY DATA ANALYSIS & STATISTICAL PROFILING\n")
cat("[INFO] ------------------------------------------------------------\n")

df <- readRDS("data/processed/superstore_clean.rds")

# Helper functions for skewness and kurtosis (base R without requiring e1071)
calc_skewness <- function(x) {
  x <- x[!is.na(x)]
  n <- length(x)
  m3 <- sum((x - mean(x))^3) / n
  s3 <- (sum((x - mean(x))^2) / n)^(3/2)
  m3 / s3
}

calc_kurtosis <- function(x) {
  x <- x[!is.na(x)]
  n <- length(x)
  m4 <- sum((x - mean(x))^4) / n
  s4 <- (sum((x - mean(x))^2) / n)^2
  (m4 / s4) - 3 # Excess kurtosis
}

# 1. Numerical Descriptive Statistics
num_vars <- c("Sales", "Profit", "Quantity", "Discount", "Shipping_Days", "Profit_Margin")
num_stats <- lapply(num_vars, function(v) {
  x <- df[[v]]
  data.frame(
    Variable = v,
    N = length(x),
    Mean = round(mean(x), 2),
    SD = round(sd(x), 2),
    Median = round(median(x), 2),
    IQR = round(IQR(x), 2),
    Min = round(min(x), 2),
    Max = round(max(x), 2),
    Skewness = round(calc_skewness(x), 2),
    Excess_Kurtosis = round(calc_kurtosis(x), 2),
    stringsAsFactors = FALSE
  )
})
num_stats_df <- bind_rows(num_stats)
write.csv(num_stats_df, "outputs/tables/03_numerical_descriptive_stats.csv", row.names = FALSE)
cat("[INFO] Exported: outputs/tables/03_numerical_descriptive_stats.csv\n")

# 2. Category Performance Summary
cat_summary <- df %>%
  group_by(Category) %>%
  summarize(
    Orders_Count = n(),
    Total_Sales = round(sum(Sales), 2),
    Sales_Share_Pct = round(sum(Sales) / sum(df$Sales) * 100, 2),
    Total_Profit = round(sum(Profit), 2),
    Profit_Share_Pct = round(sum(Profit) / sum(df$Profit) * 100, 2),
    Profit_Margin_Pct = round(sum(Profit) / sum(Sales) * 100, 2),
    Mean_Discount_Pct = round(mean(Discount) * 100, 2),
    Loss_Orders_Count = sum(Loss_Making_Flag),
    Loss_Rate_Pct = round(mean(Loss_Making_Flag) * 100, 2),
    .groups = "drop"
  ) %>%
  arrange(desc(Total_Sales))
write.csv(cat_summary, "outputs/tables/03_category_performance_summary.csv", row.names = FALSE)

# 3. Sub-Category Performance Summary
subcat_summary <- df %>%
  group_by(Category, Sub_Category) %>%
  summarize(
    Orders_Count = n(),
    Total_Sales = round(sum(Sales), 2),
    Total_Profit = round(sum(Profit), 2),
    Profit_Margin_Pct = round(sum(Profit) / sum(Sales) * 100, 2),
    Mean_Discount_Pct = round(mean(Discount) * 100, 2),
    Loss_Orders_Count = sum(Loss_Making_Flag),
    Loss_Rate_Pct = round(mean(Loss_Making_Flag) * 100, 2),
    .groups = "drop"
  ) %>%
  arrange(desc(Total_Sales))
write.csv(subcat_summary, "outputs/tables/03_subcategory_performance_summary.csv", row.names = FALSE)

# 4. Regional Performance Summary
reg_summary <- df %>%
  group_by(Region) %>%
  summarize(
    Orders_Count = n(),
    Total_Sales = round(sum(Sales), 2),
    Sales_Share_Pct = round(sum(Sales) / sum(df$Sales) * 100, 2),
    Total_Profit = round(sum(Profit), 2),
    Profit_Share_Pct = round(sum(Profit) / sum(df$Profit) * 100, 2),
    Profit_Margin_Pct = round(sum(Profit) / sum(Sales) * 100, 2),
    Mean_Discount_Pct = round(mean(Discount) * 100, 2),
    Loss_Orders_Count = sum(Loss_Making_Flag),
    Loss_Rate_Pct = round(mean(Loss_Making_Flag) * 100, 2),
    .groups = "drop"
  ) %>%
  arrange(desc(Total_Profit))
write.csv(reg_summary, "outputs/tables/03_regional_performance_summary.csv", row.names = FALSE)

# 5. Customer Segment Performance Summary
seg_summary <- df %>%
  group_by(Segment) %>%
  summarize(
    Orders_Count = n(),
    Total_Sales = round(sum(Sales), 2),
    Sales_Share_Pct = round(sum(Sales) / sum(df$Sales) * 100, 2),
    Total_Profit = round(sum(Profit), 2),
    Profit_Share_Pct = round(sum(Profit) / sum(df$Profit) * 100, 2),
    Profit_Margin_Pct = round(sum(Profit) / sum(Sales) * 100, 2),
    Avg_Order_Value = round(mean(Sales), 2),
    .groups = "drop"
  ) %>%
  arrange(desc(Total_Sales))
write.csv(seg_summary, "outputs/tables/03_segment_performance_summary.csv", row.names = FALSE)

# 6. Discount Band Performance Summary
disc_summary <- df %>%
  group_by(Discount_Band) %>%
  summarize(
    Orders_Count = n(),
    Orders_Pct = round(n() / nrow(df) * 100, 2),
    Total_Sales = round(sum(Sales), 2),
    Total_Profit = round(sum(Profit), 2),
    Mean_Profit = round(mean(Profit), 2),
    Profit_Margin_Pct = round(sum(Profit) / sum(Sales) * 100, 2),
    Loss_Orders_Count = sum(Loss_Making_Flag),
    Loss_Rate_Pct = round(mean(Loss_Making_Flag) * 100, 2),
    .groups = "drop"
  )
write.csv(disc_summary, "outputs/tables/03_discount_band_summary.csv", row.names = FALSE)

# 7. Yearly Growth Trajectory
yearly_summary <- df %>%
  group_by(Order_Year) %>%
  summarize(
    Line_Items = n(),
    Unique_Orders = length(unique(Order_ID)),
    Total_Sales = round(sum(Sales), 2),
    Total_Profit = round(sum(Profit), 2),
    Profit_Margin_Pct = round(sum(Profit) / sum(Sales) * 100, 2),
    .groups = "drop"
  ) %>%
  mutate(
    Sales_YoY_Growth_Pct = round(c(NA, diff(Total_Sales) / head(Total_Sales, -1) * 100), 2),
    Profit_YoY_Growth_Pct = round(c(NA, diff(Total_Profit) / head(Total_Profit, -1) * 100), 2)
  )
write.csv(yearly_summary, "outputs/tables/03_yearly_growth_summary.csv", row.names = FALSE)

# Capture terminal exploratory summary snapshot
sink("screenshots/outputs/03_exploratory_analysis_output.txt")
cat("================================================================================\n")
cat("SUPERSTORE EXPLORATORY DATA ANALYSIS & DESCRIPTIVE PROFILING (R v4.6.1)\n")
cat("================================================================================\n")
cat("1. NUMERICAL DESCRIPTIVE STATISTICS:\n")
print(num_stats_df)
cat("--------------------------------------------------------------------------------\n")
cat("2. CATEGORY FINANCIAL PERFORMANCE:\n")
print(cat_summary)
cat("--------------------------------------------------------------------------------\n")
cat("3. REGIONAL FINANCIAL PERFORMANCE:\n")
print(reg_summary)
cat("--------------------------------------------------------------------------------\n")
cat("4. DISCOUNT BAND FINANCIAL PERFORMANCE:\n")
print(disc_summary)
cat("--------------------------------------------------------------------------------\n")
cat("5. YEAR-OVER-YEAR GROWTH:\n")
print(yearly_summary)
cat("================================================================================\n")
sink()

cat("[INFO] Exported: screenshots/outputs/03_exploratory_analysis_output.txt\n")
cat("[INFO] Stage 3 Exploratory Analysis completed successfully.\n\n")
