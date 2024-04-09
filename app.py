from flask import Flask, request, jsonify
from flask_cors import CORS 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
CORS(app)

@app.route('/send-emails', methods=['POST'])
def send_emails():
    data = request.get_json()
    # print(data)
    to = data['to']
    subject = data['subject']
    message = data['message']

    # Replace with your email and password
    email = 'example@gmail.com'
    password = 'srfu rwed vfid gftr' # generated code from email

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, to, msg.as_string())
        server.quit()
        return jsonify({'message': 'Emails sent successfully!'})
    except Exception as e:
        print('Error:', e)
        return jsonify({'message': 'Failed to send emails'}), 500

if __name__ == '__main__':
    app.run(debug=True)
