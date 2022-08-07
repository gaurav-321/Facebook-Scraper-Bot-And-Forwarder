import time
from bs4 import BeautifulSoup
import undetected_chromedriver as uc


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


if __name__ == "__main__":
    get_posts("https://www.facebook.com/Rblcoin")
