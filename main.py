import os
import time
from links import all_links
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urlparse

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.set_page_load_timeout(60)
driver.implicitly_wait(60)

# Функция, создающая директорию, если её нет
def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

for link_index, link in enumerate(all_links):
    success_flag = False

    for try_index in range(3):
        try:
            response = driver.get(link)
            success_flag = True
            break
        except Exception as e:
            print(f'[{link_index+1}] Parsing URL: {link}, Попытка {try_index+1}. Не удалось получить страницу: {e.msg}')
            time.sleep(3)
        else:
            break
    
    if not success_flag:
        continue

    # Получаем размер страницы
    width = 1440
    height = driver.execute_script("return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")
    driver.set_window_size(width, height)

    time.sleep(3)
    # Делаем скриншот
    page_body = driver.find_element(By.TAG_NAME, "body")

    # Разбираем URL для создания структуры директорий и имени скриншота
    parsed_url = urlparse(link)
    path_parts = parsed_url.path.strip('/').split('/')
    
    if 'chat/examples' in link:
        directory = 'examples'
    elif 'case' in link:
        directory = 'case'
    elif len(path_parts) == 1:
        directory = "general"
    else:
        directory = path_parts[0]
    
    # Создаем директорию если она не существует
    create_directory(directory)
    
    # Имя файла скриншота
    screenshot_name = "".join(path_parts) + ".png"
    screenshot_path = os.path.join(directory, screenshot_name)
    
    # Сохраняем скриншот
    try:
        page_body.screenshot(screenshot_path)
    except Exception as e:
        print(
            f'[{link_index+1}] ERROR: Timed out receiving message from renderer!\n'
            f' Parsing URL: {link}\n'
            f' Screenshot_path: {screenshot_path}\n\n'
        )
        continue    
    print(
            f'[{link_index+1}] OK!\n'
            f' Parsing URL: {link}\n'
            f' Screenshot_path: {screenshot_path}\n\n'
    )

driver.quit()