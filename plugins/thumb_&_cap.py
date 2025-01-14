from pyrogram import Client, filters 
from helper.database import madflixbotz

@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**Donne la légende\n\nExample :- `/set_caption 📕Nom ➠ : {filename} \n\n🔗 Size ➠ : {filesize} \n\n⏰ Duration ➠ : {duration}`**")
    caption = message.text.split(" ", 1)[1]
    await madflixbotz.set_caption(message.from_user.id, caption=caption)
    await message.reply_text("**Ta légende été enregistré ✅**")
   
@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(client, message):
    caption = await madflixbotz.get_caption(message.from_user.id)  
    if not caption:
       return await message.reply_text("**Vous n'aviez pas encore enregistréde légende ❌**")
    await madflixbotz.set_caption(message.from_user.id, caption=None)
    await message.reply_text("**Votre légendea été bien effacé 🗑️**")
                                       
@Client.on_message(filters.private & filters.command(['see_caption', 'view_caption']))
async def see_caption(client, message):
    caption = await madflixbotz.get_caption(message.from_user.id)  
    if caption:
       await message.reply_text(f"**Votre legende :**\n\n`{caption}`")
    else:
       await message.reply_text("**Vous n'aviez enregistré aucune légende ❌**")


@Client.on_message(filters.private & filters.command(['view_thumb', 'viewthumb']))
async def viewthumb(client, message):    
    thumb = await madflixbotz.get_thumbnail(message.from_user.id)
    if thumb:
       await client.send_photo(chat_id=message.chat.id, photo=thumb)
    else:
        await message.reply_text("**Vous n'avez pas de vignette  ❌**") 
		
@Client.on_message(filters.private & filters.command(['del_thumb', 'delthumb']))
async def removethumb(client, message):
    await madflixbotz.set_thumbnail(message.from_user.id, file_id=None)
    await message.reply_text("**Votre vignette à été bien effacé 🗑️**")
	
@Client.on_message(filters.private & filters.photo)
async def addthumbs(client, message):
    mkn = await message.reply_text("Please Wait ...")
    await madflixbotz.set_thumbnail(message.from_user.id, file_id=message.photo.file_id)                
    await mkn.edit("**Votre vignette à été enregistré ✅️**")





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper
