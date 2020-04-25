# HAPPY POINTS

The initial aim of this project was to implement a rewards system for my daughter. Good behavior earns a happy face; bad behavior earns a sad face. The total number of points earned on a given day is the difference between happy faces and sad faces. Points are accumulated per week, and can be redeemed throughout the week for various prizes (ie, good behavior earns rewards).

The front-end is written in React (javascript) and the backend is written as a Flask (python) RESTful API.

## Installation

Make sure you have python (and pip) installed on your system. Make sure you have node (and npm) installed on your system.

### Prerequisites

**To install python**
Python typically comes installed on Ubuntu by default. If you need to install a later version, [click here](https://linuxize.com/post/how-to-install-python-3-8-on-ubuntu-18-04/).

**To install node:**
Follow the below instructions to install node on Ubuntu 18.04 ([click here](https://linuxize.com/post/how-to-install-node-js-on-ubuntu-18.04/) for more details)
```
sudo apt update
sudo apt install nodejs
```

To verify node installation:
```
nodejs --version
```

### Setting up Happy Points
1. Clone this repository.
2. Create a virtual environment.
3. Install the dependencies.
    * Install the frontend dependencies using node package manager
      ```
      cd frontend
      npm install
      ```
 
    * Install the backend dependencies using pip

      ```
      cd backend
      pip install -r requirements.txt
      ```

**Top-level dependencies**
* flask
* flask-sqlalchemy
* flask-migrate
* moment
* pytest
* WebTest
* factory_boy

Flask-SQLAlchemy is the ORM.
Flask-Migrate will manage migrations and schema changes.
Moment is a nice library for handling dates.
Pytest, WebTest, and FactoryBoy are already packages used for testing.

## Run the Application

To run the application, start the front-end client and the backend REST server. (I'm not using webpack or a similar tool, for now, I'm just starting each piece manually in two separate terminals.)

**To start the frontend**
```
cd frontend
npm start
```

**To start the backend**
```
cd backend
./run.sh
```

Navigate to your localhost and view the app.

## Testing



