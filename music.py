from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def extract_music_js(url):
   
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(15) 

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    songs = soup.find('div', class_='song_list') 
    list = songs.find('ul', class_='list_content')
    list_items = list.find_all('li', class_='clearfix')
    for song in list_items:
        print(f'Title: {song.text.strip()}')
    driver.quit()

url = 'https://www.kugou.com/yy/html/search.html#searchType=song&searchKeyWord=alan%C2%A0walker'
extract_music_js(url)
