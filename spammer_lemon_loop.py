from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import asyncio
import os
import random

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_string = os.getenv("SESSION_STRING")
client = TelegramClient(StringSession(session_string), api_id, api_hash)

groups = ['@chezfox', '@ChezEscroww', '@ChezVanGogh', '@LesMiserablesChat', '@chezdsavv', '@chezcesarr',
          '@chezmonkey', '@carteccdrop', '@chezexpresscc', '@chezcardhouse', '@ChezSadiooo', '@chezmousko',
          '@ChezAFT', '@ChezStagiaireDuSud', '@chezlema', '@chezDoraetLordJeff', '@Chezkaskunk', '@ChezFioum',
          '@chezmarcus', '@LantreFR', '@chezmedellincard', '@ahcommunity', '@DarkiAlpha', '@cardeurspmmeur',
          '@CHEHLACOKE']

messages = [
    '📞 LEMON SPOOFER EST EN LIGNE 🔥\n\nBesoin de changer ton numéro en 1 clic ?\nDe gérer tes appels comme un pro ?\nDe personnaliser ton Caller ID ou utiliser SIP/SMS ?\n\n🔧 LemonSpoofer c’est :\n✅ Numéro modifiable à volonté\n✅ Caller ID custom\n✅ Accès SIP + SMS + redirection\n✅ Musique d’attente\n✅ Paiement crypto auto\n✅ Interface propre, rapide\n✅ Support Telegram actif\n✅ Activation immédiate\n\n💸 120€ pour 2 mois — prix Telegram imbattable\n\n📲 Clique ici → @LemonSpoofer',
    '🚀 LEMON SPOOFER — SPOOF PRO\n\n📞 Change ton numéro en temps réel\n👁️ Caller ID personnalisé\n📡 SIP / SMS / Redirection disponibles\n🎵 Musique d’attente intégrée\n💳 Paiement crypto automatique\n💼 Interface pro et rapide\n📲 Activation instantanée + support actif\n\n🎯 120€ pour 2 mois — impossible de trouver moins cher ici\n\nRejoins le projet → @LemonSpoofer',
    '📞 SPOOFER PREMIUM DISPONIBLE — LEMON🔥\n\nTu veux appeler en numéro masqué, changer ton Caller ID ou gérer tes appels comme un pro ?\n🔐 LemonSpoofer est LA solution complète, rapide, et anonyme :\n\n✅ Change ton numéro en 1 clic\n✅ Caller ID 100% personnalisable\n✅ Accès SIP sécurisé & fiable\n✅ Envoi/Reception de SMS\n✅ Musique d’attente personnalisée\n✅ Paiement crypto automatique (toutes monnaies)\n✅ Interface propre, rapide, simple\n✅ Support actif 7j/7\n✅ Licence instantanée\n\n🔥 Rejoins-nous maintenant → @LemonSpoofer'
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
