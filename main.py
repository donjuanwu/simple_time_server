"""
Developer: Don Dang
Assignment: 05 Simple Time Server
Date: 5/6/23
File name: main.py
Purpose:
- Implement a simple microservice and deploy it to Heroku
- The microservice will convert the current human-readable time into Epoch time

Resources:
1. Epoch & Unix Timestamp Conversion Tools
- https://www.epochconverter.com/

2. flask

3. Python's time.time()
- https://docs.python.org/3/library/time.html#time.time

4. Push an existing local project to Github
- https://docs.github.com/en/get-started/importing-your-projects-to-github/importing-source-code-to-github/adding-locally-hosted-code-to-github

5. Deploy to Heroku (from Terminal)
    1. Heroku login # proceed to login to Heroku use Duo 2FA
    2. Heroku create
    3. git checkout -b dev # if haven't already create a dev branch
    4. Create Procfile # either use git or add a new file using pycharm
        web: python main.py
    5. Git add, commit and push
    git add .
    git commit -m "Complete assignment 5 and push to Heroku"
    6. Push to heroku
    git push heroku dev:main
    7. Open microservice in heroku
    heroku open





"""

import os
import time
from flask import Flask

app = Flask(__name__)


@app.route('/')
def get_epoch_time():
    """
    convert human-readable time to epoch
    :return:
    """

    time_epoch = int(time.time()) # get epoch time
    return str(time_epoch)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6739))
    app.run('0.0.0.0', port=port)
