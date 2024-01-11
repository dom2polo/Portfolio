from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

# Updated projects data
projects = [
    {
        'title': 'Emotion Detection',
        'date': '03/2023 – 05/2023',
        'overview': 'Developed real-time application using basics machine learning and computer vision, capable of accurately recognizing seven distinct emotions.',
        'tools': ['Python', 'TensorFlow', 'OpenCV'],
        'github_link': 'https://github.com/dom2polo/emotion-detection.git',
    },
    {
        'title': 'Sleep Pattern Analysis',
        'date': '09/2023 – 10/2023',
        'overview': 'Leveraged R Markdown in Posit to analyze college students’ sleep patterns. Created insightful visualizations and density plots with ggplot.',
        'tools': ['Posit', 'R'],
        'github_link': 'https://github.com/dom2polo/sleep-pattern-analysis.git',
    },
    {
        'title': 'Urban Traffic Analysis',
        'date': '11/2023 – 12/2023',
        'overview': 'Worked in teams and executed SQL queries for data retrieval and analysis. Designed a Flask-based client/server architecture for event search and detail retrieval.',
        'tools': ['MSSQL', 'Python', 'Flask', 'Folium'],
        'github_link': 'https://github.com/dom2polo/trasnportation-events.git',
    },
    {
        'title': 'Weather App',
        'overview': 'A simple web application that allows users to check the weather conditions for a specified location (city or state). The app fetches real-time weather data using the OpenWeatherMap API and displays it in an intuitive user interface.',
        'tools': ['HTML', 'CSS', 'JavaScript', 'API'],
        'github_link': 'https://github.com/dom2polo/weather-app.git',
    },
    {
        'title': 'To Do List',
        'overview': 'A simple web to do list that allow users to read, write, edit lists',
        'tools': ['HTML', 'CSS', 'JavaScript'],
        'github_link': 'https://github.com/dom2polo/to-do-list.git',
    },
]

# Brief summary about you
about_me = "Data Analyst enthusiast with a passion for leveraging data to uncover insights and drive informed decisions."

# Skills section
skills = [
    'Data Cleaning and Preprocessing',
    'R',
    'SQL',
    'Python (Pandas, NumPy)',
    'Post'
]

@app.route('/')
def index():
    return render_template('index.html', projects=projects, about_me=about_me, skills=skills)

@app.route('/project/all')
def project_all():
    return render_template('project_details_all.html', projects=projects)

@app.route('/project/<int:project_id>')
def project(project_id):
    # Check if the project_id is valid
    if 0 <= project_id < len(projects):
        project_data = projects[project_id]
        return render_template('project_details.html', project=project_data)
    else:
        return "Project not found", 404

if __name__ == '__main__':
    app.run(debug=True)
