import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # Configuration du client Pyrogram
    API_ID    = os.environ.get("API_ID", "25926022")
    API_HASH  = os.environ.get("API_HASH", "30db27d9e56d854fb5e943723268db32")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7651245111:AAFO09GZZWMhP1-OLGzxVX6gzFVz6jCEPbU") 

    # Configuration de la base de données
    DB_NAME = os.environ.get("DB_NAME", "aniflix")     
    DB_URL  = os.environ.get("DB_URL", "mongodb+srv://Aniflix:Lipun123@aniflix.q2wina5.mongodb.net/?retryWrites=true&w=majority&appName=Aniflix")
 
    # Autres configurations
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://envs.sh/vrl.jpg")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6475872631,7428552084').split(',')]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "AMAZON_ANIME") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002289696049"))
    
    # Configuration du Webhook     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # Partie pour configurer les textes du bot
        
    START_TXT = """Salut {} 
    
➻ Ceci est un bot avancé et puissant pour renommer vos fichiers.
  
➻ Avec ce bot, vous pouvez renommer automatiquement vos fichiers.  

➻ Ce bot prend également en charge les miniatures et les légendes personnalisées.  

➻ Utilisez la commande /tutorial pour savoir comment m'utiliser."""
    
    FILE_NAME_TXT = """<b><u>ÉTAPE POUR RENOMMER AUTOMATIQUEMENT</u></b>

Utilisez ces mots-clés pour configurer un nom de fichier personnalisé :

✓ episode :- Remplace le numéro de l'épisode  
✓ quality :- Remplace la résolution vidéo  

<b>➻ Exemple :</b> <code>/autorename Naruto Shippuden S02 - EPepisode - qualité  [Doublage Audio] - @Otakukingcey1</code>

<b>➻ Votre format pour renommer :</b> <code>{format_template}</code> """
    
    ABOUT_TXT = f"""<b>🤖 Nom :</b> <a href='http://t.me/Henco_autorenamebot'>Bot de Renommage Automatique ⚡</a>
<b>📝 Langage :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Bibliothèque :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🚀 Serveur :</b> <a href='https://t.me/Otakukingcey1'>KGC</a>
<b>📢 Chaîne :</b> <a href='https://t.me/otakukingcey1'>Kingcey</a>
<b>🧑‍💻 Développeur :</b> <a href='https://t.me/Kingcey'>AntiFlix</a>
    
<b>♻️ Créé par :</b> @Otakukingcey1 """

    
    THUMBNAIL_TXT = """<b><u>🖼️ Comment utiliser les miniatures</u></b>
    
⦿ Vous pouvez ajouter une miniature personnalisée en m'envoyant une photo.  
⦿ /viewthumb - Pour voir votre miniature  
⦿ /delthumb - Pour supprimer votre miniature"""

    CAPTION_TXT = """<b><u>📝 Comment configurer une légende</u></b>
    
⦿ /set_caption - Utilisez cette commande pour définir une légende  
⦿ /see_caption - Utilisez cette commande pour voir la légende actuelle  
⦿ /del_caption - Utilisez cette commande pour supprimer votre légende"""

    PROGRESS_BAR = """\n
<b>📁 Taille</b> : {1} | {2}
<b>⏳️ Fait</b> : {0}%
<b>🚀 Vitesse</b> : {3}/s
<b>⏰️ Temps restant</b> : {4} """
    
    
    DONATE_TXT = """<b>🥲 Merci pour votre intérêt à soutenir ce projet ❤️</b>
    
Si vous appréciez mes bots et mes projets, vous pouvez 🎁 me faire un don du montant de votre choix, à partir de 1 euro ou plus.
    
<b>🛍 Identifiant UPI :</b> <code>madflixofficial@axl</code> """
    
    HELP_TXT = """<b>Salut</b> {}
    
Voici un aperçu des commandes disponibles pour utiliser ce bot."""
