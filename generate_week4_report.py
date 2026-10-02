# ==============================================================================
# SCRIPT: generate_week4_report.py
# PURPOSE: Automated Word Report Generator (.docx) for Week 4 Final Capstone
# PROJECT: Comprehensive Data Analysis of Superstore Sales
# AUTHOR: Yuva Intern Data Analytics Final Project
# ==============================================================================

import os
import csv
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def create_report():
    doc = Document()

    # Page setup: Standard Letter, 1-inch margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        section.different_first_page_header_footer = True

        # Header
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("Superstore Comprehensive Data Analysis | Final Capstone Report")
        hrun.font.name = "Calibri"
        hrun.font.size = Pt(8.5)
        hrun.font.color.rgb = RGBColor(113, 128, 150)

        # Footer
        footer = section.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        frun = fp.add_run("Yuva Intern Data Analytics Final Capstone  |  Page ")
        frun.font.name = "Calibri"
        frun.font.size = Pt(9)
        frun.font.color.rgb = RGBColor(113, 128, 150)

        # Add page number XML
        fldSimple = OxmlElement('w:fldSimple')
        fldSimple.set(qn('w:instr'), 'PAGE')
        fp._p.append(fldSimple)

        frun2 = fp.add_run(" of ")
        frun2.font.name = "Calibri"
        frun2.font.size = Pt(9)
        frun2.font.color.rgb = RGBColor(113, 128, 150)

        fldSimple2 = OxmlElement('w:fldSimple')
        fldSimple2.set(qn('w:instr'), 'NUMPAGES')
        fp._p.append(fldSimple2)

    # Styles
    styles = doc.styles
    normal_style = styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(11)
    normal_style.font.color.rgb = RGBColor(45, 55, 72) # #2D3748
    normal_style.paragraph_format.line_spacing = 1.15
    normal_style.paragraph_format.space_after = Pt(6)

    # Helper functions
    def add_h1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = 'Calibri'
        run.font.size = Pt(18)
        run.font.bold = True
        run.font.color.rgb = RGBColor(26, 54, 93) # #1A365D
        return p

    def add_h2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = 'Calibri'
        run.font.size = Pt(13.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(43, 108, 176) # #2B6CB0
        return p

    def add_h3(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = 'Calibri'
        run.font.size = Pt(11.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(44, 122, 123) # #2C7A7B
        return p

    def add_p(text, bold_prefix=None):
        p = doc.add_paragraph()
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.bold = True
            r_pre.font.color.rgb = RGBColor(26, 54, 93)
        p.add_run(text)
        return p

    def add_callout(title, text, color_hex="1A365D"):
        table = doc.add_table(rows=1, cols=1)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.autofit = False
        cell = table.cell(0, 0)
        cell.width = Inches(6.5)

        # Light gray background and colored left border
        shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F7FAFC"/>')
        cell._tc.get_or_add_tcPr().append(shading)

        tcPr = cell._tc.get_or_add_tcPr()
        tcBorders = parse_xml(f'''
            <w:tcBorders {nsdecls("w")}>
                <w:top w:val="none"/>
                <w:left w:val="single" w:sz="24" w:space="0" w:color="{color_hex}"/>
                <w:bottom w:val="none"/>
                <w:right w:val="none"/>
            </w:tcBorders>
        ''')
        tcPr.append(tcBorders)

        cp = cell.paragraphs[0]
        cp.paragraph_format.space_before = Pt(4)
        cp.paragraph_format.space_after = Pt(2)
        r_title = cp.add_run(f"★ {title}\n")
        r_title.bold = True
        r_title.font.size = Pt(11)
        r_title.font.color.rgb = RGBColor(26, 54, 93)

        r_text = cp.add_run(text)
        r_text.font.size = Pt(10)
        r_text.font.color.rgb = RGBColor(45, 55, 72)

        # Empty paragraph for spacing
        p_after = doc.add_paragraph()
        p_after.paragraph_format.space_before = Pt(0)
        p_after.paragraph_format.space_after = Pt(4)

    def add_code(code_str):
        table = doc.add_table(rows=1, cols=1)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.autofit = False
        cell = table.cell(0, 0)
        cell.width = Inches(6.5)

        shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F1F5F9"/>')
        cell._tc.get_or_add_tcPr().append(shading)

        tcPr = cell._tc.get_or_add_tcPr()
        tcBorders = parse_xml(f'''
            <w:tcBorders {nsdecls("w")}>
                <w:top w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
                <w:left w:val="single" w:sz="18" w:space="0" w:color="475569"/>
                <w:bottom w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
                <w:right w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
            </w:tcBorders>
        ''')
        tcPr.append(tcBorders)

        cp = cell.paragraphs[0]
        cp.paragraph_format.space_before = Pt(3)
        cp.paragraph_format.space_after = Pt(3)
        r = cp.add_run(code_str)
        r.font.name = 'Consolas'
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(30, 41, 59)

        p_after = doc.add_paragraph()
        p_after.paragraph_format.space_before = Pt(0)
        p_after.paragraph_format.space_after = Pt(4)

    def add_image_figure(rel_path, caption_num, caption_title, caption_text, width=Inches(6.2)):
        full_path = os.path.join(BASE_DIR, rel_path)
        if not os.path.exists(full_path):
            print(f"[WARN] Image not found: {full_path}")
            return
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(4)
        run_img = p_img.add_run()
        run_img.add_picture(full_path, width=width)

        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(10)
        r_num = p_cap.add_run(f"Figure {caption_num}. {caption_title}: ")
        r_num.bold = True
        r_num.font.size = Pt(9.5)
        r_num.font.color.rgb = RGBColor(26, 54, 93)
        r_txt = p_cap.add_run(caption_text)
        r_txt.font.size = Pt(9.5)
        r_txt.font.italic = True
        r_txt.font.color.rgb = RGBColor(74, 85, 104)

    def add_table_from_csv(rel_path, table_num, table_title, max_rows=18, custom_col_widths=None):
        full_path = os.path.join(BASE_DIR, rel_path)
        if not os.path.exists(full_path):
            print(f"[WARN] Table CSV not found: {full_path}")
            return

        with open(full_path, "r", encoding="utf-8", errors="replace") as f:
            reader = list(csv.reader(f))

        if not reader:
            return

        header = reader[0]
        data_rows = reader[1:max_rows+1]

        p_cap = doc.add_paragraph()
        p_cap.paragraph_format.space_before = Pt(8)
        p_cap.paragraph_format.space_after = Pt(3)
        p_cap.paragraph_format.keep_with_next = True
        r_num = p_cap.add_run(f"Table {table_num}. {table_title}")
        r_num.bold = True
        r_num.font.size = Pt(10)
        r_num.font.color.rgb = RGBColor(26, 54, 93)

        num_cols = len(header)
        num_rows = len(data_rows) + 1
        tbl = doc.add_table(rows=num_rows, cols=num_cols)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False

        # Header formatting
        for j, col_name in enumerate(header):
            cell = tbl.cell(0, j)
            cell.text = col_name
            shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="1A365D"/>')
            cell._tc.get_or_add_tcPr().append(shading)
            cp = cell.paragraphs[0]
            cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
            cp.paragraph_format.space_before = Pt(3)
            cp.paragraph_format.space_after = Pt(3)
            for r in cp.runs:
                r.font.bold = True
                r.font.size = Pt(8.5)
                r.font.color.rgb = RGBColor(255, 255, 255)

        # Data rows formatting
        for i, row in enumerate(data_rows):
            fill_color = "F7FAFC" if i % 2 == 1 else "FFFFFF"
            for j, val in enumerate(row):
                if j >= num_cols:
                    break
                cell = tbl.cell(i + 1, j)
                cell.text = val
                shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_color}"/>')
                cell._tc.get_or_add_tcPr().append(shading)
                cp = cell.paragraphs[0]
                cp.paragraph_format.space_before = Pt(2)
                cp.paragraph_format.space_after = Pt(2)
                # Right align numbers
                if any(char.isdigit() for char in val) and not any(char.isalpha() for char in val) and len(val) < 15:
                    cp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
                else:
                    cp.alignment = WD_ALIGN_PARAGRAPH.LEFT
                for r in cp.runs:
                    r.font.size = Pt(8.0)
                    r.font.color.rgb = RGBColor(45, 55, 72)

        # Widths
        if custom_col_widths and len(custom_col_widths) == num_cols:
            for row in tbl.rows:
                for j, w in enumerate(custom_col_widths):
                    row.cells[j].width = Inches(w)

        # Borders
        for row in tbl.rows:
            for cell in row.cells:
                tcPr = cell._tc.get_or_add_tcPr()
                tcBorders = parse_xml(f'''
                    <w:tcBorders {nsdecls("w")}>
                        <w:top w:val="single" w:sz="4" w:space="0" w:color="CBD5E0"/>
                        <w:left w:val="none"/>
                        <w:bottom w:val="single" w:sz="4" w:space="0" w:color="CBD5E0"/>
                        <w:right w:val="none"/>
                    </w:tcBorders>
                ''')
                tcPr.append(tcBorders)

        p_after = doc.add_paragraph()
        p_after.paragraph_format.space_before = Pt(0)
        p_after.paragraph_format.space_after = Pt(6)

    # ==========================================================================
    # 1. COVER PAGE
    # ==========================================================================
    p_cov_space = doc.add_paragraph()
    p_cov_space.paragraph_format.space_before = Pt(60)

    p_org = doc.add_paragraph()
    r_org = p_org.add_run("YUVA INTERN DATA ANALYTICS INTERNSHIP  |  FINAL CAPSTONE")
    r_org.font.size = Pt(11)
    r_org.font.bold = True
    r_org.font.color.rgb = RGBColor(43, 108, 176)
    p_org.paragraph_format.space_after = Pt(14)

    p_title = doc.add_paragraph()
    r_title = p_title.add_run("Comprehensive Data Analysis of Superstore Sales")
    r_title.font.size = Pt(28)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(26, 54, 93)
    p_title.paragraph_format.space_after = Pt(8)

    p_sub = doc.add_paragraph()
    r_sub = p_sub.add_run("An Integrated End-to-End Investigation Encompassing Data Auditing, Robust Preprocessing, Exploratory Visualization, Inferential Hypothesis Testing, and Cross-Validated Machine Learning in R")
    r_sub.font.size = Pt(13)
    r_sub.font.color.rgb = RGBColor(74, 85, 104)
    p_sub.paragraph_format.space_after = Pt(45)

    # Decorative Rule Table
    rule_tbl = doc.add_table(rows=1, cols=1)
    r_cell = rule_tbl.cell(0, 0)
    r_cell.width = Inches(6.5)
    r_shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="2B6CB0"/>')
    r_cell._tc.get_or_add_tcPr().append(r_shd)
    rule_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    p_r = r_cell.paragraphs[0]
    p_r.paragraph_format.space_before = Pt(2)
    p_r.paragraph_format.space_after = Pt(2)

    p_meta_space = doc.add_paragraph()
    p_meta_space.paragraph_format.space_before = Pt(45)

    meta_items = [
        ("Candidate / Intern:", "Yuva Intern Data Science & Analytics Specialist"),
        ("Project Scope:", "Week 4 Final Capstone Project (Weeks 1 - 4 Synthesis)"),
        ("Technical Ecosystem:", "R (v4.6.1), RStudio, tidyverse, ggplot2, randomForest, glmnet, car"),
        ("Benchmark Dataset:", "Tableau / Kaggle Sample Superstore Sales (9,994 Records, 21 Attributes)"),
        ("Publication Date:", "October 2026"),
        ("Repository Status:", "Fully Reproducible, Automated Execution Manifest, Zero Leakage Protocol")
    ]

    for label, val in meta_items:
        p_m = doc.add_paragraph()
        p_m.paragraph_format.space_after = Pt(3)
        r_l = p_m.add_run(f"{label:<24} ")
        r_l.bold = True
        r_l.font.color.rgb = RGBColor(26, 54, 93)
        r_v = p_m.add_run(val)
        r_v.font.color.rgb = RGBColor(45, 55, 72)

    doc.add_page_break()

    # ==========================================================================
    # 2. TABLE OF CONTENTS, FIGURES & TABLES
    # ==========================================================================
    add_h1("Table of Contents")
    toc_entries = [
        ("Executive Summary", "3"),
        ("1. Introduction & Analytical Purpose", "5"),
        ("2. Business and Data Context", "6"),
        ("3. Dataset Description & Comprehensive Data Dictionary", "7"),
        ("4. Data Preparation, Sanitization & Feature Engineering", "9"),
        ("5. Exploratory Data Analysis & Moment Profiling", "11"),
        ("6. Data Visualization Framework (What? So What? Now What?)", "13"),
        ("7. Longitudinal Temporal Analysis & Seasonal Revenue Growth", "15"),
        ("8. Product Portfolio Performance & Sub-Category Divergence", "17"),
        ("9. Customer Segment & Order Fulfillment Dynamics", "19"),
        ("10. Geographic Regional Financial Matrix", "21"),
        ("11. Promotional Discounting & Empirical Margin Collapse", "23"),
        ("12. Statistical Correlation Analysis & Parametric Audits", "25"),
        ("13. Formal Inferential Hypothesis Testing Suite", "27"),
        ("14. Predictive Modeling Methodology & Regression Architecture", "30"),
        ("15. Cross-Validation & Out-of-Sample Holdout Evaluation", "33"),
        ("16. Model Interpretation & Permutation Feature Importance", "35"),
        ("17. Integrated Findings: Visualization, Statistics & Machine Learning", "37"),
        ("18. Ten Core Evidence-Based Business Insights", "39"),
        ("19. Strategic Business Implications & Prioritized Recommendations", "41"),
        ("20. Analytical Challenges Encountered & Technical Resolutions", "43"),
        ("21. Professional Lessons Learned & Analytical Reflections", "45"),
        ("22. Methodological & Observational Data Limitations", "47"),
        ("23. Future Research & Advanced Analytics Roadmap", "48"),
        ("24. Final Synthesis & Capstone Conclusion", "49"),
        ("25. Academic & Professional References", "50"),
        ("26. Appendix A: Complete Reproducible R Scripts", "51"),
        ("27. Appendix B: System Execution Manifest & Output Captures", "55")
    ]

    for title, pg in toc_entries:
        p_t = doc.add_paragraph()
        p_t.paragraph_format.space_after = Pt(2)
        r1 = p_t.add_run(title)
        r1.font.size = Pt(10)
        r1.font.color.rgb = RGBColor(45, 55, 72)
        # Leader dots
        dots_count = max(2, 75 - len(title))
        r_dots = p_t.add_run(" " + "." * dots_count + " ")
        r_dots.font.color.rgb = RGBColor(160, 174, 192)
        r_pg = p_t.add_run(pg)
        r_pg.bold = True
        r_pg.font.color.rgb = RGBColor(26, 54, 93)

    add_h2("List of Figures")
    fig_entries = [
        ("Figure 1", "Empirical Distribution Profiles of Transaction Sales and Profit", "12"),
        ("Figure 2", "Longitudinal Monthly Sales and Profit Trajectory (2011 - 2014)", "16"),
        ("Figure 3", "Cumulative Profitability Across 17 Product Sub-Categories", "18"),
        ("Figure 4", "Regional Multi-Dimensional Financial Performance Matrix", "22"),
        ("Figure 5", "Sales Distribution by Customer Segment and Shipping Class", "20"),
        ("Figure 6", "Empirical Profit Destruction Under Deep Promotional Discounting", "24"),
        ("Figure 7", "Spearman Rank Correlation Matrix of Continuous Financial Variables", "26"),
        ("Figure 8", "Empirical Evidence Panels for Four Core Hypothesis Tests", "29"),
        ("Figure 9", "Predictive Model Cross-Validation and Holdout Test Set Performance", "34"),
        ("Figure 10", "Random Forest Permutation Variable Importance (%IncMSE)", "36"),
        ("Figure 11", "Four-Panel Classical OLS Regression Diagnostics", "32"),
        ("Figure 12", "Actual vs. Predicted Profit on Holdout Test Set (N = 1,999)", "34"),
        ("Figure 13", "Holdout Test Set Residual Error Distribution & Category Profiling", "35"),
        ("Figure 14", "Executive Capstone Multi-Panel Dashboard & Enterprise KPI Summary", "4")
    ]
    for num, title, pg in fig_entries:
        p_f = doc.add_paragraph()
        p_f.paragraph_format.space_after = Pt(2)
        r_f1 = p_f.add_run(f"{num}: {title}")
        r_f1.font.size = Pt(9.5)
        dots_count = max(2, 70 - len(f"{num}: {title}"))
        r_dots = p_f.add_run(" " + "." * dots_count + " ")
        r_dots.font.color.rgb = RGBColor(160, 174, 192)
        r_f2 = p_f.add_run(pg)
        r_f2.bold = True
        r_f2.font.color.rgb = RGBColor(26, 54, 93)

    add_h2("List of Tables")
    tbl_entries = [
        ("Table 1", "Superstore Raw Dataset Schema & Structural Audit", "8"),
        ("Table 2", "Comprehensive Master Data Dictionary (21 Attributes)", "8"),
        ("Table 3", "Data Quality & Cleaning Operations Decision Log", "10"),
        ("Table 4", "Empirical Missingness Audit Across All Cells", "10"),
        ("Table 5", "Parametric & Non-Parametric Descriptive Moments Summary", "11"),
        ("Table 6", "Category Financial Performance & Loss Rate Breakdown", "17"),
        ("Table 7", "Sub-Category Cumulative Sales, Profit, and Profit Margins", "18"),
        ("Table 8", "Geographic Regional Performance & Loss Incidence Matrix", "21"),
        ("Table 9", "Customer Segment Contribution & Average Order Value", "19"),
        ("Table 10", "Promotional Discount Band Distribution & Margin Collapse", "23"),
        ("Table 11", "Annual Year-Over-Year Sales and Profit Growth Trajectory", "15"),
        ("Table 12", "Pearson Product-Moment Correlation Matrix", "25"),
        ("Table 13", "Spearman Rank-Order Correlation Matrix", "26"),
        ("Table 14", "Consolidated Master Inferential Hypothesis Testing Results", "28"),
        ("Table 15", "Regional Loss Incidence Contingency Matrix", "28"),
        ("Table 16", "Post-Hoc Tukey HSD Pairwise Category Profit Comparisons", "29"),
        ("Table 17", "Cross-Validation and Holdout Test Set Performance Master Table", "33"),
        ("Table 18", "Random Forest Permutation Feature Importance Profile", "36"),
        ("Table 19", "Forensic Audit of Top 15 Out-of-Sample Prediction Errors", "35"),
        ("Table 20", "Category-Level Out-of-Sample Holdout Error Breakdown", "35"),
        ("Table 21", "Capstone End-to-End Pipeline Execution Manifest", "55")
    ]
    for num, title, pg in tbl_entries:
        p_t = doc.add_paragraph()
        p_t.paragraph_format.space_after = Pt(2)
        r_t1 = p_t.add_run(f"{num}: {title}")
        r_t1.font.size = Pt(9.5)
        dots_count = max(2, 70 - len(f"{num}: {title}"))
        r_dots = p_t.add_run(" " + "." * dots_count + " ")
        r_dots.font.color.rgb = RGBColor(160, 174, 192)
        r_t2 = p_t.add_run(pg)
        r_t2.bold = True
        r_t2.font.color.rgb = RGBColor(26, 54, 93)

    doc.add_page_break()

    # ==========================================================================
    # 3. EXECUTIVE SUMMARY
    # ==========================================================================
    add_h1("Executive Summary")
    add_p(
        "This capstone report represents the culmination of a four-week intensive data science and business analytics internship. "
        "The overarching mission is to transform transactional retail data from the Tableau / Kaggle Sample Superstore dataset into an "
        "evidence-based, publication-grade analytical investigation. Rather than presenting four disconnected weekly assignments, this report "
        "synthesizes the analytical continuum: establishing structural data integrity (Week 1), communicating multidimensional insights through "
        "publication-quality data visualizations (Week 2), executing formal inferential hypothesis testing and predictive machine learning (Week 3), "
        "and integrating these diverse empirical strands into actionable corporate intelligence (Week 4)."
    )
    add_p(
        "The commercial investigation spans 9,994 line-item transactions executed between January 4, 2011, and December 31, 2014, across 49 US states. "
        "Over this four-year observation window, Superstore generated $2,297,200.86 in gross revenue and accumulated $286,397.02 in operating profit, "
        "reflecting an enterprise-wide profit margin of 12.47%. However, macroscopic profitability masks severe operational vulnerabilities: "
        "1,871 transactions (18.72% of all line items) resulted in negative net margins, cumulatively destroying substantial commercial capital."
    )

    add_image_figure(
        "figures/executive_summary/fig14_executive_dashboard_summary.png",
        14, "Executive Capstone Multi-Panel Dashboard & Enterprise KPI Summary",
        "Enterprise financial performance scorecard, longitudinal growth trajectory, category margin distribution, promotional cliff threshold, and regional profit contributions."
    )

    add_callout(
        "EXECUTIVE BOTTOM LINE & STRATEGIC HIGHLIGHTS",
        "1. Promotional Discount Destruction: Unconstrained discounting (>20%) is the single largest driver of capital loss. Orders discounted beyond 20% experience an average profit margin collapse to -41.8%, costing the firm over $90,000 in lost gross margin.\n"
        "2. Merchandise Divergence: Technology drives $145.5k in profit (17.4% margin) led by Copiers ($55.6k), whereas Furniture generates only $18.5k (2.5% margin) due to catastrophic losses in Tables (-$17.7k) and Bookcases (-$3.5k).\n"
        "3. Regional Disparity: The Central region suffers from an elevated loss rate of 31.9% (vs 9.9% in the West), generating only $39.7k profit despite $501.2k in revenue.\n"
        "4. Machine Learning Champion: An ensemble Random Forest regressor achieved a Holdout Test R² of 78.45% (Test RMSE = $119.16, MAE = $26.66), outperforming classical OLS regression by resolving sharp non-linear discount cliffs."
    )

    doc.add_page_break()

    # ==========================================================================
    # 4. SECTION 1: INTRODUCTION & PURPOSE
    # ==========================================================================
    add_h1("1. Introduction & Analytical Purpose")
    add_p(
        "In modern multi-channel retail enterprises, commercial success requires rigorous data-driven decision-making. "
        "Organizations frequently accumulate massive repositories of transactional records but struggle to synthesize raw operational data "
        "into clear strategic direction. Common corporate pitfalls include treating top-line revenue growth as a proxy for profitability, "
        "deploying across-the-board promotional discounting without quantifying price elasticity, and failing to detect structural margin bleed across product hierarchies."
    )
    add_p(
        "The purpose of this capstone research is to demonstrate an integrated, reproducible analytics lifecycle using the statistical programming language R (v4.6.1). "
        "Specifically, the project addresses the core question: How can Superstore sales data be analyzed through data cleaning, visualization, statistical testing, "
        "and predictive modeling to identify meaningful sales and profitability patterns and communicate actionable business insights?"
    )
    add_p(
        "To achieve this objective, the analytical inquiry is governed by ten targeted business questions:",
        bold_prefix="Core Analytical Questions: "
    )
    b_questions = [
        "Q1. Temporal Dynamics: How do sales and profit evolve longitudinally, and what seasonal surges characterize the retail calendar?",
        "Q2. Category Revenue Generation: Which product categories and sub-categories generate the greatest top-line commercial revenue?",
        "Q3. Category Profitability: Which product categories yield the highest net margins, and which sub-categories destroy capital?",
        "Q4. Regional Performance: How do geographic territories diverge in sales volume, operating margin, and operational loss incidence?",
        "Q5. Customer Segmentation: How do purchasing behavior, basket size, and fulfillment class differ across Consumer, Corporate, and Home Office clients?",
        "Q6. Promotional Discount Elasticity: How does promotional discounting relate empirically to line-item profit and gross margin sustainability?",
        "Q7. Extreme Line-Item Losses: Which specific products contribute disproportionately to enterprise capital destruction?",
        "Q8. Inferential Group Differences: Are observed differences in profit across discount tiers and merchandise categories statistically significant?",
        "Q9. Regional Dependence: Is the probability of incurring a transaction loss statistically dependent on geographic sales territory?",
        "Q10. Predictive Modeling: Can future transaction profitability be predicted out-of-sample using accessible operational predictors, and what model architecture best resolves non-linear retail dynamics?"
    ]
    for bq in b_questions:
        add_p(bq)

    # ==========================================================================
    # 5. SECTION 2: BUSINESS AND DATA CONTEXT
    # ==========================================================================
    add_h1("2. Business and Data Context")
    add_p(
        "The Superstore sales dataset reflects the operational footprint of a national corporate supplier operating within the United States. "
        "The business model encompasses a B2B and B2C commercial retail model, servicing individual consumers, small-to-medium businesses (Corporate), "
        "and residential professionals (Home Office). Transactions originate across four major geographic divisions: West, East, Central, and South, spanning 49 states."
    )
    add_p(
        "The merchandise catalog is structured hierarchically across three broad sectors: Furniture, Office Supplies, and Technology. "
        "These sectors are further segmented into 17 specialized sub-categories ranging from high-turnover commodity consumables (Paper, Binders, Labels) "
        "to high-value commercial capital equipment (Copiers, Machines, Phones) and bulky office furnishings (Chairs, Tables, Bookcases, Furnishings)."
    )
    add_p(
        "Operational fulfillment is handled through four contracted shipping classes: Standard Class (representing the economical volume baseline), "
        "Second Class, First Class, and Same Day courier delivery. The commercial transaction flow is recorded at the line-item level: each unique Order ID "
        "may encompass multiple product purchases, each carrying its own pricing, quantity, promotional discount, and realized profit."
    )

    # ==========================================================================
    # 6. SECTION 3: DATASET DESCRIPTION & COMPREHENSIVE DATA DICTIONARY
    # ==========================================================================
    add_h1("3. Dataset Description & Comprehensive Data Dictionary")
    add_p(
        "The primary data asset analyzed is the Superstore Sales Dataset obtained from the Tableau / Kaggle public benchmark repository. "
        "The dataset represents an observational transaction log containing exactly 9,994 rows and 21 raw variables, encompassing 209,874 total data cells. "
        "The observation window extends from January 4, 2011, through December 31, 2014, capturing four complete calendar years of trading activity."
    )

    add_table_from_csv("outputs/tables/01_raw_schema_audit.csv", 1, "Superstore Raw Dataset Schema & Structural Audit", max_rows=21, custom_col_widths=[0.6, 1.3, 1.0, 1.1, 1.1, 0.7, 0.7])

    add_p(
        "To ensure precise analytical traceability, Table 2 documents the master data dictionary, defining the business meaning, data type, "
        "and analytical role of all primary variables present in the cleaned dataset."
    )

    # Master Data Dictionary Table
    dict_headers = ["Variable", "Data Type", "Business Meaning", "Analytical Role", "Missing", "Example"]
    dict_rows = [
        ["Order_ID", "Character", "Unique commercial transaction identifier", "Primary Key / Grouping", "0 (0%)", "CA-2013-152156"],
        ["Order_Date", "Date", "Date purchase order was officially authorized", "Temporal Independent Var", "0 (0%)", "2013-11-09"],
        ["Ship_Date", "Date", "Date order was dispatched from fulfillment center", "Fulfillment Latency", "0 (0%)", "2013-11-13"],
        ["Ship_Mode", "Factor", "Logistical delivery tier (Standard, Second, First, Same Day)", "Logistical Predictor", "0 (0%)", "Second Class"],
        ["Customer_ID", "Character", "Unique customer account identifier", "Customer Dimension", "0 (0%)", "CG-12520"],
        ["Customer_Name", "Character", "Full legal name of purchasing client", "Descriptive Attribute", "0 (0%)", "Claire Gute"],
        ["Segment", "Factor", "Client market classification (Consumer, Corporate, Home Office)", "Segmentation Predictor", "0 (0%)", "Consumer"],
        ["Country", "Character", "Country of commercial transaction (United States)", "Constant Geographic Field", "0 (0%)", "United States"],
        ["City", "Character", "Municipality of delivery destination", "Spatial Dimension", "0 (0%)", "Henderson"],
        ["State", "Character", "US State of delivery destination (49 states recorded)", "Regional Spatial Unit", "0 (0%)", "Kentucky"],
        ["Postal_Code", "Character", "Standardized 5-digit US ZIP postal code (padded)", "GIS Spatial Attribute", "0 (0%)", "42420"],
        ["Region", "Factor", "Geographic management division (Central, East, South, West)", "Territorial Predictor", "0 (0%)", "South"],
        ["Product_ID", "Character", "Unique merchandise stock-keeping SKU code", "Catalog Dimension", "0 (0%)", "FUR-BO-10001798"],
        ["Category", "Factor", "Broad merchandise sector (Furniture, Office Supplies, Technology)", "Categorical Predictor", "0 (0%)", "Furniture"],
        ["Sub_Category", "Factor", "Granular merchandise classification (17 sub-types)", "High-Importance Predictor", "0 (0%)", "Bookcases"],
        ["Product_Name", "Character", "Full retail commercial description of merchandise item", "Descriptive Attribute", "0 (0%)", "Bush Somerset Bookcase"],
        ["Sales", "Numeric", "Gross transaction revenue realized ($ USD)", "Continuous Predictor", "0 (0%)", "261.96"],
        ["Quantity", "Integer", "Total units purchased in line item", "Volume Predictor", "0 (0%)", "2"],
        ["Discount", "Numeric", "Promotional discount percentage applied (0.00 to 0.80)", "Continuous Predictor", "0 (0%)", "0.00"],
        ["Profit", "Numeric", "Net operating profit realized on line item ($ USD)", "PRIMARY MODEL TARGET", "0 (0%)", "41.9136"],
        ["Shipping_Days", "Integer", "Fulfillment latency in calendar days (Ship Date - Order Date)", "Engineered Operational Var", "0 (0%)", "4"]
    ]

    p_dict = doc.add_paragraph()
    p_dict.paragraph_format.space_before = Pt(8)
    p_dict.paragraph_format.space_after = Pt(3)
    p_dict.paragraph_format.keep_with_next = True
    r_dn = p_dict.add_run("Table 2. Comprehensive Master Data Dictionary (21 Variables)")
    r_dn.bold = True
    r_dn.font.size = Pt(10)
    r_dn.font.color.rgb = RGBColor(26, 54, 93)

    t_dict = doc.add_table(rows=len(dict_rows)+1, cols=6)
    t_dict.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_dict.autofit = False

    for j, h in enumerate(dict_headers):
        cell = t_dict.cell(0, j)
        cell.text = h
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="1A365D"/>')
        cell._tc.get_or_add_tcPr().append(shd)
        cp = cell.paragraphs[0]
        cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cp.runs[0].font.bold = True
        cp.runs[0].font.size = Pt(8.5)
        cp.runs[0].font.color.rgb = RGBColor(255, 255, 255)

    widths = [1.1, 0.8, 1.8, 1.3, 0.6, 0.9]
    for i, row in enumerate(dict_rows):
        fill = "F7FAFC" if i % 2 == 1 else "FFFFFF"
        for j, val in enumerate(row):
            cell = t_dict.cell(i+1, j)
            cell.text = val
            shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill}"/>')
            cell._tc.get_or_add_tcPr().append(shd)
            cp = cell.paragraphs[0]
            cp.runs[0].font.size = Pt(8.0)
            cp.runs[0].font.color.rgb = RGBColor(45, 55, 72)

    for row in t_dict.rows:
        for j, w in enumerate(widths):
            row.cells[j].width = Inches(w)
            tcPr = row.cells[j]._tc.get_or_add_tcPr()
            tcBorders = parse_xml(f'''
                <w:tcBorders {nsdecls("w")}>
                    <w:top w:val="single" w:sz="4" w:space="0" w:color="CBD5E0"/>
                    <w:left w:val="none"/>
                    <w:bottom w:val="single" w:sz="4" w:space="0" w:color="CBD5E0"/>
                    <w:right w:val="none"/>
                </w:tcBorders>
            ''')
            tcPr.append(tcBorders)

    doc.add_page_break()

    # ==========================================================================
    # 7. SECTION 4: DATA PREPARATION AND CLEANING
    # ==========================================================================
    add_h1("4. Data Preparation, Sanitization & Feature Engineering")
    add_p(
        "Data quality is the bedrock of valid statistical inference and reliable predictive modeling. "
        "During Phase 9 of the project lifecycle, the data engineering pipeline established in Week 1 was fully audited, "
        "hardened, and integrated. Table 3 delineates the seven critical data preparation operations executed on the raw ingestion layer."
    )

    add_table_from_csv("outputs/tables/02_cleaning_actions_log.csv", 3, "Data Quality & Cleaning Operations Decision Log", max_rows=7, custom_col_widths=[0.4, 1.8, 1.4, 1.4, 1.5])

    add_p(
        "A primary concern in retail data auditing is identifying incomplete records. Table 4 presents the empirical missingness audit, "
        "confirming that the Superstore dataset exhibits 100% empirical completeness across all 209,874 cells (0 missing values, 0 blank strings). "
        "Similarly, duplicate record auditing confirmed 0 exact duplicate rows. While certain Order IDs appear across multiple rows, "
        "these reflect multi-item baskets rather than erroneous duplication."
    )

    add_table_from_csv("outputs/tables/02_missingness_audit.csv", 4, "Empirical Missingness Audit Across All Cells", max_rows=22, custom_col_widths=[1.5, 1.2, 1.5, 1.5])

    add_p(
        "To enable temporal, financial, and logistical analysis, several analytical features were engineered in R:",
        bold_prefix="Engineered Feature Set: "
    )
    add_code(
        "# Excerpt from R/02_data_cleaning.R\n"
        "df <- df %>%\n"
        "  mutate(\n"
        "    Order_Year       = as.integer(format(Order_Date, '%Y')),\n"
        "    Order_Month      = as.integer(format(Order_Date, '%m')),\n"
        "    Order_Quarter    = paste0('Q', ceiling(Order_Month / 3)),\n"
        "    Shipping_Days    = as.integer(Ship_Date - Order_Date),\n"
        "    Profit_Margin    = ifelse(Sales > 0, Profit / Sales, 0),\n"
        "    Loss_Making_Flag = ifelse(Profit < 0, 1L, 0L),\n"
        "    Discount_Band    = case_when(\n"
        "      Discount == 0    ~ '0% (None)',\n"
        "      Discount <= 0.20 ~ '1%-20% (Low/Moderate)',\n"
        "      TRUE             ~ '>20% (Deep Promotional)'\n"
        "    )\n"
        "  )"
    )

    add_image_figure(
        "screenshots/outputs/card02_data_cleaning.png",
        "Card 2", "R Console Execution Snapshot: Data Cleaning & Feature Transformation",
        "Terminal output verifying zero missing cells, zero exact duplicates, date range span, and feature summaries.",
        width=Inches(6.0)
    )

    doc.add_page_break()

    # ==========================================================================
    # 8. SECTION 5: EXPLORATORY DATA ANALYSIS
    # ==========================================================================
    add_h1("5. Exploratory Data Analysis & Moment Profiling")
    add_p(
        "Exploratory data analysis began with parametric and non-parametric moment profiling of all continuous numerical attributes. "
        "Table 5 outlines sample size (N), mean, standard deviation (SD), median, interquartile range (IQR), minimum, maximum, "
        "Fisher-Pearson skewness, and excess kurtosis across the six primary continuous variables."
    )

    add_table_from_csv("outputs/tables/03_numerical_descriptive_stats.csv", 5, "Parametric & Non-Parametric Descriptive Moments Summary", max_rows=6, custom_col_widths=[1.2, 0.5, 0.7, 0.7, 0.6, 0.6, 0.6, 0.7, 0.7, 0.8])

    add_p(
        "Descriptive statistics reveal extreme distributional properties that fundamentally govern all downstream modeling: "
        "Transaction Sales displays severe positive skewness (Skewness = 12.97, Kurtosis = 304.45), with a mean of $229.86 and a median of $54.49. "
        "Similarly, Transaction Profit exhibits extreme heavy-tailed leptokurtosis (Kurtosis = 286.77) with values spanning from -$6,599.98 to +$8,399.98. "
        "The standard deviation of Profit ($234.26) exceeds the mean ($28.66) by a factor of eight, indicating substantial volatility."
    )

    add_image_figure(
        "figures/exploratory/fig01_sales_profit_distributions.png",
        1, "Empirical Distribution Profiles of Transaction Sales and Profit",
        "Panel A presents the log-scaled Sales distribution highlighting extreme right-skew. Panel B depicts the central Profit distribution (-$1k to +$1k) with dashed red line indicating the break-even threshold."
    )

    add_callout(
        "METHODOLOGICAL LESSON: NON-NORMALITY & LEPTOCURTOSIS",
        "Because Sales and Profit severely violate Gaussian normality assumptions (p < 0.0001), standard parametric methods relying on normality must be interpreted cautiously. Welch's unpooled t-tests and non-parametric rank tests (Spearman rho) are mandated to prevent spurious inferences."
    )

    doc.add_page_break()

    # ==========================================================================
    # 9. SECTION 6: DATA VISUALIZATION FRAMEWORK
    # ==========================================================================
    add_h1("6. Data Visualization Framework (What? So What? Now What?)")
    add_p(
        "To ensure that visual analytics communicate actionable insights rather than merely displaying decorative graphics, "
        "every major visualization in this capstone adheres to a structured three-tier interpretive framework: "
        "WHAT (Empirical description of patterns, peaks, and spreads), SO WHAT (Strategic business meaning and operational impact), "
        "and NOW WHAT (Analytical implications, operational interventions, and policy adjustments)."
    )
    add_p(
        "All visualizations were rendered using R's ggplot2 engine under a unified corporate design standard: "
        "a clean minimalist layout (theme_capstone), high-contrast accessible color palette (Navy #1A365D, Slate Blue #2B6CB0, Deep Teal #2C7A7B, "
        "Amber #DD6B20, and Coral #C53030), standardized typography, descriptive subtitles, and explicit source attribution."
    )

    # ==========================================================================
    # 10. SECTION 7: TEMPORAL ANALYSIS
    # ==========================================================================
    add_h1("7. Longitudinal Temporal Analysis & Seasonal Revenue Growth")
    add_p(
        "Longitudinal analysis of the Superstore dataset reveals sustained top-line revenue expansion coupled with pronounced annual seasonality. "
        "Table 11 tracks annual performance from 2011 to 2014, showing that annual sales grew from $484,247.50 to $733,215.26 (a 51.4% expansion), "
        "while annual profit expanded from $49,543.97 to $93,439.27 (an 88.6% increase)."
    )

    add_table_from_csv("outputs/tables/03_yearly_growth_summary.csv", 11, "Annual Year-Over-Year Sales and Profit Growth Trajectory", max_rows=4, custom_col_widths=[1.0, 1.0, 1.1, 1.1, 1.1, 1.2])

    add_image_figure(
        "figures/exploratory/fig02_monthly_sales_profit_trends.png",
        2, "Longitudinal Monthly Sales and Profit Trajectory (2011 - 2014)",
        "Dual-axis time series depicting monthly revenue (blue) and scaled profit (teal), highlighting recurring fourth-quarter commercial surges."
    )

    add_callout(
        "TEMPORAL NARRATIVE: WHAT? SO WHAT? NOW WHAT?",
        "• WHAT: Monthly sales exhibit a recurring seasonal cycle: Q1 starts modestly (averaging $35k/month in January-February), steadily builds through summer, and peaks dramatically in Q4 (averaging $85k/month in November-December).\n"
        "• SO WHAT: The retail business generates over 35% of its annual sales and 38% of its annual profit during the final three months of the year, driven by holiday promotional demand and corporate budget exhaustion.\n"
        "• NOW WHAT: Supply chain planning must aggressively align warehouse inventory, staffing, and freight capacity between August and October to prevent fulfillment bottlenecks during the Q4 peak."
    )

    doc.add_page_break()

    # ==========================================================================
    # 11. SECTION 8: PRODUCT PORTFOLIO ANALYSIS
    # ==========================================================================
    add_h1("8. Product Portfolio Performance & Sub-Category Divergence")
    add_p(
        "A critical finding of this investigation is the dramatic profitability divergence across merchandise categories. "
        "While all three categories generate comparable sales volume ($719k to $836k), their profit contribution is highly asymmetric. "
        "Table 6 breaks down financial performance by product category."
    )

    add_table_from_csv("outputs/tables/03_category_performance_summary.csv", 6, "Category Financial Performance & Loss Rate Breakdown", max_rows=3, custom_col_widths=[1.2, 0.7, 0.9, 0.9, 0.9, 0.8, 0.8, 0.7])

    add_image_figure(
        "figures/exploratory/fig03_category_subcategory_performance.png",
        3, "Cumulative Profitability Across 17 Product Sub-Categories",
        "Horizontal ranking of cumulative profit by sub-category, highlighting the stark contrast between Technology cash generators (Copiers, Phones) and Furniture capital destructors (Tables, Bookcases)."
    )

    add_p(
        "Table 7 presents the complete sub-category ranking. Technology's superior performance is anchored by Copiers ($55,617.82 profit, 36.6% margin), "
        "Phones ($44,515.73), and Accessories ($41,936.63). Conversely, Furniture is dragged down by Tables, which accumulated a staggering -$17,725.48 loss "
        "across 319 transactions, and Bookcases (-$3,472.56)."
    )

    add_table_from_csv("outputs/tables/03_subcategory_performance_summary.csv", 7, "Sub-Category Cumulative Sales, Profit, and Profit Margins", max_rows=17, custom_col_widths=[1.2, 1.2, 0.7, 1.0, 1.0, 0.8, 0.8])

    doc.add_page_break()

    # ==========================================================================
    # 12. SECTION 9: CUSTOMER & SEGMENT BEHAVIOR
    # ==========================================================================
    add_h1("9. Customer Segment & Order Fulfillment Dynamics")
    add_p(
        "Customer segmentation analysis indicates that Superstore services three distinct customer clienteles: Consumer, Corporate, and Home Office. "
        "Table 9 demonstrates that while Consumer clients represent the majority of volume (5,191 order lines, $1.16M sales, 50.5% share), "
        "profit margins are remarkably consistent across segments: Consumer (11.53%), Corporate (13.00%), and Home Office (13.79%)."
    )

    add_table_from_csv("outputs/tables/03_segment_performance_summary.csv", 9, "Customer Segment Contribution & Average Order Value", max_rows=3, custom_col_widths=[1.2, 0.9, 1.1, 0.9, 1.1, 0.9, 0.9])

    add_image_figure(
        "figures/exploratory/fig05_segment_shipping_dynamics.png",
        5, "Sales Distribution by Customer Segment and Shipping Class",
        "Faceted bar chart showing volume concentration in Standard Class across Consumer, Corporate, and Home Office client segments."
    )

    # ==========================================================================
    # 13. SECTION 10: GEOGRAPHIC REGIONAL ANALYSIS
    # ==========================================================================
    add_h1("10. Geographic Regional Financial Matrix")
    add_p(
        "Superstore's operations span four major administrative regions. Table 8 demonstrates substantial geographic heterogeneity: "
        "The West region leads in both revenue ($725,457.82) and profitability ($108,418.45), achieving a healthy 14.95% profit margin. "
        "In contrast, the Central region generates $501,239.89 in sales but realizes only $39,706.32 in profit (7.92% margin)—the lowest in the company."
    )

    add_table_from_csv("outputs/tables/03_regional_performance_summary.csv", 8, "Geographic Regional Performance & Loss Incidence Matrix", max_rows=4, custom_col_widths=[1.0, 0.8, 1.0, 0.9, 1.0, 0.9, 0.9, 0.9])

    add_image_figure(
        "figures/exploratory/fig04_regional_performance_matrix.png",
        4, "Regional Multi-Dimensional Financial Performance Matrix",
        "Four-panel dashboard comparing Regional Sales, Cumulative Profit, Operating Margin %, and Transaction Loss Rate %."
    )

    add_callout(
        "GEOGRAPHIC INSIGHT: THE CENTRAL REGION DILEMMA",
        "The Central region exhibits a staggering 31.90% loss rate (741 out of 2,323 line items lost money). This elevated loss frequency is directly attributable to uncurbed promotional discounting in states such as Texas (where median discounts exceed 30%), demonstrating that decentralized regional discount authority can severely erode corporate capital."
    )

    doc.add_page_break()

    # ==========================================================================
    # 14. SECTION 11: DISCOUNTING & PROFITABILITY EROSION
    # ==========================================================================
    add_h1("11. Promotional Discounting & Empirical Margin Collapse")
    add_p(
        "The single most impactful finding of this capstone research is the destructive nature of promotional discounting. "
        "Retail management frequently utilizes price markdowns to stimulate unit velocity under the assumption that volume compensates for lower margin. "
        "Table 10 and Figure 6 provide conclusive empirical refutation of this hypothesis for the Superstore business model."
    )

    add_table_from_csv("outputs/tables/03_discount_band_summary.csv", 10, "Promotional Discount Band Distribution & Margin Collapse", max_rows=3, custom_col_widths=[1.5, 0.8, 0.8, 1.0, 1.0, 0.9, 0.9])

    add_image_figure(
        "figures/exploratory/fig06_discount_vs_profit_cliff.png",
        6, "Empirical Profit Destruction Under Deep Promotional Discounting",
        "Scatter plot with LOESS regression curve demonstrating the catastrophic 20% discount cliff where median profitability collapses below zero."
    )

    add_callout(
        "THE 20% PROMOTIONAL CLIFF",
        "• 0% Discount: Generates $66.90 mean profit per order with a 30.1% margin (Loss rate: 0.0%).\n"
        "• 1% - 20% Discount: Yields $34.22 mean profit with a 17.2% margin (Loss rate: 9.8%).\n"
        "• >20% Discount: Median profit plummets to -$62.58, with average margin collapsing to -41.8% (Loss rate: 58.4%). Over 2,100 orders fall into this destructive tier."
    )

    doc.add_page_break()

    # ==========================================================================
    # 15. SECTION 12: STATISTICAL CORRELATION ANALYSIS
    # ==========================================================================
    add_h1("12. Statistical Correlation Analysis & Parametric Audits")
    add_p(
        "To evaluate bivariate associations while accounting for non-normality, both Pearson product-moment and Spearman rank-order correlation "
        "matrices were computed across all continuous variables. Tables 12 and 13 present the resulting correlation coefficients."
    )

    add_table_from_csv("outputs/statistics/pearson_correlation_matrix.csv", 12, "Pearson Product-Moment Correlation Matrix", max_rows=6, custom_col_widths=[1.2, 0.8, 0.8, 0.8, 0.8, 0.9, 0.9])
    add_table_from_csv("outputs/statistics/spearman_correlation_matrix.csv", 13, "Spearman Rank-Order Correlation Matrix", max_rows=6, custom_col_widths=[1.2, 0.8, 0.8, 0.8, 0.8, 0.9, 0.9])

    add_image_figure(
        "figures/exploratory/fig07_correlation_heatmap.png",
        7, "Spearman Rank Correlation Matrix of Continuous Financial Variables",
        "Heatmap visualization illustrating monotonic associations between financial variables, emphasizing the robust negative discount-profit link."
    )

    add_p(
        "Crucially, while Pearson correlation between Discount and Profit is modest (r = -0.064) due to extreme outliers and non-linearities, "
        "Spearman's rank correlation reveals a powerful, highly significant monotonic inverse relationship (rho = -0.5434, p < 0.0001). "
        "This confirms that higher promotional discounts systematically degrade relative transaction profitability."
    )

    # ==========================================================================
    # 16. SECTION 13: FORMAL HYPOTHESIS TESTING
    # ==========================================================================
    add_h1("13. Formal Inferential Hypothesis Testing Suite")
    add_p(
        "To establish rigorous inferential proof rather than relying solely on descriptive observations, four formal hypothesis tests "
        "were executed at an alpha significance threshold of 0.05. Table 14 consolidates the research questions, null hypotheses, "
        "test statistics, p-values, effect sizes, and practical business interpretations."
    )

    add_table_from_csv("outputs/statistics/hypothesis_testing_summary.csv", 14, "Consolidated Master Inferential Hypothesis Testing Results", max_rows=4, custom_col_widths=[0.4, 1.8, 1.4, 1.1, 0.7, 0.7, 1.5])

    add_image_figure(
        "figures/statistical/fig08_hypothesis_test_panels.png",
        8, "Empirical Evidence Panels for Four Core Hypothesis Tests",
        "Four-panel visualization illustrating Welch's t-test mean profit contrast (A), ANOVA category divergence (B), Chi-Square regional loss incidence (C), and Spearman rank correlation trend (D)."
    )

    add_p(
        "Detailed Examination of Test Results:",
        bold_prefix="Inferential Breakdown: "
    )
    add_p(
        "1. Welch's Two-Sample t-Test: t(9162.2) = 15.74, p < 0.0001, Cohen's d = 0.318. Non-discounted transactions generated an average profit of $66.90, "
        "compared to -$6.66 for discounted transactions (95% CI of difference: [$64.40, $82.72]). The null hypothesis is emphatically rejected."
    )
    add_p(
        "2. One-Way ANOVA: F(2, 9991) = 54.31, p < 0.0001, eta-squared = 0.0108. Post-hoc Tukey HSD pairwise comparisons (Table 16) confirm that Technology "
        "($78.75/order) significantly outperforms Furniture ($8.40/order, diff = $70.36, p < 0.0001) and Office Supplies ($20.33/order, diff = $58.42, p < 0.0001)."
    )

    add_table_from_csv("outputs/statistics/tukey_hsd_category_summary.csv", 16, "Post-Hoc Tukey HSD Pairwise Category Profit Comparisons", max_rows=3, custom_col_widths=[1.8, 1.1, 1.1, 1.1, 1.1])

    add_p(
        "3. Pearson Chi-Square Test of Independence: Chi-Square(3) = 436.70, p < 0.0001, Cramer's V = 0.2090. As shown in the contingency matrix (Table 15), "
        "regional loss incidence is highly non-random, with the Central region recording 741 loss transactions (31.90%) compared to 318 (9.93%) in the West."
    )

    add_table_from_csv("outputs/statistics/contingency_table_region_loss.csv", 15, "Regional Loss Incidence Contingency Matrix", max_rows=4, custom_col_widths=[1.2, 1.2, 1.2, 1.2, 1.2])

    add_p(
        "4. Spearman Rank Correlation: rho = -0.5434, S = 2.57e+11, p < 0.0001. Confirms an extensive, statistically significant monotonic inverse association."
    )

    add_callout(
        "STATISTICAL SIGNIFICANCE VS. BUSINESS SIGNIFICANCE",
        "A critical distinction emphasized in this capstone is that statistical significance (p < 0.05) proves an effect is unlikely due to random chance, but does not guarantee operational importance. However, in our analysis, the effect sizes are operationally massive: a $73.56 mean profit swing between discounted and non-discounted orders (d = 0.318) and a Cramer's V of 0.209 represent decisive, high-stakes business impacts that demand immediate management restructuring."
    )

    doc.add_page_break()

    # ==========================================================================
    # 17. SECTION 14 & 15: PREDICTIVE MODELING & EVALUATION
    # ==========================================================================
    add_h1("14. Predictive Modeling Methodology & Regression Architecture")
    add_p(
        "To transition from descriptive and inferential analysis to forward-looking predictive decision support, a rigorous predictive modeling "
        "framework was developed. The objective is to predict transaction-level Profit ($ USD, continuous target) using nine operational predictors: "
        "Sales, Discount, Quantity, Shipping_Days, Category, Sub_Category, Region, Segment, and Ship_Mode."
    )
    add_p(
        "Methodological safeguards were strictly enforced to guarantee technical validity:",
        bold_prefix="Methodological Protocol: "
    )
    add_p("• Zero Data Leakage: The dataset was partitioned into an 80% Training Set (n = 7,995) and a 20% Holdout Test Set (n = 1,999) using a fixed random seed (12345). All model fitting and contrast coding were performed exclusively on the training partition.")
    add_p("• 5-Fold Cross-Validation: Internal cross-validation was conducted across 5 random folds on the training set to prevent overfitting.")
    add_p("• Candidate Model Suite: Four distinct model architectures were evaluated: (1) Naive Mean Baseline Benchmark, (2) Multiple Linear Regression (OLS), (3) Regularized Elastic Net (alpha = 0.5), and (4) Random Forest Regressor (ntree = 200, mtry = 3).")

    add_h1("15. Cross-Validation & Out-of-Sample Holdout Evaluation")
    add_p(
        "Table 17 presents the comprehensive performance benchmarking across both 5-fold cross-validation and the untouched holdout test partition. "
        "Evaluation metrics include Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), Coefficient of Determination (R²), and Error Reduction %."
    )

    add_table_from_csv("outputs/model_results/model_comparison_master.csv", 17, "Cross-Validation and Holdout Test Set Performance Master Table", max_rows=4, custom_col_widths=[1.8, 0.7, 0.7, 0.6, 0.7, 0.7, 0.6, 0.7])

    add_image_figure(
        "figures/modeling/fig09_model_cv_test_comparison.png",
        9, "Predictive Model Cross-Validation and Holdout Test Set Performance",
        "Benchmarking RMSE reduction (Panel A) and Holdout Test Explained Variance R² (Panel B) across all four candidate model architectures."
    )

    add_p(
        "Model Performance Insights:",
        bold_prefix="Empirical Takeaways: "
    )
    add_p(
        "1. Classical Linear Regression (OLS) achieved a Test R² of 41.86% (Test RMSE = $195.71, MAE = $64.07). While an improvement over the baseline, "
        "OLS struggles because linear additive formulations cannot model threshold discount collapse or non-linear commodity margins."
    )
    add_p(
        "2. Regularized Elastic Net achieved comparable test metrics (Test RMSE = $197.74, R² = 40.65%), demonstrating that collinearity shrinkage alone cannot overcome non-linearities."
    )
    add_p(
        "3. Champion Random Forest achieved an outstanding Holdout Test R² of 78.45% (Test RMSE = $119.16, Test MAE = $26.66). "
        "Random Forest reduced test prediction error by 53.59% over the baseline, establishing superior generalization capability."
    )

    add_image_figure(
        "figures/modeling/fig11_regression_diagnostics_4panel.png",
        11, "Four-Panel Classical OLS Regression Diagnostics",
        "Diagnostic plots showing severe heteroscedastic funneling (Residuals vs Fitted), heavy leptokurtic tails (Normal Q-Q), and influential leverage points (Cook's Distance)."
    )

    add_image_figure(
        "figures/modeling/fig12_actual_vs_predicted_rf.png",
        12, "Actual vs. Predicted Profit on Holdout Test Set (N = 1,999)",
        "Scatter plot of actual versus predicted profit for the Champion Random Forest model, demonstrating tight alignment along the 45-degree parity reference line."
    )

    add_image_figure(
        "figures/modeling/fig13_error_distribution_residuals.png",
        13, "Holdout Test Set Residual Error Distribution & Category Profiling",
        "Panel A depicts the residual error histogram centered tightly at $0.00. Panel B shows absolute error distributions across merchandise categories."
    )

    add_p(
        "Table 20 confirms that Random Forest achieves remarkable precision in commodity sectors: in Office Supplies, the median absolute error is just $2.41! "
        "Table 19 documents a forensic audit of the largest residual errors, revealing that the primary sources of model discrepancy stem from rare, high-value enterprise machines (e.g., $9,099 Lexmark machines) with unique contract pricing."
    )

    add_table_from_csv("outputs/model_results/category_error_breakdown.csv", 20, "Category-Level Out-of-Sample Holdout Error Breakdown", max_rows=3, custom_col_widths=[1.5, 1.2, 1.2, 1.2, 1.2])

    doc.add_page_break()

    # ==========================================================================
    # 18. SECTION 16: MODEL INTERPRETATION
    # ==========================================================================
    add_h1("16. Model Interpretation & Permutation Feature Importance")
    add_p(
        "To prevent treating the Random Forest ensemble as an uninterpretable 'black box', permutation variable importance was extracted. "
        "Figure 10 and Table 18 report the percent increase in Mean Squared Error (%IncMSE) and Increase in Node Purity (IncNodePurity) when each feature is randomly permuted."
    )

    add_table_from_csv("outputs/model_results/rf_feature_importance.csv", 18, "Random Forest Permutation Feature Importance Profile", max_rows=9, custom_col_widths=[1.5, 1.8, 1.8])

    add_image_figure(
        "figures/modeling/fig10_rf_feature_importance.png",
        10, "Random Forest Permutation Variable Importance (%IncMSE)",
        "Ranked horizontal bar chart demonstrating that Transaction Sales and Promotional Discount drive the majority of predictive accuracy."
    )

    add_p(
        "Feature Importance Insights:",
        bold_prefix="Model Interpretability: "
    )
    add_p(
        "The permutation importance profile confirms that Sales (%IncMSE = 25.66%) and Discount (%IncMSE = 25.61%) are the primary drivers of profit prediction. "
        "Sub_Category (6.83%) and Category (5.19%) provide essential categorical anchoring, allowing the decision trees to apply different margin baselines "
        "for Copiers versus Tables. Conversely, logistical features such as Shipping_Days and Ship_Mode exert negligible influence on unit profitability."
    )

    # ==========================================================================
    # 19. SECTION 17: INTEGRATED FINDINGS
    # ==========================================================================
    add_h1("17. Integrated Findings: Visualization, Statistics & Machine Learning")
    add_p(
        "The primary intellectual achievement of this Week 4 capstone is the complete integration of descriptive visualization, "
        "inferential statistics, and machine learning into a single unified analytical continuum. "
        "Table 22 establishes an internal traceability matrix connecting every empirical discovery across analytical tiers."
    )

    matrix_headers = ["Analytical Finding", "Descriptive Visualization", "Statistical Inferential Evidence", "Predictive Machine Learning Evidence", "Business Strategy Implication"]
    matrix_rows = [
        [
            "Promotional Discount Cliff",
            "Figure 6 LOESS curve shows profit collapse at >20% discount.",
            "Welch's t-test: t = 15.74, p < 0.0001, d = 0.318. Spearman rho = -0.5434.",
            "Discount is the #2 predictor in Random Forest (%IncMSE = 25.61%).",
            "Establish strict hard discount caps at 20%; require executive override for deeper markdowns."
        ],
        [
            "Merchandise Profit Asymmetry",
            "Figure 3 shows Copiers leading ($55.6k) vs Tables losing (-$17.7k).",
            "ANOVA: F(2, 9991) = 54.31, p < 0.0001. Tukey HSD Tech vs Furn diff = $70.36.",
            "Sub-Category is the #3 predictor (%IncMSE = 6.83%).",
            "Restructure Table manufacturer contracts; reallocate marketing spend toward Technology."
        ],
        [
            "Regional Margin Disparity",
            "Figure 4 shows Central region achieving lowest margin (7.9%) and 31.9% loss rate.",
            "Chi-Square test: Chi2(3) = 436.70, p < 0.0001, Cramer's V = 0.2090.",
            "Region dummy variables capture geographical loss clusters.",
            "Audit Central region sales incentives; eliminate regional discount autonomy in Texas and Illinois."
        ],
        [
            "Fourth-Quarter Revenue Surges",
            "Figure 2 shows annual Q4 spikes generating over 35% of revenue.",
            "Yearly growth summary tracks consistent 51.4% expansion over 4 years.",
            "Order timing interacts with Sales volume to scale profit potential.",
            "Optimize inventory stocking and staffing schedules 60 days prior to Q4 holiday influx."
        ]
    ]

    p_mat = doc.add_paragraph()
    p_mat.paragraph_format.space_before = Pt(8)
    p_mat.paragraph_format.space_after = Pt(3)
    p_mat.paragraph_format.keep_with_next = True
    r_mn = p_mat.add_run("Table 22. Triangulated Analytical Evidence & Integration Matrix")
    r_mn.bold = True
    r_mn.font.size = Pt(10)
    r_mn.font.color.rgb = RGBColor(26, 54, 93)

    t_mat = doc.add_table(rows=len(matrix_rows)+1, cols=5)
    t_mat.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_mat.autofit = False

    for j, h in enumerate(matrix_headers):
        cell = t_mat.cell(0, j)
        cell.text = h
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="1A365D"/>')
        cell._tc.get_or_add_tcPr().append(shd)
        cp = cell.paragraphs[0]
        cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cp.runs[0].font.bold = True
        cp.runs[0].font.size = Pt(8.5)
        cp.runs[0].font.color.rgb = RGBColor(255, 255, 255)

    m_widths = [1.2, 1.3, 1.4, 1.3, 1.3]
    for i, row in enumerate(matrix_rows):
        fill = "F7FAFC" if i % 2 == 1 else "FFFFFF"
        for j, val in enumerate(row):
            cell = t_mat.cell(i+1, j)
            cell.text = val
            shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill}"/>')
            cell._tc.get_or_add_tcPr().append(shd)
            cp = cell.paragraphs[0]
            cp.runs[0].font.size = Pt(8.0)
            cp.runs[0].font.color.rgb = RGBColor(45, 55, 72)

    for row in t_mat.rows:
        for j, w in enumerate(m_widths):
            row.cells[j].width = Inches(w)
            tcPr = row.cells[j]._tc.get_or_add_tcPr()
            tcBorders = parse_xml(f'''
                <w:tcBorders {nsdecls("w")}>
                    <w:top w:val="single" w:sz="4" w:space="0" w:color="CBD5E0"/>
                    <w:left w:val="none"/>
                    <w:bottom w:val="single" w:sz="4" w:space="0" w:color="CBD5E0"/>
                    <w:right w:val="none"/>
                </w:tcBorders>
            ''')
            tcPr.append(tcBorders)

    doc.add_page_break()

    # ==========================================================================
    # 20. SECTION 18 & 19: BUSINESS INSIGHTS & RECOMMENDATIONS
    # ==========================================================================
    add_h1("18. Ten Core Evidence-Based Business Insights")
    insights = [
        ("Insight 1: The 20% Discount Cliff Destroys Profitability", "Orders discounted beyond 20% experience an empirical profit collapse to -$62.58 median profit and -41.8% margin, costing the enterprise over $90k in cumulative margin bleed."),
        ("Insight 2: Furniture Sub-Categories Suffer Severe Structural Losses", "While Technology generates $145.5k in profit (17.4% margin), Furniture produces only $18.5k (2.5% margin), driven by severe losses in Tables (-$17.7k) and Bookcases (-$3.5k)."),
        ("Insight 3: Central Region Suffers Systemic Margin Degradation", "The Central territory exhibits an anomalous 31.90% transaction loss rate, resulting in an operating margin of just 7.92% compared to 14.95% in the West."),
        ("Insight 4: Technology Hardware Drives Disproportionate Returns", "Copiers ($55.6k), Phones ($44.5k), and Accessories ($41.9k) represent the company's primary profit engine, generating over 49% of all net earnings."),
        ("Insight 5: Fourth-Quarter Revenue Surges Dominate the Annual Cycle", "Over 35% of sales and 38% of profits occur between October and December, requiring highly specialized seasonal procurement and logistics planning."),
        ("Insight 6: Customer Segments Exhibit Identical Underlying Margins", "Consumer, Corporate, and Home Office clients generate nearly identical operating margins (11.5% to 13.8%), indicating that client type does not drive margin variation."),
        ("Insight 7: Standard Class Shipping Represents the Operational Workhorse", "Standard Class fulfillment accounts for 59.7% of order volume with a reliable mean dispatch latency of 5.0 days, proving effective for customer retention."),
        ("Insight 8: OLS Linear Models Underfit Due to Severe Non-Linearities", "Classical regression captures only 41.86% of profit variance due to extreme heteroscedasticity and non-linear threshold effects."),
        ("Insight 9: Random Forest Resolves Retail Complexities (78.45% Test R²)", "The non-linear ensemble cuts test error by 53.59% over baseline, delivering a median absolute prediction error of just $2.41 in commodity office supplies."),
        ("Insight 10: Transaction Size Interacts Non-Linearly with Margin Risk", "High-value enterprise transactions (> $2,000) carry catastrophic capital risk if discounted even moderately, requiring specialized margin gates.")
    ]
    for ins_title, ins_desc in insights:
        add_p(ins_desc, bold_prefix=f"{ins_title}: ")

    add_h1("19. Strategic Business Implications & Prioritized Recommendations")
    add_p(
        "To ensure business impact, recommendations are categorized into three evidence-weighted tiers: "
        "Tier 1 (High-Evidence Analytical Opportunities), Tier 2 (Moderate-Evidence Operational Interventions), "
        "and Tier 3 (Strategic Data & Governance Improvements)."
    )

    recs = [
        (
            "Recommendation 1: Implement an Automated Hard Cap at 20% Promotional Discount (Tier 1)",
            "Evidence: Figures 6 & 8; Tables 10 & 14 (t = 15.74, p < 0.0001, d = 0.318).\n"
            "Action: Restructure POS and ERP software to reject discounts exceeding 20% without regional VP authorization.\n"
            "Expected Impact: Recovers an estimated $45,000 - $60,000 in annual net profit with negligible impact on unit demand."
        ),
        (
            "Recommendation 2: Renegotiate or Rationalize the Table and Bookcase Catalog (Tier 1)",
            "Evidence: Figure 3; Table 7 (Tables accumulate -$17,725 loss; Bookcases -$3,473 loss).\n"
            "Action: Conduct vendor supplier review on Tables; increase baseline MSRP by 12% or transition unprofitable SKUs to drop-ship.\n"
            "Expected Impact: Eliminates $21,000+ in chronic capital drag across the Furniture division."
        ),
        (
            "Recommendation 3: Standardize Regional Discount Governance in the Central Territory (Tier 2)",
            "Evidence: Figures 4 & 8; Tables 8 & 15 (Chi-Square = 436.70, Central loss rate = 31.90%).\n"
            "Action: Revoke localized promotional discount authority for sales reps in Texas, Illinois, and Ohio; align Central pricing rules with West protocols.\n"
            "Expected Impact: Elevates Central region operating margin from 7.92% toward the corporate benchmark of 12.5%."
        ),
        (
            "Recommendation 4: Deploy the Random Forest Model for Real-Time Deal Margin Scoring (Tier 2)",
            "Evidence: Figures 9, 10, 12; Table 17 (Champion RF Test R² = 78.45%, Test RMSE = $119.16).\n"
            "Action: Integrate the trained Random Forest model artifact (random_forest_model.rds) into a lightweight sales scoring API.\n"
            "Expected Impact: Provides instantaneous margin guidance to account executives before customer price quotes are finalized."
        ),
        (
            "Recommendation 5: Build Pre-Q4 Logistical Buffer & Inventory Pre-Stocking (Tier 3)",
            "Evidence: Figure 2; Table 11 (Longitudinal 51.4% expansion and recurring Q4 demand spikes).\n"
            "Action: Initiate pre-holiday inventory build in August; pre-contract third-party logistics freight capacity for October-December.\n"
            "Expected Impact: Prevents stockouts in high-margin Technology hardware (Copiers, Phones) during peak demand."
        )
    ]

    for r_title, r_desc in recs:
        add_callout(r_title, r_desc, color_hex="2B6CB0")

    doc.add_page_break()

    # ==========================================================================
    # 21. SECTION 20 - 24: CHALLENGES, LESSONS, LIMITATIONS, CONCLUSION
    # ==========================================================================
    add_h1("20. Analytical Challenges Encountered & Technical Resolutions")
    challenges = [
        ("Challenge 1: Extreme Non-Normality and Heavy Kurtosis", "Transaction Sales and Profit exhibited extreme right-skew and heavy leptokurtic tails (Kurtosis > 280), violating ordinary least squares assumptions. Resolved by using log-transforms for visualization, unpooled Welch t-tests, non-parametric rank correlations, and tree-based ensemble modeling."),
        ("Challenge 2: Severe Non-Linear Discount Cliffs", "Discounts above 20% triggered sudden margin collapse that linear regression lines could not capture. Resolved by engineering discrete discount bands and deploying Random Forest, which naturally splits on non-linear threshold interactions."),
        ("Challenge 3: Postal Code Truncation in Raw Export", "Leading zeroes were dropped in raw CSV exports (e.g., Burlington, VT '5408'). Resolved by applying string zero-padding (sprintf('%05d', as.integer(Postal_Code))) to restore valid 5-digit US ZIPs."),
        ("Challenge 4: R Package Namespace Clashes", "Namespace collision occurred between randomForest::margin and ggplot2::margin. Resolved by enforcing explicit namespace prefixing (ggplot2::margin) across all visual scripts."),
        ("Challenge 5: Windows UTF-8 Character Sanitization", "Special characters in product descriptions caused encoding artifacts in Windows R. Resolved by wrapping text attributes in iconv(x, to = 'UTF-8', sub = '') prior to trimming.")
    ]
    for ch_title, ch_desc in challenges:
        add_p(ch_desc, bold_prefix=f"{ch_title}: ")

    add_h1("21. Professional Lessons Learned & Analytical Reflections")
    lessons = [
        ("Lesson 1: Top-Line Revenue is a Deceptive Proxy for Success", "Categories generating substantial sales (e.g., Furniture, $742k) can produce negligible profits ($18.5k) if promotional discounts and product margins are unmonitored."),
        ("Lesson 2: Non-Linearity Mandates Machine Learning Over OLS", "While linear regression offers interpretability, modern retail relationships (such as price cliffs) require non-linear ensemble models like Random Forest to achieve high predictive accuracy (78.45% R²)."),
        ("Lesson 3: Strict Zero-Leakage Data Partitioning is Non-Negotiable", "Fitting feature scalers, contrasts, or models on pooled data causes optimistic overfitting. Enforcing strict 80/20 train/test separation ensures realistic out-of-sample error estimates."),
        ("Lesson 4: Communicating Insights Requires Narrative Framing", "Executives do not read raw ANOVA tables or code dumps. Framing findings through WHAT? SO WHAT? NOW WHAT? bridges the gap between data science and corporate strategy.")
    ]
    for l_title, l_desc in lessons:
        add_p(l_desc, bold_prefix=f"{l_title}: ")

    add_h1("22. Methodological & Observational Data Limitations")
    add_p(
        "Scientific integrity requires transparent acknowledgment of analytical limitations:",
        bold_prefix="Methodological Boundaries: "
    )
    add_p("1. Observational Nature: The Superstore dataset is observational. While statistical associations and predictive relationships are robustly verified, non-experimental data cannot establish absolute counterfactual causality.")
    add_p("2. Omitted Commercial Variables: Crucial operational drivers—including customer acquisition costs (CAC), digital marketing spend, return/refund rates, and warehouse handling fees—are absent from the transactional schema.")
    add_p("3. Static Historical Window: Data spans 2011 to 2014. Macroeconomic shifts, inflation, e-commerce evolution, and modern supply chain disruptions require recalibrating findings before applying to contemporary retail markets.")
    add_p("4. Extrapolation Boundaries: Predictive models are trained on domestic US transactions; extrapolating predictions to international markets or different merchandise verticals would introduce severe covariate shift.")

    add_h1("23. Future Research & Advanced Analytics Roadmap")
    add_p(
        "To extend this capstone foundation into enterprise-scale intelligence, several future initiatives are proposed:",
        bold_prefix="Future Analytics Directions: "
    )
    add_p("• Phase 1: Interactive Shiny BI Dashboard: Develop an interactive R Shiny web application enabling executive scenario modeling and dynamic discount threshold simulation.")
    add_p("• Phase 2: Price Elasticity Econometric Modeling: Formulate two-stage log-log econometric models to estimate exact price elasticity of demand across all 17 sub-categories.")
    add_p("• Phase 3: Time-Series Forecasting Engine: Implement Prophet and ARIMA models to generate granular 90-day forward SKU-level demand forecasts for Q4 seasonal inventory management.")
    add_p("• Phase 4: Customer Lifetime Value (CLV) & Churn Analysis: Transition from transactional line items to customer-centric RFM (Recency, Frequency, Monetary) and Pareto/NBD retention modeling.")

    add_h1("24. Final Synthesis & Capstone Conclusion")
    add_p(
        "This capstone project successfully demonstrates an end-to-end data analytics and predictive science workflow. "
        "By systematically moving through data quality auditing, exploratory visual discovery, rigorous hypothesis testing, and cross-validated "
        "machine learning, raw retail transactions were transformed into a coherent, highly actionable strategic narrative."
    )
    add_p(
        "The empirical findings deliver immediate corporate value: proving that promotional discounting beyond 20% severely cannibalizes profit, "
        "identifying systemic margin destruction in Furniture Tables (-$17.7k), uncovering geographic vulnerabilities in the Central region (31.9% loss rate), "
        "and deploying a Champion Random Forest model that explains 78.45% of out-of-sample profit variance. "
        "Through reproducible R code, rigorous statistical reasoning, and clear business communication, this capstone delivers a comprehensive "
        "blueprint for evidence-based enterprise decision-making."
    )

    doc.add_page_break()

    # ==========================================================================
    # 22. SECTION 25: REFERENCES
    # ==========================================================================
    add_h1("25. Academic & Professional References")
    references = [
        "Breiman, L. (2001). Random Forests. Machine Learning, 45(1), 5-32. https://doi.org/10.1023/A:1010933404324",
        "Cleveland, W. S. (1979). Robust locally weighted regression and scatterplot smoothing. Journal of the American Statistical Association, 74(368), 829-836.",
        "Cohen, J. (1988). Statistical Power Analysis for the Behavioral Sciences (2nd ed.). Lawrence Erlbaum Associates.",
        "Fox, J., & Weisberg, S. (2019). An R Companion to Applied Regression (3rd ed.). Sage Publications.",
        "Friedman, J., Hastie, T., & Tibshirani, R. (2010). Regularization paths for generalized linear models via coordinate descent. Journal of Statistical Software, 33(1), 1-22.",
        "Kuhn, M., & Johnson, K. (2013). Applied Predictive Modeling. Springer New York.",
        "R Core Team. (2026). R: A Language and Environment for Statistical Computing. R Foundation for Statistical Computing, Vienna, Austria. https://www.R-project.org/",
        "Tableau Software. (2014). Sample - Superstore Sales Dataset. Tableau Public Community Resources.",
        "Tukey, J. W. (1977). Exploratory Data Analysis. Addison-Wesley.",
        "Wickham, H. (2016). ggplot2: Elegant Graphics for Data Analysis (2nd ed.). Springer-Verlag New York.",
        "Wickham, H., Averick, M., Bryan, J., et al. (2019). Welcome to the Tidyverse. Journal of Open Source Software, 4(43), 1686."
    ]
    for ref in references:
        p_ref = doc.add_paragraph()
        p_ref.paragraph_format.left_indent = Inches(0.5)
        p_ref.paragraph_format.first_line_indent = Inches(-0.5)
        p_ref.paragraph_format.space_after = Pt(4)
        r_rf = p_ref.add_run(ref)
        r_rf.font.size = Pt(9.5)
        r_rf.font.color.rgb = RGBColor(45, 55, 72)

    doc.add_page_break()

    # ==========================================================================
    # 23. SECTION 26 & 27: APPENDICES (CODE & OUTPUTS)
    # ==========================================================================
    add_h1("26. Appendix A: Complete Reproducible R Scripts")
    add_p(
        "To ensure total reproducibility in accordance with academic and professional standards, the primary R scripts "
        "powering this capstone are documented below. The master pipeline runner (scripts/run_all.R) executes all eight modular stages in 44.35 seconds."
    )

    add_h2("A.1 Data Cleaning & Feature Transformation (R/02_data_cleaning.R)")
    add_code(
        "# R/02_data_cleaning.R (Key Excerpt)\n"
        "df$Order_Date <- as.Date(df$Order_Date, format = '%d-%m-%Y')\n"
        "df$Ship_Date  <- as.Date(df$Ship_Date, format = '%d-%m-%Y')\n"
        "df$Postal_Code <- sprintf('%05d', as.integer(df$Postal_Code))\n"
        "df <- df %>%\n"
        "  mutate(\n"
        "    Order_Year = as.integer(format(Order_Date, '%Y')),\n"
        "    Shipping_Days = as.integer(Ship_Date - Order_Date),\n"
        "    Profit_Margin = ifelse(Sales > 0, Profit / Sales, 0),\n"
        "    Loss_Making_Flag = ifelse(Profit < 0, 1L, 0L),\n"
        "    Discount_Band = case_when(\n"
        "      Discount == 0 ~ '0% (None)',\n"
        "      Discount <= 0.20 ~ '1%-20% (Low/Moderate)',\n"
        "      TRUE ~ '>20% (Deep Promotional)'\n"
        "    )\n"
        "  )"
    )

    add_h2("A.2 Inferential Hypothesis Testing (R/05_statistical_analysis.R)")
    add_code(
        "# R/05_statistical_analysis.R (Key Excerpt)\n"
        "# 1. Welch's t-Test\n"
        "t_res <- t.test(Profit ~ Discount_Group, data = df, var.equal = FALSE)\n"
        "# 2. One-Way ANOVA & Tukey HSD\n"
        "anova_mod <- aov(Profit ~ Category, data = df)\n"
        "tukey_res <- TukeyHSD(anova_mod)\n"
        "# 3. Chi-Square Test of Independence\n"
        "chisq_res <- chisq.test(table(df$Region, df$Loss_Status))\n"
        "# 4. Spearman Rank Correlation\n"
        "spearman_res <- cor.test(df$Discount, df$Profit, method = 'spearman')"
    )

    add_h2("A.3 Machine Learning & Random Forest (R/06_predictive_modeling.R)")
    add_code(
        "# R/06_predictive_modeling.R (Key Excerpt)\n"
        "set.seed(12345)\n"
        "train_idx <- sample(1:nrow(model_df), size = 0.80 * nrow(model_df))\n"
        "train_set <- model_df[train_idx, ]\n"
        "test_set  <- model_df[-train_idx, ]\n\n"
        "rf_final <- randomForest(\n"
        "  Profit ~ Sales + Discount + Quantity + Shipping_Days + Category + Sub_Category + Region + Segment + Ship_Mode,\n"
        "  data = train_set, ntree = 200, mtry = 3, importance = TRUE\n"
        ")\n"
        "test_preds <- predict(rf_final, newdata = test_set)\n"
        "test_rmse  <- sqrt(mean((test_set$Profit - test_preds)^2))\n"
        "test_r2    <- 1 - (sum((test_set$Profit - test_preds)^2) / sum((test_set$Profit - mean(test_set$Profit))^2))"
    )

    add_h1("27. Appendix B: System Execution Manifest & Output Captures")
    add_p(
        "Table 21 presents the master execution manifest tracking the end-to-end execution of all analytical stages. "
        "Figure captures document raw R console snapshots generated during verified script execution."
    )

    add_table_from_csv("outputs/execution_manifest.csv", 21, "Capstone End-to-End Pipeline Execution Manifest", max_rows=8, custom_col_widths=[0.6, 1.8, 2.5, 1.6])

    add_image_figure(
        "screenshots/outputs/card05_hypothesis_testing.png",
        "Card 5", "R Console Execution Snapshot: Formal Hypothesis Testing Results",
        "Terminal capture detailing exact t-test statistics, ANOVA F-values, Tukey pairwise contrasts, and Chi-square independence results.",
        width=Inches(6.0)
    )

    add_image_figure(
        "screenshots/outputs/card06_predictive_modeling.png",
        "Card 6", "R Console Execution Snapshot: Cross-Validation & Test Set Evaluation",
        "Terminal capture detailing 5-fold CV metrics, holdout test evaluations, Random Forest architecture parameters, and feature importance.",
        width=Inches(6.0)
    )

    add_image_figure(
        "screenshots/diagnostics/card07_model_diagnostics.png",
        "Card 7", "R Console Execution Snapshot: Model Diagnostics & Error Audit",
        "Terminal capture detailing category error breakdowns, residual distribution moments, and top prediction outliers.",
        width=Inches(6.0)
    )

    # Save document
    out_dir = os.path.join(BASE_DIR, "report")
    os.makedirs(out_dir, exist_ok=True)
    out_docx = os.path.join(out_dir, "Week4_Superstore_Comprehensive_Data_Analysis_Final_Report.docx")
    doc.save(out_docx)
    print(f"\n[SUCCESS] Final Capstone Report generated successfully at:\n{out_docx}")
    file_size_kb = os.path.getsize(out_docx) / 1024
    print(f"[INFO] Report File Size: {file_size_kb:.1f} KB")

if __name__ == "__main__":
    create_report()
