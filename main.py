import requests

webhook_url = input("Enter your webhook:")
webhook_name = "Hooked by cubehook lmao"
webhook_avatar = "https://example.com/avatar.png"  # Default avatar URL

print("Hooked in")

print("1: Rename webhook")
print("2: Type a message")
print("3: Spam a message")
print("4: Delete Webhook")
print("5: Set Avatar")
print("6: Exit")

while True:
    command = input("Enter a command: ")
    command = int(command)

    if command == 1:
        new_name = input("Type in the new name:")
        webhook_name = new_name  # Update the webhook_name
        requests.patch(webhook_url, json={'name': new_name})
        print("Webhook renamed successfully.")
    elif command == 2:
        message = input("Type in the message:")
        requests.post(webhook_url, json={'content': message, 'username': webhook_name, 'avatar_url': webhook_avatar})
        print("Message sent successfully.")
    elif command == 3:
        spam_message = input("Type in the spam message:")
        quantity = input("Spam for how many times? :")
        for _ in range(int(quantity)):
            requests.post(webhook_url, json={'content': spam_message, 'username': webhook_name, 'avatar_url': webhook_avatar})
        print("Spam complete.")
    elif command == 4:
        requests.delete(webhook_url)
        print("Webhook deleted successfully.")
        break  # Exit the loop
    elif command == 5:
        new_avatar = input("Enter the URL of the new avatar:")
        webhook_avatar = new_avatar
        print("Avatar set successfully.")
    elif command == 6:
        print("Exiting the loop.")
        break  # Exit the loop
    else:
        print("Invalid command. Please enter a valid option.")
