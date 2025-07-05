from telethon.sync import TelegramClient
import asyncio
import random

api_id = 25924294
session_string = """1ApWapzMBuxDe6SfQn0-t918WTihPeawT7rm2wtfMVv0a F142RT-0Xv0Cx16RekvuQta4tfnS1sU42VYDsg81H1Ufe DomqxnwkI49ZTjzOe-3uJZJaYouMrJJy0-L497N4MXy14 08hJ3RgcpxsRhggtCBGCHActG4QyPcu7qEHKxdqY_rTqD vt_Ovza62hzL-vC1MmW6DcZQWwBSQ2yRmYBMsTfC1staJ TjVl6mvV-Ugd-uzXEAi1H5xlKuixnLxGo4M_tBIqpJR0s ssKc_AWXWUYZ2zzOLzsa7JHiC0xmLCdj6XYDZGT7qrC_M ehKEohiX66ded_DoU5aJRIFYKmQZXvEXPT1ZQ="""
api_hash = '2eab80a404b5815dcf0abe3d5b31f851'
client = TelegramClient('lemon_session', api_id, api_hash)

groups = ['@chezfox', '@ChezEscroww', '@ChezVanGogh', '@LesMiserablesChat', '@chezdsavv', '@chezcesarr', '@chezmonkey', '@carteccdrop', '@chezexpresscc', '@chezcardhouse', '@ChezSadiooo', '@chezmousko', '@ChezAFT', '@ChezStagiaireDuSud', '@chezlema', '@chezDoraetLordJeff', '@Chezkaskunk', '@ChezFioum', '@chezmarcus', '@LantreFR', '@chezmedellincard', '@ahcommunity', '@DarkiAlpha', '@cardeurspmmeur', '@CHEHLACOKE']
messages = ['📞 LEMON SPOOFER EST EN LIGNE 🔥\n\nBesoin de changer ton numéro en 1 clic ?  \nDe gérer tes appels comme un pro ?  \nDe personnaliser ton Caller ID ou utiliser SIP/SMS ?  \n\n🔧 LemonSpoofer c’est :\n✅ Numéro modifiable à volonté  \n✅ Caller ID custom  \n✅ Accès SIP + SMS + redirection  \n✅ Musique d’attente  \n✅ Paiement crypto auto  \n✅ Interface propre, rapide  \n✅ Support Telegram actif  \n✅ Activation immédiate\n\n💸 120€ pour 2 mois — prix Telegram imbattable\n\n📲 Clique ici → @LemonSpoofer', '🚀 LEMON SPOOFER — SPOOF PRO\n\n📞 Change ton numéro en temps réel  \n👁️ Caller ID personnalisé  \n📡 SIP / SMS / Redirection disponibles  \n🎵 Musique d’attente intégrée  \n💳 Paiement crypto automatique  \n💼 Interface pro et rapide  \n📲 Activation instantanée + support actif\n\n🎯 120€ pour 2 mois — impossible de trouver moins cher ici\n\nRejoins le projet → @LemonSpoofer', '📞 SPOOFER PREMIUM DISPONIBLE — LEMON🔥\n\nTu veux appeler en numéro masqué, changer ton Caller ID ou gérer tes appels comme un pro ?  \n🔐 LemonSpoofer est LA solution complète, rapide, et anonyme :\n\n✅ Change ton numéro en 1 clic  \n✅ Caller ID 100% personnalisable  \n✅ Accès SIP sécurisé & fiable  \n✅ Envoi/Reception de SMS  \n✅ Musique d’attente personnalisée  \n✅ Paiement crypto automatique (toutes monnaies)  \n✅ Interface propre, rapide, simple  \n✅ Support actif 7j/7  \n✅ Licence instantanée\n\n🔥 Rejoins-nous maintenant → @LemonSpoofer']

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
