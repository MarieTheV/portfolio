from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


def write_to_db(data):
    with open('database.csv', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/')
def my_homepage():
    return render_template("index.html")


@app.route('/<string:page_name>')
def my_served_page(page_name):
    return render_template(f"{page_name}")


@app.route('/send_message', methods=['POST', 'GET'])
def send_message():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_db(data)
            return redirect('thx.html')
        except Exception as err:
            return f'Could not save to DB :\n{err}'
    else:
        return redirect('contact.html')
