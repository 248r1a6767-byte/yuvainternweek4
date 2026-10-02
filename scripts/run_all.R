# ==============================================================================
# MASTER PIPELINE ORCHESTRATOR: run_all.R
# PROJECT: Week 4 Final Capstone - Comprehensive Data Analysis of Superstore Sales
# AUTHOR: Yuva Intern Data Analytics Final Project
# ENVIRONMENT: R Version 4.6.1 (Windows x64)
# ==============================================================================

cat("================================================================================\n")
cat("STARTING SUPERSTORE WEEK 4 FINAL CAPSTONE PIPELINE EXECUTION\n")
cat("================================================================================\n")
cat(sprintf("Execution Start Timestamp: %s\n", Sys.time()))
cat(sprintf("R Version:                  %s\n", R.version.string))
cat(sprintf("Working Directory:          %s\n", getwd()))
cat("================================================================================\n\n")

overall_start_time <- Sys.time()

scripts <- c(
  "R/01_data_import.R",
  "R/02_data_cleaning.R",
  "R/03_exploratory_analysis.R",
  "R/04_visualizations.R",
  "R/05_statistical_analysis.R",
  "R/06_predictive_modeling.R",
  "R/07_model_diagnostics.R",
  "R/08_final_analysis.R"
)

for (s in scripts) {
  if (!file.exists(s)) {
    stop("[FATAL ERROR] Required script missing: ", s)
  }
  cat(sprintf(">>> RUNNING: %s ...\n", s))
  step_start <- Sys.time()
  source(s, local = FALSE)
  step_duration <- round(as.numeric(difftime(Sys.time(), step_start, units = "secs")), 2)
  cat(sprintf(">>> COMPLETED: %s in %.2f seconds.\n\n", s, step_duration))
}

overall_duration <- round(as.numeric(difftime(Sys.time(), overall_start_time, units = "secs")), 2)

cat("================================================================================\n")
cat("SUPERSTORE WEEK 4 FINAL CAPSTONE PIPELINE EXECUTION COMPLETE\n")
cat("================================================================================\n")
cat(sprintf("Total Elapsed Execution Time: %.2f seconds\n", overall_duration))
cat(sprintf("Completion Timestamp:         %s\n", Sys.time()))
cat("All 8 stages executed with 0 fatal errors.\n")
cat("Datasets, tables, figures, models, and diagnostics are fully refreshed.\n")
cat("================================================================================\n")
