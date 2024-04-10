> -------------  Windows -------------
> 
> Running the server:
> 
> set FLASK_ENV=development
> 
> set FLASK_APP=application_name.py
> 
> flask run

> -------------  Mac -------------
> 
> export FLASK_ENV=development 
> 
> export FLASK_APP=application_name.py 
> flask run

> ------------- Server Error -------------
> 
> chrome://net-internals/#sockets

> -------- After creating the model database ------- 
> 
> Run in the terminal ( in mac run python3, in windows run 'py')
> 
> from app_name import db, app 
> 
> app.app_context().push() 
> 
> db.create_all()

> you can see the database created inside the folder instances run the terminal again
>
> ------------- Use mysql instead of sqlite ----------- 
> 
> pip3 install mysql-connector 
>
> pip3 install mysql-connector-python

> Create a python file create_db_file.py 
> 
> ------------- Migrations ----------- 
> 
> In case you want to add few columns to the database
>
> pip3 install Flask-Migrate 
> 
> from flask_migrate import Migrate 
> 
> -------> Under this line: db = SQLAlchemy(app) 
> 
> Put this:
> 
> db = SQLAlchemy(app) 
> 
> migrate = Migrate(app, db) 
> 
> In the terminal type: 
> flask db init 
> 
> flask db migrate -m 'initial migration' 
> 
> flask db upgrade

>> NOTE: in case you have a prblm like this:
> ERROR [flask_migrate] Error: Can't locate revision identified by 'ee6db864e433'
> 
> Run this:  
> flask db revision --rev-id ee6db864e433

Run server and check

NOTE: Any time you want to make migrations just type: 

->>>>> flask db migrate -m "added something" 

->>>>> flask db upgrade

-------- NOTES ----------

In case that you faced an error like this: 

sqlalchemy.exc.NoReferencedTableError: 
Foreign key associated with column 'post_model.poster_id' 
could not find table 'usersmodel' 
with which to generate a foreign key to target column 'id'


> In my case i have a UsersModel as a model for my database, 
> in relashionship the model will be like this:
> 
> new_field = db.Column(db.Integer,db.ForeignKey('users_model.id')) 
> 
> So, Why users_model? the reason is because the data is 
> the tabel is containing two words: Users and Model, 
> in every word is uppercased, so, in the database, 
> the table should be called like this:
> 
> db.ForeignKey('users_model.id')
> 
> .