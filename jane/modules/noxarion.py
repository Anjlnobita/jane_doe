# Promote User in Telegram Chat

from telethon import events, functions
from telethon.tl.types import ChatAdminRights
from telethon.errors import UserNotParticipant
from jane import telethn

@telethn.on(events.NewMessage(pattern=f"^[!/]promote ?(.*)"))
async def promote(event):
    chat = await event.get_chat()
    user = await event.get_reply_message()
    if user:
        user_id = user.from_id
        try:
            user_member = await chat.get_member(user_id)
        except UserNotParticipant:
            await event.reply("» The user is not a member of this chat.")
            return
        if user_member.status in ("administrator", "creator"):
            await event.reply("» According to me that user is already an admin here!")
            return
        if user_id == telethn.me.id:
            await event.reply("» I can't promote myself.")
            return
        try:
            await telethn.edit_admin(
                chat_id=chat.id,
                user_id=user_id,
                admin_rights=ChatAdminRights(
                    change_info=True,
                    post_messages=True,
                    edit_messages=True,
                    delete_messages=True,
                    ban_users=True,
                    invite_users=True,
                    pin_messages=True,
                    add_admins=True
                )
            )
            await event.reply(f"» Promoted {user_member.user.first_name} in {chat.title}!")
        except Exception:
            await event.reply("» Something went wrong.")
    else:
        await event.reply("» You don't have permissions to add new admins.")
