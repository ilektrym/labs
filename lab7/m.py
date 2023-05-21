import telebot
from telebot import types
import psycopg2
from datetime import datetime, timedelta

token = "6067524678:AAEjg59UOSUAKeQPT9bqgjbuu7uYkkhOAw0"

bot = telebot.TeleBot(token)

con = psycopg2.connect(database="mtusi_tg",
                        user="postgres",
                        password="12DImA567",
                        host="localhost",
                        port="5432")

cursor = con.cursor()
def week(w):
    now = datetime.now()
    sep = datetime(now.year if now.month >= 9 else now.year - 1, 9, 1)
    d1 = sep - timedelta(days=sep.weekday())
    d2 = now - timedelta(days=now.weekday())
    weekC = ((d2 - d1).days // 7) % 2
    if weekC == 0 and w == 0:
        week = 2
    elif weekC == 0 and w == 1:
        week = 1
    elif weekC == 1 and w == 0:
        week = 1
    elif weekC == 1 and w == 1:
        week = 2
    return week

def day(day1, day2, week):
    lines = ''
    for day in range(day2, day1 + 1):
        rec3 = ['ПОНЕДЕЛЬНИК', 'ВТОРНИК', 'СРЕДА', 'ЧЕТВЕРГ', 'ПЯТНИЦА', 'СУБОТА']
        rec4 = ['1. 09:30 - 11:05', '2. 11:20 - 12:55', '3. 13:10 - 14:45', '4. 15:25 - 17:00', '5. 17:15 - 18:50']
        cursor.execute("SELECT par, room_numb, vers, name_p, start_time, day \
                           FROM timetable JOIN day ON day.id = timetable.day_id\
                           JOIN par ON par.id = timetable.start_time \
                           JOIN week ON week.id = timetable.week_id \
                           JOIN subject ON subject.id = timetable.subject_id \
                           JOIN vers ON vers.id = timetable.vers_id \
                           WHERE week_id = %s and day_id = %s", (int(week), int(day)))
        rec = list(cursor.fetchall())
        lines += '\n\n' + rec3[day - 1]
        rec2 = []
        for i in range(0,len(rec)):
            vers = rec[i][2]
            name_p = rec[i][3]
            cursor.execute("SELECT full_name FROM teacher_vers\
                           JOIN vers ON vers.id = teacher_vers.vers_id \
                           JOIN teacher ON teacher.id = teacher_vers.teacher_id \
                           JOIN subject ON subject.id = teacher.subject_id \
                       WHERE vers = %s and name_p = %s", (str(vers), str(name_p)))
            rec2 += list(cursor.fetchall())
        st = ''
        s = ''
        for h in range(len(rec)):
            s += str(h)
        for i in range(len(rec)):
            st += str(rec[i][4])
        for n in range(1, 6):
            if str(n) in st:
                a = int(s[:1])
                name = str(rec2[a])
                time = str(rec[a][0])
                subject = str(rec[a][3])
                vers = str(rec[a][2])
                kab = str(rec[a][1])
                start = str(rec[a][4])
                line = '\n' + start + '. ' + time + '\n' + subject + '\n' + (name[2:])[:-4] + '\n' + vers + ' в ' + kab + '\n'
                lines = lines + str(line)
                s = s[1:]
            else:
                lines += '\n' + str(rec4[n - 1]) + '\n' + '<Нет пары>' + '\n'
    return lines


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text = '/help',callback_data='/help'))
    keyboard.add(types.InlineKeyboardButton(text = '/Monday',callback_data='/Monday'))
    keyboard.add(types.InlineKeyboardButton(text = '/Tuesday',callback_data='/Tuesday'))
    keyboard.add(types.InlineKeyboardButton(text = '/Wednesday',callback_data='/Wednesday'))
    keyboard.add(types.InlineKeyboardButton(text = '/Thursday',callback_data='/Thursday'))
    keyboard.add(types.InlineKeyboardButton(text = '/Friday',callback_data='/Friday'))
    keyboard.add(types.InlineKeyboardButton(text = '/Saturday',callback_data='/Saturday'))
    keyboard.add(types.InlineKeyboardButton(text = '/Week',callback_data='/Week'))
    keyboard.add(types.InlineKeyboardButton(text = '/Next_week',callback_data='/Next_week'))
    keyboard.add(types.InlineKeyboardButton(text = '/mtusi',callback_data='/mtusi'))
    bot.send_message(message.chat.id, 'Здравствуйте! Хотите узнать свежую информацию о МТУСИ?', reply_markup=keyboard )


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, '/help - списк команд\n/Monday - Расписание на понедельник\n/Tuesday - Расписание на вторник\n\
/Wednesday - Расписание на среду\n/Thursday - Расписание на четверг\n\
/Friday - Расписание на пятницу\n/Saturday - Расписание на субботу\n\
/Week - Расписание на текущую неделю\n/Next_week - Расписание на следующую неделю\n\
/mtusi - Информация о МТУСИ')


@bot.message_handler(commands=['mtusi'])
def answer(message):
    bot.send_message(message.chat.id, 'МТУСИ - https://mtuci.ru/')


@bot.message_handler(commands=['Monday'])
def answer(message):
    lines = day(1, 1, week(0))
    bot.send_message(message.chat.id, lines)


@bot.message_handler(commands=['Tuesday'])
def answer(message):
    lines = day(2, 2, week(0))
    bot.send_message(message.chat.id, lines)


@bot.message_handler(commands=['Wednesday'])
def answer(message):
    lines = day(3, 3, week(0))
    bot.send_message(message.chat.id, lines)


@bot.message_handler(commands=['Thursday'])
def answer(message):
    lines = day(4, 4, week(0))
    bot.send_message(message.chat.id, lines)


@bot.message_handler(commands=['Friday'])
def answer(message):
    lines = day(5, 5, week(0))
    bot.send_message(message.chat.id, lines)


@bot.message_handler(commands=['Saturday'])
def answer(message):
    lines = day(6, 6, week(0))
    bot.send_message(message.chat.id, lines)


@bot.message_handler(commands=['Week'])
def answer(message):
    lines = day(6, 1, week(0))
    bot.send_message(message.chat.id, lines)


@bot.message_handler(commands=['Next_week'])
def answer(message):
    lines = day(6, 1, week(1))
    bot.send_message(message.chat.id, lines)

bot.polling()