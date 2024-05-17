
# Django WebSocket Authentication

This project demonstrates how to implement WebSocket authentication in Django using Django Channels and Django Rest Framework with JWT.

## Overview

WebSocket authentication is crucial for real-time communication applications to ensure secure access to WebSocket connections. This project provides a comprehensive guide on setting up authentication for WebSocket connections in Django, including project setup, model creation, Django Channels configuration, custom middleware implementation for authentication, and testing to ensure functionality.

## Features

- Secure WebSocket authentication using Django Channels and Django Rest Framework with JWT.
- Project setup guide with step-by-step instructions.
- Model creation for handling user authentication and chat functionalities.
- Configuration of Django Channels for WebSocket communication.
- Implementation of custom middleware for WebSocket authentication.


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/JoseMiracle/AUTH_OVER_WEBSOCKET.git
   ```
2. Create and activate virtual environment
    ```
    virtual env

    env\Scripts\activate  : on Windows
    source env/bin/activate : on Linux/Mac
    ```


2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations:

   ```bash
   python manage.py migrate
   ```

4. Start the development server:

   ```bash
   python manage.py runserver
   ```

5. Access the application at `http://localhost:8000`.

## Usage

Follow the detailed instructions provided in the [documentation](docs/) to set up WebSocket authentication in your Django project.

## Contributing

Contributions are welcome! Please refer to the [contribution guidelines](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Django Channels](https://channels.readthedocs.io/en/latest/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [JWT Authentication](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)

---
