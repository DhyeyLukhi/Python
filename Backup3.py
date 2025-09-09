from tempmail import EMail

try:
    email = EMail()
    print(f"Your temporary email address: {email.address}")
    print("Waiting for a message...")
    msg = email.wait_for_message(timeout=60)
    print(f"Received message from: {msg.sender}")
    print(f"Subject: {msg.subject}")
    print(f"Body: {msg.body}")
except Exception as e:
    print(f"Error: {e}")
