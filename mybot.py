import vk_api
import time
import random


gennik=['1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM']
oskorbl=['сука','Сука','бля','Бля','блять','Блять','пидор','Пидор','Пидорас','пидорас']
pohval=['молодец','Молодец','Красава','красава','молорик','Молорик','Няша','няша','няшка','Няшка','молорик','Молорик']
adminstr = ['http://vk.com/taipancool','http://vk.com/id212198981']
privet=['Привет','привет','салам','Салам','ку','Ку','Шалом','шалом','Прев','прев','Прив','прив']
otv_privet=['Здравствуй','Приветик😊','Ку😊','Привет😊','Прив']
kak_dela=['Как твои дела?','Как твои дела','как твои дела?','как твои дела','Как дела?','как дела?','как дела','Как дела','']










vk = vk_api.VkApi(login = '12107452345', password = 'taipan20912')
vk.auth()
zagadka = ['Пожирает всё кругом:\nЗверя, птицу, лес и дом.\n Сталь сгрызёт, железо сгложет,\n Крепкий камень уничтожит,\n Власть его всего сильней,\n Даже власти королей.','Не отыскать её корней,\nВсё круче вверх она идёт- \nА не растёт. ']
zagadka.append(str('Больше часа, меньше минуты. '))
zagadka.append(str('К реке подходят два человека. У берега лодка, которая может выдержать только одного. Оба человека переправились на противоположный берег. Как?'))
zagadka.append(str('Летели галки, сели на палки. Сядут по одной — галка лишняя, сядут по две — палка лишняя. Сколько было палок и сколько было галок? '))
zagadka.append(str('Какой слон без носа? '))
zagadka.append(str('Сколько лет в году? '))
zagadka.append(str('Какой пробкой нельзя заткнуть ни одну бутылку? '))
zagadka.append(str('Какая мышца в теле человека самая сильная? '))
zagadka.append(str('Без чего ничего никогда не бывает?'))
zagadka.append(str('Как написать «уточка» в 2 клетках? '))

anekdot =[]
anekdot.append(str('Женьщина может сделать 4 чуда: стать влажной не намокая, кровоточить не поранившись,\n давать молоко не поев травы, и ЗАЕБ@ТЬ не раздеваясь. '))
anekdot.append(str('Пьяный, покачиваясь, никак не может попасть ключом в замочную скважину. Мимо проходит сосед и спрашивает:\n — Помочь?\n — Угу. Дом подержи!'))
anekdot.append(str('Девушка, которая думает, что меняет парней как перчатки, просто еще не понимает, что "пошла по рукам"... '))
anekdot.append(str('Звонок в Скорую помощь:\n — У моего мужа — 38, 5.\n — Ни хрена себе, какой длинный!'))
anekdot.append(str('Стоит ли опасаться женщины, которой палец в рот не клади, если планируешь класть вовсе и не палец?'))
anekdot.append(str('- Смотри, на восьмом этаже целуются!\n- Да, здорово! Им бы бабу...'))
anekdot.append(str('Целый месяц учил правила дорожного движения. Выехал в город.\nГОСПОДИ!!! Лучше бы я молитвы учил!!!'))
anekdot.append(str('Была абсолютно уверена, что заняла место в его сердце.\n Оказалось сижу в печенке и выношу мозг.'))
anekdot.append(str('Целый час ждала Аня возвращения своего парня из армии.'))
anekdot.append(str('- Теперь ты её никогда не забудешь. \n- Кого?'))
anekdot.append(str('Жена кричит мужу из кухни:\n- Дорогой, ты любишь сыр с плесенью?\n- Обожаю, дорогая!\n- Ну, тогда тебе и колбаска понравится!'))
anekdot.append(str('Российская армия - она комплексная. При этом её действительная часть воюет в Сирии, а мнимая - на Украине.'))
anekdot.append(str('- Я заняла третье место в конкурсе двойников принцессы Дианы.\n- До или после аварии?'))
anekdot.append(str('Поскольку нет желания и мочи, любимой пожелай: «Спокойной ночи!»'))
anekdot.append(str('Челябинские ириски настолько суровы, что растворяются во рту вместе с зубами.'))




def write_msg(user_id, s):
    vk.method('messages.send', {'user_id':user_id,'message':s,})

values = {'out': 0, 'count': 100, 'time_offset': 60}
vk.method('messages.get', values)


while True:
    response = vk.method('messages.get', values)
    if response['items']:
        values['last_message_id'] = response['items'][0]['id']
        for item in response['items']:

            if response['items'][0]['body'] in privet:
                write_msg(item['user_id'], (random.choice(otv_privet)))



            if response['items'][0]['body']=='*анекдот':
                write_msg(item['user_id'], random.choice(anekdot))

            if response['items'][0]['body']=='*хозяин бота':
                write_msg(item['user_id'], 'Мой хозяин НЯ!❤\n')
                write_msg(item['user_id'],random.choice(adminstr))

            if response['items'][0]['body']=='/cmd':
                write_msg(item['user_id'],'Мои команды:\n*загадка\n*хозяин бота\n*анекдот\n')
        if response['items'][0]['body']=='*загадка':
            write_msg(item['user_id'], random.choice(zagadka))







        if response['items'][0]['body']=='Что делаешь?':
            write_msg(item['user_id'], 'Жду пока мой хоязин придумает что нибудь новое для меня😌')
        elif response['items'][0]['body']=='что делаешь?':
            write_msg(item['user_id'], 'Жду пока мой хоязин придумает что нибудь новое для меня😌')
        elif response['items'][0]['body']=='Что делаешь':
            write_msg(item['user_id'], 'Жду пока мой хоязин придумает что нибудь новое для меня😌')
        elif response['items'][0]['body']=='что делаешь':
            write_msg(item['user_id'], 'Жду пока мой хоязин придумает что нибудь новое для меня😌')
        if response['items'][0]['body']=='как дела':
            write_msg(item['user_id'], 'Лучше чем у тебя😋')
        elif response['items'][0]['body']=='Как дела?':
            write_msg(item['user_id'], 'Лучше чем у тебя😋')
        elif response['items'][0]['body']=='как дела?':
            write_msg(item['user_id'], 'Лучше чем у тебя😋')
        elif response['items'][0]['body']=='Как дела':
            write_msg(item['user_id'], 'Лучше чем у тебя😋')

        if response['items'][0]['body']=='Марина':
            write_msg(item['user_id'], 'Что?')
        elif response['items'][0]['body']=='марина':
            write_msg(item['user_id'], 'Что?')

        if response['items'][0]['body']=='Грустно':
            write_msg(item['user_id'], 'Не грусти ты няша💋')
        elif response['items'][0]['body']=='грустно':
            write_msg(item['user_id'], 'Не грусти ты няша💋')

        if response['items'][0]['body'] in pohval:
            write_msg(item['user_id'], 'Cпасибо😋')

        if response['items'][0]['body'] in oskorbl:
            write_msg(item['user_id'], 'Не лугайся Б$ЯТЬ!🔥')

        if response['items'][0]['body']=='Давай играть':
            write_msg(item['user_id'], 'Во что?')
            write_msg(item['user_id'], 'Я еще не умею играть(((')

        if response['items'][0]['body']=='Ты где?':
            write_msg(item['user_id'], 'Дома')
        if response['items'][0]['body']=='я твой хозяин':
            write_msg(item['user_id'], 'Врешь!!')
































    time.sleep(1)
