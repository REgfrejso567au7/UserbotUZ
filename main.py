from telethon import TelegramClient
import asyncio
import os
import random
import time

# API ma'lumotlaring (o'zgartirmang)
api_id = 27050524
api_hash = 'd3ac48b864c2b8c84dc7192436ff28cf'
client = TelegramClient('session', api_id, api_hash)

# Guruhlar ro'yxati
groups = [
    '@garantliy', '@garantuzfor', '@ixtiyor_savdo_tm', '@uzfor_rubluz', '@uzfor_savdo',
    'https://t.me/+fpS0SqUTyW0yNGUy', '@jild_bor', 'https://t.me/papka_jildd', 'https://t.me/+pEQ4gBrYrnE4ZTU6',
    'https://t.me/Uzbek_forum_savdo_chat', '@forum_obmen', 'https://t.me/GROUPGARANT',
    'https://t.me/tezkor_uzfor', 'https://t.me/Garand_savdo_guruhi', 'https://t.me/rek_vz_reak_jild_papka',
    'https://t.me/uzfornet_25', 'https://t.me/UZFORNET_GARANT', 'https://t.me/uzfornet',
    'https://t.me/Kanallar_va_Guruhlar_Savdosi_uz', 'https://t.me/instasavdolar'
]

# Rasmlar va ularning matnlari
image_messages = [
    {"file": "images/rasm1.jpg", "caption": "📦 Jild va papkalar sotiladi. Sifatli va arzon!"},
    {"file": "images/rasm2.jpg", "caption": "💼 Garant bilan xavfsiz savdo. Ishonchli xizmat."},
    {"file": "images/rasm3.jpg", "caption": "📁 Har xil dizayndagi papkalar bor. Bog'laning!"}
]

# Matnli xabar
text_messages = [
    "📢 Arzon narxda kanal va guruhlar sotiladi! Garant orqali savdo! 🤝",
    "🎯 Siz izlagan papkalar bizda! Tezda buyurtma bering 📩",
    "📬 Yangilik: Endi to‘lovlar kafolat bilan! @garantliy orqali murojaat qiling!",
    "🛍️ Rasmli papkalar, maxsus dizayn – faqat bizda!"
]

# Xabar yuborish funksiyasi
async def send_messages():
    while True:
        for group in groups:
            try:
                # 3 ta rasmli xabar
                for item in image_messages:
                    await client.send_file(group, item["file"], caption=item["caption"])
                    await asyncio.sleep(3)

                # 1 ta matnli xabar
                text = random.choice(text_messages)
                await client.send_message(group, text)
                print(f"Yuborildi: {group}")
                await asyncio.sleep(10)  # Guruhlar orasida pauza
            except Exception as e:
                print(f"Xatolik: {e}")
        
        # 10–15 daqiqa kutish
        delay = random.randint(600, 900)
        print(f"\n⏳ Keyingi yuborish {delay//60} daqiqadan so‘ng bo‘ladi...\n")
        await asyncio.sleep(delay)

# Botni ishga tushurish
async def main():
    await client.start()
    print("✅ Userbot ishga tushdi!")
    await send_messages()

with client:
    client.loop.run_until_complete(main())
