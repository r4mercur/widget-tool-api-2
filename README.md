# widget-tool-api-2

This is a simple API that allows you to create, read, update, and delete widgets. 
It is built using Flask and MySQL.

# Installation

1. Clone the repository
2. Install the required packages using `pip install -r requirements.txt`
3. Create a MySQL database and update the `config.py` file with your database credentials
4. Run the application using `python app.py`

## Docker Installation

1. Clone the repository
2. Update the .env file with your database credentials & configuration
3. Use docker-compose to build and run the application using `docker-compose up --build`
4. The application will be running on `http://localhost:8000`