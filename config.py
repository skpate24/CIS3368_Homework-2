from app import app
from flaskext.mysql import MySQL
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Welcome3'
app.config['MYSQL_DATABASE_DB'] = 'CIS3368db'
app.config['MYSQL_DATABASE_HOST'] = 'cis3368-spring23.civhut35a9ka.us-east-1.rds.amazonaws.com'
mysql.init_app(app)