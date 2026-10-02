from flask import Flask,render_template
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/informations")
def information():
    informations = ["2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.", "Akıllı telefon kullanımı, özellikle genç nesil için günlük hayatta önemli bir rol oynamaktadır.", "Akıllı telefonlar, sosyal medya, oyunlar ve diğer uygulamalar aracılığıyla sürekli olarak dikkat çekici içerikler sunarak kullanıcıların bağımlılık geliştirmesine neden olabilir.", "Akıllı telefon bağımlılığı, uyku düzenini bozabilir, sosyal ilişkileri olumsuz etkileyebilir ve zihinsel sağlık sorunlarına yol açabilir.", "Bağımlılıkla mücadele etmek için kullanıcıların ekran süresini sınırlamaları, bildirimleri kapatmaları ve dijital detoks yapmaları önerilmektedir."]
    return '<p>' + random.choice(informations) + '</p>'

@app.route("/emoji")
def emoji_olusturucu():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emoji)

app.run(debug=True)