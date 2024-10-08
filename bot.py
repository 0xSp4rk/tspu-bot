import config
import telebot
from telebot import types


bot = telebot.TeleBot(config.token)

# global videoInspector
# global videoHelper
# global videoSub1
# global videoSub2

# videoInspector = open('files/inspector.mp4', 'rb')
# videoHelper = open('files/Помощник.mp4', 'rb')
# videoSub1 = open('files/Субъект1.mp4', 'rb')
# videoSub2 = open('files/Субъект2.mp4', 'rb')

# Обработка команды для старта
@bot.message_handler(commands=['go', 'start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = types.KeyboardButton("Начнём!")

    markup.add(item1)

    bot.send_message(message.chat.id,"Добро пожаловать!".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def go_send_messages(message):
    if message.text == "Начнём!":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        group1 = types.KeyboardButton('1️⃣ Через тернии к свободе')
        group2 = types.KeyboardButton('2️⃣ Бедность - не порок')
        group3 = types.KeyboardButton('3️⃣ Не имей сто рублей, а имей сто друзей')

        markup.add(group1, group2, group3)

        bot.send_message(message.chat.id,"Выбери группу".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)

    elif message.text == '1️⃣ Через тернии к свободе':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        role1 = types.KeyboardButton("Учитель труда")
        role2 = types.KeyboardButton("Родители")
        role3 = types.KeyboardButton("Ребенок")
        button = types.KeyboardButton("В начало")

        markup.add(role1, role2, role3, button)
        bot.send_message(message.chat.id,"Выбери роль".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)

    elif message.text == "Учитель труда":
        bot.send_message(message.chat.id, "Вы учитель труда (на время классный руководитель) и на ваших занятиях Алёна отлично справляется со всеми заданиями: и по шитью, и по кройке, и по вязанию, и по готовке. Вы были удивлены, что в столь юном возрасте девочка может практически все. Однако, вы как-то заметили, что ее руки усыпаны царапинами, ссадинами, мозолями и синяками. Вас это смутило и вы спросили у ребенка, откуда у нее такие травмы - ребенок молчал, боясь что-то рассказать. \n" 
                         "\n<i><b>Ваша задача</b></i> - узнайте информацию у девочки и её родителей. Что можно предпринять в данном случае?\n".format(message.from_user, bot.get_me()), parse_mode='html')
        # bot.send_video(message.chat.id, videoInspector)
    elif message.text == "Родители":
        bot.send_message(message.chat.id, "Вы - родители Алёны. Вы считаете, что девочка должна вам во всем помогать по дому, потому что вы уже пенсионного возраста. Ссадины и синяки вашей дочери вызвали подозрение на домашнее насилие и рабство. Но вы не виноваты в том, что у ребенка тонкая кожа и все свои синяки она получает при выполнении своих обязанностей по дому: готовка на всю семью, мытье полов во всем доме, шитье и ремонт вещей и т.д.\n"
                                        "\n<i><b>Ваша задача:</b></i> оправдайте себя и материалы, лежащие на столе.".format(message.from_user, bot.get_me()), parse_mode='html')
        # bot.send_video(message.chat.id, videoHelper)
    elif message.text == "Ребенок":
        bot.send_message(message.chat.id,"Вы - несовершеннолетняя Алена. Дома вас принуждают к труду и домашним делам. Вам давно не покупали новую одежду, вы ходите в школу в обносках, маленькой обуви. Вы согласны с тем, что должны помогать родителям по дому. Но за невыполнение (или плохое выполнение ваших обязанностей), Вас либо заставляют все переделывать, либо наказывают: принуждают вставать коленями на крупу, носить мешки с мукой или выполнять тяжелую изнурительную работу. \n"
                         "\n<i><b>Ваша задача:</b></i> объяснить откуда ваши шрамы, найти помощь у учителя труда (классного руководителя).".format(message.from_user, bot.get_me()),parse_mode='html')
        # bot.send_video(message.chat.id, videoSub1)
    elif message.text == "В начало":
        welcome(message)

    elif message.text == '2️⃣ Бедность - не порок':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        role1 = types.KeyboardButton("Учитель физкультуры")
        role2 = types.KeyboardButton("Ребенок")
        role3 = types.KeyboardButton("Школьный психолог")
        button = types.KeyboardButton("В начало")

        markup.add(role1, role2, role3, button)
        bot.send_message(message.chat.id,"Выбери роль".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)

    elif message.text == "Учитель физкультуры":
        bot.send_message(message.chat.id,"Вы - учитель физкультуры. На ваши занятия девочка приходит то без формы, то эта форма постоянно очень грязная и неприятно выглядит и пахнет. Вы много раз писали её замечание в дневник, хотя ребенок очень сильно плакал и просил вас этого не делать, поскольку её мама будет очень сильно ругаться и плакать. Вас беспокоит финансовое состояние семьи, вы заметили, что ребенок не может играть в мяч - её обувь ей не по размеру.\n"
                         "\n<i><b>Ваша задача:</b></i> как вы можете помочь девочке? Разузнайте информацию и придите к общему мнению в группе.".format(message.from_user, bot.get_me()),parse_mode='html')
        # bot.send_video(message.chat.id, videoSub1)
    
    elif message.text == "Ребенок":
        bot.send_message(message.chat.id,"Вы - ученица Анна, дело в том, что у вашей семьи очень низкий достаток. Родители не могут купить Вам новую одежду, а из старой вы давно выросли. На уроке физкультуры вы не можете бегать, играть в мяч - давит обувь, у вас постоянно нет сил на активную деятельность ( вы очень мало кушаете, иногда это приводит к тому, что у вас трясутся руки). Когда вас зовут гулять после школы одноклассники - вы отказываетесь, говорите, что у вас очень строгие родители, которые будут вас бить за опоздания (но вы знаете, что это неправда). Вы просто боитесь, что вас засмеют за вашу потрепанную одежду и старые сапоги, поэтому убегаете домой пораньше.\n"
                         "\n<i><b>Ваша задача:</b></i> объясните те материалы. которые лежат на столе, попросите помощи у школы.".format(message.from_user, bot.get_me()),parse_mode='html')
        # bot.send_video(message.chat.id, videoSub1)

    elif message.text == "Школьный психолог":
        bot.send_message(message.chat.id,"Вы - школьный психолог. С девочкой вы работаете постоянно, по просьбе классного руководителя. <u>Родители не принимают особо участия в воспитании ребенка, поскольку заняты заработком денег.</u> С Анной вы прошли несколько тестов, но Тест №1 и Тест №3 (материалы на столе) показались вам наиболее тревожными.\n"
                         "\n<i><b>Ваша задача:</b></i> Поговорите с девочкой и учителем. Как вы можете помочь ребенку?".format(message.from_user, bot.get_me()),parse_mode='html')
        # bot.send_video(message.chat.id, videoSub1)


    elif message.text == '3️⃣ Не имей сто рублей, а имей сто друзей':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        role1 = types.KeyboardButton("Классный руководитель")
        role2 = types.KeyboardButton("Ребенок")
        role3 = types.KeyboardButton("Свидетель драки")
        role4 = types.KeyboardButton("Родители")
        button = types.KeyboardButton("В начало")

        markup.add(role1, role2, role3, role4, button)
        bot.send_message(message.chat.id,"Выбери роль".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)

    elif message.text == "Классный руководитель":
        bot.send_message(message.chat.id,"Вы - классный руководитель Гарри. Среди ваших учеников постоянно рождаются конфликты, драки. Особенно достается Гарри, его постоянно задирают, с ним никто не хочет сидеть за партой, на переменах в его учебниках пишут матерные слова. Однажды после уроков, на заднем дворе школы развязалась драка, Гарри разбили нос, сломали очки, родители, увидев своего сына дома, сразу написал вам. Однако, вы не несете ответственность за то, что случилось после уроков.\n"
                         "\n<i><b>Ваша задача:</b></i> постарайтесь решить конфликт и найти выход из этой ситуации. Что вы можете посоветовать ребенку и его родителям. Что вы можете сделать как классный руководитель?".format(message.from_user, bot.get_me()),parse_mode='html')
        # bot.send_video(message.chat.id, videoSub1)

    elif message.text == "Ребенок":
        bot.send_message(message.chat.id,"Вы - несовершеннолетний Гарри. Вы считаете себя изгоем в школе. С вами не хотят сидеть за одной партой, вас обзывают 'чудилой' и 'очкариком'.  Вам постоянно мешают на уроках, подкидывая записки и пиная ваш рюкзак. Однажды вас очень сильно избил почти весь класс на заднем дворе школы, потому что вы единственный, кто на 'отлично' написал контрольную в классе. Вас разбили нос и сломали очки. Теперь вы отказываетесь ходить в школу, и просите родителей перевести вас на дистанционное обучение.\n"
                         "\n<i><b>Ваша задача:</b></i> просите помощи у классного руководителя и родителей. Добейтесь такого решения, чтобы оно <b>вас устраивало.</b>".format(message.from_user, bot.get_me()),parse_mode='html')
        # bot.send_video(message.chat.id, videoSub1)

    elif message.text == "Свидетель драки":
        bot.send_message(message.chat.id,"Вы не раз видели, как Гарри подкидывают записки на уроке (материалы на столе). Однажды, вы услышали на перемене, что ребята всем классом хотят избить мальчика за то, что он ведет себя как выскочка (он единственный написал контрольную классе на 'отлично'. Вы хотели помочь ему, но побоялись, что вас побьют вместе с ним, а потом и вовсе вы станете изгоем, как Гарри.\n"
                         "\n<i><b>Ваша задача:</b></i> вот ваш шанс помочь мальчику, расскажите то, что знаете и видели, предложите свои варианты помощи при обсуждении.".format(message.from_user, bot.get_me()),parse_mode='html')
        # bot.send_video(message.chat.id, videoSub1)
    elif message.text == "Родители":
        bot.send_message(message.chat.id,"Вашего ребенка Гарри постоянно обижаю одноклассники, иногда даже доходит до драк. Ребенок стал мало кушать, ночью просыпается от кошмаров. Вы стали замечать, что он перестал брать карманные деньги с собой в школу, его рюкзак стал грязным и рваным. Беседы с классным руководителем ни к чему не привели. Сменить школу вы не можете, поскольку все другие школы очень далеко от дома. Вы считаете, что не вам стоит переходить в другую школу, а наказать обидчиков своего сына.\n"
                         "\n<i><b>Ваша задача:</b></i> найти решения данного конфликта, придите к точному решению, чтобы ваш ребенок больше не терпел угрозы и драки.".format(message.from_user, bot.get_me()),parse_mode='html')
        # bot.send_video(message.chat.id, videoSub2)

# Обработка команды для выхода
@bot.message_handler(commands=['stop'])
def bye(message):
    hideBoard = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id,
                     "Пока, Пока!".format(
                         message.from_user, bot.get_me()), parse_mode='html', reply_markup=hideBoard)


bot.polling(none_stop=True, interval=0)
