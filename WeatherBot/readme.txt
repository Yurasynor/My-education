Створення Телеграм-боту "Погода у Львові" (псевдонім "@WeatherLvBot"), який буде показувати погоду у Львові, зі щоденним оновленням з ресурсу sinoptik.ua

----------------------

встановлення бібліотеки 
pyTelegramBotAPI: "$ pip install pyTelegramBotAPI";
BeautifulSoup: "pip install beautifulsoup4";
Requests: "pip install requests";
Telebot: "pip install telebot";

---------------------

створюємо головний файл main.py
створюємо файл config.py в якому буде зберігатися token для телеграм-боту
BeautifulSoup надали ім`я BS

---------------------
початкова команда:
 
def main(message):
	bot.send_message(message.chat.id, "Привіт, погода на сьогодні:")

прописуємо 
        if __name__ == "__main__":
            bot.polling(none_stop=True)
        щоб "зациклити" бота і він запуститься тоді, коли _main_ головний файл 

---------------------

cтворюємо нового бота newbot у Телеграмі за допомогою BotFather. Надаємо йому ім`я/псевдонім.
отримуємо токен, вставляємо його у файл config.py. Створюємо опис бота та фото його профілю.
Призначаємо команди для бота: 
    start - показати погоду на сьогодні
    help - показати погоду на сьогодні

---------------------

створюємо запит на ресурс sinoptik.ua (погода у Львові)

     r = requests.get('https://ua.sinoptik.ua/погода-львів')

---------------------
створюємо перемінну 
         html = BS(r.content, 'html.parser')

перебрати елемент і вказати селектор. З консолі розробника сайту https://ua.sinoptik.ua/погоді-львів, знаходимо id для максимально/мінімальної температури та опису погоди
        for el in html.select('#content'):
            t_min = el.select('.temperature .min')[0].text
            t_max = el.select('.temperature .max')[0].text 
            text = el.select('.wDescription .description')[0].text 

--------------------
виводимо дані в бота:
def main(message):
	bot.send_message(message.chat.id, "Привіт, погода на сьогодні: \n" +
    t_min + ',' + t_max + '\n' + text)
