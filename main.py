    import time
    import os
    from telethon.sync import TelegramClient
    from telethon.sessions import StringSession
    from telethon import TelegramClient, sync, events, utils
    from telethon.tl.functions.channels import JoinChannelRequest
    from telethon.tl.functions.channels import LeaveChannelRequest

    APP_ID = API
    API_HASH = 'HASH' 

    client = TelegramClient('anon', APP_ID, API_HASH).start()
    #6281315912347
    seconds= int(0)
    minutes= int(0)
    run = "dia"
    while run.lower()=="dia":
      if seconds == 35:
          pesan = "/promote"
          client.send_message('promoteautobot', pesan)
          
      if seconds == 50:
          #print ("ok")
          for message in client.iter_messages('promoteautobot', limit=1):
            (utils.get_display_name(message.sender), message.message)
            user = (message.message)
            pesan = client.get_messages('promoteauto', None)
            #print(pesan[0])
            client(JoinChannelRequest(user))
            client.forward_messages(user, pesan[0])
            client(LeaveChannelRequest(user))
            pesanisi = ("@"+user)
            client.send_message('niddumulu', pesanisi)
      if seconds == 120:
          seconds = 1  
      os.system('clear')
      seconds = (seconds+1)
      print (seconds)
      time.sleep(1)
