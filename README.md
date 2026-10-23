# Mayur Pandey — Data Analytics Portfolio

**"The Data Dimension"** — A premium, custom-designed portfolio for Mayur Pandey, Aspiring Data Analyst.

Built with **Python Flask**, **MySQL**, pure **HTML5/CSS3**, and **vanilla JavaScript**. No React, no Node.js, no Bootstrap.

---

## Live Preview

Run locally by following the instructions below. Deploy to any Python-capable host (PythonAnywhere, Railway, Render, etc.).

---

## Required Software

| Software   | Version  | Purpose                        |
|------------|----------|--------------------------------|
| Python     | 3.10+    | Application runtime            |
| pip        | latest   | Python package manager         |
| MySQL      | 8.0+     | Contact form message storage   |
| Git        | any      | Version control (optional)     |

---

## Quick Start

### 1. Clone or download the project

```bash
git clone <your-repository-url>
cd mayur-portfolio
```

### 2. Create and activate a Python virtual environment

**Windows (PowerShell)**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Dependencies installed:
- `Flask==3.0.3` — web framework
- `mysql-connector-python==8.4.0` — MySQL database driver
- `python-dotenv==1.0.1` — environment variable loading

### 4. Configure environment variables

Copy the example file and fill in your details:

```bash
cp .env.example .env
```

Open `.env` and set your values:

```ini
SECRET_KEY=your-very-strong-secret-key-here
DB_HOST=localhost
DB_PORT=3306
DB_NAME=mayur_portfolio
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
FLASK_ENV=development
FLASK_DEBUG=True
```

To generate a strong secret key:
```python
python -c "import secrets; print(secrets.token_hex(32))"
```

> **Never commit your `.env` file to version control. It is already listed in `.gitignore`.**

---

## MySQL Setup

### 1. Install MySQL

Download from [https://dev.mysql.com/downloads/](https://dev.mysql.com/downloads/) or install via your system package manager.

### 2. Create the database and table

Log in to MySQL:

```bash
mysql -u root -p
```

Then run the SQL script:

```sql
source database.sql;
```

Or from the command line:

```bash
mysql -u root -p < database.sql
```

This creates:
- Database: `mayur_portfolio`
- Table: `contact_messages` (id, name, email, subject, message, ip_address, created_at)

### 3. Create a dedicated MySQL user (recommended)

```sql
CREATE USER 'mayur_portfolio'@'localhost' IDENTIFIED BY 'strong_password_here';
GRANT SELECT, INSERT ON mayur_portfolio.contact_messages TO 'mayur_portfolio'@'localhost';
FLUSH PRIVILEGES;
```

Update your `.env` with this user's credentials.

---

## Running the Portfolio Locally

```bash
python app.py
```

Open your browser at: **http://localhost:5000**

---

## Adding Your Profile Picture

Your profile photo has been detected at `static/images/Professional.jpg` and is already configured as the profile image throughout the site.

If you ever want to replace it, place a new photo at:
```
static/images/Professional.jpg
```

Requirements:
- High-resolution, professional headshot
- Minimum 600×600 px recommended
- JPEG or PNG format

---

## Adding Your Resume

Place your resume PDF at:
```
static/documents/resume.pdf
```

The "Resume" download button in the hero section and footer will then work automatically.

---

## Adding Your IBM Certificate

Place your IBM SkillsBuild certificate PDF at:
```
static/documents/ibm-certificate.pdf
```

The "View Certificate" link in the Experience section will then resolve correctly.

---

## Updating Projects

All project data is defined in a single location inside [`app.py`](app.py) — the `PROJECTS` list near the top of the file.

For each project you can update:
- `title`, `short_desc`, `category`, `tech`
- `problem`, `dataset`, `approach`, `findings`, `challenges`, `learnings`
- `github` — replace `"#"` with your real GitHub repository URL
- `demo` — add a live demo URL if applicable

Project SVG previews are in:
```
templates/partials/project_svg_<slug>.html
```

Replace these with actual screenshots when available. Place screenshot images in `static/images/projects/`.

---

## Updating Social Links and Contact Details

These appear in `templates/base.html` (footer), `templates/index.html` (contact section), and `templates/contact.html`.

Update the following placeholders with your real information:
- `your.email@example.com` — your professional email
- `https://linkedin.com/in/mayurpandey` — your LinkedIn profile URL
- `https://github.com/mayurpandey` — your GitHub profile URL
- `https://mayurpandey.dev` — your domain (in `base.html` Open Graph tags)

---

## Project Structure

```
mayur-portfolio/
│
├── app.py                  ← Flask application (routes, DB, validation)
├── requirements.txt        ← Python dependencies
├── database.sql            ← MySQL schema creation script
├── .env.example            ← Configuration template (copy to .env)
├── .gitignore
├── README.md
│
├── templates/
│   ├── base.html           ← Shared layout (navbar, footer)
│   ├── index.html          ← Homepage (all sections)
│   ├── projects.html       ← Project gallery
│   ├── project_detail.html ← Case study page
│   ├── contact.html        ← Standalone contact page
│   ├── 404.html            ← Error page
│   └── partials/
│       └── project_svg_*.html   ← Inline SVG project previews
│
└── static/
    ├── css/
    │   └── style.css       ← Complete design system
    ├── js/
    │   └── script.js       ← All interactivity (no frameworks)
    ├── images/
    │   ├── Professional.jpg ← Your profile photo
    │   ├── favicon.svg
    │   └── projects/       ← Optional project screenshots
    └── documents/
        ├── resume.pdf      ← Add your resume here
        └── ibm-certificate.pdf  ← Add your certificate here
```

---

## Deployment

### PythonAnywhere (recommended for beginners)

1. Upload your project files.
2. Create a new web app, choose Flask, select your Python version.
3. Set the working directory and WSGI file path.
4. Add your environment variables in the PythonAnywhere dashboard.
5. Set up a MySQL database and run `database.sql`.

### Railway / Render

1. Push to a GitHub repository.
2. Connect the repository to Railway or Render.
3. Add environment variables in the platform's settings panel.
4. Add a MySQL plugin/addon and run `database.sql`.

### Important for production

- Set `FLASK_ENV=production` and `FLASK_DEBUG=False` in your environment.
- Use a production WSGI server such as Gunicorn: `gunicorn app:app`
- Consider placing the app behind a reverse proxy (Nginx/Caddy) for SSL.

---

## What Was Not Tested Locally

- **MySQL integration**: requires a running MySQL server with credentials in `.env`. The application degrades gracefully — the site works fully without a database; only contact form submissions are affected.
- **Resume and certificate downloads**: require the PDF files to be present at their documented paths.
- **Google Fonts**: loaded from an external CDN; requires an internet connection. The CSS includes system font fallbacks for offline use.

---

## Contact

This portfolio belongs to **Mayur Pandey**. For any questions about this codebase, raise an issue in the repository or use the contact form once the site is live.
