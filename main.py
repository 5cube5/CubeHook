import requests

webhookUrl = input("Enter your webhook:")
webhookName = "Hooked by cubehook lmao"
webhookAvatar = "https://example.com/avatar.png"  # Default avatar URL

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
        newName = input("Type in the new name:")
        payload = {'name': newName}
        requests.patch(webhookUrl, json=payload)
    elif command == 2:
        message = input("Type in the message:")
        payload = {'content': message, 'username': webhookName, 'avatar_url': webhookAvatar}
        requests.post(webhookUrl, json=payload)
    elif command == 3:
        spamMessage = input("Type in the spam message:")
        quantity = input("Spam for how many times? :")
        for i in range(int(quantity)):
            requests.post(webhookUrl, json={'content': spamMessage, 'username': webhookName, 'avatar_url': webhookAvatar})
    elif command == 4:
        requests.delete(webhookUrl)
        print("Command executed!")
        break  # Exit the loop
    elif command == 5:
        newAvatar = input("Enter the URL of the new avatar:")
        webhookAvatar = newAvatar
        print("Avatar set successfully.")
    elif command == 6:
        print("Exiting the loop.")
        break  # Exit the loop
    else:
        print("Invalid command. Please enter a valid option.")
