PRODUCTS = {
    "disposables": {
    "🔥 FUMMO LIT 🔥": {
        "name": f"FUMMO LIT (25000 затяжек)\n"
        f"1.🍭🍬 фруктовые конфеты ( ассорти из тропических фруктов)\n"
        f"Цена: 952 ₽"
        ,
        "photos": "photos/fumo_lit.jpg",
        },
    "💥 VOZOL VISTA 💥": {
        "name":
        f"VOZOL VISTA (20000 затяжек)\n"
        f"1.🍓🥭 клубника манго(нет в наличии)\n"
        f"2.🍑🧊 персиковый лед\n"
        f"Цена: 1149 ₽"
        ,
        "photos": "photos/vozol_vista.jpg",
        },
    "✨ WAKA EXTRA ✨": {
        "name": f"WAKA EXTRA V2 SOPRO (20000 затяжек)\n"
        f"🍒 Ежевика, вишня, гранат\n"
        f"Цена: 1599 ₽",
        "photos": "photos/waka_extra_v2.jpg",
        },
    },
    "liquids": {
    "💞 Annima Love Gold 💛": {
        "name": f"🚬🍓✨ | Annima Love Gold 80 мг 💎\n"
        f"Новые поступления ароматов премиум-класса: \n\n"
        f"1.🫐 Blueberry Pomegranate\n\n"
        f"2.🫐 Blueberry Blackberry\n"
        f"Цена: 450 ₽",
        "photos": "photos/annima_love.jpg",
        },
    "🦔 Monstervapor Ice 7 % 🧊": {
        "name": f"☃️🔥🌿 | Monstervapor Ice 7%\n"
        f"Новый вкус свежести и прохлады: \n\n"
        f"1.🥃🍋 Кола лимон лед(нет в наличии)\n"
        f"Цена: 400 ₽",
        "photos": "photos/monstervapor_ice.jpg",
        },
    "🌪️ VYEBON 🌪️": {
        "name": f"💥VYEBON💥  70 мг\n\n"
        f"1. 🍒 Currant raspberry\n\n"
        f". 🍉 Pomegranate lemonade\n\n"
        f"3. 🍦 Raspberry yogurt\n\n"
        f"4. 🍓 Strawberry puer\n"
        f"Цена: 349 ₽",
        "photos": "photos/vyebon.jpg",
        },
    "🐱 CATS&DOTA ❌": {
        "name": f"CATS&DOTA 50 мг\n\n"
        f"1🍬 Кислые желейные мишки с ананасом и бананом\n\n"
        f"2. 🍎 Освежающий яблочный сидр\n"
        f"Цена: 400 ₽",
        "photos": "photos/catsdota.jpg",
        },
    "💊 Анархия V2 ‼️": {
        "name": f"Анархия V2 70 мг\n\n"
        f"1. 🍒 Клюква яблоко\n\n"
        f"2. 🍓 Малиновый лимонад\n\n"
        f"3. 🥭 Манго, пина колада\n\n"
        f"4. ⚡ Энергетик с лесными ягодами(нет в наличии)\n"
        f"Цена: 400 ₽",
        "photos": "photos/anarchy.jpg",
        },
    },
    "cartridges": {
        "🔒 XROS": {
            "name":
            f"0,4 | 0,6 ом(нет в наличии)\n"
            f"Цена: 350 ₽",
            "photos": "photos/cartridge.jpg",
        },
    },
}

def get_products(products_name):

    for category in PRODUCTS:
        if products_name in PRODUCTS[category]:
            return PRODUCTS[category][products_name]

    return None