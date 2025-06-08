import smtplib
from email.message import EmailMessage
import time

# --- SETTINGS (replace with yours) ---
SENDER_EMAIL = "bibidbiju0@gmail.com"
APP_PASSWORD = "zrkv hydc jvce ajqx"
RECEIVER_EMAIL = "bibidbiju0@gmail.com"  # or any other receiver
COOLDOWN_SECONDS = 300  # 5 minutes cooldown

last_alert_time = 0

def send_email_alert(subject, body):
    global last_alert_time
    current_time = time.time()

    # Cooldown check
    if current_time - last_alert_time < COOLDOWN_SECONDS:
        print("⚠️ Cooldown active. No alert sent.")
        return

    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(SENDER_EMAIL, APP_PASSWORD)
            smtp.send_message(msg)
        print("✅ Email alert sent!")
        last_alert_time = current_time

    except Exception as e:
        print("❌ Failed to send email:", e)
