#!/bin/bash
cd "$(dirname "$0")"
source .env
export TG_BOT_TOKEN TG_CHANNEL_ID MAX_BOT_TOKEN MAX_CHANNEL_ID
python3 bot.py
