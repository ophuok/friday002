import requests
from telethon.events import ChatAction

@borg.on(ChatAction)
async def ok(event):
    if Configs.ANTISPAM_FEATURE != 'ENABLE':
        return
    if event.user_joined or event.user_added:
        juser = await event.get_user()
        data = {
          'token': Config.ANTI_SPAMINC_TOKEN,
          'userid': juser.id
          }
        url = f'http://antispaminc.tk/info/'
        sed = requests.post(url=url, data=data).json()
        if sed['error'] == True:
            logger.info(f"Errors, I Got Error While Detecting Antispam, Please Report This Error, \nERROR : {sed['full']}")
            return
        else:
            if sed['banned'] == True:
              try:
                  await borg.edit_permissions(
                  event.chat_id, juser.id, view_messages=False
                )
                  await event.reply(f"**#FRIDAY-ANTISPAM** \n**Detected Malicious User.** \n**User-ID :** `{juser.id}`  \n**Reason :** `{sed['reason']}`")
              except:
                  pass
          else:
              pass
