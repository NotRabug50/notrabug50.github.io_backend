import multiprocessing

# Bind to 0.0.0.0:8000, replace with your desired host and port
bind = "0.0.0.0:8000"

# Number of worker processes (adjust based on your server's CPU cores)
workers = multiprocessing.cpu_count() * 2 + 1

# Worker class for handling requests
worker_class = "gthread"

# Enable threading
threads = 2

# Timeout for handling requests (adjust as needed)
timeout = 60

# Log file location (change to your desired log file path)
accesslog = "/path/to/access.log"
errorlog = "/path/to/error.log"

# Set the application module (replace 'main' with your actual app module)
# This should point to the Flask app in your project
# Example: 'myapp:app' where 'myapp' is the module and 'app' is the Flask app instance
# app = "main:app"

# Environment variable for MongoDB URL (replace with your actual variable name)
# env = "MONGODB_SERVER_URL=mongodb://your-mongodb-uri"

# Use the below environment variable if you're setting app-specific configurations
# For example, you could use this to specify a production configuration file
# env = "FLASK_ENV=production"

# Additional environment variables can be set here if needed
# env = "KEY=VALUE"

# Preload the application for improved performance (recommended for production)
preload_app = True
