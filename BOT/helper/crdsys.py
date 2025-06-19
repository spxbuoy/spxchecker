from FUNC.defs import *
from pyrogram import Client, filters


@Client.on_message(filters.command("howcrd", [".", "/"]))
async def cmd_crdsystem(client, message):
    try:
        resp = f"""<b>
💳 𝘾𝙝𝙖𝙧𝙜𝙚 𝙈𝙖𝙨𝙩𝙚𝙧 𝘾𝙝𝙠  Credit System
━━━━━━━━━━━━━━
● AUTH GATES
   ➔ 1 credit per CC check

● CHARGE GATES
   ➔ 1 credit per CC check

● MASS AUTH GATES
   ➔ 1 credit per CC check

● MASS CHARGE GATES
   ➔ 1 credit per CC check

● CC SCRAPER GATES
   ➔ 1 credit per scraping
        </b>"""
        await message.reply_text(resp, quote=True)

    except Exception:
        import traceback
        await error_log(traceback.format_exc())
