Hantal Selenium ile Twitter APIsiz Kullanıcı Takibi
Bu proje, Twitter'da belirtilen arama terimlerini kullanarak kullanıcı adları toplamak ve bu kullanıcıları Telegram botuna göndermek için Hantal Selenium'u kullanır. Bu proje, Twitter API'sine ihtiyaç duymaz.

Gereksinimler
Python 3.x
Selenium
Telegram bot token
Kurulum
Bu depoyu klonlayın veya indirin.

Gerekli bağımlılıkları yüklemek için terminalde proje klasörüne gidin ve şu komutu çalıştırın:

pip install selenium python-telegram-bot
bot.py dosyasını bir düzenleyicide açın ve BOT_TOKEN değişkenini Telegram botunuzun token'iyle değiştirin.

Arama yapmak istediğiniz terimleri SEARCH_TERM değişkeninde belirtin.

Twitter'da kullanıcı adlarını toplamak için belirtilen terimleri kullanarak Selenium botunu çalıştırmak için şu komutu çalıştırın:

python bot.py
Toplanan kullanıcı adları, Telegram botunuza gönderilecektir.

Lisans
Bu proje, MIT lisansı altında lisanslanmıştır.