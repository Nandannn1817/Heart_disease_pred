import sys
import os

# Add your project directory to the sys.path
path = '/home/yourusername/Heart_disease_prediction'
if path not in sys.path:
    sys.path.append(path)

# Set the environment variable for Flask
os.environ['FLASK_APP'] = 'app.py'

# Import your Flask app
from app import app as application 