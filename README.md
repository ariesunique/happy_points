# HAPPY POINTS

The initial aim of this project was to implement a rewards system for my daughter. Good behavior earns a happy face; bad behavior earns a sad face. The total number of points earned on a given day is the difference between happy faces and sad faces. Points are accumulated per week, and can be redeemed throughout the week for various prizes (ie, good behavior earns rewards).

The front-end is written in React (javascript) and the backend is written as a Flask (python) RESTful API.

![alt text](https://github.com/ariesunique/happy_points/blob/master/docs/images/happy-points-with-data-820x461.png "Happy Points Application")


- [Installation](#installation)
  * [Prerequisites](#prerequisites)
  * [Install Happy Points](#install-happy-points)
  * [Managing settings](#managing-settings)
- [Run the Application](#run-the-application)
- [Testing](#testing)

## Installation

Make sure you have python (and pip) installed on your system. Make sure you have node (and npm) installed on your system. Make sure you have some type of database system on your site (the default setup uses sqlite for local development.) The installation instructions below assume code is running on a Linux (Ubuntu) machine.

### Prerequisites

**To install python**
Python typically comes installed on Ubuntu by default. If you need to install a later version, [click here](https://linuxize.com/post/how-to-install-python-3-8-on-ubuntu-18-04/).

**To install node:**
Follow the below instructions to install node on Ubuntu 18.04 ([click here](https://linuxize.com/post/how-to-install-node-js-on-ubuntu-18.04/) for more details)
```
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt update
sudo apt install nodejs
```

To verify node installation:
```
node --version
npm --version
```

**To install sqlite**
Read more [here](https://linuxhint.com/install_sqlite_browser_ubuntu_1804/)
```
sudo apt update
sudo apt install sqlite3
```

### Install Happy Points
1. Clone this repository.
2. Create a virtual environment.
3. Install the dependencies.
    * Install the frontend dependencies using node package manager
      ```
      cd {happy-points-install-dir}/frontend
      npm install
      ```
 
    * Install the backend dependencies using pip

      ```
      cd {happy-points-install-dir}/backend
      pip install -r requirements.txt
      ```

    * **Top-level dependencies for the backend server**
      * flask
      * flask-sqlalchemy -- this is the ORM
      * flask-migrate -- manage migrations and schema changes
      * Environs -- manage environment variables
      * moment -- nice library for handling dates
      * pytest -- testing framework
      * WebTest -- helps with testing apis
      * factory_boy -- helps create mock objects for testing

4. Set up the database 
   This script will create the main table needed for the application. If you want to populate the table with test data, open testdb.sql and uncomment the sql statements.
   ```
   cd {happy-points-install-dir}/backend/happy_points
   cat testdb.sql | sqlite3 happy.db
   ```

### Managing settings
The .env file included is meant for dev purposes only, and should not be used on a production server. The settings specifed in this file will be read in settings.py and passed to the flask application. If an app is not specified in the .env file, the appropriate default will be used the settings.py. You should not need to modify this file to get started -- the defaults will work fine for local development.

| var | description |
| -- | -- |
|FLASK_APP| (required) Specifies the file running the flask server|
|FLASK_ENV| (required; default=production) Specifies the environment (development or production)|
|DATABASE_URL| (optional; default=sqlite db named happy.db in your current working dir) By default, this app will use a sqlite db when running locally. You can install postgres or another db compatible with SQLAlchemy |
|DATE_FORMAT| (optional; default="ddd, MM-DD-YYYY") Specifies the date format used to display the dates in the API and on the front-end






## Run the Application

To run the application, start the front-end client and the backend REST server. (I'm not using webpack or a similar tool, for now, I'm just starting each piece manually in two separate terminals.)

**To start the frontend**
```
cd {happy-points-install-dir}/frontend
npm start
```

**To start the backend**
```
cd {happy-points-install-dir}/backend
./run.sh
```

The run script is provided for convenience. It starts the flask server on port 5000 because your front end application will be running on port 3000 (the default port used by node).

Navigate to your localhost and view the app. It should look like below:

![alt text](https://github.com/ariesunique/happy_points/blob/master/docs/images/happy-points-initial-screenshot.png "Happy Points Application")



## Testing

This project provides several unit tests. 

To run the test cases:
```
cd {happy-points-install-dir}/backend/tests
pytest
```

The tests are also categorized according to functionality - whether they tests the api or whether they test a database operation. To run the api tests, run:
```
pytest -m api
```

To run the database tests, run:
```
pytest -m db
````

You can add additional categories of tests by modifying the pytest.ini file, which is also in that same tests dir. Just add another category name and description under "marks". To specify a test as part of that category, modify test_app.py. Add the annotation @pytest.mark.{category} above the desired method.    


