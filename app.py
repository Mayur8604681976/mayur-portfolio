"""
app.py — Mayur Pandey Portfolio
"""

import os
import logging

from flask import Flask, render_template, request, abort
from dotenv import load_dotenv

# ---------------------------------------------------------------------------
# Load environment variables from .env (if present)
# ---------------------------------------------------------------------------
load_dotenv()

# ---------------------------------------------------------------------------
# App setup
# ---------------------------------------------------------------------------
app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Project data (single source of truth — edit here to update the site)
# ---------------------------------------------------------------------------
PROJECTS = [
    {
        "slug": "sales-performance-dashboard",
        "title": "Sales Performance Dashboard",
        "category": "Business Intelligence",
        "category_slug": "bi",
        "tech": ["Microsoft Power BI"],
        "short_desc": (
            "An interactive sales dashboard built in Power BI to explore "
            "business performance, compare metrics across dimensions, and "
            "identify key sales trends."
        ),
        "problem": (
            "Business teams often struggle to interpret large volumes of sales "
            "data spread across multiple sources. This project aimed to "
            "consolidate that data into a single, intuitive dashboard that "
            "makes performance visible at a glance."
        ),
        "dataset": (
            "Sales transaction data containing order details, product "
            "categories, regional information, and time dimensions."
        ),
        "approach": (
            "Data was imported into Power BI, relationships were defined "
            "across tables, and DAX measures were written to calculate "
            "aggregated KPIs. Visual elements including bar charts, line "
            "charts, KPI cards, and slicers were arranged for clarity."
        ),
        "findings": (
            "The dashboard revealed seasonal variation in sales volume and "
            "highlighted which product categories and regions contributed "
            "most consistently. Specific numerical outcomes are intentionally "
            "omitted to avoid presenting unverified figures."
        ),
        "challenges": (
            "Designing a layout that balanced information density with "
            "readability required iterative refinement. DAX calculations for "
            "period-over-period comparisons needed careful scoping."
        ),
        "learnings": (
            "Gained practical experience with Power BI data modelling, DAX "
            "expressions, and the principles of dashboard design for "
            "business audiences."
        ),
        "github": "https://github.com/Mayur8604681976/Executive-Sales-Performance-Dashboard",          # Replace with real URL
        "demo": "",
        "image": "projects/sales-dashboard.svg",
        "featured": True,
    },
    {
        "slug": "hotel-booking-cancellation-analysis",
        "title": "Hotel Booking Cancellation Analysis",
        "category": "Data Analytics",
        "category_slug": "analytics",
        "tech": ["Microsoft Excel"],
        "short_desc": (
            "An analytical project exploring hotel booking data to understand "
            "cancellation patterns and derive actionable business insights "
            "using Excel."
        ),
        "problem": (
            "Hotel cancellations represent a significant operational challenge. "
            "Understanding which booking segments cancel most frequently can "
            "inform better pricing and reservation policies."
        ),
        "dataset": (
            "Hotel booking records including booking lead time, customer "
            "segment, room type, arrival dates, and cancellation status."
        ),
        "approach": (
            "Data was cleaned to remove incomplete records, pivot tables were "
            "used to segment cancellations by customer type and lead time, and "
            "charts were created to visualise the distribution of cancellations "
            "across key dimensions."
        ),
        "findings": (
            "Patterns in the data suggested that bookings made significantly "
            "in advance and those from certain market segments had higher "
            "cancellation rates. Specific percentages are withheld as the "
            "analysis is exploratory."
        ),
        "challenges": (
            "Handling inconsistent date formats and missing values required "
            "systematic data cleaning before any meaningful analysis could "
            "begin."
        ),
        "learnings": (
            "Developed practical Excel skills including pivot tables, "
            "conditional formatting, data validation, and chart creation for "
            "analytical storytelling."
        ),
        "github": "#",          # Replace with real URL
        "demo": "",
        "image": "projects/hotel-analysis.svg",
        "featured": True,
    },
    {
        "slug": "hospital-management-system",
        "title": "Hospital Management System",
        "category": "SQL & Database Projects",
        "category_slug": "sql",
        "tech": ["MySQL", "Python", "HTML", "CSS"],
        "short_desc": (
            "A hospital management application built with MySQL and Python, "
            "organising patient records, appointments, and hospital-related "
            "information through structured database operations."
        ),
        "problem": (
            "Hospital information is often fragmented across paper records and "
            "disconnected systems. This project aimed to organise core hospital "
            "entities — patients, doctors, departments, and appointments — "
            "within a relational database."
        ),
        "dataset": "Custom-designed relational schema for hospital data.",
        "approach": (
            "An entity-relationship model was designed first, translated into "
            "normalised MySQL tables. Python scripts provided an interface for "
            "common operations including record insertion, retrieval, and "
            "appointment scheduling queries."
        ),
        "findings": (
            "The schema successfully modelled core hospital relationships. "
            "SQL queries for patient lookup, appointment filtering by doctor "
            "or date, and department summaries all functioned as designed."
        ),
        "challenges": (
            "Designing referential integrity constraints and handling cascading "
            "updates required careful consideration of real-world hospital "
            "workflows."
        ),
        "learnings": (
            "Deepened understanding of relational database design, "
            "normalisation principles, foreign key constraints, and writing "
            "practical SQL queries for operational use."
        ),
        "github": "https://github.com/Mayur8604681976/hospital-management-system",          # Replace with real URL
        "demo": "",
        "image": "projects/hospital-db.svg",
        "featured": False,
    },
    {
        "slug": "library-management-system",
        "title": "Library Management System",
        "category": "SQL & Database Projects",
        "category_slug": "sql",
        "tech": ["SQL", "MySQL", "Python", "HTML", "CSS"],
        "short_desc": (
            "A library management application using MySQL and Python to "
            "organise book records, member information, and borrowing "
            "transactions through structured database operations."
        ),
        "problem": (
            "Library operations involve managing books, members, loans, and "
            "returns in a consistent and queryable way. This project implemented "
            "that structure using a relational database."
        ),
        "dataset": "Custom schema designed to represent library entities.",
        "approach": (
            "Tables for books, members, categories, and loan transactions were "
            "designed and normalised. Python provided the application layer "
            "for adding, searching, and managing records. SQL queries handled "
            "filtering, availability checks, and overdue detection."
        ),
        "findings": (
            "Core library operations including book search, loan recording, "
            "and member lookup functioned correctly. The schema supported "
            "future extension for additional features."
        ),
        "challenges": (
            "Handling concurrent loan states and ensuring data consistency "
            "across related tables required careful use of transactions and "
            "constraints."
        ),
        "learnings": (
            "Gained experience in schema design, SQL DML and DDL operations, "
            "data integrity enforcement, and building a small Python application "
            "on top of a relational database."
        ),
        "github": "https://github.com/Mayur8604681976/LibraryManagementSystem",          # Replace with real URL
        "demo": "",
        "image": "projects/library-db.svg",
        "featured": False,
    },
    {
        "slug": "ibm-hr-analytics",
        "title": "IBM HR Analytics Project",
        "category": "Data Analytics & Data Science",
        "category_slug": "datascience",
        "tech": ["Python", "Pandas", "Matplotlib", "Seaborn", "Scikit-learn"],
        "short_desc": (
            "An HR analytics project based on the IBM HR Analytics dataset, "
            "covering data preparation, exploratory analysis, visualisation, "
            "and clustering using Python."
        ),
        "problem": (
            "Understanding patterns in employee data — such as attrition "
            "indicators, department distributions, and demographic trends — "
            "can support data-driven HR decision-making."
        ),
        "dataset": (
            "The publicly available IBM HR Analytics Employee Attrition & "
            "Performance dataset, containing employee demographic, role, "
            "compensation, and satisfaction attributes."
        ),
        "approach": (
            "Data was loaded using Pandas and inspected for missing values "
            "and data types. Exploratory data analysis was conducted through "
            "Matplotlib and Seaborn visualisations. Clustering using "
            "Scikit-learn was applied to explore natural groupings in the data "
            "where implemented."
        ),
        "findings": (
            "Visual exploration revealed distributional patterns across "
            "departments, job roles, and satisfaction ratings. Clustering "
            "identified distinct employee profile groups. Specific numerical "
            "outcomes are intentionally omitted to avoid presenting "
            "unverified figures."
        ),
        "challenges": (
            "Encoding categorical variables for clustering and interpreting "
            "cluster results in a meaningful business context required "
            "additional analysis and domain thinking."
        ),
        "learnings": (
            "Developed practical skills in Python data analysis, Pandas "
            "data manipulation, Seaborn/Matplotlib visualisation, and "
            "an introduction to unsupervised learning with Scikit-learn."
        ),
        "github": "https://github.com/Mayur8604681976/IBM-HR-Analytics-Employee-Attrition-Performance-project",          # Replace with real URL
        "demo": "",
        "image": "projects/hr-analytics.svg",
        "featured": True,
    },
]

# Lookup by slug
PROJECT_MAP = {p["slug"]: p for p in PROJECTS}


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    featured = [p for p in PROJECTS if p.get("featured")]
    return render_template("index.html", projects=featured, all_projects=PROJECTS)


@app.route("/projects")
def projects():
    category = request.args.get("category", "all")
    return render_template("projects.html", projects=PROJECTS, active_category=category)


@app.route("/projects/<slug>")
def project_detail(slug):
    project = PROJECT_MAP.get(slug)
    if not project:
        abort(404)
    return render_template("project_detail.html", project=project)



# ---------------------------------------------------------------------------
# Error handlers
# ---------------------------------------------------------------------------

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(e):
    logger.error("Server error: %s", e)
    return render_template("404.html", error_code=500), 500


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    debug = os.environ.get("FLASK_DEBUG", "True").lower() in ("true", "1", "yes")
    app.run(debug=debug, host="0.0.0.0", port=5000)
