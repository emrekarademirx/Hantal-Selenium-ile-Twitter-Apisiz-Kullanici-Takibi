from selenium import webdriver
import time
import telegram

# Telegram botunu başlatmak için token bilgileri girin
bot_token = 'YOUR_BOT_TOKEN'
bot_chatID = 'YOUR_CHAT_ID'
bot = telegram.Bot(token=bot_token)

# Twitter'da arama yapmak için gereken URL'yi oluşturun
search_term = 'QUERY_TERM' # Bu yerine arama terimini yazın
url = 'https://twitter.com/search?q=' + search_term + '&src=typd'

# Firefox WebDriver'ını başlatın ve Twitter arama sayfasına gidin
driver = webdriver.Firefox()
driver.get(url)

# Sayfayı yüklemek için biraz bekleyin
time.sleep(5)

# Twitter'da kullanıcı adlarını toplamak için XPath kullanın
usernames = driver.find_elements_by_xpath('//div[@class="content"]/div[@class="stream-item-header"]/a[@class="account-group js-account-group js-action-profile js-user-profile-link js-nav"]')

# Toplanan kullanıcı adlarını Telegram botuna gönderin
for username in usernames:
    bot.send_message(chat_id=bot_chatID, text=username.get_attribute('href'))

# WebDriver'ı kapatın
driver.quit()
