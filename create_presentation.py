import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    # 16:9 Widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]
    
    # Theme colors matching DLK / College presentation
    COLOR_DARK_BLUE = RGBColor(10, 25, 47)       # #0A192F
    COLOR_TEAL_HEADER = RGBColor(0, 150, 190)    # #0096BE header in cards
    COLOR_TEAL_BG = RGBColor(225, 243, 250)      # light teal card bg
    COLOR_ACCENT = RGBColor(0, 209, 255)         # #00D1FF
    COLOR_PURPLE = RGBColor(123, 97, 255)        # #7B61FF
    COLOR_TEXT_DARK = RGBColor(30, 41, 59)       # dark gray text
    COLOR_TEXT_MUTED = RGBColor(100, 116, 139)   # muted text
    COLOR_WHITE = RGBColor(255, 255, 255)
    COLOR_RED = RGBColor(220, 38, 38)
    COLOR_BG_LIGHT = RGBColor(248, 250, 252)     # #F8FAFC
    COLOR_TABLE_HDR = RGBColor(43, 163, 209)     # teal table header

    def add_footer(slide, page_num):
        # Footer text frame
        tx_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.0), Inches(11.733), Inches(0.4))
        tf = tx_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = "9/25/2026"
        p.font.size = Pt(10)
        p.font.color.rgb = COLOR_TEXT_MUTED
        
        # Center text
        p2 = tf.add_paragraph()
        p2.text = "SUMMER INTERNSHIP"
        p2.alignment = PP_ALIGN.CENTER
        p2.font.size = Pt(10)
        p2.font.color.rgb = COLOR_TEXT_MUTED
        
        # Right page number
        p3 = tf.add_paragraph()
        p3.text = str(page_num)
        p3.alignment = PP_ALIGN.RIGHT
        p3.font.size = Pt(10)
        p3.font.color.rgb = COLOR_TEXT_MUTED

    def add_standard_header(slide, title_text):
        # Header Title
        tx_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.733), Inches(0.8))
        tf = tx_box.text_frame
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.size = Pt(26)
        p.font.bold = True
        p.font.color.rgb = RGBColor(15, 23, 42)
        p.alignment = PP_ALIGN.CENTER

    # =========================================================================
    # SLIDE 1: TITLE SLIDE
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    
    # College Logo
    if os.path.exists("static/college_logo.png"):
        slide1.shapes.add_picture("static/college_logo.png", Inches(0.8), Inches(0.4), width=Inches(1.5))
    
    # College Header Info
    hdr_box = slide1.shapes.add_textbox(Inches(2.5), Inches(0.4), Inches(10.0), Inches(1.8))
    htf = hdr_box.text_frame
    htf.word_wrap = True
    
    p = htf.paragraphs[0]
    p.text = "Dr. N.G.P. INSTITUTE OF TECHNOLOGY"
    p.font.size = Pt(22)
    p.font.bold = True
    p.font.color.rgb = RGBColor(15, 23, 42)
    p.alignment = PP_ALIGN.CENTER
    
    sub_lines = [
        "Coimbatore - 48",
        "(An Autonomous Institution)",
        "(Approved by AICTE, New Delhi & Affiliated to Anna University, Chennai)",
        "Recognized by UGC & Accredited by NAAC A+ and NBA (CSE, BME, EEE, ECE and Mech) Dr.N.G.P. Nagar,",
        "Kalapatti Main Rd, Coimbatore, Tamil Nadu 641048",
        "Ph No: 0422 - 236 9105, Fax: 04222369106, E-mail: info@drngpit.ac.in"
    ]
    for line in sub_lines:
        sp = htf.add_paragraph()
        sp.text = line
        sp.font.size = Pt(10.5)
        sp.font.color.rgb = RGBColor(30, 41, 59)
        sp.alignment = PP_ALIGN.CENTER
        if "Autonomous" in line:
            sp.font.bold = True

    # Department
    dept_box = slide1.shapes.add_textbox(Inches(0.8), Inches(2.5), Inches(11.733), Inches(0.5))
    dtf = dept_box.text_frame
    dp = dtf.paragraphs[0]
    dp.text = "DEPARTMENT OF ARTIFICIAL INTELLIGENCE AND DATA SCIENCE"
    dp.font.size = Pt(16)
    dp.font.bold = True
    dp.font.color.rgb = RGBColor(15, 23, 42)
    dp.alignment = PP_ALIGN.CENTER

    # Course details
    course_box = slide1.shapes.add_textbox(Inches(0.8), Inches(3.2), Inches(11.733), Inches(1.2))
    ctf = course_box.text_frame
    cp1 = ctf.paragraphs[0]
    cp1.text = "22EEC501 – PROFESSIONAL READINESS COURSE"
    cp1.font.size = Pt(17)
    cp1.font.bold = True
    cp1.font.color.rgb = RGBColor(15, 23, 42)
    cp1.alignment = PP_ALIGN.CENTER

    cp2 = ctf.add_paragraph()
    cp2.text = "on"
    cp2.font.size = Pt(14)
    cp2.font.bold = True
    cp2.font.color.rgb = RGBColor(15, 23, 42)
    cp2.alignment = PP_ALIGN.CENTER

    cp3 = ctf.add_paragraph()
    cp3.text = "16/05/2026 – 30/05/2026"
    cp3.font.size = Pt(16)
    cp3.font.bold = True
    cp3.font.color.rgb = COLOR_RED
    cp3.alignment = PP_ALIGN.CENTER

    # Faculty & Student Details (2 columns)
    fac_box = slide1.shapes.add_textbox(Inches(1.2), Inches(4.8), Inches(5.0), Inches(1.8))
    ftf = fac_box.text_frame
    fp1 = ftf.paragraphs[0]
    fp1.text = "FACULTY IN-CHARGE"
    fp1.font.size = Pt(14)
    fp1.font.bold = True
    fp1.font.color.rgb = RGBColor(15, 23, 42)
    
    fp2 = ftf.add_paragraph()
    fp2.text = "Ms. C. DIVYA REVATHI M.E."
    fp2.font.size = Pt(14)
    fp2.font.bold = True
    fp2.font.underline = True
    fp2.font.color.rgb = RGBColor(15, 23, 42)

    fp3 = ftf.add_paragraph()
    fp3.text = "Assistant Professor (AI & DS)"
    fp3.font.size = Pt(14)
    fp3.font.bold = True
    fp3.font.color.rgb = RGBColor(15, 23, 42)

    stud_box = slide1.shapes.add_textbox(Inches(7.2), Inches(4.8), Inches(5.2), Inches(1.8))
    stf = stud_box.text_frame
    stp1 = stf.paragraphs[0]
    stp1.text = "STUDENT NAME: DHANVANTH SENTHIL KUMAR"
    stp1.font.size = Pt(14)
    stp1.font.bold = True
    stp1.font.color.rgb = RGBColor(15, 23, 42)

    stp2 = stf.add_paragraph()
    stp2.text = "REG NO: 710724243020"
    stp2.font.size = Pt(14)
    stp2.font.bold = True
    stp2.font.color.rgb = RGBColor(15, 23, 42)
    
    add_footer(slide1, 1)

    # =========================================================================
    # SLIDE 2: OUTLINE
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    add_standard_header(slide2, "OUTLINE")
    
    out_box = slide2.shapes.add_textbox(Inches(1.5), Inches(1.5), Inches(10.0), Inches(5.2))
    otf = out_box.text_frame
    otf.word_wrap = True
    
    items = [
        "ABOUT THE COMPANY",
        "KEY LEARNINGS FROM THE INTERNSHIP",
        "ABOUT THE PROJECT",
        "TOOLS AND TECHNOLOGY USED",
        "LIST OF MODULES WITH EXPLANATION",
        "IMPLEMENTATION",
        "OUTPUT SCREENSHOTS",
        "CONCLUSION",
        "CONTRIBUTIONS IN THE PROJECT",
        "REFERENCES"
    ]
    for i, item in enumerate(items):
        p = otf.paragraphs[0] if i == 0 else otf.add_paragraph()
        p.text = f"➤   {item}"
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = RGBColor(15, 23, 42)
        p.space_before = Pt(8)
    
    add_footer(slide2, 2)

    # =========================================================================
    # SLIDE 3: ABOUT THE COMPANY
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    add_standard_header(slide3, "ABOUT THE COMPANY")
    
    # Table of company info
    rows, cols = 7, 2
    left, top, width, height = Inches(1.5), Inches(1.6), Inches(10.333), Inches(4.8)
    tbl_shape = slide3.shapes.add_table(rows, cols, left, top, width, height)
    table = tbl_shape.table
    table.columns[0].width = Inches(3.8)
    table.columns[1].width = Inches(6.533)
    
    table_data = [
        ["COMPANY NAME", "DLK SOFTWARE SOLUTIONS"],
        ["STARTED YEAR", "2012"],
        ["LOCATION", "Vadapalani, Chennai, Tamil Nadu"],
        ["SERVICES OFFERED", "Software Development, Web & Mobile Apps, Data Science & AI, Digital Marketing & Internships"],
        ["INDUSTRY MENTOR NAME", "Mr. Satheesh Kumar"],
        ["DESIGNATION", "Chief Executive Officer"],
        ["DURATION OF INTERN", "16/05/2026 – 30/05/2026 (15 days)"]
    ]
    
    for r_idx, row in enumerate(table_data):
        for c_idx, cell_value in enumerate(row):
            cell = table.cell(r_idx, c_idx)
            cell.text = cell_value
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            cell_p = cell.text_frame.paragraphs[0]
            cell_p.font.size = Pt(13)
            if r_idx == 0:
                cell.fill.solid()
                cell.fill.fore_color.rgb = COLOR_TABLE_HDR
                cell_p.font.bold = True
                cell_p.font.color.rgb = COLOR_WHITE
                cell_p.alignment = PP_ALIGN.CENTER
            else:
                cell.fill.solid()
                cell.fill.fore_color.rgb = RGBColor(238, 246, 252) if r_idx % 2 == 1 else COLOR_WHITE
                cell_p.font.color.rgb = RGBColor(15, 23, 42)
                if c_idx == 0:
                    cell_p.font.bold = True
                    cell_p.alignment = PP_ALIGN.CENTER
                else:
                    cell_p.alignment = PP_ALIGN.LEFT
                    
    add_footer(slide3, 3)

    # =========================================================================
    # SLIDE 4: KEY LEARNINGS FROM THE INTERNSHIP
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    add_standard_header(slide4, "KEY LEARNINGS FROM THE INTERNSHIP")
    
    kl_box = slide4.shapes.add_textbox(Inches(1.2), Inches(1.6), Inches(11.0), Inches(5.0))
    kltf = kl_box.text_frame
    kltf.word_wrap = True
    
    kp1 = kltf.paragraphs[0]
    kp1.text = "Technical Skills"
    kp1.font.size = Pt(18)
    kp1.font.bold = True
    kp1.font.color.rgb = RGBColor(15, 23, 42)
    kp1.space_after = Pt(12)
    
    points = [
        ("Programming & Data Handling", "Python, NumPy, Pandas and Matplotlib"),
        ("Machine Learning", "Regression, Classification, Clustering and Model Evaluation"),
        ("Deep Learning", "Artificial Neural Networks (ANN) and CNN for image classification"),
        ("Deployment & Testing", "Flask API and Postman"),
        ("Generative AI, Prompt Engineering and Responsible AI", "Fairness, transparency, privacy, and ethics")
    ]
    
    for title, desc in points:
        p = kltf.add_paragraph()
        p.text = f"•  {title} – {desc}"
        p.font.size = Pt(15.5)
        p.font.color.rgb = RGBColor(30, 41, 59)
        p.space_before = Pt(12)
        
    add_footer(slide4, 4)

    # =========================================================================
    # SLIDE 5: ABOUT THE PROJECT
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    add_standard_header(slide5, "ABOUT THE PROJECT")
    
    # Left column: Description & Objectives
    left_box = slide5.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(7.5), Inches(5.2))
    ltf = left_box.text_frame
    ltf.word_wrap = True
    
    p = ltf.paragraphs[0]
    p.text = "AI-Powered Diabetes Predictor"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = RGBColor(15, 23, 42)
    
    p_desc = ltf.add_paragraph()
    p_desc.text = "A machine learning and healthcare web application that predicts whether a patient belongs to the diabetic or non-diabetic class from numerical clinical features – Pregnancies, Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, Pedigree, and Age. The trained models are served through a Flask API and presented in the DiabetesPredict.AI dashboard."
    p_desc.font.size = Pt(12.5)
    p_desc.font.color.rgb = RGBColor(51, 65, 85)
    p_desc.space_before = Pt(6)
    p_desc.space_after = Pt(12)
    
    p_obj_hdr = ltf.add_paragraph()
    p_obj_hdr.text = "Objectives"
    p_obj_hdr.font.size = Pt(15)
    p_obj_hdr.font.bold = True
    p_obj_hdr.font.color.rgb = RGBColor(15, 23, 42)
    
    objs = [
        "Prepare raw clinical data through zero-value cleaning, median imputation, scaling, and feature engineering.",
        "Train and compare supervised classification models (Logistic Regression, KNN, Decision Tree, ANN) on real-world medical data.",
        "Evaluate performance with standard metrics (Accuracy, Precision, Recall, Confusion Matrix) and identify sources of error.",
        "Deploy the trained models as a usable Flask API with an interactive web dashboard."
    ]
    for obj in objs:
        op = ltf.add_paragraph()
        op.text = f"•  {obj}"
        op.font.size = Pt(12)
        op.font.color.rgb = RGBColor(51, 65, 85)
        op.space_before = Pt(6)

    # Right column: Project Workflow
    right_box = slide5.shapes.add_textbox(Inches(8.8), Inches(2.2), Inches(3.8), Inches(4.0))
    rtf = right_box.text_frame
    rtf.word_wrap = True
    
    r_hdr = rtf.paragraphs[0]
    r_hdr.text = "Project workflow :"
    r_hdr.font.size = Pt(16)
    r_hdr.font.bold = True
    r_hdr.font.color.rgb = RGBColor(15, 23, 42)
    r_hdr.space_after = Pt(10)
    
    wf_steps = [
        "1. Data collection & preprocessing",
        "2. Feature engineering & EDA",
        "3. Model training & evaluation",
        "4. Flask API & dashboard deployment"
    ]
    for st in wf_steps:
        sp = rtf.add_paragraph()
        sp.text = st
        sp.font.size = Pt(13)
        sp.font.color.rgb = RGBColor(51, 65, 85)
        sp.space_before = Pt(8)
        
    add_footer(slide5, 5)

    # =========================================================================
    # SLIDE 6: SYSTEM REQUIREMENTS
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    add_standard_header(slide6, "SYSTEM REQUIREMENTS")
    
    sr_box = slide6.shapes.add_textbox(Inches(1.2), Inches(1.6), Inches(11.0), Inches(5.0))
    srtf = sr_box.text_frame
    srtf.word_wrap = True
    
    p = srtf.paragraphs[0]
    p.text = "Software:"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = RGBColor(15, 23, 42)
    
    softwares = [
        "Visual Studio Code",
        "Python, Jupyter Notebook / Google Colab",
        "Web Browser",
        "Postman"
    ]
    for s in softwares:
        sp = srtf.add_paragraph()
        sp.text = f"•  {s}"
        sp.font.size = Pt(14)
        sp.font.color.rgb = RGBColor(51, 65, 85)
        sp.space_before = Pt(4)
        
    p_dev = srtf.add_paragraph()
    p_dev.text = "Development Environment"
    p_dev.font.size = Pt(17)
    p_dev.font.bold = True
    p_dev.font.color.rgb = RGBColor(15, 23, 42)
    p_dev.space_before = Pt(16)
    
    envs = [
        "Machine Learning: Scikit-Learn, Pandas, NumPy",
        "Deep Learning: TensorFlow / Keras",
        "Backend & API: Flask",
        "Frontend: HTML templates & CSS"
    ]
    for e in envs:
        ep = srtf.add_paragraph()
        ep.text = f"•  {e}"
        ep.font.size = Pt(14)
        ep.font.color.rgb = RGBColor(51, 65, 85)
        ep.space_before = Pt(4)

    add_footer(slide6, 6)

    # =========================================================================
    # SLIDE 7: TOOLS AND TECHNOLOGIES USED
    # =========================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    add_standard_header(slide7, "TOOLS AND TECHNOLOGIES USED")
    
    col_data = [
        ("Data & Visualisation", [
            ("Python", "Core programming language"),
            ("NumPy", "Numerical arrays, vectorised maths"),
            ("Pandas", "Data loading, cleaning, analysis"),
            ("Matplotlib", "Charts and data visualisation")
        ]),
        ("Machine Learning", [
            ("Scikit-Learn", "Classification, clustering, evaluation"),
            ("TensorFlow / Keras", "Deep learning and neural networks"),
            ("PyTorch", "Deep learning framework (introduction)")
        ]),
        ("Deployment", [
            ("Flask", "REST API to serve the model"),
            ("Postman", "Testing prediction requests"),
            ("Web UI", "DiabetesPredict.AI dashboard")
        ]),
        ("Environments", [
            ("Jupyter Notebook", "Interactive coding and experiments"),
            ("Google Colab", "Cloud notebooks, no local setup"),
            ("VS Code", "Project and script development")
        ])
    ]
    
    card_width = Inches(2.7)
    card_gap = Inches(0.25)
    start_left = Inches(1.0)
    top_pos = Inches(1.6)
    
    for i, (title, items_list) in enumerate(col_data):
        c_left = start_left + i * (card_width + card_gap)
        
        # Header block
        hdr_shape = slide7.shapes.add_shape(MSO_SHAPE.RECTANGLE, c_left, top_pos, card_width, Inches(0.6))
        hdr_shape.fill.solid()
        hdr_shape.fill.fore_color.rgb = COLOR_TABLE_HDR
        hdr_shape.line.color.rgb = COLOR_TABLE_HDR
        hdr_tf = hdr_shape.text_frame
        hdr_p = hdr_tf.paragraphs[0]
        hdr_p.text = title
        hdr_p.font.size = Pt(13)
        hdr_p.font.bold = True
        hdr_p.font.color.rgb = COLOR_WHITE
        hdr_p.alignment = PP_ALIGN.CENTER
        
        # Body block
        body_shape = slide7.shapes.add_shape(MSO_SHAPE.RECTANGLE, c_left, top_pos + Inches(0.6), card_width, Inches(4.5))
        body_shape.fill.solid()
        body_shape.fill.fore_color.rgb = COLOR_BG_LIGHT
        body_shape.line.color.rgb = RGBColor(226, 232, 240)
        btf = body_shape.text_frame
        btf.word_wrap = True
        
        first = True
        for name, desc in items_list:
            p_n = btf.paragraphs[0] if first else btf.add_paragraph()
            first = False
            p_n.text = name
            p_n.font.size = Pt(13)
            p_n.font.bold = True
            p_n.font.color.rgb = RGBColor(15, 23, 42)
            p_n.space_before = Pt(8)
            
            p_d = btf.add_paragraph()
            p_d.text = desc
            p_d.font.size = Pt(10)
            p_d.font.color.rgb = RGBColor(100, 116, 139)
            p_d.space_before = Pt(1)
            p_d.space_after = Pt(4)

    add_footer(slide7, 7)

    # =========================================================================
    # SLIDE 8: LIST OF MODULES WITH EXPLANATION
    # =========================================================================
    slide8 = prs.slides.add_slide(blank_layout)
    add_standard_header(slide8, "LIST OF MODULES WITH EXPLANATION")
    
    modules_6 = [
        ("1", "Data Preprocessing", "Loads diabetes.csv (768 records), cleans invalid zeros, imputes missing values with median, and scales numeric features."),
        ("2", "Exploratory Data Analysis", "Pandas summaries, class balance checks, and correlation checks with Matplotlib charts show Glucose and BMI drive risk most."),
        ("3", "Feature Engineering", "Creates interaction feature (Glucose * Age), evaluates correlation rankings, and prepares optimal training matrices."),
        ("4", "Model Training & Evaluation", "Trains Logistic Regression, KNN, and Decision Trees; evaluates with Accuracy, Precision, Recall, and Confusion Matrices."),
        ("5", "Clustering & Neural Network", "Demonstrates K-Means & Hierarchical grouping (K=3) and builds a Keras ANN with ReLU and Sigmoid activations."),
        ("6", "DiabetesPredict.AI Dashboard", "Web front-end where patient health metrics are entered and independent multi-model prediction reports are generated.")
    ]
    
    m_w = Inches(3.6)
    m_h = Inches(2.2)
    gap_x = Inches(0.4)
    gap_y = Inches(0.4)
    grid_left = Inches(1.0)
    grid_top = Inches(1.6)
    
    for idx, (num, title, desc) in enumerate(modules_6):
        r_i = idx // 3
        c_i = idx % 3
        pos_x = grid_left + c_i * (m_w + gap_x)
        pos_y = grid_top + r_i * (m_h + gap_y)
        
        # Card background
        card = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, pos_x, pos_y, m_w, m_h)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_BG_LIGHT
        card.line.color.rgb = RGBColor(203, 213, 225)
        
        # Number badge circle
        circle = slide8.shapes.add_shape(MSO_SHAPE.OVAL, pos_x + Inches(0.2), pos_y + Inches(0.2), Inches(0.55), Inches(0.55))
        circle.fill.solid()
        circle.fill.fore_color.rgb = COLOR_TABLE_HDR
        circle.line.color.rgb = COLOR_TABLE_HDR
        ctf = circle.text_frame
        cp = ctf.paragraphs[0]
        cp.text = num
        cp.font.size = Pt(14)
        cp.font.bold = True
        cp.font.color.rgb = COLOR_WHITE
        cp.alignment = PP_ALIGN.CENTER
        
        # Title
        t_box = slide8.shapes.add_textbox(pos_x + Inches(0.85), pos_y + Inches(0.15), m_w - Inches(0.95), Inches(0.6))
        ttf = t_box.text_frame
        ttf.word_wrap = True
        tp = ttf.paragraphs[0]
        tp.text = title
        tp.font.size = Pt(13)
        tp.font.bold = True
        tp.font.color.rgb = RGBColor(15, 23, 42)
        
        # Desc
        d_box = slide8.shapes.add_textbox(pos_x + Inches(0.2), pos_y + Inches(0.8), m_w - Inches(0.4), m_h - Inches(0.9))
        dtf = d_box.text_frame
        dtf.word_wrap = True
        dp = dtf.paragraphs[0]
        dp.text = desc
        dp.font.size = Pt(10.5)
        dp.font.color.rgb = RGBColor(71, 85, 105)

    add_footer(slide8, 8)

    # =========================================================================
    # SLIDE 9: IMPLEMENTATION
    # =========================================================================
    slide9 = prs.slides.add_slide(blank_layout)
    add_standard_header(slide9, "IMPLEMENTATION")
    
    impl_6 = [
        ("1", "Data Collection & Preprocessing", [
            "Collected diabetes.csv dataset (768 records)",
            "Handled missing and zero readings in vital signs",
            "Imputed missing observations using column median",
            "Standardized features with StandardScaler"
        ]),
        ("2", "Exploratory Data Analysis", [
            "Pandas summaries and statistical analysis",
            "Visualized distributions using Matplotlib",
            "Correlation analysis to identify key risk features",
            "Found Glucose and BMI strongly correlate with class"
        ]),
        ("3", "Feature Engineering", [
            "Created interaction feature (Glucose * Age)",
            "Calculated correlation importance scores",
            "Engineered optimal feature input representations",
            "Prepared train/test split for validation"
        ]),
        ("4", "Model Training", [
            "Trained Logistic Regression, KNN, Decision Tree",
            "Built & trained Keras Artificial Neural Network",
            "Executed K-Means & Hierarchical clustering",
            "Optimized models on 80% training split"
        ]),
        ("5", "Model Evaluation", [
            "Evaluated Accuracy, Precision, and Recall",
            "Generated Confusion Matrices (TP, TN, FP, FN)",
            "Compared performance across all classifiers",
            "Selected ANN (75.3%) & Decision Tree for deployment"
        ]),
        ("6", "Flask API Deployment & Web Dashboard", [
            "Integrated trained models with Flask REST API",
            "Tested prediction endpoints and payload validation",
            "Developed 10-page responsive web dashboard",
            "Embedded medical disclaimer for Responsible AI"
        ])
    ]
    
    for idx, (num, title, bullets) in enumerate(impl_6):
        r_i = idx // 3
        c_i = idx % 3
        pos_x = grid_left + c_i * (m_w + gap_x)
        pos_y = grid_top + r_i * (m_h + gap_y)
        
        card = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, pos_x, pos_y, m_w, m_h)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_BG_LIGHT
        card.line.color.rgb = RGBColor(203, 213, 225)
        
        circle = slide9.shapes.add_shape(MSO_SHAPE.OVAL, pos_x + Inches(0.15), pos_y + Inches(0.15), Inches(0.45), Inches(0.45))
        circle.fill.solid()
        circle.fill.fore_color.rgb = COLOR_TABLE_HDR
        circle.line.color.rgb = COLOR_TABLE_HDR
        ctf = circle.text_frame
        cp = ctf.paragraphs[0]
        cp.text = num
        cp.font.size = Pt(12)
        cp.font.bold = True
        cp.font.color.rgb = COLOR_WHITE
        cp.alignment = PP_ALIGN.CENTER
        
        t_box = slide9.shapes.add_textbox(pos_x + Inches(0.65), pos_y + Inches(0.1), m_w - Inches(0.75), Inches(0.55))
        ttf = t_box.text_frame
        ttf.word_wrap = True
        tp = ttf.paragraphs[0]
        tp.text = title
        tp.font.size = Pt(11.5)
        tp.font.bold = True
        tp.font.color.rgb = RGBColor(15, 23, 42)
        
        d_box = slide9.shapes.add_textbox(pos_x + Inches(0.15), pos_y + Inches(0.65), m_w - Inches(0.3), m_h - Inches(0.7))
        dtf = d_box.text_frame
        dtf.word_wrap = True
        
        first = True
        for b in bullets:
            bp = dtf.paragraphs[0] if first else dtf.add_paragraph()
            first = False
            bp.text = f"• {b}"
            bp.font.size = Pt(9.2)
            bp.font.color.rgb = RGBColor(51, 65, 85)
            bp.space_before = Pt(2)

    add_footer(slide9, 9)

    # =========================================================================
    # SLIDE 10: OUTPUT SCREENSHOTS (WEB DASHBOARD UI)
    # =========================================================================
    slide10 = prs.slides.add_slide(blank_layout)
    add_standard_header(slide10, "OUTPUT SCREENSHOTS")
    
    # Place 2 UI mockup images side by side
    img1 = "static/presentation_assets/ui_prediction_dashboard.png"
    img2 = "static/presentation_assets/ui_analytics_dashboard.png"
    
    if os.path.exists(img1):
        slide10.shapes.add_picture(img1, Inches(1.0), Inches(1.6), width=Inches(5.4))
    if os.path.exists(img2):
        slide10.shapes.add_picture(img2, Inches(6.8), Inches(1.6), width=Inches(5.4))
        
    add_footer(slide10, 10)

    # =========================================================================
    # SLIDE 11: OUTPUT SCREENSHOTS (EDA & MODEL EVALUATION PLOTS)
    # =========================================================================
    slide11 = prs.slides.add_slide(blank_layout)
    add_standard_header(slide11, "OUTPUT SCREENSHOTS")
    
    plot1 = "static/plots/class_dist.png"
    plot2 = "static/plots/feature_histograms.png"
    plot3 = "static/plots/correlation_matrix.png"
    plot4 = "static/plots/model_comparison.png"
    
    # 4 grid plots
    if os.path.exists(plot1):
        slide11.shapes.add_picture(plot1, Inches(1.0), Inches(1.5), width=Inches(2.6))
    if os.path.exists(plot2):
        slide11.shapes.add_picture(plot2, Inches(3.9), Inches(1.5), width=Inches(2.8))
    if os.path.exists(plot3):
        slide11.shapes.add_picture(plot3, Inches(7.0), Inches(1.5), width=Inches(2.7))
    if os.path.exists(plot4):
        slide11.shapes.add_picture(plot4, Inches(10.0), Inches(1.5), width=Inches(2.5))
        
    # Lower row: Clustering & Confusion Matrix
    plot5 = "static/plots/clustering_kmeans.png"
    plot6 = "static/plots/clustering_hierarchical.png"
    plot7 = "static/plots/cm_logistic_regression.png"
    plot8 = "static/plots/ann_training.png"
    
    if os.path.exists(plot5):
        slide11.shapes.add_picture(plot5, Inches(1.0), Inches(4.2), width=Inches(2.6))
    if os.path.exists(plot6):
        slide11.shapes.add_picture(plot6, Inches(3.9), Inches(4.2), width=Inches(2.6))
    if os.path.exists(plot7):
        slide11.shapes.add_picture(plot7, Inches(6.8), Inches(4.2), width=Inches(2.6))
    if os.path.exists(plot8):
        slide11.shapes.add_picture(plot8, Inches(9.7), Inches(4.2), width=Inches(2.8))

    add_footer(slide11, 11)

    # =========================================================================
    # SLIDE 12: CONCLUSION
    # =========================================================================
    slide12 = prs.slides.add_slide(blank_layout)
    add_standard_header(slide12, "CONCLUSION")
    
    conc_box = slide12.shapes.add_textbox(Inches(1.2), Inches(1.8), Inches(11.0), Inches(4.8))
    ctf2 = conc_box.text_frame
    ctf2.word_wrap = True
    
    conc_points = [
        "The 15-day internship at DLK Software Solutions provided practical exposure to Artificial Intelligence, Machine Learning and Data Science, and helped bridge academic knowledge with real-world application.",
        "The AI-Powered Diabetes Prediction & Healthcare Intelligence System successfully integrated data preprocessing, classification algorithms, unsupervised clustering, ANN, and a Flask API tested with Postman.",
        "The internship strengthened my skills in Python, NumPy, Pandas, Matplotlib, Scikit-Learn, TensorFlow/Keras, Flask and Postman.",
        "It also improved my problem-solving, debugging and systematic project development skills."
    ]
    
    first = True
    for cp_text in conc_points:
        p = ctf2.paragraphs[0] if first else ctf2.add_paragraph()
        first = False
        p.text = f"•  {cp_text}"
        p.font.size = Pt(15.5)
        p.font.color.rgb = RGBColor(30, 41, 59)
        p.space_before = Pt(16)
        
    add_footer(slide12, 12)

    # =========================================================================
    # SLIDE 13: CONTRIBUTIONS IN THE PROJECT
    # =========================================================================
    slide13 = prs.slides.add_slide(blank_layout)
    add_standard_header(slide13, "CONTRIBUTIONS IN THE PROJECT")
    
    cont_box = slide13.shapes.add_textbox(Inches(1.2), Inches(1.6), Inches(11.0), Inches(5.0))
    cntf = cont_box.text_frame
    cntf.word_wrap = True
    
    contributions = [
        "Prepared and engineered features for model training and resolved clinical zero readings",
        "Trained and evaluated supervised classification models (Logistic Regression, KNN, Decision Tree)",
        "Constructed and optimized a multi-layer Artificial Neural Network using TensorFlow/Keras",
        "Implemented K-Means and Hierarchical clustering for unsupervised patient profiling",
        "Integrated the trained models with a Flask-based REST API and web application",
        "Tested API requests and responses systematically using Postman",
        "Tested each stage separately and debugged errors systematically",
        "Worked on improving the overall application workflow, data privacy and responsible AI practices"
    ]
    
    first = True
    for c_text in contributions:
        p = cntf.paragraphs[0] if first else cntf.add_paragraph()
        first = False
        p.text = f"•  {c_text}"
        p.font.size = Pt(14)
        p.font.color.rgb = RGBColor(30, 41, 59)
        p.space_before = Pt(10)
        
    add_footer(slide13, 13)

    # =========================================================================
    # SLIDE 14: REFERENCES
    # =========================================================================
    slide14 = prs.slides.add_slide(blank_layout)
    add_standard_header(slide14, "REFERENCES")
    
    ref_box = slide14.shapes.add_textbox(Inches(1.2), Inches(1.6), Inches(11.0), Inches(5.0))
    rtf2 = ref_box.text_frame
    rtf2.word_wrap = True
    
    refs = [
        ("Python Documentation", "https://docs.python.org/3/"),
        ("NumPy Documentation", "https://numpy.org/doc/"),
        ("Pandas Documentation", "https://pandas.pydata.org/docs/"),
        ("Matplotlib Documentation", "https://matplotlib.org/stable/"),
        ("Scikit-Learn Documentation", "https://scikit-learn.org/stable/"),
        ("TensorFlow & Keras Documentation", "https://www.tensorflow.org/"),
        ("Flask Documentation", "https://flask.palletsprojects.com/"),
        ("Postman Documentation", "https://learning.postman.com/docs/")
    ]
    
    first = True
    for title, link in refs:
        p = rtf2.paragraphs[0] if first else rtf2.add_paragraph()
        first = False
        p.text = f"•  {title} – {link}"
        p.font.size = Pt(14.5)
        p.font.color.rgb = RGBColor(30, 41, 59)
        p.space_before = Pt(10)
        
    add_footer(slide14, 14)

    # =========================================================================
    # SLIDE 15: THANK YOU
    # =========================================================================
    slide15 = prs.slides.add_slide(blank_layout)
    
    # Soft mint background
    bg_shape = slide15.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg_shape.fill.solid()
    bg_shape.fill.fore_color.rgb = RGBColor(190, 222, 216) # #BEDFD8 soft mint
    bg_shape.line.color.rgb = RGBColor(190, 222, 216)
    
    ty_box = slide15.shapes.add_textbox(Inches(2.0), Inches(2.5), Inches(9.333), Inches(2.5))
    ty_tf = ty_box.text_frame
    tp1 = ty_tf.paragraphs[0]
    tp1.text = "Thank"
    tp1.font.size = Pt(64)
    tp1.font.bold = True
    tp1.font.color.rgb = COLOR_WHITE
    tp1.alignment = PP_ALIGN.CENTER
    
    tp2 = ty_tf.add_paragraph()
    tp2.text = "you"
    tp2.font.size = Pt(64)
    tp2.font.bold = True
    tp2.font.color.rgb = COLOR_WHITE
    tp2.alignment = PP_ALIGN.CENTER

    os.makedirs("presentation", exist_ok=True)
    out_path = "presentation/Diabetes_Prediction_AI_Internship_Presentation.pptx"
    prs.save(out_path)
    print(f"Presentation successfully created at {out_path}")

if __name__ == "__main__":
    create_deck()
