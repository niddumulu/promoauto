import time
import os
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon import TelegramClient, sync, events, utils
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import LeaveChannelRequest

api_id = 682610
api_hash = '030132b51d598e464419ccee7f20212d'
client = TelegramClient('munajatkeren', api_id, api_hash).start()

seconds = int(0)
minutes = int(0)

run = "dia"
while run.lower() == "dia":
    if seconds == 10:
          pesan = "/promote"
          client.send_message('promoteautobot', pesan)
      
    if seconds == 25:
        for message in client.iter_messages('promoteautobot', limit=1):
          (utils.get_display_name(message.sender), message.message)
          user = (message.message)
          pesan = client.get_messages('promoteauto', None)
          #print(pesan[0])
          client(JoinChannelRequest(user))
          client.forward_messages(user, pesan[0])
          #client(LeaveChannelRequest(user))
          #print ("Lapor")
          pesanisi = ("Lapor!! Posting ke group @"+user)
          client.send_message('checkonoff', pesanisi)

    if seconds == 240:
        seconds = 0

    os.system('clear')
    seconds = (seconds+1)
    print (seconds)
    time.sleep(1)
