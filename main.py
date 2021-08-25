
from flask import Flask, render_template
from datetime import timedelta

import jinja2


# Functions created by web app developer


global timesheets_to_print
global web_site

loader=jinja2.FileSystemLoader('templates')

# migration update point - 'hunterseeker.eu.pythonanywhere.com'
URL = 'http://0.0.0.0:5000/'
# UPLOAD_FOLDER = '/home/pi/PycharmProjects/eProTMS/static/files/aefrty_asd_dttrjhkcciibiixi_srx/approvedtimesheets'
ALLOWED_EXTENSIONS = set(['pdf'])
# timesheets_to_print = []
app = Flask(__name__)

app.secret_key = "Seq#usHz39"
app.permanent_session_lifetime = timedelta(days=1)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/decommissioning')
def decomm():
    return render_template('decommissioning.html')

@app.route('/decontamination')
def decon():
    return render_template('decontamination.html')

@app.route('/deinstallation')
def deinstall():
    return render_template('deinstallation.html')

@app.route('/disposal')
def dispose():
    return render_template('disposal.html')

if __name__ == '__main__':
    # driver.execute_script("document.body.style.zoom='zoom 90%'")
    app.run(port=5000, debug=True, host='0.0.0.0')
    # app.run(host='192.168.8.238')