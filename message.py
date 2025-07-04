import pywhatkit as pwk

# Take phone number and message from user
phone_number = input("Enter the recipient's phone number (with country code, e.g., +1234567890): ")
message = input("Enter the message to send: ")

# Ask user for time input
hour_input = input("Enter hour to send (24-hour format, leave blank to send immediately): ")
minute_input = input("Enter minute to send (leave blank to send immediately): ")

if hour_input.strip() and minute_input.strip():
    scheduled_hour = int(hour_input)
    scheduled_minute = int(minute_input)
    pwk.sendwhatmsg(phone_number, message, scheduled_hour, scheduled_minute)
else:
    pwk.sendwhatmsg_instantly(phone_number, message)