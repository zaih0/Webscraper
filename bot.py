from newspaper import Article
from newspaper import Config
import nltk
import selenium
from selenium import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import NoSuchElementException, ElementNotInteractableException
import tkinter as tk 




#DRIVER_PATH = "C:\\Users\\Zaine Horn\\Documents\\chrome\\chromedriver-win64\\chromedriver.exe"


#options = Options()
#options.headless = True
#options.add_argument("--window-size=1920,1200")
#driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
#driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

#url = requests.get("https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen")
#soup = BeautifulSoup(url.content, 'html.parser')
#TOP_ARTICLE_ELEMENT= soup.find('a', class_='WwrzSb')
#TOP_ARTICLE_URL = soup.a
#URL = TOP_ARTICLE_URL.get('href')



#setup for selenium bot to interact with the google news website

#options = Options()
#options.headless = True
#options.add_argument("--window-size=1920,1200")
#driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
#wait = WebDriverWait(driver, timeout=9)
#wait.until(lambda d : URL)


#This function scrapes the news from the google news website
def news_scraper(): 
    nltk.download('punkt')
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    config = Config()
    config.browser_user_agent = user_agent
    my_article = Article("https://www.macrumors.com/2023/10/25/next-gen-imac-details-rumored-ahead-of-event/")
    my_article.download()
    my_article.parse()
    title = my_article.title
    author = my_article.authors
    pub_date = my_article.publish_date
    my_article.nlp()
    summary = my_article.summary
    return title,author,summary
title,author,summary = news_scraper()

#This function allows for the close button to work
def CLOSE(event):
    quit()

#GUI USING TKINTER
window = tk.Tk()
window.geometry("7000x700")
window.title("News:")
ARTICLE_TITLE = tk.StringVar(window, title )
WRITER = tk.StringVar(window, author)
ARTICLE_SUMMARY = tk.StringVar(window, summary)
label1 = tk.Label(text="Get the latest news", font=("Times new roman",20), fg="white", bg="#5A5A5A")
label2 = tk.Label(text="Title : ")
label3 = tk.Label(text="Author : ")
label4 = tk.Label(text ="Summary : ")
label1.grid(column=0, row=0)
label2.grid(column=0,row=1)
label3.grid(column=0,row=3)
label4.grid(column=0, row=4)

#Displays data that has been retrieved onto to the screen
def ON_SCREEN_TEXT():
    TITLE_LABLE = tk.Label(textvariable=ARTICLE_TITLE)
    AUTHOR_LABEL = tk.Label(textvariable=WRITER)
    SUMMARY_LABEL = tk.Label(textvariable=ARTICLE_SUMMARY)
    TITLE_LABLE.grid(column=1,row=1)
    AUTHOR_LABEL.grid(column=1,row=3)
    SUMMARY_LABEL.grid(column=1,row=5)




global GENERATE_BTN
GENERATE_BTN = tk.Button(window, text="Get News",command=ON_SCREEN_TEXT, fg="white", bg="#00b89f")

GENERATE_BTN.grid(column=2,row=1)
CLOSE_BTN = tk.Button(window, text="Close",fg="white", bg="Red")
CLOSE_BTN.grid(column=3, row=1)
CLOSE_BTN.bind("<Button-1>", CLOSE)
GENERATE_BTN.bind("<Button-2>", ON_SCREEN_TEXT)

window.mainloop()






#window.after(3000, news_scraper)



















