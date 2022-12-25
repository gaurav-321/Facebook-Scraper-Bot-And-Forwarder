# Facebook Scraper Bot
This is a bot that scraps posts from a specific Facebook page and sends them to a designated Telegram channel at regular intervals. It uses the telegram, colorama, time, bs4, and undetected_chromedriver libraries.

# How it works
The bot uses the undetected_chromedriver library to open a headless Chrome browser and navigate to the Facebook page specified in the get_posts function. It then uses BeautifulSoup to parse the page source and find all posts with the data-ad-preview attribute set to message. It then sends these posts to the Telegram channel specified in the channel_id variable using the telegram library. The bot will repeat this process at regular intervals specified by the time_delay_hr variable.

# Running the Bot
To run the bot, simply execute the main.py script. You will need to have the telegram and undetected_chromedriver libraries installed, as well as a valid Telegram bot token. You will also need to specify the Facebook page URL and the Telegram channel ID in the appropriate variables in the code.
