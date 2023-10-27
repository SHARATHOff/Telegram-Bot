import telegram.ext
import wikipedia
import csv

def read_csv_file(day):
    global out_data
    out_data = ""
    fp  = open('timetable.csv','r')
    reader = csv.reader(fp)
    for i in reader:
        if i[0].lower()==day:
            f = i
            for j in f:
                out_data+=f'{j}\n'



TOKKEN = "6502181588:AAEifHo_iMMmZi7YjUcPO2EoN2yy7pjenxY"

updater = telegram.ext.Updater(TOKKEN,use_context=True)
dispature = updater.dispatcher



# /period day period
def period(update,context):
    data = str(update.message.text).lower()
    print(data)
    ty = data.split()
    str1=""
    if len(ty)==2:
        read_csv_file(ty[1])
        update.message.reply_text(out_data)
    else:
        update.message.reply_text('Try Again later')


def wiki(update,context):
    text = str(update.message.text).lower()
    dat = text.split()
    person = dat[1::]
    try:
        info = wikipedia.summary(person,sentences=2)
        update.message.reply_text(str(info))
    except:
        update.message.reply_text('unable to find try again!')

def spam_msg(update,context):

    text = str(update.message.text).lower()
    temp = text.split()
    # /spammsg number msgtosend numberofimes
    if len(temp)==4:
        number = temp[1]
        msg = temp[2]
        times = temp[3]
        temp_string = ''''''
        for i in range(1,int(times)+1):
            temp_string+=f'''{msg}\n'''
        link = f'''https://api.whatsapp.com/send?phone={number}&text="{temp_string}"'''
        update.message.reply_text(link)
    else:
        update.message.reply_text("send commands as per given bellow \n /spammsg phone-number msgtosend msg-times-to-type")

def start(update,context):
    update.message.reply_text("hello Guys This BOT is on Developing Focus on UNIQUE_TASK until now we have createad program to generate the whatsapp Direct Link \n we will work on so \n Say /help to know more")
def whatsapp(update,context):
    text1 = str(update.message.text).lower()
    text = text1.split()
    if len(text)==2:
        number = text[1]
        link = f'https://wa.me/+91{number}'
        update.message.reply_text(link)
    else:
        update.message.reply_text('''Send number to Me to generate the link...\nfor eg :    \nuser : /whatsapp 94333#####\nBot : link(https://a.....\ntest now''')


def help(update,context):
    help_text='''/whatsapp to generate direct message link\n '''
    update.message.reply_text('''Send number to Me to generate the link...\nfor eg :    \nuser : /whatsapp 94333#####\nBot : link(https://a.....\ntest now''')


dispature.add_handler(telegram.ext.CommandHandler('start', start))
dispature.add_handler(telegram.ext.CommandHandler('whatsapp',whatsapp))
#dispature.add_handler(telegram.ext.CommandHandler('spammsg',spam_msg))
dispature.add_handler(telegram.ext.CommandHandler('period',period))
dispature.add_handler(telegram.ext.CommandHandler('wiki',wiki))
dispature.add_handler(telegram.ext.CommandHandler('help', help))

updater.start_polling()
updater.idle()