import os
import yaml

from dotenv import load_dotenv

load_dotenv()

# Load the config file
with open('config/config.yaml', 'r') as f:
    global config
    config = yaml.safe_load(f)

# Replace the environment variables in the config file
config['database_uri'] = os.environ['DATABASE_URI']
config['http_user'] = os.environ['HTTP_USER']
config['http_password'] = os.environ['HTTP_PASSWORD']

# Save the updated config file
with open("config/config.yaml", "w") as f:
    yaml.safe_dump(config, f)
