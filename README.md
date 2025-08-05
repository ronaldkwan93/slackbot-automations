# Slack Weather Bot

A simple Python bot that sends a daily weather update for any city to your Slack via direct message.  
Perfect for getting a quick weather summary to start your day

---

## Features

- Fetches current weather data for Sydney from OpenWeatherMap API
- Sends a Slack DM to your user with the weather update
- Can be scheduled to run daily (e.g., via GitHub Actions)

---

## Prerequisites

- Python 3.8+
- Slack Bot Token with `chat:write` permission
- OpenWeatherMap API key
- Your Slack User ID (to send yourself DMs)

---

## Setup

1. **Clone this repository**

   ```bash
   git clone https://github.com/yourusername/slack-weather-bot.git
   cd slack-weather-bot
   ```

2. **Environment setup**
   Create a `.env` file in the root directory with your secrets:

```ini
SLACK_TOKEN=
SLACK_USER_ID=
WEATHER_API_KEY=
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

```bash
python bot.py
```
