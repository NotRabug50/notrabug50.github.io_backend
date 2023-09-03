# gunicorn_config.py

bind = "127.0.0.1:8000"  # Change this to your desired host and port
workers = 4  # Adjust the number of workers as needed
timeout = 60  # Set a reasonable timeout value
loglevel = "info"  # Adjust the log level as needed
