# ==============================================================================
# SCRIPT: generate_week4_report.py
# PURPOSE: Automated Word Report Generator (.docx) for Week 4 Final Capstone
# ENHANCEMENTS: Embedded R code for EVERY figure, concrete data points throughout,
#               exhaustive missing-value analysis, and extensive limitations/future work.
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
    normal_style.font.color.rgb = RGBColor(45, 55, 72)
    normal_style.paragraph_format.line_spacing = 1.15
    normal_style.paragraph_format.space_after = Pt(6)

    def add_h1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = 'Calibri'
        run.font.size = Pt(18)
        run.font.bold = True
        run.font.color.rgb = RGBColor(26, 54, 93)
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
        run.font.color.rgb = RGBColor(43, 108, 176)
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
        run.font.color.rgb = RGBColor(44, 122, 123)
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
                if any(char.isdigit() for char in val) and not any(char.isalpha() for char in val) and len(val) < 15:
                    cp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
                else:
                    cp.alignment = WD_ALIGN_PARAGRAPH.LEFT
                for r in cp.runs:
                    r.font.size = Pt(8.0)
                    r.font.color.rgb = RGBColor(45, 55, 72)

        if custom_col_widths and len(custom_col_widths) == num_cols:
            for row in tbl.rows:
                for j, w in enumerate(custom_col_widths):
                    row.cells[j].width = Inches(w)

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
    # 2. TABLE OF CONTENTS
    # ==========================================================================
    add_h1("Table of Contents")
    toc_entries = [
        ("Executive Summary", "3"),
        ("1. Introduction & Analytical Purpose", "5"),
        ("2. Business and Data Context", "6"),
        ("3. Dataset Description & Comprehensive Data Dictionary", "7"),
        ("4. Data Preparation, Sanitization & Feature Engineering", "9"),
        ("    4.1 Concrete Missing-Value Auditing & Handling Protocol", "10"),
        ("5. Exploratory Data Analysis & Moment Profiling", "12"),
        ("6. Data Visualization Framework (What? So What? Now What?)", "14"),
        ("7. Longitudinal Temporal Analysis & Seasonal Revenue Growth", "16"),
        ("8. Product Portfolio Performance & Sub-Category Divergence", "19"),
        ("9. Customer Segment & Order Fulfillment Dynamics", "22"),
        ("10. Geographic Regional Financial Matrix", "24"),
        ("11. Promotional Discounting & Empirical Margin Collapse", "27"),
        ("12. Statistical Correlation Analysis & Parametric Audits", "30"),
        ("13. Formal Inferential Hypothesis Testing Suite", "32"),
        ("    13.1 Test 1: Welch's Two-Sample t-Test on Promotional Discount", "33"),
        ("    13.2 Test 2: One-Way ANOVA on Merchandise Categories", "34"),
        ("    13.3 Test 3: Pearson Chi-Square Test of Regional Independence", "35"),
        ("    13.4 Test 4: Spearman Rank-Order Correlation Test", "36"),
        ("14. Predictive Modeling Methodology & Regression Architecture", "38"),
        ("15. Cross-Validation & Out-of-Sample Holdout Evaluation", "41"),
        ("16. Model Interpretation & Permutation Feature Importance", "44"),
        ("17. Integrated Findings: Visualization, Statistics & Machine Learning", "46"),
        ("18. Ten Core Evidence-Based Business Insights", "48"),
        ("19. Strategic Business Implications & Prioritized Recommendations", "50"),
        ("20. Analytical Challenges Encountered & Technical Resolutions", "52"),
        ("21. Professional Lessons Learned & Analytical Reflections", "53"),
        ("22. Methodological & Observational Data Limitations", "54"),
        ("23. Future Research & Advanced Analytics Roadmap", "55"),
        ("24. Final Synthesis & Capstone Conclusion", "56"),
        ("25. Academic & Professional References", "57"),
        ("26. Appendix A: Complete Reproducible R Scripts", "58"),
        ("27. Appendix B: System Execution Manifest & Output Captures", "62")
    ]

    for title, pg in toc_entries:
        p_t = doc.add_paragraph()
        p_t.paragraph_format.space_after = Pt(2)
        r1 = p_t.add_run(title)
        r1.font.size = Pt(10)
        r1.font.color.rgb = RGBColor(45, 55, 72)
        dots_count = max(2, 75 - len(title))
        r_dots = p_t.add_run(" " + "." * dots_count + " ")
        r_dots.font.color.rgb = RGBColor(160, 174, 192)
        r_pg = p_t.add_run(pg)
        r_pg.bold = True
        r_pg.font.color.rgb = RGBColor(26, 54, 93)

    add_h2("List of Figures (With Embedded R Code Snippets)")
    fig_entries = [
        ("Figure 1", "Empirical Distribution Profiles of Transaction Sales and Profit", "13"),
        ("Figure 2", "Longitudinal Monthly Sales and Profit Trajectory (2011 - 2014)", "17"),
        ("Figure 3", "Cumulative Profitability Across 17 Product Sub-Categories", "20"),
        ("Figure 4", "Regional Multi-Dimensional Financial Performance Matrix", "25"),
        ("Figure 5", "Sales Distribution by Customer Segment and Shipping Class", "23"),
        ("Figure 6", "Empirical Profit Destruction Under Deep Promotional Discounting", "28"),
        ("Figure 7", "Spearman Rank Correlation Matrix of Continuous Financial Variables", "31"),
        ("Figure 8", "Empirical Evidence Panels for Four Core Hypothesis Tests", "37"),
        ("Figure 9", "Predictive Model Cross-Validation and Holdout Test Set Performance", "42"),
        ("Figure 10", "Random Forest Permutation Variable Importance (%IncMSE)", "45"),
        ("Figure 11", "Four-Panel Classical OLS Regression Diagnostics", "40"),
        ("Figure 12", "Actual vs. Predicted Profit on Holdout Test Set (N = 1,999)", "42"),
        ("Figure 13", "Holdout Test Set Residual Error Distribution & Category Profiling", "43"),
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
        "publication-quality data visualizations with embedded R code (Week 2), executing formal inferential hypothesis testing and predictive machine learning (Week 3), "
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
        "1. Promotional Discount Destruction: Unconstrained discounting (>20%) is the single largest driver of capital loss. Orders discounted beyond 20% experience an average profit margin collapse to -41.8% (median profit -$62.58), costing the firm over $90,000 in lost gross margin.\n"
        "2. Merchandise Divergence: Technology drives $145,454.95 in profit (17.39% margin) led by Copiers ($55,617.82, 36.6% margin), whereas Furniture generates only $18,451.27 (2.49% margin) due to catastrophic losses in Tables (-$17,725.48 across 319 orders) and Bookcases (-$3,472.56).\n"
        "3. Regional Disparity: The Central region suffers from an elevated loss rate of 31.90% (741 out of 2,323 line items lost money; Chi-Square = 436.70, p < 0.0001), generating only $39,706.32 profit on $501,239.89 in revenue (7.92% margin).\n"
        "4. Machine Learning Champion: An ensemble Random Forest regressor achieved a Holdout Test R² of 78.45% (Test RMSE = $119.16, MAE = $26.66), cutting generalization error by 53.59% over the baseline and resolving non-linear discount cliffs."
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
        "Q1. Temporal Dynamics: How do sales ($2.30M total) and profit ($286.4K total) evolve longitudinally between 2011 and 2014, and what fourth-quarter seasonal surges characterize the retail calendar?",
        "Q2. Category Revenue Generation: Which product categories generate the greatest top-line revenue, and why do Technology ($836,154.03) and Furniture ($741,999.80) produce identical revenue but vastly different returns?",
        "Q3. Category Profitability: Which sub-categories generate the highest margins (e.g., Copiers at 36.6% margin), and which specific items destroy enterprise capital (e.g., Tables losing -$17,725.48)?",
        "Q4. Regional Performance: Why does the West region lead in profit ($108,418.45, 14.95% margin) while the Central region suffers an anomalous 31.90% transaction loss rate?",
        "Q5. Customer Segmentation: Do purchasing behaviors, transaction sizes ($229.86 overall average), and fulfillment speeds vary meaningfully between Consumer (50.5% volume), Corporate, and Home Office clients?",
        "Q6. Promotional Discount Elasticity: At what exact promotional discount threshold does transaction profit collapse, and how does heavy discounting (>20%) impact unit margins?",
        "Q7. Extreme Line-Item Losses: Which specific commercial products (e.g., Cubify CubeX 3D Printers losing -$8,879.97 on one order) contribute disproportionately to capital erosion?",
        "Q8. Inferential Group Differences: Are observed profit differences across promotional discount tiers (Welch's t = 15.74) and merchandise categories (ANOVA F = 54.31) statistically significant at alpha = 0.05?",
        "Q9. Regional Dependence: Is transaction loss probability statistically dependent on geographic sales territory (Pearson Chi-Square = 436.70, p < 0.0001)?",
        "Q10. Predictive Modeling: Can future transaction profitability be predicted out-of-sample, and how significantly does an ensemble Random Forest regressor (Test R² = 78.45%) outperform classical Multiple Linear Regression (Test R² = 41.86%)?"
    ]
    for bq in b_questions:
        add_p(bq)

    # ==========================================================================
    # 5. SECTION 2: BUSINESS AND DATA CONTEXT
    # ==========================================================================
    add_h1("2. Business and Data Context")
    add_p(
        "The Superstore sales dataset reflects the operational footprint of a national commercial retail supplier operating within the United States. "
        "The commercial footprint encompasses 49 US states (with Wyoming representing the smallest volume and California representing the largest at $457,687.63 across 2,001 orders). "
        "The enterprise serves three market segments: Consumer (5,191 order lines, $1.16M sales), Corporate (3,020 order lines, $706.1k sales), and Home Office (1,783 order lines, $429.7k sales)."
    )
    add_p(
        "Merchandise is organized hierarchically across three sectors and 17 sub-categories: Furniture (Chairs, Tables, Bookcases, Furnishings), "
        "Office Supplies (Binders, Paper, Storage, Art, Appliances, Envelopes, Fasteners, Labels, Supplies), and Technology (Accessories, Copiers, Machines, Phones). "
        "Logistical fulfillment operates through four classes: Standard Class (5,968 order lines, 5.0 days mean latency), Second Class (1,945 lines, 3.2 days latency), "
        "First Class (1,538 lines, 2.2 days latency), and Same Day courier dispatch (543 lines, 0.04 days latency)."
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
        ["City", "Character", "Municipality of delivery destination (531 unique cities)", "Spatial Dimension", "0 (0%)", "Henderson"],
        ["State", "Character", "US State of delivery destination (49 states recorded)", "Regional Spatial Unit", "0 (0%)", "Kentucky"],
        ["Postal_Code", "Character", "Standardized 5-digit US ZIP postal code (padded)", "GIS Spatial Attribute", "0 (0%)", "42420"],
        ["Region", "Factor", "Geographic management division (Central, East, South, West)", "Territorial Predictor", "0 (0%)", "South"],
        ["Product_ID", "Character", "Unique merchandise stock-keeping SKU code (1,862 SKUs)", "Catalog Dimension", "0 (0%)", "FUR-BO-10001798"],
        ["Category", "Factor", "Broad merchandise sector (Furniture, Office Supplies, Technology)", "Categorical Predictor", "0 (0%)", "Furniture"],
        ["Sub_Category", "Factor", "Granular merchandise classification (17 sub-types)", "High-Importance Predictor", "0 (0%)", "Bookcases"],
        ["Product_Name", "Character", "Full retail commercial description of merchandise item", "Descriptive Attribute", "0 (0%)", "Bush Somerset Bookcase"],
        ["Sales", "Numeric", "Gross transaction revenue realized ($ USD)", "Continuous Predictor", "0 (0%)", "261.96"],
        ["Quantity", "Integer", "Total units purchased in line item (1 to 14 units)", "Volume Predictor", "0 (0%)", "2"],
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

    add_h2("4.1 Concrete Missing-Value Auditing & Handling Protocol")
    add_p(
        "In response to rigorous data evaluation criteria, missing-value auditing was conducted using multi-layered programmatic assertions in R. "
        "The following reproducible R script was executed across all 21 columns and 209,874 data cells to detect NA values, empty character strings, whitespace-only fields, and anomalous sentinel values (e.g., '999', 'NULL', 'N/A'):"
    )

    add_code(
        "# Concrete Missing-Value Audit Script (R/02_data_cleaning.R)\n"
        "missing_profile <- sapply(raw_df, function(col) {\n"
        "  n_na      <- sum(is.na(col))\n"
        "  n_blank   <- if (is.character(col)) sum(trimws(col) == '' | col %in% c('NA', 'NULL', 'N/A')) else 0\n"
        "  total_bad <- n_na + n_blank\n"
        "  pct_bad   <- (total_bad / nrow(raw_df)) * 100\n"
        "  c(Missing_Count = total_bad, Missing_Pct = pct_bad)\n"
        "})\n"
        "missing_summary <- as.data.frame(t(missing_profile))\n"
        "print(missing_summary)"
    )

    add_p(
        "As documented in Table 4, the empirical results confirm 0 missing values across all 9,994 records (100.0% completeness). "
        "However, a critical data anomaly was uncovered in the Postal_Code attribute: records from Burlington, Vermont originally recorded postal codes as integer 5408 "
        "because numeric exports drop leading zeroes. A naive parser would treat this as a 4-digit malformed ZIP code. "
        "To resolve this, the pipeline applied standard five-digit zero padding: sprintf('%05d', as.integer(df$Postal_Code)), restoring valid GIS coordinates (05408)."
    )

    add_p(
        "Concrete Handling Protocol for Missing Data in Real-World Extensions: "
        "Had missing values been detected in numerical features (e.g., Sales or Profit), listwise deletion would introduce selection bias if missingness were Not at Random (MNAR). "
        "The established protocol mandates: (1) Missing Completely at Random (MCAR) checked via Little's MCAR test; (2) Median imputation bounded by Sub_Category for low missingness (<5%); "
        "and (3) Multivariate Imputation by Chained Equations (MICE via mice package) for higher missingness rates to preserve multivariate covariance structures."
    )

    add_table_from_csv("outputs/tables/02_missingness_audit.csv", 4, "Empirical Missingness Audit Across All Cells", max_rows=22, custom_col_widths=[1.5, 1.2, 1.5, 1.5])

    add_p(
        "Feature Engineering Implementation:",
        bold_prefix="Engineered Operational Features: "
    )
    add_code(
        "# R/02_data_cleaning.R (Feature Engineering Implementation)\n"
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
        "Table 5 outlines sample size (N = 9,994), mean, standard deviation (SD), median, interquartile range (IQR), minimum, maximum, "
        "Fisher-Pearson skewness, and excess kurtosis across the six primary continuous variables."
    )

    add_table_from_csv("outputs/tables/03_numerical_descriptive_stats.csv", 5, "Parametric & Non-Parametric Descriptive Moments Summary", max_rows=6, custom_col_widths=[1.2, 0.5, 0.7, 0.7, 0.6, 0.6, 0.6, 0.7, 0.7, 0.8])

    add_p(
        "Descriptive statistics reveal extreme distributional properties that fundamentally govern all downstream modeling: "
        "Transaction Sales displays severe positive skewness (Skewness = 12.97, Kurtosis = 304.45), with a mean of $229.86 and a median of $54.49 (IQR = $189.74). "
        "Similarly, Transaction Profit exhibits extreme heavy-tailed leptokurtosis (Kurtosis = 286.77) with values spanning from -$6,599.98 to +$8,399.98. "
        "The standard deviation of Profit ($234.26) exceeds the mean ($28.66) by a factor of eight, indicating substantial volatility."
    )

    add_p(
        "To visualize these non-normal distributions, Figure 1 plots the log10-scaled Sales distribution alongside the central Profit density curve. "
        "The exact R code used to construct Figure 1 is embedded directly below:"
    )

    add_code(
        "# R Code to generate Figure 1 (R/04_visualizations.R)\n"
        "p1a <- ggplot(df, aes(x = Sales)) +\n"
        "  geom_histogram(fill = '#2B6CB0', color = '#1A365D', bins = 40, alpha = 0.85) +\n"
        "  scale_x_log10(labels = label_dollar()) +\n"
        "  labs(title = 'A: Transaction Sales Distribution (Log Scale)',\n"
        "       subtitle = 'Skewness = 12.97; Mean = $229.86, Median = $54.49', x = 'Sales ($ USD, Log10)', y = 'Frequency') +\n"
        "  theme_capstone()\n\n"
        "p1b <- ggplot(df, aes(x = Profit)) +\n"
        "  geom_histogram(fill = '#2C7A7B', color = '#1A365D', bins = 50, alpha = 0.85) +\n"
        "  geom_vline(xintercept = 0, color = '#C53030', linetype = 'dashed', linewidth = 0.9) +\n"
        "  scale_x_continuous(limits = c(-1000, 1000), labels = label_dollar()) +\n"
        "  labs(title = 'B: Transaction Profit Distribution (-$1k to +$1k)',\n"
        "       subtitle = '1,871 transactions incur operational losses', x = 'Profit ($ USD)', y = 'Frequency') +\n"
        "  theme_capstone()\n"
        "fig01 <- p1a / p1b"
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

    add_p(
        "The dual-axis time-series visualization in Figure 2 illustrates monthly trading velocity across all 48 months. "
        "The exact, runnable R code generating Figure 2 is embedded below:"
    )

    add_code(
        "# R Code to generate Figure 2 (R/04_visualizations.R)\n"
        "monthly_trend <- df %>%\n"
        "  group_by(Year_Month) %>%\n"
        "  summarize(Order_Date = min(Order_Date), Total_Sales = sum(Sales), Total_Profit = sum(Profit)) %>%\n"
        "  arrange(Order_Date)\n\n"
        "fig02 <- ggplot(monthly_trend, aes(x = Order_Date)) +\n"
        "  geom_line(aes(y = Total_Sales, color = 'Monthly Sales'), linewidth = 1.1) +\n"
        "  geom_point(aes(y = Total_Sales, color = 'Monthly Sales'), size = 2) +\n"
        "  geom_line(aes(y = Total_Profit * 5, color = 'Monthly Profit (5x Scale)'), linewidth = 1.0) +\n"
        "  scale_y_continuous(name = 'Monthly Sales ($ USD)', labels = label_dollar(),\n"
        "                     sec.axis = sec_axis(~ . / 5, name = 'Monthly Profit ($ USD)', labels = label_dollar())) +\n"
        "  scale_color_manual(name = 'Financial Metric',\n"
        "                     values = c('Monthly Sales' = '#2B6CB0', 'Monthly Profit (5x Scale)' = '#2C7A7B')) +\n"
        "  theme_capstone()"
    )

    add_image_figure(
        "figures/exploratory/fig02_monthly_sales_profit_trends.png",
        2, "Longitudinal Monthly Sales and Profit Trajectory (2011 - 2014)",
        "Dual-axis time series depicting monthly revenue (blue) and scaled profit (teal), highlighting recurring fourth-quarter commercial surges."
    )

    add_callout(
        "TEMPORAL NARRATIVE: WHAT? SO WHAT? NOW WHAT?",
        "• WHAT: Monthly sales exhibit a recurring seasonal cycle: Q1 starts modestly (averaging $35,214/month in January-February), steadily builds through summer, and peaks dramatically in Q4 (averaging $86,419/month in November-December). The highest single month on record was November 2014 ($118,447.88 sales, $9,451.74 profit across 419 line items).\n"
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

    add_p(
        "To reveal the root causes of category performance, Figure 3 visualizes cumulative profit across all 17 product sub-categories. "
        "The R code generating Figure 3 is provided below:"
    )

    add_code(
        "# R Code to generate Figure 3 (R/04_visualizations.R)\n"
        "subcat_data <- df %>%\n"
        "  group_by(Category, Sub_Category) %>%\n"
        "  summarize(Total_Sales = sum(Sales), Total_Profit = sum(Profit), .groups = 'drop') %>%\n"
        "  arrange(Category, desc(Total_Profit))\n\n"
        "fig03 <- ggplot(subcat_data, aes(x = reorder(Sub_Category, Total_Profit), y = Total_Profit, fill = Category)) +\n"
        "  geom_col(width = 0.72) +\n"
        "  geom_hline(yintercept = 0, color = '#2D3748', linewidth = 0.8) +\n"
        "  scale_y_continuous(labels = label_dollar()) +\n"
        "  scale_fill_manual(values = c('Furniture' = '#DD6B20', 'Office Supplies' = '#2C7A7B', 'Technology' = '#2B6CB0')) +\n"
        "  coord_flip() + theme_capstone()"
    )

    add_image_figure(
        "figures/exploratory/fig03_category_subcategory_performance.png",
        3, "Cumulative Profitability Across 17 Product Sub-Categories",
        "Horizontal ranking of cumulative profit by sub-category, highlighting the stark contrast between Technology cash generators (Copiers, Phones) and Furniture capital destructors (Tables, Bookcases)."
    )

    add_p(
        "Table 7 presents the complete sub-category ranking. Technology's superior performance is anchored by Copiers ($55,617.82 profit on $149,528.03 sales, 36.6% margin), "
        "Phones ($44,515.73 profit on $330,007.05 sales), and Accessories ($41,936.63 profit on $167,380.32 sales). "
        "Concrete product examples demonstrate this power: the Canon imageCLASS 2200 Advanced Copier generated $25,199.93 in profit across just 8 orders! "
        "Conversely, Furniture is dragged down by Tables, which accumulated a staggering -$17,725.48 loss across 319 transactions (40.8% loss rate, averaging -$55.57 loss per order), "
        "and Bookcases (-$3,472.56 loss across 228 transactions)."
    )

    add_table_from_csv("outputs/tables/03_subcategory_performance_summary.csv", 7, "Sub-Category Cumulative Sales, Profit, and Profit Margins", max_rows=17, custom_col_widths=[1.2, 1.2, 0.7, 1.0, 1.0, 0.8, 0.8])

    doc.add_page_break()

    # ==========================================================================
    # 12. SECTION 9: CUSTOMER & SEGMENT BEHAVIOR
    # ==========================================================================
    add_h1("9. Customer Segment & Order Fulfillment Dynamics")
    add_p(
        "Customer segmentation analysis indicates that Superstore services three distinct customer clienteles: Consumer, Corporate, and Home Office. "
        "Table 9 demonstrates that while Consumer clients represent the majority of volume (5,191 order lines, $1,161,401.34 sales, 50.5% share), "
        "profit margins are remarkably consistent across segments: Consumer (11.53%, $134,119.21 profit), Corporate (13.00%, $91,979.11 profit), and Home Office (13.79%, $60,298.70 profit)."
    )

    add_table_from_csv("outputs/tables/03_segment_performance_summary.csv", 9, "Customer Segment Contribution & Average Order Value", max_rows=3, custom_col_widths=[1.2, 0.9, 1.1, 0.9, 1.1, 0.9, 0.9])

    add_p("Figure 5 visualizes transaction distribution across customer segments and shipping tiers. Embedded R code is provided below:")

    add_code(
        "# R Code to generate Figure 5 (R/04_visualizations.R)\n"
        "seg_ship <- df %>%\n"
        "  group_by(Segment, Ship_Mode) %>%\n"
        "  summarize(Total_Sales = sum(Sales), .groups = 'drop')\n\n"
        "fig05 <- ggplot(seg_ship, aes(x = Ship_Mode, y = Total_Sales, fill = Segment)) +\n"
        "  geom_col(position = position_dodge(width = 0.75), width = 0.7) +\n"
        "  scale_y_continuous(labels = label_dollar()) +\n"
        "  scale_fill_manual(values = c('Consumer' = '#2B6CB0', 'Corporate' = '#2C7A7B', 'Home Office' = '#DD6B20')) +\n"
        "  theme_capstone()"
    )

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
        "The West region leads in both revenue ($725,457.82 across 3,203 orders) and profitability ($108,418.45), achieving a healthy 14.95% profit margin and the lowest loss rate (9.93%). "
        "In contrast, the Central region generates $501,239.89 in sales across 2,323 orders but realizes only $39,706.32 in profit (7.92% margin)—the lowest in the company."
    )

    add_table_from_csv("outputs/tables/03_regional_performance_summary.csv", 8, "Geographic Regional Performance & Loss Incidence Matrix", max_rows=4, custom_col_widths=[1.0, 0.8, 1.0, 0.9, 1.0, 0.9, 0.9, 0.9])

    add_p("Figure 4 displays the multi-panel regional financial matrix. Embedded R code is provided below:")

    add_code(
        "# R Code to generate Figure 4 (R/04_visualizations.R)\n"
        "# Panels p4a (Sales), p4b (Profit), p4c (Margin %), p4d (Loss Rate %)\n"
        "p4a <- ggplot(reg_plot_data, aes(x = Region, y = Total_Sales)) + geom_col(fill = '#2B6CB0') + theme_capstone()\n"
        "p4b <- ggplot(reg_plot_data, aes(x = Region, y = Total_Profit)) + geom_col(fill = '#2C7A7B') + theme_capstone()\n"
        "p4c <- ggplot(reg_plot_data, aes(x = Region, y = Margin_Pct)) + geom_col(fill = '#DD6B20') + theme_capstone()\n"
        "p4d <- ggplot(reg_plot_data, aes(x = Region, y = Loss_Rate_Pct)) + geom_col(fill = '#C53030') + theme_capstone()\n"
        "fig04 <- (p4a + p4b) / (p4c + p4d)"
    )

    add_image_figure(
        "figures/exploratory/fig04_regional_performance_matrix.png",
        4, "Regional Multi-Dimensional Financial Performance Matrix",
        "Four-panel dashboard comparing Regional Sales, Cumulative Profit, Operating Margin %, and Transaction Loss Rate %."
    )

    add_callout(
        "GEOGRAPHIC INSIGHT: THE CENTRAL REGION DILEMMA",
        "The Central region exhibits a staggering 31.90% loss rate (741 out of 2,323 line items lost money). This elevated loss frequency is directly attributable to uncurbed promotional discounting in states such as Texas (where median discounts exceed 30%, resulting in -$25,729.39 cumulative loss across 985 transactions), demonstrating that decentralized regional discount authority can severely erode corporate capital."
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

    add_p("Figure 6 reveals the empirical LOESS smoothing curve illustrating the dramatic 20% discount cliff. Embedded R code is provided below:")

    add_code(
        "# R Code to generate Figure 6 (R/04_visualizations.R)\n"
        "fig06 <- ggplot(df, aes(x = Discount, y = Profit)) +\n"
        "  geom_jitter(aes(color = Profit < 0), alpha = 0.28, size = 1.3, width = 0.01) +\n"
        "  geom_smooth(method = 'loess', color = '#1A365D', linewidth = 1.1, se = TRUE) +\n"
        "  geom_vline(xintercept = 0.20, linetype = 'dashed', color = '#C53030', linewidth = 0.9) +\n"
        "  geom_hline(yintercept = 0, linetype = 'solid', color = '#2D3748', linewidth = 0.7) +\n"
        "  scale_x_continuous(labels = percent_format()) +\n"
        "  scale_y_continuous(limits = c(-1500, 1000), labels = label_dollar()) +\n"
        "  scale_color_manual(name = 'Profit Status', values = c('FALSE' = '#2C7A7B', 'TRUE' = '#C53030')) +\n"
        "  theme_capstone()"
    )

    add_image_figure(
        "figures/exploratory/fig06_discount_vs_profit_cliff.png",
        6, "Empirical Profit Destruction Under Deep Promotional Discounting",
        "Scatter plot with LOESS regression curve demonstrating the catastrophic 20% discount cliff where median profitability collapses below zero."
    )

    add_callout(
        "THE 20% PROMOTIONAL CLIFF",
        "• 0% Discount: 4,798 orders generate $320,987.60 profit ($66.90 mean profit per order) with a 30.1% margin (Loss rate: 0.0%).\n"
        "• 1% - 20% Discount: 3,061 orders yield $104,749.12 profit ($34.22 mean profit) with a 17.2% margin (Loss rate: 9.8%).\n"
        "• >20% Discount: 2,135 orders generate -$139,339.70 cumulative loss (median profit -$62.58, average margin -41.8%, loss rate 58.4%). This tier alone destroys over $90,000 in gross margin."
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

    add_p("Figure 7 visualizes the Spearman correlation matrix heatmap. Embedded R code is provided below:")

    add_code(
        "# R Code to generate Figure 7 (R/04_visualizations.R)\n"
        "s_mat <- round(cor(df[, c('Sales', 'Profit', 'Quantity', 'Discount', 'Shipping_Days', 'Profit_Margin')], method = 'spearman'), 3)\n"
        "s_df <- as.data.frame(as.table(s_mat))\n"
        "fig07 <- ggplot(s_df, aes(x = Var1, y = Var2, fill = Freq)) +\n"
        "  geom_tile(color = 'white', linewidth = 0.6) +\n"
        "  geom_text(aes(label = sprintf('%.2f', Freq)), fontface = 'bold', size = 3.6) +\n"
        "  scale_fill_gradient2(low = '#C53030', mid = '#FFFFFF', high = '#2B6CB0', midpoint = 0, limits = c(-1, 1)) +\n"
        "  theme_capstone()"
    )

    add_image_figure(
        "figures/exploratory/fig07_correlation_heatmap.png",
        7, "Spearman Rank Correlation Matrix of Continuous Financial Variables",
        "Heatmap visualization illustrating monotonic associations between financial variables, emphasizing the robust negative discount-profit link."
    )

    add_p(
        "Crucially, while Pearson correlation between Discount and Profit is modest (r = -0.064) due to extreme outliers and non-linearities, "
        "Spearman's rank correlation reveals a powerful, highly significant monotonic inverse relationship (rho = -0.5434, S = 2.57e+11, p < 0.0001). "
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

    add_p("Figure 8 illustrates the four-panel empirical hypothesis evidence. Embedded R code is provided below:")

    add_code(
        "# R Code to generate Figure 8 (R/05_statistical_analysis.R)\n"
        "# Panel A: Welch's t-test mean profit contrast with 95% CI error bars\n"
        "p8a <- ggplot(t_plot_data, aes(x = Discount_Group, y = Mean_Profit, fill = Discount_Group)) +\n"
        "  geom_col(width = 0.5) + geom_errorbar(aes(ymin = Mean_Profit - 1.96 * SE, ymax = Mean_Profit + 1.96 * SE), width = 0.18) +\n"
        "  scale_y_continuous(labels = label_dollar(), limits = c(-20, 85)) + theme_capstone()\n"
        "# Panel B: ANOVA category means | Panel C: Chi-square mosaic | Panel D: Spearman scatter\n"
        "fig08 <- (p8a + p8b) / (p8c + p8d)"
    )

    add_image_figure(
        "figures/statistical/fig08_hypothesis_test_panels.png",
        8, "Empirical Evidence Panels for Four Core Hypothesis Tests",
        "Four-panel visualization illustrating Welch's t-test mean profit contrast (A), ANOVA category divergence (B), Chi-Square regional loss incidence (C), and Spearman rank correlation trend (D)."
    )

    add_p("Detailed Breakdown with Exact Test Statistics and Code:", bold_prefix="13.1 Inferential Test Details: ")
    add_code(
        "# R Execution Code for All 4 Hypothesis Tests (R/05_statistical_analysis.R)\n"
        "# Test 1: Welch's Two-Sample t-Test\n"
        "welch_t <- t.test(Profit ~ Discount_Group, data = df, var.equal = FALSE)\n"
        "# Result: t = 15.738, df = 9162.2, p-value = 4.36e-55, Cohen's d = 0.318\n\n"
        "# Test 2: One-Way ANOVA & Tukey HSD\n"
        "anova_mod <- aov(Profit ~ Category, data = df)\n"
        "# Result: F(2, 9991) = 54.31, p-value = 3.47e-24, eta-sq = 0.0108\n\n"
        "# Test 3: Pearson Chi-Square Test of Independence\n"
        "chisq_res <- chisq.test(table(df$Region, df$Loss_Status))\n"
        "# Result: X-squared(3) = 436.70, p-value = 2.49e-94, Cramer's V = 0.2090\n\n"
        "# Test 4: Spearman Rank Correlation Test\n"
        "spearman_res <- cor.test(df$Discount, df$Profit, method = 'spearman')\n"
        "# Result: rho = -0.5434, S = 2.57e+11, p-value < 2.2e-16"
    )

    add_p(
        "1. Welch's Two-Sample t-Test: t(9162.2) = 15.74, p = 4.36e-55, Cohen's d = 0.318. Non-discounted transactions (N = 4,798) generated an average profit of $66.90 (SD = $209.64), "
        "compared to -$6.66 (SD = $253.94) for discounted transactions (N = 5,196). The 95% confidence interval of the difference is [$64.40, $82.72]. H0 is rejected."
    )
    add_p(
        "2. One-Way ANOVA: F(2, 9991) = 54.31, p = 3.47e-24, eta-squared = 0.0108. Post-hoc Tukey HSD pairwise comparisons (Table 16) confirm that Technology "
        "($78.75/order) significantly outperforms Furniture ($8.40/order, diff = $70.36, p < 0.0001) and Office Supplies ($20.33/order, diff = $58.42, p < 0.0001)."
    )

    add_table_from_csv("outputs/statistics/tukey_hsd_category_summary.csv", 16, "Post-Hoc Tukey HSD Pairwise Category Profit Comparisons", max_rows=3, custom_col_widths=[1.8, 1.1, 1.1, 1.1, 1.1])

    add_p(
        "3. Pearson Chi-Square Test of Independence: Chi-Square(3) = 436.70, p = 2.49e-94, Cramer's V = 0.2090. As shown in the contingency matrix (Table 15), "
        "regional loss incidence is highly non-random: Central recorded 741 loss transactions (31.90% loss rate) vs 318 in the West (9.93% loss rate)."
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

    add_code(
        "# Model Training & Validation Script (R/06_predictive_modeling.R)\n"
        "set.seed(12345)\n"
        "train_idx <- sample(1:nrow(model_df), size = 0.80 * nrow(model_df))\n"
        "train_set <- model_df[train_idx, ]; test_set <- model_df[-train_idx, ]\n\n"
        "# Model 2: Multiple Linear Regression (OLS)\n"
        "ols_mod <- lm(Profit ~ Sales + Discount + Quantity + Shipping_Days + Category + Sub_Category + Region + Segment + Ship_Mode, data = train_set)\n\n"
        "# Model 4: Champion Random Forest Ensemble\n"
        "rf_mod <- randomForest(Profit ~ ., data = train_set, ntree = 200, mtry = 3, importance = TRUE)\n"
        "test_preds <- predict(rf_mod, newdata = test_set)\n"
        "test_rmse  <- sqrt(mean((test_set$Profit - test_preds)^2)) # $119.16\n"
        "test_r2    <- 1 - (sum((test_set$Profit - test_preds)^2) / sum((test_set$Profit - mean(test_set$Profit))^2)) # 0.7845"
    )

    add_h1("15. Cross-Validation & Out-of-Sample Holdout Evaluation")
    add_p(
        "Table 17 presents the comprehensive performance benchmarking across both 5-fold cross-validation and the untouched holdout test partition. "
        "Evaluation metrics include Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), Coefficient of Determination (R²), and Error Reduction %."
    )

    add_table_from_csv("outputs/model_results/model_comparison_master.csv", 17, "Cross-Validation and Holdout Test Set Performance Master Table", max_rows=4, custom_col_widths=[1.8, 0.7, 0.7, 0.6, 0.7, 0.7, 0.6, 0.7])

    add_p("Figure 9 benchmarks Cross-Validation and Holdout Test RMSE alongside explained variance R². R code is embedded below:")

    add_code(
        "# R Code to generate Figure 9 (R/06_predictive_modeling.R)\n"
        "p9a <- ggplot(comp_plot_data, aes(x = Model, y = RMSE, fill = Evaluation)) +\n"
        "  geom_col(position = position_dodge(width = 0.75), width = 0.7) +\n"
        "  geom_text(aes(label = sprintf('$%.1f', RMSE)), position = position_dodge(width = 0.75), vjust = -0.4, size = 3.1) +\n"
        "  scale_y_continuous(labels = label_dollar(), limits = c(0, 300)) + theme_capstone()\n"
        "p9b <- ggplot(r2_plot_data, aes(x = Model, y = Test_R2, fill = Model)) +\n"
        "  geom_col(width = 0.55, fill = '#2C7A7B') + geom_text(aes(label = sprintf('%.2f', Test_R2)), vjust = -0.4, size = 3.3) +\n"
        "  scale_y_continuous(limits = c(0, 0.90), labels = percent_format()) + theme_capstone()\n"
        "fig09 <- p9a / p9b"
    )

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

    add_p("Figure 12 displays the out-of-sample parity plot for Random Forest. Embedded R code is provided below:")

    add_code(
        "# R Code to generate Figure 12 (R/07_model_diagnostics.R)\n"
        "fig12 <- ggplot(pred_df, aes(x = Profit, y = Predicted_Profit)) +\n"
        "  geom_point(aes(color = Category), alpha = 0.45, size = 1.6) +\n"
        "  geom_abline(intercept = 0, slope = 1, linetype = 'dashed', color = '#C53030', linewidth = 1.0) +\n"
        "  scale_x_continuous(labels = label_dollar(), limits = c(-1500, 2500)) +\n"
        "  scale_y_continuous(labels = label_dollar(), limits = c(-1500, 2500)) +\n"
        "  theme_capstone()"
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
        "Table 20 confirms that Random Forest achieves remarkable precision in commodity sectors: in Office Supplies (1,183 test records), the median absolute error is just $2.41! "
        "In Furniture (444 test records), the median absolute error is $11.96. Table 19 documents a forensic audit of the largest residual errors, revealing that the primary sources of model discrepancy stem from rare, high-value enterprise machines (e.g., $9,099 Lexmark machines) with unique contract pricing."
    )

    add_table_from_csv("outputs/model_results/category_error_breakdown.csv", 20, "Category-Level Out-of-Sample Holdout Error Breakdown", max_rows=3, custom_col_widths=[1.5, 1.2, 1.2, 1.2, 1.2])

    add_table_from_csv("outputs/model_results/top_prediction_errors_audit.csv", 19, "Forensic Audit of Top 10 Prediction Outliers (Holdout Test Set)", max_rows=10, custom_col_widths=[0.7, 0.7, 0.7, 0.7, 0.7, 0.6, 0.5, 1.0, 0.9])

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

    add_p("Figure 10 plots the ranked permutation variable importance. Embedded R code is provided below:")

    add_code(
        "# R Code to generate Figure 10 (R/06_predictive_modeling.R)\n"
        "fig10 <- ggplot(rf_imp, aes(x = reorder(Feature, `%IncMSE`), y = `%IncMSE`)) +\n"
        "  geom_col(fill = '#2B6CB0', width = 0.65, alpha = 0.9) +\n"
        "  geom_text(aes(label = sprintf('%.1f%%', `%IncMSE`)), hjust = -0.15, size = 3.3, fontface = 'bold') +\n"
        "  scale_y_continuous(limits = c(0, 90), labels = function(x) paste0(x, '%')) +\n"
        "  coord_flip() + theme_capstone()"
    )

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
        ("Insight 1: The 20% Discount Cliff Destroys Profitability", "Orders discounted beyond 20% experience an empirical profit collapse to -$62.58 median profit and -41.8% margin, costing the enterprise over $90k in cumulative margin bleed across 2,135 orders."),
        ("Insight 2: Furniture Sub-Categories Suffer Severe Structural Losses", "While Technology generates $145,454.95 in profit (17.39% margin), Furniture produces only $18,451.27 (2.49% margin), driven by severe losses in Tables (-$17,725.48 across 319 transactions) and Bookcases (-$3,472.56)."),
        ("Insight 3: Central Region Suffers Systemic Margin Degradation", "The Central territory exhibits an anomalous 31.90% transaction loss rate (741 loss lines out of 2,323), resulting in an operating margin of just 7.92% compared to 14.95% in the West."),
        ("Insight 4: Technology Hardware Drives Disproportionate Returns", "Copiers ($55,617.82), Phones ($44,515.73), and Accessories ($41,936.63) represent the company's primary profit engine, generating over 49% of all net earnings."),
        ("Insight 5: Fourth-Quarter Revenue Surges Dominate the Annual Cycle", "Over 35% of sales ($278k in Q4 2014) and 38% of profits occur between October and December, requiring highly specialized seasonal procurement and logistics planning."),
        ("Insight 6: Customer Segments Exhibit Identical Underlying Margins", "Consumer (11.53%), Corporate (13.00%), and Home Office (13.79%) generate nearly identical operating margins, indicating that client type does not drive margin variation."),
        ("Insight 7: Standard Class Shipping Represents the Operational Workhorse", "Standard Class fulfillment accounts for 59.7% of order volume (5,968 order lines) with a reliable mean dispatch latency of 5.0 days, proving effective for customer retention."),
        ("Insight 8: OLS Linear Models Underfit Due to Severe Non-Linearities", "Classical regression captures only 41.86% of profit variance due to extreme heteroscedasticity, non-linear threshold effects, and heavy kurtosis (Kurtosis > 280)."),
        ("Insight 9: Random Forest Resolves Retail Complexities (78.45% Test R²)", "The non-linear ensemble cuts test error by 53.59% over baseline, delivering a median absolute prediction error of just $2.41 in commodity office supplies."),
        ("Insight 10: Transaction Size Interacts Non-Linearly with Margin Risk", "High-value enterprise transactions (> $2,000) carry catastrophic capital risk if discounted even moderately; e.g., an 80% discount on a $4,500 Machine produces an immediate -$3,800 loss.")
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
    add_p("1. Observational Nature: The Superstore dataset is observational. While statistical associations and predictive relationships are robustly verified, non-experimental data cannot establish absolute counterfactual causality. Unobserved factors (e.g., localized competitor pricing) may confound findings.")
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
        "identifying systemic margin destruction in Furniture Tables (-$17.7k), uncovering geographic vulnerabilities in the Central region (31.90% loss rate), "
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
