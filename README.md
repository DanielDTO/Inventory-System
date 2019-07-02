# Inventory-System

The System is designed to store items. Major python scripts are: forms, models, urls(App), views and all HTML files in the template folder.

WINDOWS INSTALLATION
---------------------
The software was developed using python3, sqlite3 and Django. It is essential to have python3 installed on Windows and have it added to Windows Path. Once that is done, the other packages can easily be installed using python with the help of windows command prompt.

RUNNING APPLICATION
--------------------
To run the application, use the command in command prompt :
        python mange.py runserver
Once that is run, a link will be shown in the terminal window. CLICK the link to use the interface for the system.

The system also supports the import of data files (CSV and others.) but only works when logged in as an admin. To login as an admin, add "/admin" to the link provided when running the server.
Administrator credential are as follows:
        
        Username:       Admin
        Password:       administrator1234
        
You can also perform tasks as an admin.

PRECAUTION
-----------------
In case there is an error when trying to run the server, delete the 'dbsqlite3' and '0001_initial file' found in the migrations folder then  try the following commands before running the "runserver" command again:
        1) python manage.py makemigrations
        2) python manage.py migrate.

This is just to reset the database and should only be done when there is a problem running the server.
