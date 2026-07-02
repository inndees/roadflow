"""
RoadFlow AI - Flask Web Application for Civil Construction Scheduling
===============================================================
Simplified version focusing on Project Creation Page only.

Routes:
- /           -> Project Creation Page (main dashboard)
- /create-gantt  -> Handle form submission and show success message

This version does NOT use database, authentication, or real AI yet.
"""

from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)


# ==============================================================================
# Route 1: Home / Project Creation Page
# ==============================================================================
@app.route("/", methods=["GET", "POST"])
def project_creation_page():
    
    return render_template("index.html")


# ==============================================================================
# API Endpoint: Create Gantt Chart Button Handler
# ==============================================================================
@app.route("/gantt", methods=["GET", "POST"])
def create_gantt_chart():

    return render_template("gantt.html", project_name="Road Construction Project", tasks=[
        {
            "id": "1",
            "name": "Site Clearing",
            "start": "2026-07-01",
            "end": "2026-07-03",
            "progress": 20
        },
        {
            "id": "2",
            "name": "Asphalt Laying",
            "start": "2026-07-04",
            "end": "2026-07-08",
            "progress": 0
        }
    ])


if __name__ == "__main__":
    print("=" * 70)
    print("RoadFlow AI - Civil Construction Scheduling Platform")
    print("=" * 70)
    print("Starting Flask development server...")
    print()
    print("Available routes:")
    print("  /              -> Project Creation Page (Main Dashboard)")
    print("  /gantt         -> API endpoint for Gantt chart creation")
    print("=" * 70)
    print()
    
    # Run on all network interfaces so you can access from other devices if needed
    app.run(host="0.0.0.0", port=8000, debug=True)
