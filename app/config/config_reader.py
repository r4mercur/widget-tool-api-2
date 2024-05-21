import os
import yaml

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
load_dotenv(dotenv_path=dotenv_path)

# Load the config file and store it in a global variable
with open('config/config.yaml', 'r') as f:
    global config
    config = yaml.safe_load(f)

# Replace the environment variables in the config file
config['database_uri'] = os.environ['DATABASE_URI']
config['general_sharing_settings']['http_user'] = os.environ['HTTP_USER']
config['general_sharing_settings']['http_password'] = os.environ['HTTP_PASSWORD']

# Save the updated config file
with open("config/config.yaml", "w") as f:
    yaml.safe_dump(config, f)
