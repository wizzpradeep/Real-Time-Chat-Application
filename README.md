# Real-Time Chat Application

This is a real-time chat application built using Python, Django, WebSockets, and Django Channels. The app allows users to create an account, log in, and chat with other users in real time by joining different chat rooms.

## Features

- User authentication (login and registration).
- Real-time messaging using WebSockets.
- Chat rooms where users can join and chat with others.
- Notifications for new messages in the room.

## Technologies Used

- **Python**: Backend logic.
- **Django**: Web framework.
- **Django Channels**: WebSockets for real-time communication.
- **Redis**: Used as a channel layer to support WebSocket connections (optional, depending on your setup).
- **HTML/CSS/JavaScript**: Frontend for the chat interface.

## Installation

### Prerequisites

- Python 3.6 or higher
- Django 3.x or higher
- Redis (optional, but recommended for production setup)

### Clone the repository

```bash
git clone https://github.com/wizzpradeep/Real-Time-Chat-Application
cd Real-Time-Chat-Application
```

### Set up a virtual environment

It's recommended to use a virtual environment to manage project dependencies.

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Apply database migrations

```bash

python manage.py migrate
```

### Start the Django development server to test the app locally:

```bash
python manage.py runserver
```

The application will be accessible at http://127.0.0.1:8000/

# How to Use

- Register an Account: Create a new account by visiting the registration page and providing a username, email, and password.
- Log in: After registration, log in with your credentials.
- Join a Chat Room: After logging in, you can join existing chat rooms or create a new room.
- Send Messages: Once in a room, you can send real-time messages to all members of that room.
- Leave Room: You can leave the room at any time and join a new one.

# Features in Progress

- Private messaging.
- Chat history storage (currently only real-time messages are available).
- Improved UI/UX.
