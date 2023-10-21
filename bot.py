from newspaper import Article
from newspaper import Config
import nltk
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DRIVER_PATH = "C://Users//Zaine Horn//Documents//chrome//chrome-win64"
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
url = driver.get("https://news.google.com/home?hl=en-US&gl=US&ceid=US:en")



def news_scraper(): 
    url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen"
    nltk.download('punkt')
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    config = Config()
    config.browser_user_agent = user_agent
    my_article = Article(url)
    my_article.download()
    my_article.parse()

    title = my_article.title
    author = my_article.authors
    pub_date = my_article.publish_date
    my_article.nlp()
    summary = my_article.summary
    return title, author, summary
title, author, summary = news_scraper()
news_scraper()

with open('news.txt', 'w') as file:
    writer = file.write(f"Title: {title}")
    file.writelines([f"Title: {title} \n", f"Author: {author} \n", f"Summary: {summary} \n"])
