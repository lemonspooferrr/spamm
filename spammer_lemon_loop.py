from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import asyncio
import os
import random

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_string = os.getenv("SESSION_STRING")

client = TelegramClient(StringSession(session_string), api_id, api_hash)

groups = [
    '@chezfox', '@ChezEscroww', '@ChezVanGogh', '@LesMiserablesChat',
    '@chezdsavv', '@chezcesarr', '@chezmonkey', '@carteccdrop',
    '@chezexpresscc', '@chezcardhouse', '@ChezSadiooo', '@chezmousko',
    '@ChezAFT', '@ChezStagiaireDuSud', '@chezlema', '@chezDoraetLordJeff',
    '@Chezkaskunk', '@ChezFioum', '@chezmarcus', '@LantreFR',
    '@chezmedellincard', '@ahcommunity', '@DarkiAlpha', '@cardeurspmmeur', '@CHEHLACOKE'
]

messages = [
    """📞 LEMON SPOOFER EST EN LIGNE 🔥

Tu veux :
🔹 Changer ton numéro instantanément ?
🔹 Personnaliser ton Caller ID ?
🔹 Envoyer/recevoir des SMS anonymes ?
🔹 Passer des appels via SIP sécurisé ?
🔹 Utiliser une musique d’attente stylée ?
🔹 Payer en crypto automatiquement ?

➡️ Alors @LemonCloudSF_bot est fait pour toi ! 💼
➡️ Rejoins-nous sur @LemonCloudSF_bot
➡️ Commande ta licence depuis @LemonCloudSF_bot

✅ Activation immédiate
✅ Paiement crypto automatique
✅ Interface claire & simple à utiliser
✅ Support actif 7j/7 → @LemonCloudSL

💸 120€ pour 2 mois — prix imbattable Telegram.

📲 Rejoins maintenant → @LemonCloudSF_bot
""",

    """🚨 SPOOFER PRO DISPONIBLE

📞 @LemonCloudSF_bot — pour gérer tes appels comme un pro :
🔧 Numéro modifiable à volonté
👁️ Caller ID personnalisé
📡 SIP, SMS, redirection disponibles
🎵 Musique d’attente intégrée
💳 Paiement crypto automatisé

Pourquoi choisir @LemonCloudSF_bot ?
✅ Interface propre & rapide
✅ Licence instantanée via @LemonCloudSF_bot
✅ Assistance active : @LemonCloudSL

💰 Seulement 120€ pour 2 mois complets

🔥 Lance-toi maintenant → @LemonCloudSF_bot
""",

    """🍋 LEMON SPOOFER PREMIUM — @LemonCloudSF_bot

Tu veux :
📞 Appeler avec un numéro différent ?
👁️ Gérer ton Caller ID ?
📡 Accéder au SIP / SMS comme un pro ?

Tout est dispo sur @LemonCloudSF_bot :
➡️ Commande sur @LemonCloudSF_bot
➡️ Infos et démos dans @LemonCloudSF_bot

✅ Numéro modifiable
✅ Caller ID custom
✅ Accès SIP + SMS + redirection
✅ Paiement 100% crypto
✅ Activation instantanée
✅ Support actif : @LemonCloudSL

🎯 Le tout pour seulement 120€ → 2 mois complets

📲 Prêt ? Clique ici → @LemonCloudSF_bot
"""
]

async def main():
    await client.start()
    while True:
        for group in groups:
            try:
                msg = random.choice(messages)
                await client.send_file(group, 'lemon_spoofer_pub.jpg', caption=msg)
                print(f"[OK] Message envoyé dans : {group}")
                await asyncio.sleep(60)
            except Exception as e:
                print(f"[ERREUR] {group} -> {e}")

with client:
    client.loop.run_until_complete(main())
