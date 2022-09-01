from telegram.ext import *
from colorama import init, Fore
import time
from bs4 import BeautifulSoup
import undetected_chromedriver as uc

init()
red, blue, green = Fore.RED, Fore.BLUE, Fore.GREEN
token = "token"
channel_id = 999999999999
time_delay_hr = 2
updater = Updater(token=token)


def get_posts(url):
    options = uc.ChromeOptions()
    options.headless = True
    browser = uc.Chrome(options=options)
    browser.get(url)
    browser.save_screenshot("test.png")
    for i in range(10):
        time.sleep(10)
        soup = BeautifulSoup(browser.page_source, "html.parser")
        posts = soup.find_all("div", {'data-ad-preview': 'message'})
        print(len(posts))
        post_list = []
        if len(posts) > 0:
            for x in posts:
                temp = []
                temp.append(x.text)
                try:
                    temp.append(x.parent.parent.find("img", src=True)['src'])
                except:
                    pass
                post_list.append(temp)
            browser.quit()
            return post_list
        else:
            time.sleep(1)
            continue


def send_post(text, photo=None):
    updater.dispatcher.bot.send_message(chat_id=channel_id, text=text)
    if photo:
        updater.dispatcher.bot.send_photo(chat_id=channel_id, photo=photo)


def repeat_task():
    last_post = None
    while True:
        print(f"{green}[+]Started The Program with time delay {time_delay_hr} hrs")
        posts = get_posts("https://www.facebook.com/page_name")

        if last_post != posts[0]:
            print(f"{green}[+]New Post Found, Sending it")
            send_post(posts[0][0], posts[0][1])
            last_post = posts[0]
        else:
            print(f"{red}[-]No New Post Found")
        print(f"{blue}[+]Sleeping for {time_delay_hr} hrs")
        time.sleep(int(time_delay_hr * 3600))


if __name__ == "__main__":
    repeat_task()
