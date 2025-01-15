import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "25926022")
    API_HASH  = os.environ.get("API_HASH", "30db27d9e56d854fb5e943723268db32")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7920699861:AAH2CXFZUbTyST4E9Llx9TFHqoDZWkLabdg") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","auto")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://auto:autoren@auto.0igu7.mongodb.net/?retryWrites=true&w=majority&appName=auto")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://envs.sh/vrl.jpg")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6475872631,7428552084').split(',')]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "AMAZON_ANIME") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002289696049"))
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """Salut {} 
    
➻ Ceci est un bot de renommage avancé et puissant.
  
➻ Avec ce bot, vous pouvez renommer automatiquement vos fichiers.  

➻ Ce bot prend également en charge les miniatures personnalisées et les légendes personnalisées.  

➻ Utilisez la commande /tutorial pour savoir comment m'utiliser."""
    
    FILE_NAME_TXT = """<b><u>ÉTAPE D'AUTO RENAME</u></b>

Utilisez ces mots-clés pour configurer un nom de fichier personnalisé :

✓ episode :- Pour remplacer le numéro de l'épisode  
✓ quality :- Pour remplacer la résolution vidéo  

<b>➻ Example :</b> <code> /autorename Naruto Shippuden S02 - EPepisode - qualité  [Doublage Audio] - @Otakukingcey1 </code>

<b>➻ Votre Format d'auto rename :</b> <code>{format_template}</code> """
    
    ABOUT_TXT = f"""<b>🤖 Mon Nom :</b> <a href='http://t.me/Henco_autorenamebot'>Auto Rename Bot ⚡</a>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🚀 Server :</b> <a href='https://t.me/Otakukingcey1'>KGC</a>
<b>📢 Chaine :</b> <a href='https://t.me/otakukingcey1'>Kingcey</a>
<b>🧑‍💻 Developer :</b> <a href='https://t.me/Kingcey'>AntiFlix</a>
    
<b>♻️ Bot crée par :</b> @Otakukingcey1 """

    
    THUMBNAIL_TXT = """<b><u>🖼️  Comment utiliser La Vignette</u></b>
    
⦿ Vous pouvez ajouter une miniature personnalisée simplement en m'envoyant une photo...  
⦿ /viewthumb - Utilisez cette commande pour voir votre miniature  
⦿ /delthumb - Utilisez cette commande pour supprimer votre miniature"""

    CAPTION_TXT = """<b><u>📝  COMMENT AJOUTER UNE LÉGENDE</u></b>
    
⦿ /set_caption - Utilisez cette commande pour définir votre légende  
⦿ /see_caption - Utilisez cette commande pour voir votre légende  
⦿ /del_caption - Utilisez cette commande pour supprimer votre légende"""

    PROGRESS_BAR = """\n
<b>📁 Size</b> : {1} | {2}
<b>⏳️ Done</b> : {0}%
<b>🚀 Speed</b> : {3}/s
<b>⏰️ ETA</b> : {4} """
    
    
    DONATE_TXT = """<b>🥲 Merci pour être intéressé à la donation! ❤️</b>
    
Si vous aimez mes bots et projets, vous pouvez 🎁 me faire un don de n'importe quel montant à partir de 1 ou 500f euros jusqu'à ce que vous le souhaitiez.
    
<b>🛍 UPI ID:</b> <code>madflixofficial@axl</code> """
    
    HELP_TXT = """<b>Hey</b> {}
    
Ici, c'est juste l'aide pour mes commandes."""





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper
