��������� ��������-���� "������ � �����" (�������� "@WeatherLvBot"), ���� ���� ���������� ������ � �����, � �������� ���������� � ������� sinoptik.ua

----------------------

������������ �������� 
pyTelegramBotAPI: "$ pip install pyTelegramBotAPI";
BeautifulSoup: "pip install beautifulsoup4";
Requests: "pip install requests";
Telebot: "pip install telebot";

---------------------

��������� �������� ���� main.py
��������� ���� config.py � ����� ���� ���������� token ��� ��������-����
BeautifulSoup ������ ��`� BS

---------------------
��������� �������:
 
def main(message):
	bot.send_message(message.chat.id, "�����, ������ �� �������:")

��������� 
        if __name__ == "__main__":
            bot.polling(none_stop=True)
        ��� "���������" ���� � �� ����������� ���, ���� _main_ �������� ���� 

---------------------

c�������� ������ ���� newbot � �������� �� ��������� BotFather. ������ ���� ��`�/��������.
�������� �����, ���������� ���� � ���� config.py. ��������� ���� ���� �� ���� ���� �������.
���������� ������� ��� ����: 
    start - �������� ������ �� �������
    help - �������� ������ �� �������

---------------------

��������� ����� �� ������ sinoptik.ua (������ � �����)

     r = requests.get('https://ua.sinoptik.ua/������-����')

---------------------
��������� �������� 
         html = BS(r.content, 'html.parser')

��������� ������� � ������� ��������. � ������ ���������� ����� https://ua.sinoptik.ua/�����-����, ��������� id ��� �����������/�������� ����������� �� ����� ������
        for el in html.select('#content'):
            t_min = el.select('.temperature .min')[0].text
            t_max = el.select('.temperature .max')[0].text 
            text = el.select('.wDescription .description')[0].text 

--------------------
�������� ��� � ����:
def main(message):
	bot.send_message(message.chat.id, "�����, ������ �� �������: \n" +
    t_min + ',' + t_max + '\n' + text)
