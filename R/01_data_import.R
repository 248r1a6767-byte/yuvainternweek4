# ==============================================================================
# SCRIPT: 01_data_import.R
# PURPOSE: Data Ingestion, Schema Auditing, and Initial Inspection
# PROJECT: Week 4 Final Capstone - Comprehensive Data Analysis of Superstore Sales
# ==============================================================================

suppressPackageStartupMessages({
  library(dplyr)
  library(readr)
})

cat("[INFO] ------------------------------------------------------------\n")
cat("[INFO] STAGE 1: DATA INGESTION & STRUCTURAL AUDITING\n")
cat("[INFO] ------------------------------------------------------------\n")

raw_path <- "data/raw/superstore_raw.csv"
if (!file.exists(raw_path)) {
  stop("[ERROR] Raw data file not found at: ", raw_path)
}

# Ingest raw dataset
raw_df <- read.csv(raw_path, stringsAsFactors = FALSE, check.names = FALSE)
cat(sprintf("[INFO] Raw data loaded: %d rows x %d columns\n", nrow(raw_df), ncol(raw_df)))

# Audit column names and types
schema_audit <- data.frame(
  Column_Index = 1:ncol(raw_df),
  Variable_Name = colnames(raw_df),
  Raw_Data_Type = sapply(raw_df, class),
  Sample_Value_1 = sapply(raw_df, function(x) as.character(x[1])),
  Sample_Value_2 = sapply(raw_df, function(x) as.character(x[2])),
  Missing_Count = sapply(raw_df, function(x) sum(is.na(x) | x == "" | x == "NA")),
  Unique_Values = sapply(raw_df, function(x) length(unique(x))),
  stringsAsFactors = FALSE
)

# Export schema audit table
write.csv(schema_audit, "outputs/tables/01_raw_schema_audit.csv", row.names = FALSE)
cat("[INFO] Exported: outputs/tables/01_raw_schema_audit.csv\n")

# Capture terminal structure snapshot
sink("screenshots/outputs/01_dataset_structure_output.txt")
cat("================================================================================\n")
cat("SUPERSTORE RAW DATASET STRUCTURE AUDIT (R v4.6.1)\n")
cat("================================================================================\n")
cat(sprintf("Observations (Rows): %d\n", nrow(raw_df)))
cat(sprintf("Variables (Columns): %d\n", ncol(raw_df)))
cat(sprintf("Total Data Cells:    %d\n", nrow(raw_df) * ncol(raw_df)))
cat("--------------------------------------------------------------------------------\n")
str(raw_df)
cat("--------------------------------------------------------------------------------\n")
cat("HEAD (First 3 Records):\n")
print(head(raw_df, 3))
cat("--------------------------------------------------------------------------------\n")
cat("TAIL (Last 3 Records):\n")
print(tail(raw_df, 3))
cat("================================================================================\n")
sink()

cat("[INFO] Exported: screenshots/outputs/01_dataset_structure_output.txt\n")
cat("[INFO] Stage 1 Data Import completed successfully.\n\n")
