import smtplib
import random

# Function to generate a random OTP
def generate_otp():
    return random.randint(1000, 9999)

# Function to send an OTP via email
def send_otp_email(receiver_email, otp):
    sender_email = "harshilbhatt21@gnu.ac.in"  # Replace with your email address
    sender_password = "harshil@06"      # Replace with your email password

    subject = "Your OTP Verification Code"
    body = f"Your OTP is: {otp}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)

        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(sender_email, receiver_email, message)
        print("OTP sent successfully!")
        server.quit()
    except Exception as e:
        print(f"Error: {e}")
        print("Failed to send OTP.")

# Function to verify the entered OTP
def verify_otp(otp, user_input):
    return otp == int(user_input)

# Example usage
if __name__ == "__main__":
    receiver_email = input("Enter your email address: - ")  # Replace with the recipient's email address

    # Generate and send OTP
    otp = generate_otp()
    send_otp_email(receiver_email, otp)

    # Prompt the user to enter OTP
    user_input = input("Enter the OTP sent to your email: ")

    # Verify the entered OTP
    if verify_otp(otp, user_input):
        print("OTP verification successful!")
    else:
        print("OTP verification failed.")
