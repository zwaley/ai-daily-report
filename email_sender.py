import smtplib
import traceback
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, receiver_emails, smtp_server, smtp_port, smtp_user, smtp_password, subject, html_content):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = ", ".join(receiver_emails)

    part = MIMEText(html_content, 'html', 'utf-8')
    msg.attach(part)

    server = None
    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        # server.set_debuglevel(1) # Keep this commented out unless debugging
        server.login(smtp_user, smtp_password)
        server.sendmail(sender_email, receiver_emails, msg.as_string())
        print("Email sent successfully!")
    except smtplib.SMTPResponseException as e:
        # If the error happens after QUIT, the mail is already sent.
        if e.smtp_code == -1 and e.smtp_error == b'\x00\x00\x00':
            print("Email sent, but server returned a non-standard response on QUIT. Ignoring.")
        else:
            print(f"Error sending email: {e}")
            print("Full traceback:")
            traceback.print_exc()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Full traceback:")
        traceback.print_exc()
    finally:
        if server:
            try:
                # The problematic quit() is called here
                server.quit()
            except smtplib.SMTPResponseException as e:
                 if e.smtp_code == -1 and e.smtp_error == b'\x00\x00\x00':
                    print("Server returned a non-standard response on QUIT. This is expected with QQ Mail.")
                 else:
                    raise # Re-raise other quit errors
