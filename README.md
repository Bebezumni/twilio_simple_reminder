# WhatsApp Бот для напоминаний

Это простой WhatsApp бот, который позволяет пользователям устанавливать напоминания, отправляя сообщение с датой, временем и текстом напоминания. Бот затем отправит сообщение обратно пользователю в указанную дату и время с текстом напоминания.

## Использованные технологии

- Python
- Flask (для Webhook)
- Twilio API (для отправки и получения сообщений WhatsApp)

## Установка

1. Клонируйте этот репозиторий или загрузите исходный код.
2. Установите необходимые Python пакеты с помощью pip: 

```pip install twilio```
```pip install flask```

3. Укажите учетные данные своего аккаунта Twilio в файле `main.py`:

```python
account_sid = 'ВАШ_TWILIO_ACCOUNT_SID'
auth_token = 'ВАШ_TWILIO_AUTH_TOKEN'
twilio_number = 'ВАШ_TWILIO_НОМЕР_ТЕЛЕФОНА'
server_ip = 'АЙПИ_ВАШЕГО_СЕРВЕРА'
```

Замените 'ВАШ_TWILIO_ACCOUNT_SID', 'ВАШ_TWILIO_AUTH_TOKEN' и 'ВАШ_TWILIO_НОМЕР_ТЕЛЕФОНА' на ваши реальные учетные данные Twilio и номер телефона.

Замените 'SERVER_IP' на айпи сервера на котором запускается скрипт(без порта)

## Использование
Запустите скрипт main.py:

```python main.py```

Бот запустится и отобразит следующее сообщение: "Бот запущен. Отправьте 'YYYY-MM-DD HH:MM Текст напоминания' для создания напоминания."
Отправьте сообщение WhatsApp на ваш Twilio номер телефона в формате 'YYYY-MM-DD HH:MM Текст напоминания'. Например: '2023-05-20 14:30 Купить продукты'.
Бот подтвердит напоминание и выведет сообщение в консоли.
В указанную дату и время бот отправит обратно сообщение WhatsApp с текстом напоминания.
## API
Этот бот использует Twilio API для отправки и получения сообщений WhatsApp. Twilio API предоставляет RESTful интерфейс для различных коммуникационных сервисов, включая SMS, голосовые вызовы и мессенджеры, такие как WhatsApp.

Бот взаимодействует с Twilio API следующим образом:

Отправка сообщений: Функция send_reminder использует метод client.messages.create из Twilio API для отправки сообщения WhatsApp на номер телефона пользователя с текстом напоминания.

Получение сообщений: Бот устанавливает Twilio WebHook, который позволяет Twilio отправлять входящие сообщения WhatsApp на указанный URL. Функция incoming_message вызывается Twilio при получении нового сообщения, и она передает данные сообщения в функцию handle_message для обработки.
