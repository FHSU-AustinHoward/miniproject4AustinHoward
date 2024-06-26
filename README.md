### Mini Project 4
### Austin Howard
### INF601 - Advanced Programming in Python

# Mini Project 4 - VLNRbull Reporting System

## Description
This project is an introduction into making webapps with Django and Bootstrap.  
  
I decided to make mine into a basic vulnerability system to warn users and administrators about known organizational 
vulnerabilities. This will allow users to create reports and administrators to edit them.

The site uses bootstrap for its base html file and uses a modal button to log out of the system (a project requirement).

## Getting Started
The running environment and all dependencies can be obtained through the command console in the Python IDE of your 
choosing.

### Step 1: Pip install requirements.txt
Before getting started, you will need to install this application's dependencies.  

In a terminal window, please type the following:
```
pip install -r requirements.txt
```

### Step 2: Create SQL entries needed for the database
The SQLite database is not yet in the project, you will need to generate a migration to tell Django which model
variables need to be added to the database.  

In a terminal window, please type the following:
```
python manage.py makemigrations reports
```

### Step 3: Apply the migrations to the SQL database
Now, you need to apply those migrations to the project.  

In a terminal window, please type the following:
```
python manage.py migrate 
```

### Step 4: Create a super user
Before you start using the program, you will need to generate a superuser account so that you can add users through the
admin interface.

In a terminal window, please type the following:
```
python manage.py createsuperuser 
```

### Step 5: Start the server
Now, you will need to start the development server that will be hosting this webapp.

In a terminal window, please type the following:
```
python manage.py runserver
```

### Step 6: Navigate to the site
You're ready to view the website. The console should have a link to the server but if not,
In your browser's URL bar, please type the following:
```
http://localhost:8000
```

## Authors
Austin Howard - [Email](A_Howard4@mail.fhsu.edu)  


## Version History

* 0.1
    * Initial release to complete the assignment

## License

This project is licensed under the GNU GPL-3.0 License - see the LICENSE file for details

## Acknowledgments
### Huge thanks to:
* [Jason Zeller](https://www.youtube.com/watch?v=DZWe-oU5Rfg&list=PLE5nOs3YmC2THmgcLi-ogD8KiIfCjS06V&pp=iAQB)
* [Django Tutorial](https://docs.djangoproject.com/en/5.0/intro/tutorial01/)
* [Bootstrap](https://getbootstrap.com/docs/4.0/components/modal/)
* [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website)
