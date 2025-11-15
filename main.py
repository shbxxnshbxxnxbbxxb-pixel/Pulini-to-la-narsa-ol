from flask import Flask, render_template, abort

app = Flask(__name__)

# Mahsulotlar ro'yxati
products = [
    {
        "id": 1,
        "slug": "laptop-sumka",
        "name": "Laptop Sumkasi",
        "description": "Yuqori sifatli, suvga chidamli laptop sumkasi. 15.6 dyuymgacha noutbuklar uchun mos. Ko'p cho'ntakli va bardoshli dizayn.",
        "image": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60",
        "price": "250,000"
    },
    {
        "id": 2,
        "slug": "simsiz-quloqchin",
        "name": "Simsiz Quloqchin",
        "description": "Bluetooth quloqchin, bass musiqalar uchun ideal. 20 soat batareya quvvati va shovqinni kamaytirish funksiyasi.",
        "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60",
        "price": "450,000"
    },
    {
        "id": 3,
        "slug": "smartfon-uchun-uskunalar",
        "name": "Smartfon Aksessuarlari To'plami",
        "description": "Himoya oynasi, silikonli qopqoq, zaryadlovchi va telefon uchun ushlagich. 4 ta mahsulot bitta to'plamda!",
        "image": "https://images.unsplash.com/photo-1556656793-08538906a9f8?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60",
        "price": "180,000"
    },
    {
        "id": 4,
        "slug": "portativ-zaryadlovchi",
        "name": "20,000mAh Powerbank",
        "description": "Tezkor zaryadlash funksiyasiga ega portativ zaryadlovchi. Barcha qurilmalar bilan mos. 3 marta to'liq zaryadlash imkoniyati.",
        "image": "https://images.unsplash.com/photo-1609091839311-d5365f9ff1c5?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60",
        "price": "320,000"
    },
    {
        "id": 5,
        "slug": "rgb-klaviatura",
        "name": "Gaming RGB Klaviatura",
        "description": "Mexanik tugmachalar, RGB yoritgich, o'yinchilar uchun maxsus dizayn. Anti-ghosting texnologiyasi bilan.",
        "image": "https://images.unsplash.com/photo-1587829741301-dc798b83add3?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60",
        "price": "550,000"
    },
    {
        "id": 6,
        "slug": "smart-soat",
        "name": "Smart Soat Pro",
        "description": "Fitness tracker, yurak urishi monitori, uyqu tahlili va 50+ sport rejimlari. Suvga chidamli 5ATM.",
        "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60",
        "price": "890,000"
    },
    {
        "id": 7,
        "slug": "veb-kamera",
        "name": "Full HD Veb Kamera",
        "description": "1080p sifatida video qo'ng'iroqlar uchun professional veb-kamera. Mikrofon va avtofokus bilan jihozlangan.",
        "image": "https://images.unsplash.com/photo-1588508065123-287b28e013da?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60",
        "price": "380,000"
    },
    {
        "id": 8,
        "slug": "usb-flash",
        "name": "128GB USB Flash",
        "description": "Tezkor USB 3.0 flesh xotira. Yuqori tezlikda ma'lumot o'tkazish. Metall korpusli va bardoshli dizayn.",
        "image": "https://images.unsplash.com/photo-1588423771073-b8903fbb85b5?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60",
        "price": "85,000"
    }
]


@app.route('/')
def home():
    """Bosh sahifa - barcha mahsulotlarni ko'rsatadi"""
    return render_template('index.html', products=products)


@app.route('/product/<slug>')
def product_detail(slug):
    """Mahsulot tafsilotlari sahifasi"""
    # Slug bo'yicha mahsulotni topish
    product = next((p for p in products if p['slug'] == slug), None)
    
    # Agar mahsulot topilmasa, 404 sahifasini ko'rsatish
    if product is None:
        abort(404)
    
    return render_template('product.html', product=product)


@app.errorhandler(404)
def page_not_found(e):
    """404 xatolik sahifasi"""
    return render_template('404.html'), 404


# Vercel uchun bu juda muhim
# Local ishga tushirish uchun: python main.py
if __name__ == '__main__':
    app.run(debug=True)