# Website for Gateway Baptist Church
## Backend built using Django on Python 3.8.2


## Guide to set up the development environment on a Mac OS

### The first step is to build a virtual environment

1. Open a terminal
2. `sudo pip3 install virtualenv`
3. Navigate to the folder which contains this repository
4. Change directories `cd` into the new directory (eg `website`)
5. Run the command `virtualenv newenv`
6. Activate the virtual environment with `source newenv/bin/activate`

### Now we need to install the dependencies required for the website to run correctly

7. Now the pip dependencies can be installed with `pip install -r requirements.txt`

8. At this point, `cd ..` back to the base level of the directory
9. Then you can run `python3 manage.py runserver`
10. Visit `localhost:8000` and the site will be active

*** If you want to exit the virtual environment, use the command `deactivate`
