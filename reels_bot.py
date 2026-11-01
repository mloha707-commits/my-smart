name: Automatic Reels Generator Bot

on:
  workflow_dispatch:
  schedule:
    - cron: '0 8 * * *' # يعمل تلقائياً كل يوم صباحاً

jobs:
  build-and-run:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install System Dependencies for Video
        run: |
          sudo apt-get update
          sudo apt-get install -y ffmpeg

      - name: Install Python Libraries
        run: |
          pip install --upgrade pip
          pip install moviepy edge-tts feedparser requests pillow

      - name: Run Reels Generator Bot
        env:
          TELEGRAM_BOT_TOKEN: ${{ secrets.TELEGRAM_BOT_TOKEN }}
          TELEGRAM_CHAT_ID: ${{ secrets.TELEGRAM_CHAT_ID }}
        run: |
          python reels_bot.py

      - name: Upload Generated Video Artifact
        uses: actions/upload-artifact@v4
        with:
          name: exclusive-reel-video
          path: exclusive_reel.mp4