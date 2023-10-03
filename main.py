
import telegram.ext
import wikipedia

time_table = {
    'monday':{'1':'Physics LHS','2':'Chemistry LHS','3':'Mentor','4':'English LHS','5':'Mat LHS','6':'Phy/Chem Lab','7':'Phy/Chem Lab'},
    'tuesday':{'1':'Py LHS','2':'LIB','3':'Chemistry LHS','4':'Physics LHS','5':'English LHS','6':'Mat LHS','7':'Mat LHS'},
    'wednesday':{'1':'Py Lab','2':'PY Lab','3':'Py Lab','4':'Py Lab','5':'Mat LHS','6':'English LHS','7':'Mentor'},
    'thursday':{'1':'Chemistry LHS','2':'Py LHS','3':'Physics LHS','4':'Py LHS','5':'Phy Lab','6':'Phy Lab','7':'Math LHS'},
    'friday':{'1':'Physics LHS','2':'Py LHS','3':'PY LHS','4':'Chemistry LHS','5':'COMM Lab','6':'COMM Lab','7':'COMM Lab'},
    'saturday':{'1':'Py LHS','2':'English LHS','3':'Mat LHS','4':'Physics LHS','5':'Chemistry LHS','6':'Tamil LHS','7':'Mat LHS'}

}

TOKKEN = "6502181588:AAEifHo_iMMmZi7YjUcPO2EoN2yy7pjenxY"

updater = telegram.ext.Updater(TOKKEN,use_context=True)
dispature = updater.dispatcher

# /period day period
def period(update,context):
    data = str(update.message.text).lower()
    ty = data.split()
    if len(ty)==2:
        str1 =""
        d = time_table[f'{ty[1]}'].values()
        #f = time_table[]
        for i in d:
            #print(i)
            str1+=f'{i} \n'
        update.message.reply_text(str1)
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
    update.message.reply_text('''Send number to Me to generate the link...\nfor eg :    \nuser : /whatsapp 94333#####\nBot : link(https://a.....\ntest now''')


dispature.add_handler(telegram.ext.CommandHandler('start', start))
dispature.add_handler(telegram.ext.CommandHandler('whatsapp',whatsapp))
dispature.add_handler(telegram.ext.CommandHandler('spammsg',spam_msg))
dispature.add_handler(telegram.ext.CommandHandler('period',period))
dispature.add_handler(telegram.ext.CommandHandler('wiki',wiki))
dispature.add_handler(telegram.ext.CommandHandler('help', help))

updater.start_polling()
updater.idle()