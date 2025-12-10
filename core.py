import requests

# Переменные со значениями
TOKEN = '8566716533:AAHrWaacuJXfRB6x81_geR1Gh-xvHJqPw0I'
CHAT_ID = '6591584526'  # ID
FILE_PATH = 'message.txt'  # путь к файлу с текстом

def send_text(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        'chat_id': CHAT_ID,
        'text': text
    }
    response = requests.post(url, data=data)
    return response.json()

def main():
    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        text = file.read()
    result = send_text(text)
    print(result)

if __name__ == "__main__":
    main()
