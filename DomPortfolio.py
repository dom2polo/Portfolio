import markdown

# Define your portfolio content in Markdown format
portfolio_content = """
# John Doe - Data Analyst

## Skills
- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Data Visualization (Matplotlib, Seaborn)
- Statistical Analysis
- SQL
- Python (Pandas, NumPy)
- Machine Learning Basics

## Education
- B.Sc. in Statistics, University XYZ, Year

## Work Experience
**Data Analyst | ABC Company | Jan 2022 - Present**
- Conducted EDA on large datasets, identifying trends and anomalies.
- Created interactive visualizations to communicate insights to stakeholders.

**Junior Data Analyst | XYZ Corporation | May 2020 - Dec 2021**
- Assisted in data cleaning and preprocessing tasks.
- Collaborated with the team to develop statistical models for forecasting.

## Projects
1. **Sales Analysis Dashboard**
   - Analyzed sales data to identify key performance indicators.
   - Created an interactive dashboard using Matplotlib and Seaborn.

2. **Customer Segmentation**
   - Utilized clustering algorithms to segment customers based on behavior.
   - Presented actionable insights to improve marketing strategies.

## Tools and Technologies
- Python, SQL, Matplotlib, Seaborn, Pandas, NumPy, Excel

## Certifications
- Data Science Certification, Online Course, Year

## GitHub
[Link to GitHub Repository](https://github.com/yourusername)

## Contact
- Email: john.doe@example.com
- LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/johndoe)

## Resume
[Download Resume (PDF)](link-to-your-resume-pdf)
"""

# Convert Markdown to HTML
html_content = markdown.markdown(portfolio_content)

# Save the HTML content to a file
with open("portfolio.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("Portfolio HTML file generated successfully.")
