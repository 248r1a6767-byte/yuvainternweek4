# ==============================================================================
# SCRIPT: 04_visualizations.R
# PURPOSE: Publication-Grade Visualizations (EDA, Trends, Product, Region, Discount)
# PROJECT: Week 4 Final Capstone - Comprehensive Data Analysis of Superstore Sales
# ==============================================================================

suppressPackageStartupMessages({
  library(dplyr)
  library(ggplot2)
  library(scales)
  library(patchwork)
})

cat("[INFO] ------------------------------------------------------------\n")
cat("[INFO] STAGE 4: PUBLICATION-GRADE DATA VISUALIZATIONS\n")
cat("[INFO] ------------------------------------------------------------\n")

df <- readRDS("data/processed/superstore_clean.rds")

# Master Theme Definition (Corporate Academic Standard)
theme_capstone <- function(base_size = 11) {
  theme_minimal(base_size = base_size) +
    theme(
      plot.title = element_text(face = "bold", size = rel(1.15), color = "#1A365D", hjust = 0, margin = ggplot2::margin(b = 6)),
      plot.subtitle = element_text(size = rel(0.92), color = "#4A5568", hjust = 0, margin = ggplot2::margin(b = 10)),
      plot.caption = element_text(size = rel(0.75), color = "#718096", hjust = 1, margin = ggplot2::margin(t = 8)),
      axis.title = element_text(face = "bold", size = rel(0.9), color = "#2D3748"),
      axis.text = element_text(size = rel(0.85), color = "#4A5568"),
      panel.grid.minor = element_blank(),
      panel.grid.major = element_line(color = "#E2E8F0", linewidth = 0.4),
      panel.background = element_rect(fill = "#FAFBFC", color = NA),
      plot.background = element_rect(fill = "#FFFFFF", color = NA),
      legend.position = "top",
      legend.title = element_text(face = "bold", size = rel(0.85), color = "#2D3748"),
      legend.text = element_text(size = rel(0.8), color = "#4A5568"),
      strip.background = element_rect(fill = "#EDF2F7", color = "#CBD5E0", linewidth = 0.5),
      strip.text = element_text(face = "bold", size = rel(0.85), color = "#1A365D")
    )
}

# ------------------------------------------------------------------------------
# FIGURE 1: Distribution Analysis (Sales & Profit Heavy-Tailed Profiling)
# ------------------------------------------------------------------------------
p1a <- ggplot(df, aes(x = Sales)) +
  geom_histogram(fill = "#2B6CB0", color = "#1A365D", bins = 40, alpha = 0.85) +
  scale_x_log10(labels = label_dollar()) +
  labs(
    title = "A: Transaction Sales Distribution (Log Scale)",
    subtitle = "Severe positive skewness (Skew = 12.97; Mean = $229.86, Median = $54.49)",
    x = "Sales ($ USD, Log10 Scale)", y = "Frequency"
  ) +
  theme_capstone()

p1b <- ggplot(df, aes(x = Profit)) +
  geom_histogram(fill = "#2C7A7B", color = "#1A365D", bins = 50, alpha = 0.85) +
  geom_vline(xintercept = 0, color = "#C53030", linetype = "dashed", linewidth = 0.9) +
  scale_x_continuous(limits = c(-1000, 1000), labels = label_dollar()) +
  annotate("text", x = -450, y = 2500, label = "Loss-Making Zone\n(18.72% of orders)", color = "#C53030", fontface = "bold", size = 3.2) +
  labs(
    title = "B: Transaction Profit Distribution (-$1,000 to +$1,000)",
    subtitle = "Heavy negative tail; 1,871 transactions incur operational losses",
    x = "Profit ($ USD)", y = "Frequency"
  ) +
  theme_capstone()

fig01 <- p1a / p1b + 
  plot_annotation(
    title = "Figure 1: Empirical Distribution Profiles of Transaction Sales and Profit",
    subtitle = "Diagnostic log-distribution and central density profiling across 9,994 line-item transactions",
    caption = "Source: Superstore Dataset (2011-2014) | Yuva Intern Final Capstone",
    theme = theme(plot.title = element_text(face = "bold", size = 13, color = "#1A365D"))
  )

ggsave("figures/exploratory/fig01_sales_profit_distributions.png", fig01, width = 9.5, height = 7.5, dpi = 300)
cat("[INFO] Saved: figures/exploratory/fig01_sales_profit_distributions.png\n")

# ------------------------------------------------------------------------------
# FIGURE 2: Temporal Trends (Monthly Sales & Profit Trajectory 2011-2014)
# ------------------------------------------------------------------------------
monthly_trend <- df %>%
  group_by(Year_Month) %>%
  summarize(
    Order_Date = min(Order_Date),
    Total_Sales = sum(Sales),
    Total_Profit = sum(Profit),
    Profit_Margin = sum(Profit) / sum(Sales),
    .groups = "drop"
  ) %>%
  arrange(Order_Date)

fig02 <- ggplot(monthly_trend, aes(x = Order_Date)) +
  geom_line(aes(y = Total_Sales, color = "Monthly Sales"), linewidth = 1.1) +
  geom_point(aes(y = Total_Sales, color = "Monthly Sales"), size = 2) +
  geom_line(aes(y = Total_Profit * 5, color = "Monthly Profit (5x Scale)"), linewidth = 1.0, linetype = "solid") +
  geom_point(aes(y = Total_Profit * 5, color = "Monthly Profit (5x Scale)"), size = 1.8) +
  scale_y_continuous(
    name = "Monthly Sales ($ USD)",
    labels = label_dollar(),
    sec.axis = sec_axis(~ . / 5, name = "Monthly Profit ($ USD)", labels = label_dollar())
  ) +
  scale_x_date(date_breaks = "6 months", date_labels = "%b %Y") +
  scale_color_manual(name = "Financial Metric", values = c("Monthly Sales" = "#2B6CB0", "Monthly Profit (5x Scale)" = "#2C7A7B")) +
  annotate("rect", xmin = as.Date("2014-09-01"), xmax = as.Date("2014-12-31"), ymin = 0, ymax = 120000, alpha = 0.12, fill = "#DD6B20") +
  annotate("text", x = as.Date("2014-10-15"), y = 105000, label = "Q4 2014 Surge:\n$278k Sales\n$35k Profit", color = "#DD6B20", fontface = "bold", size = 3.3) +
  labs(
    title = "Figure 2: Longitudinal Monthly Sales and Profit Trajectory (2011 - 2014)",
    subtitle = "Dual-axis time series demonstrating prominent fourth-quarter seasonal surges and sustained revenue expansion",
    x = "Timeline (Monthly Aggregation)",
    caption = "Source: Superstore Dataset (2011-2014) | Yuva Intern Final Capstone"
  ) +
  theme_capstone() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

ggsave("figures/exploratory/fig02_monthly_sales_profit_trends.png", fig02, width = 10.5, height = 5.8, dpi = 300)
cat("[INFO] Saved: figures/exploratory/fig02_monthly_sales_profit_trends.png\n")

# ------------------------------------------------------------------------------
# FIGURE 3: Product Category & Sub-Category Performance Matrix
# ------------------------------------------------------------------------------
subcat_data <- df %>%
  group_by(Category, Sub_Category) %>%
  summarize(
    Total_Sales = sum(Sales),
    Total_Profit = sum(Profit),
    Profit_Margin = sum(Profit) / sum(Sales),
    .groups = "drop"
  ) %>%
  arrange(Category, desc(Total_Profit))

fig03 <- ggplot(subcat_data, aes(x = reorder(Sub_Category, Total_Profit), y = Total_Profit, fill = Category)) +
  geom_col(width = 0.72) +
  geom_hline(yintercept = 0, color = "#2D3748", linewidth = 0.8) +
  scale_y_continuous(labels = label_dollar()) +
  scale_fill_manual(values = c("Furniture" = "#DD6B20", "Office Supplies" = "#2C7A7B", "Technology" = "#2B6CB0")) +
  coord_flip() +
  annotate("text", x = "Tables", y = 5000, label = "Tables: -$17,725 Loss!", color = "#C53030", fontface = "bold", size = 3.2, hjust = 0) +
  annotate("text", x = "Copiers", y = 35000, label = "Copiers: +$55,618 (Leader)", color = "#2B6CB0", fontface = "bold", size = 3.2, hjust = 0) +
  labs(
    title = "Figure 3: Cumulative Profitability Across 17 Product Sub-Categories",
    subtitle = "Sub-category ranking highlighting massive profit generation in Copiers/Phones versus severe capital destruction in Tables",
    x = "Product Sub-Category", y = "Cumulative Profit ($ USD)", fill = "Product Category",
    caption = "Source: Superstore Dataset (2011-2014) | Yuva Intern Final Capstone"
  ) +
  theme_capstone()

ggsave("figures/exploratory/fig03_category_subcategory_performance.png", fig03, width = 9.8, height = 6.2, dpi = 300)
cat("[INFO] Saved: figures/exploratory/fig03_category_subcategory_performance.png\n")

# ------------------------------------------------------------------------------
# FIGURE 4: Regional Financial Performance Matrix
# ------------------------------------------------------------------------------
reg_plot_data <- df %>%
  group_by(Region) %>%
  summarize(
    Total_Sales = sum(Sales),
    Total_Profit = sum(Profit),
    Margin_Pct = (sum(Profit) / sum(Sales)) * 100,
    Loss_Rate_Pct = mean(Loss_Making_Flag) * 100,
    .groups = "drop"
  )

p4a <- ggplot(reg_plot_data, aes(x = Region, y = Total_Sales, fill = Region)) +
  geom_col(width = 0.6, fill = "#2B6CB0", alpha = 0.9) +
  geom_text(aes(label = dollar(Total_Sales, accuracy = 1)), vjust = -0.4, size = 3.3, fontface = "bold") +
  scale_y_continuous(labels = label_dollar(), limits = c(0, 850000)) +
  labs(title = "A: Total Sales by Geographic Region", y = "Total Sales ($ USD)", x = NULL) +
  theme_capstone() + theme(legend.position = "none")

p4b <- ggplot(reg_plot_data, aes(x = Region, y = Total_Profit, fill = Region)) +
  geom_col(width = 0.6, fill = "#2C7A7B", alpha = 0.9) +
  geom_text(aes(label = dollar(Total_Profit, accuracy = 1)), vjust = -0.4, size = 3.3, fontface = "bold") +
  scale_y_continuous(labels = label_dollar(), limits = c(0, 130000)) +
  labs(title = "B: Cumulative Profit by Geographic Region", y = "Cumulative Profit ($ USD)", x = NULL) +
  theme_capstone() + theme(legend.position = "none")

p4c <- ggplot(reg_plot_data, aes(x = Region, y = Margin_Pct)) +
  geom_col(width = 0.6, fill = "#DD6B20", alpha = 0.9) +
  geom_text(aes(label = paste0(round(Margin_Pct, 1), "%")), vjust = -0.4, size = 3.3, fontface = "bold") +
  scale_y_continuous(limits = c(0, 18), labels = function(x) paste0(x, "%")) +
  labs(title = "C: Operating Profit Margin (%)", y = "Profit Margin (%)", x = NULL) +
  theme_capstone()

p4d <- ggplot(reg_plot_data, aes(x = Region, y = Loss_Rate_Pct)) +
  geom_col(width = 0.6, fill = "#C53030", alpha = 0.9) +
  geom_text(aes(label = paste0(round(Loss_Rate_Pct, 1), "%")), vjust = -0.4, size = 3.3, fontface = "bold") +
  scale_y_continuous(limits = c(0, 30), labels = function(x) paste0(x, "%")) +
  labs(title = "D: Loss-Making Transaction Rate (%)", y = "Loss Rate (%)", x = NULL) +
  theme_capstone()

fig04 <- (p4a + p4b) / (p4c + p4d) +
  plot_annotation(
    title = "Figure 4: Regional Multi-Dimensional Performance Matrix",
    subtitle = "Comparative analysis of revenue generation, profit contribution, operating margin, and loss incidence across US territories",
    caption = "Source: Superstore Dataset (2011-2014) | Yuva Intern Final Capstone",
    theme = theme(plot.title = element_text(face = "bold", size = 13, color = "#1A365D"))
  )

ggsave("figures/exploratory/fig04_regional_performance_matrix.png", fig04, width = 10, height = 7.5, dpi = 300)
cat("[INFO] Saved: figures/exploratory/fig04_regional_performance_matrix.png\n")

# ------------------------------------------------------------------------------
# FIGURE 5: Customer Segment & Shipping Tier Dynamics
# ------------------------------------------------------------------------------
seg_ship <- df %>%
  group_by(Segment, Ship_Mode) %>%
  summarize(
    Mean_Days = mean(Shipping_Days),
    Total_Sales = sum(Sales),
    Total_Profit = sum(Profit),
    Order_Count = n(),
    .groups = "drop"
  )

fig05 <- ggplot(seg_ship, aes(x = Ship_Mode, y = Total_Sales, fill = Segment)) +
  geom_col(position = position_dodge(width = 0.75), width = 0.7) +
  scale_y_continuous(labels = label_dollar()) +
  scale_fill_manual(values = c("Consumer" = "#2B6CB0", "Corporate" = "#2C7A7B", "Home Office" = "#DD6B20")) +
  labs(
    title = "Figure 5: Sales Distribution by Customer Segment and Shipping Class",
    subtitle = "Standard Class dominates fulfillment across all customer sectors; Consumer segment accounts for 50.5% of total volume",
    x = "Fulfillment Shipping Class", y = "Total Sales ($ USD)", fill = "Customer Segment",
    caption = "Source: Superstore Dataset (2011-2014) | Yuva Intern Final Capstone"
  ) +
  theme_capstone()

ggsave("figures/exploratory/fig05_segment_shipping_dynamics.png", fig05, width = 9.2, height = 5.5, dpi = 300)
cat("[INFO] Saved: figures/exploratory/fig05_segment_shipping_dynamics.png\n")

# ------------------------------------------------------------------------------
# FIGURE 6: Promotional Discount vs Profit Cliff Analysis
# ------------------------------------------------------------------------------
fig06 <- ggplot(df, aes(x = Discount, y = Profit)) +
  geom_jitter(aes(color = Profit < 0), alpha = 0.28, size = 1.3, width = 0.01) +
  geom_smooth(method = "loess", color = "#1A365D", linewidth = 1.1, se = TRUE, fill = "#CBD5E0") +
  geom_vline(xintercept = 0.20, linetype = "dashed", color = "#C53030", linewidth = 0.9) +
  geom_hline(yintercept = 0, linetype = "solid", color = "#2D3748", linewidth = 0.7) +
  scale_x_continuous(labels = percent_format()) +
  scale_y_continuous(limits = c(-1500, 1000), labels = label_dollar()) +
  scale_color_manual(name = "Profit Status", values = c("FALSE" = "#2C7A7B", "TRUE" = "#C53030"), labels = c("Profitable", "Loss-Making")) +
  annotate("rect", xmin = 0.20, xmax = 0.85, ymin = -1500, ymax = 0, alpha = 0.08, fill = "#C53030") +
  annotate("text", x = 0.50, y = -800, label = "The 20% Discount Cliff:\nMedian Profit collapses to -$62.58\nProfit Margin sinks to -41.8%", 
           color = "#C53030", fontface = "bold", size = 3.6) +
  labs(
    title = "Figure 6: Empirical Profit Destruction Under Deep Promotional Discounting",
    subtitle = "Scatter plot with LOESS regression smoothing revealing immediate profit collapse beyond the 20% promotional threshold",
    x = "Promotional Discount Rate (%)", y = "Transaction Profit ($ USD)",
    caption = "Source: Superstore Dataset (2011-2014) | Yuva Intern Final Capstone"
  ) +
  theme_capstone()

ggsave("figures/exploratory/fig06_discount_vs_profit_cliff.png", fig06, width = 9.8, height = 6.0, dpi = 300)
cat("[INFO] Saved: figures/exploratory/fig06_discount_vs_profit_cliff.png\n")

# ------------------------------------------------------------------------------
# FIGURE 7: Correlation Heatmap (Pearson vs Spearman Co-Movements)
# ------------------------------------------------------------------------------
corr_vars <- df[, c("Sales", "Profit", "Quantity", "Discount", "Shipping_Days", "Profit_Margin")]
p_mat <- round(cor(corr_vars, method = "pearson"), 3)
s_mat <- round(cor(corr_vars, method = "spearman"), 3)

write.csv(as.data.frame(p_mat), "outputs/statistics/pearson_correlation_matrix.csv")
write.csv(as.data.frame(s_mat), "outputs/statistics/spearman_correlation_matrix.csv")

# Convert Spearman matrix to long format for ggplot heatmap
s_df <- as.data.frame(as.table(s_mat))
colnames(s_df) <- c("Var1", "Var2", "Correlation")

fig07 <- ggplot(s_df, aes(x = Var1, y = Var2, fill = Correlation)) +
  geom_tile(color = "white", linewidth = 0.6) +
  geom_text(aes(label = sprintf("%.2f", Correlation)), color = ifelse(abs(s_df$Correlation) > 0.45, "white", "#1A365D"), fontface = "bold", size = 3.6) +
  scale_fill_gradient2(low = "#C53030", mid = "#FFFFFF", high = "#2B6CB0", midpoint = 0, limits = c(-1, 1), name = "Spearman Rho") +
  labs(
    title = "Figure 7: Spearman Rank Correlation Matrix of Continuous Financial Variables",
    subtitle = "Non-parametric rank association highlights robust negative discount-profit relationship (rho = -0.54)",
    x = NULL, y = NULL,
    caption = "Source: Superstore Dataset (2011-2014) | Yuva Intern Final Capstone"
  ) +
  theme_capstone() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

ggsave("figures/exploratory/fig07_correlation_heatmap.png", fig07, width = 7.5, height = 6.2, dpi = 300)
cat("[INFO] Saved: figures/exploratory/fig07_correlation_heatmap.png\n")
cat("[INFO] Stage 4 Visualizations generated successfully.\n\n")
