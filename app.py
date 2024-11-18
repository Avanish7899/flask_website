from flask import Flask, render_template, request, redirect
import openpyxl
from datetime import datetime
app = Flask(__name__)
excel_file = "login_details.xlsx"
def save_to_excel(name, school_name, id_number):
    try:
        # Load the workbook or create a new one if it doesn't exist
        workbook = openpyxl.load_workbook(excel_file)
        sheet = workbook.active
    except FileNotFoundError:
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.append(["Name", "School Name", "ID Number", "Timestamp"])
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append([name, school_name, id_number, timestamp])
    workbook.save(excel_file)
@app.route('/')
def login_page():
    return render_template('login.html')
@app.route('/login', methods=['POST'])
def login():
    name = request.form['name']
    school_name = request.form['school_name']
    id_number = request.form['id_number']
    save_to_excel(name, school_name, id_number)
    return redirect('/home')
@app.route('/home')
def home_page():
    return render_template('home.html')
# Add routes for all other pages
@app.route('/resources')
def resources_page():
    return render_template('resource.html')
@app.route('/projects')
def projects_page():
    return render_template('projects.html')
@app.route('/activities')
def activities_page():
    return render_template('activities.html')
@app.route('/gallery')
def gallery_page():
    return render_template('gallery.html')
@app.route('/aboutus')
def aboutus_page():
    return render_template('aboutus.html')
@app.route('/logout')
def logout():
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)