import multiprocessing
import os

bind = "0.0.0.0:8000"  # IP address and port number to bind
workers = multiprocessing.cpu_count() * 2 + 1  # Number of worker processes
worker_class = "uvicorn.workers.UvicornWorker"  # Worker class for UVicorn
timeout = 120  # Timeout for worker connections

# Logging configuration
current_dir = os.path.dirname(os.path.abspath(__file__))
accesslog = os.path.join(current_dir, 'logs/access.log')  # Path to the access log file
errorlog = os.path.join(current_dir, 'logs/error.log')  # Path to the error log file
loglevel = "info"  # Log level (info, debug, warning, error, critical)
