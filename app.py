from flask import Flask, request, jsonify
from flask_cors import CORS 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
CORS(app)

# Replace with your email and password
email = 'Example@gmail.com'
password = 'srfu nwbv vfid zfui'

@app.route('/send-emails', methods=['POST'])
def send_emails():
    data = request.get_json()
    print(data)
    to = data['to']
    emadd = to.split(",")
    # print(emadd)
    subject = data['subject']
    message = data['message']

    for too in emadd:
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = too
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email, password)
            server.sendmail(email, too, msg.as_string())
            server.quit()
        except Exception as e:
            print('Error:', e)
            return jsonify({'message': 'Failed to send emails'}), 500

    return jsonify({'message': 'Emails sent successfully!'})

@app.route('/upload-csv', methods=['POST'])
def uploadCSV():
    data = request.get_json()
    print(data)
    to = data['to']
    emadd = to
    # print(emadd)
    subject = data['subject']
    message = data['message']

    for too in emadd:
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = too
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email, password)
            server.sendmail(email, too, msg.as_string())
            server.quit()
        except Exception as e:
            print('Error:', e)
            return jsonify({'message': 'Failed to send emails'}), 500

    return jsonify({'message': 'Emails sent successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
