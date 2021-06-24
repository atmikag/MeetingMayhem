"""
File: run.py
Author: Robert Shovan /Voitheia
Date Created: 6/15/2021
Last Modified: 6/24/2021
E-mail: rshovan1@umbc.edu
Description: python file responsible for running the Meeting Mayhem website/package

Initially, this project was largley based on the tutorial video series:
https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH
"""

#import the app from the package so that we can run it here
from Meeting_Mayhem import app

"""
Runs the app. For now, the app is run in debug mode for ease of development. This allows us to see changes we make to
the website without restarting the server. This will need to change in the future
"""
if __name__ == '__main__':
    app.run(debug=True)