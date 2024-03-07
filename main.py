from twilio.rest import Client
import datetime
import schedule
import time


# Ваши учетные данные Twilio
secret = ''
account_sid = ''
auth_token = ''
twilio_number = ''

# Создаем клиент Twilio
client = Client(account_sid, auth_token)

# Список для хранения напоминаний
reminders = []
def send_reminder(to_number, text):
    message = client.messages.create(
        body=text,
        from_=twilio_number,
        to=to_number
    )
    print(f"Напоминание '{text}' отправлено на номер {to_number}")

def handle_message(from_number, text):
    try:
        time_str, reminder_text = text.split(' ', 1)
        reminder_time = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M")
        reminders.append((from_number, reminder_time, reminder_text))
        schedule.every().day.at(reminder_time.strftime("%H:%M")).do(send_reminder, from_number, reminder_text)
        print(f"Напоминание '{reminder_text}' установлено для {from_number} на {reminder_time}")
    except ValueError:
        send_reminder(from_number, "Неверный формат сообщения. Используйте: 'YYYY-MM-DD HH:MM Текст напоминания'")

# Обработчик входящих сообщений от Twilio
def incoming_message(msg):
    from_number = msg.from_
    text = msg.body
    handle_message(from_number, text)

# Создаем Twilio WebHook
webhook = client.incoming_phone_numbers.list(
    limit=1
)[0].update(sms_url=f'http://example.com/handle_sms')

print("Бот запущен. Отправьте 'YYYY-MM-DD HH:MM Текст напоминания' для создания напоминания.")

while True:
    schedule.run_pending()
    time.sleep(1)
