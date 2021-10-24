# Flask - api template

Template to start building quickly a API using Python and Flask framework. 


## Install

To install the app you must follow the next steps:
* Prepare Python dependencies
* Config environment varibles
* Install the database
* Run the server

First of all, you must define an environment variable with the run.py file path, located at the repository root.
With the next command you can achieve that
 ```
$ export FLASK_APP=manage.py
```

### Python dependencies
Python dependencies can be configured in setup.py file. In this case you can build the python module using the next command:
```{bash}
$ pip install .
```

Alternatively, the python dependencies can be found in the requirements.txt file. You can install all those dependencies with the next command. 
```
$ pip install -r requirements.txt
```

**Note:** If your are not using docker we recommend to install it in a python local environment.

### Configutation parameters
Create .env file at root project directory with the definition of the next properties, those atributtes are used as
OS environment variables:
```
APP_PREFIX_DEBUG=True
APP_PREFIX_SECRET_KEY='fhshark@n*$ixdz_p)m8h-kzf#cte(+dx#h%grdjz-j0473c_u'

APP_PREFIX_DATABASE_URI='mysql://hydros:hydros@localhost/hydros?unix_socket=/opt/lampp/var/mysql/mysql.sock'
APP_PREFIX_DATABASE_TRACK_MODIFICATIONS=False

APP_PREFIX_AEMET_API_KEY='your-aemet-api-key'
```
Then, if you have changed the app prefix or added new config properties, 
you must modify the settings.py file to read the new properties or read the new names.
  

### Instalar base de dades

Once you have the database created and the config properties properly configured, the execution of the next command 
create all the app database tables.
```
$ python -m flask install
```

### Server 
Now, the app is ready. The last step is to mount it onto server.

#### Docker
You can use this app template to create a micro-service with an API.
In this case you should configure it in your docker-compose file or equivalent.


#### Development server
To run a development server you can simply run the next command:
```
$ python -m flask run
```

## Commands
### Install
Command to install the tables database. 
```
$ python -m flask install
```