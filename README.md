# Facebook Scraper Bot And Forwarder 📈🤖

## Description
Facebook Scraper Bot And Forwarder is a Python program designed to automate the process of scraping posts from a specified Facebook page and forwarding them to a designated Telegram channel at regular intervals. This tool is particularly useful for content aggregation, social media monitoring, or simply keeping up with updates from friends and pages you care about.

## Features
- **Scraping Posts**: Automatically scrape new posts from a Facebook page.
- **Real-time Forwarding**: Send scraped posts to a Telegram channel in real-time.
- **Regular Intervals**: Schedule the scraping and forwarding process at specified intervals.
- **Colorful Output**: Use `colorama` for colorful terminal output.

## Installation
To install the dependencies, run:
```bash
pip install -r requirements.txt
```

## Usage
Here's a basic example of how to use the program:

1. **Configure Facebook and Telegram Credentials**:
   - Set up your Facebook page URL.
   - Get your Telegram bot token and chat ID.

2. **Run the Script**:
   ```bash
   python tele_bot.py --url <FACEBOOK_PAGE_URL> --token <TELEGRAM_BOT_TOKEN> --chat_id <TELEGRAM_CHAT_ID>
   ```

## Configuration
### Environment Variables
- `FB_PAGE_URL`: URL of the Facebook page to scrape.
- `TELEGRAM_BOT_TOKEN`: Token for your Telegram bot.
- `TELEGRAM_CHAT_ID`: ID of the Telegram chat where messages will be sent.

### Command-line Arguments
You can also pass these configurations via command-line arguments as shown in the usage example above.

## Tests
Tests are not available at this time. However, you can manually test the script by running it with different parameters and checking if it works as expected.

## Project Structure
```
Facebook-Scraper-Bot-And-Forwarder/
├── README.md
├── requirements.txt
└── tele_bot.py
```

## Contributing
Contributions are welcome! Please follow these guidelines:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Make your changes and commit them (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to reach out if you have any questions or need further assistance! 🚀