from twilio.rest import Client
import datetime
import schedule
import time
from flask import Flask, request

# Ваши учетные данные Twilio
account_sid = ''
auth_token = ''
twilio_number = ''
server_ip = ''

# Создаем клиент Twilio
client = Client(account_sid, auth_token)

# Список для хранения напоминаний
reminders = []

# Инициализируем фласк приложение
app = Flask(__name__)

#Создаем вебхук на фласке
@app.route('/webhook', methods=['POST'])
def webhook_handler():
    # Получаем данные запроса от Twilio
    message_data = request.form
    # Вызываем функцию incoming_message с данными сообщения
    incoming_message(message_data)
    # Возвращаем успешный ответ Twilio
    return '', 200

# Получаем текст и номер из сообщения
def incoming_message(msg):
    from_number = msg.from_
    text = msg.body
    handle_message(from_number, text)


#Функция отправляющая конечное уведомление
def send_reminder(to_number, text):
    message = client.messages.create(
        body=text,
        from_=twilio_number,
        to=to_number
    )
    print(f"Напоминание '{text}' отправлено на номер {to_number}")

#Обработчик сообщений
def handle_message(from_number, text):
    try:
        time_str, reminder_text = text.split(' ', 1)
        reminder_time = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M")
        reminders.append((from_number, reminder_time, reminder_text))
        schedule.every().day.at(reminder_time.strftime("%H:%M")).do(send_reminder, from_number, reminder_text)
        print(f"Напоминание '{reminder_text}' установлено для {from_number} на {reminder_time}")
    except ValueError:
        send_reminder(from_number, "Неверный формат сообщения. Используйте: 'YYYY-MM-DD HH:MM Текст напоминания'")


# Говорим Twilio где наш вебхук WebHook
webhook = client.incoming_phone_numbers.list(limit=1)[0].update(sms_url=f'http://{server_ip}:5000/webhook')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    while True:
        schedule.run_pending()
        time.sleep(1)
