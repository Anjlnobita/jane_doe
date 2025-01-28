
from jane import dispatcher 
from telegram import Update, ParseMode
from telegram.ext import CallbackContext, MessageHandler, Filters
from telegram.error import BadRequest
from jane import OWNER_ID

def promote(update: Update, context: CallbackContext) -> str:
    bot = context.bot
    args = context.args
    message = update.effective_message
    chat = update.effective_chat
    user = update.effective_user

    if not user.id in OWNER_ID:
        message.reply_text("» ʏᴏᴜ ᴄᴀɴ'ᴛ ᴘʀᴏᴍᴏᴛᴇ ᴜsᴇʀs, ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴀ ᴅʀᴀɢᴏɴ !")
        return

    user_id = extract_user(message, args)
    if not user_id:
        message.reply_text("» ɪ ᴅᴏɴ'ᴛ ᴋɴᴏᴡ ᴡʜᴏ's ᴛʜᴀᴛ ᴜsᴇʀ, ɴᴇᴠᴇʀ sᴇᴇɴ ʜɪᴍ ɪɴ ᴀɴʏ ᴏғ ᴛʜᴇ ᴄʜᴀᴛs ᴡʜᴇʀᴇ ɪ ᴀᴍ ᴩʀᴇsᴇɴᴛ !")
        return

    try:
        user_member = chat.get_member(user_id)
    except:
        return

    if user_member.status in ("administrator", "creator"):
        message.reply_text("» ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴍᴇ ᴛʜᴀᴛ ᴜsᴇʀ ɪs ᴀʟʀᴇᴀᴅʏ ᴀɴ ᴀᴅᴍɪɴ ʜᴇʀᴇ !")
        return

    if user_id == bot.id:
        message.reply_text("» ɪ ᴄᴀɴ'ᴛ ᴩʀᴏᴍᴏᴛᴇ ᴍʏsᴇʟғ, ᴍʏ ᴏᴡɴᴇʀ ᴅɪᴅɴ'ᴛ ᴛᴏʟᴅ ᴍᴇ ᴛᴏ ᴅᴏ sᴏ.")
        return

    bot_member = chat.get_member(bot.id)
    try:
        bot.promoteChatMember(
            chat.id,
            user_id,
            can_change_info=bot_member.can_change_info,
            can_post_messages=bot_member.can_post_messages,
            can_edit_messages=bot_member.can_edit_messages,
            can_delete_messages=bot_member.can_delete_messages,
            can_invite_users=bot_member.can_invite_users,
            can_manage_voice_chats=bot_member.can_manage_voice_chats,
            can_pin_messages=bot_member.can_pin_messages,
        )
        message.reply_text(f"» ᴩʀᴏᴍᴏᴛᴇᴅ {user_member.user.first_name} ɪɴ {chat.title}!")
    except BadRequest as err:
        if err.message == "User_not_mutual":
            message.reply_text("» ᴛʜᴇ ᴜsᴇʀ ᴅᴏᴇs ɴᴏᴛ ʜᴀᴠᴇ ᴀ ᴍᴜᴛᴜᴀʟ ᴄʜᴀᴛ ᴡɪᴛʜ ᴛʜᴇ ʙᴏᴛ.")
        else:
            message.reply_text("» ᴛʜᴇʀᴇ ᴡᴀs ᴀɴ ᴇʀʀᴏʀ ᴡʜɪʟᴇ ᴘʀᴏᴍᴏᴛɪɴɢ ᴛʜᴇ ᴜsᴇʀ.")


dispatcher.add_handler(MessageHandler(Filters.command('promote') & Filters.group, promote))
