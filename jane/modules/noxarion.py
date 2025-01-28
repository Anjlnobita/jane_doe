from telethon import events, functions
from telethon.tl.types import ChatAdminRights

@events.register(outgoing=True, pattern=r"\.promote")
async def promote(event):
    chat = await event.get_chat()
    user = await event.get_reply_message()
    if user:
        user_id = user.from_id
        await event.client(functions.channels.EditAdmin(
            channel=chat.id,
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
        ))
        await event.reply("promoted!")
    else:
        await event.reply("reply a user give me id!")

@events.register(outgoing=True, pattern=r"\.demote")
async def demote(event):
    chat = await event.get_chat()
    user = await event.get_reply_message()
    if user:
        user_id = user.from_id
        await event.client(functions.channels.EditAdmin(
            channel=chat.id,
            user_id=user_id,
            admin_rights=ChatAdminRights(
                change_info=False,
                post_messages=False,
                edit_messages=False,
                delete_messages=False,
                ban_users=False,
                invite_users=False,
                pin_messages=False,
                add_admins=False
            )
        ))
        await event.reply("demoted!")
    else:
        await event.reply("reply a user or give me id!")