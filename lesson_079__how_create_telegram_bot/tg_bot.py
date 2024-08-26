"""pip install pyTelegramBotAPI"""

from telebot import TeleBot
from telebot.types import Message

from local_settings import TG_TOKEN

# сохраняем инициализированный объект бота
bot = TeleBot(TG_TOKEN)

# хранилище запросов пользователя
queries: list[list[str]] = []

genres = [
    '1. Жанр 01',
    '2. Жанр 02',
    '3. Жанр 03',
]


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: Message) -> None:
    """Отправляет приветственное сообщение и помощь по использованию бота."""
    welcome_text = """
    Привет! Я бот для управления задачами. Вот как со мной работать:
    - Показать все жанры /show_genres
    - Поиск фильма по ключевому слову /show_by_keyword <ключевое_слово>
    - Поиск фильма по году /show_by_year <0000>
    - Чтобы посмотреть эту памятку снова, отправьте /help
    """

    user_id: int = message.chat.id
    bot.send_message(user_id, welcome_text)


@bot.message_handler(commands=['show_genres'])
def show_genres(message: Message) -> None:
    """Обрабатывает команду /add_task."""
    user_id: int = message.chat.id
    response_text = f"Список доступных жанров: {'\n'.join(genres)}\n "
    response_text += 'для вывода фильмов по жанру введите команду /show_by_genre <номер жанра>\n'
    response_text += 'возврат в главное меню /help'
    bot.send_message(user_id, response_text)


@bot.message_handler(commands=['show_by_genre'])
def add_task(message: Message) -> None:
    """Обрабатывает команду /add_task."""
    user_id: int = message.chat.id
    text: str = message.text[14:].strip()  # берём текст после '/show_by_genre'

    if not text:
        bot.send_message(user_id, "Вы не указали жанр. Памятка - /help")
        return
    else:
        num_genre = int(text)
        response_text = f"Список фильмов по жанру {num_genre}\n "
        bot.send_message(user_id, response_text)


@bot.message_handler(content_types=['text'])
def handle_text_message(message: Message) -> None:
    """Обрабатывает любые текстовые сообщения, которые не являются командами."""
    user_id: int = message.chat.id
    user_text: str = message.text.strip()

    # Здесь можно добавить логику обработки текста
    response_text = f"Вы написали: {user_text}\nЭта команда мне неизвестна"

    bot.send_message(user_id, response_text)


if __name__ == "__main__":  # для запуска скрипта только напрямую
    bot.infinity_polling()  # проверяет чат на наличие новых сообщений

