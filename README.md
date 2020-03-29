# Website for Gateway Baptist Church
## Backend built using Django 


## Guide to set up the development environment on a Mac OS

### The first step is to build a virtual environment

1. Open a terminal
2. `sudo pip3 install virtualenv`
3. Navigate to the parent folder which contains this repository
4. Make a new directory in the parent folder (`mkdir <directoryName>`); for example, call it `new-gateway`
5. Change directories `cd` into the newly created directory (e.g. `new-gateway`)
6. Run the command `virtualenv newenv`
7. Activate the virtual environment with `source newenv/bin/activate`

### Now we need to install the dependencies required for the website to run correctly

8. Now the pip dependencies can be installed with `pip install -r requirements.txt`

9. At this point, switch back to the old directory (not `new-gateway)
10. Then you can run `python3 manage.py runserver`
11. Visit `localhost:8000` and the site will be active

*** If you want to exit the virtual environment, use the command `deactivate`
