# Towers of Cards
An experimental game, a synergy of tower defense and TCG type of games. No resources, limited time, persistent massacre, 
overdose of adrenaline.

# Requirements (not in requirements.txt)
* localsettings.py - we use a (well known) hack to use personalized settings additions for the core. Just copy localsettings.py.template to localsettings.py and change the settings to suit your environment.
* mongodb

# Data
There are fixtures, just a bit different. Since the project is using mongodb and relies on mongoengine (DjangoORM) only 
for auth, you need to import the data manually. To do this you run the script with __python manage.py importdata__.

# Sockets/Torando
Will be there, and will be run with __python towersofcards/sockets.py__.
By default Tornado will be waiting on port 8888, but you can change that in localsettings.py.

# Deploying
To set-up the code for deployment, just run __python manage.py constructcmscss__ and __python manage.py preparedeploy__. 
The first command will scrape the database and construct the appropriate lines in the css files. The second will update 
the values in certain files with timestamps from the script runtime so that the static content gets served fresh to the end users.
