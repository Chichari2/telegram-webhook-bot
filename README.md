# Telegram Bot Project

This project is a Telegram bot that interacts with users via messages, webhooks, and other services. It is built using Python, and utilizes Docker for containerization.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Running the Project](#running-the-project)
- [Configuration](#configuration)
- [License](#license)

## Features
- Telegram bot integration.
- Asynchronous communication using Uvicorn and Gunicorn.
- PostgreSQL for database storage.
- Nginx for reverse proxy and security.

## Requirements
- Docker (for containerization)
- Python 3.9+
- PostgreSQL (for data storage)
- Ngrok (for creating a secure tunnel for testing the webhook)
- Google Sheets API (for integrating with Google Sheets)

## Setup Instructions

### Step 1: Clone the repository
Clone the repository to your local machine:

    ```bash
    git clone <repository-url>
    cd telegram-bot


### Step 2: Create a virtual environment
Create a virtual environment and install dependencies:
    
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On macOS/Linux
    # .venv\Scripts\activate  # On Windows
    pip install -r requirements.txt

### Step 3: Set up environment variables
Create a .env file in the root directory of the project and include the following environment variables:

    ```bash
    TELEGRAM_BOT_TOKEN=<your-bot-token>
    TELEGRAM_WEBHOOK_URL=<your-ngrok-or-production-webhook-url>
    POSTGRES_DSN=<your-postgres-connection-string>
    GOOGLE_SHEETS_CREDENTIALS=<your-google-sheets-credentials-json>
    GOOGLE_SHEET_ID=<your-google-sheet-id>

### Step 4: Configure Docker
Ensure Docker is installed and running on your machine. You can build the Docker containers by running the following command:

    ```bash
    docker-compose up --build
This will start up the containers for the app, PostgreSQL, and Nginx.

### Running the Project
Once the containers are running, the bot will start handling requests. Make sure that:

* Nginx is serving the web application.

* The bot listens for incoming updates via webhook.

* The PostgreSQL database is set up and connected correctly.

You can check if everything is running properly by visiting the application URL in your browser or checking logs for the containers.

### Step 1: Set the webhook
You can set up the webhook for your bot using the following API request:

    ```bash
    curl -F "url=https://<your-webhook-url>" https://api.telegram.org/bot<your-bot-token>/setWebhook

### Step 2: Test the bot
Once the webhook is set, you can interact with the bot on Telegram. The bot should now process incoming messages and respond accordingly.

# Configuration
### Docker Compose Configuration
This project uses Docker Compose for container management. The docker-compose.yml file contains the definitions for:

* app: The Python application for the bot.

* postgres: The PostgreSQL database used to store data.

* nginx: Nginx reverse proxy for handling HTTP and HTTPS traffic.

The configuration sets up networking between the containers, mounts necessary volumes, and exposes ports for accessing the services.

## License
This project is licensed under the MIT License - see the LICENSE file for details.