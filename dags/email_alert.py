# email_alert.py

import smtplib
from email.mime.text import MIMEText

def send_anomaly_email(subject: str, message: str, recipient: str):
    sender = "myakalarajkumar1998@gmail.com"  # Use Gmail or company email
    password = "your_password_or_app_password"

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.sendmail(sender, recipient, msg.as_string())
        print(f"✅ Alert email sent to {recipient}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

if __name__ == "__main__":
    subject = "🚨 Anomaly Detected in Forecast"
    message = "An anomaly was detected in the forecasted data. Please check the system for details."
    recipient = "recipient@example.com"
    
    send_anomaly_email(subject, message, recipient)