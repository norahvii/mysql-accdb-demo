We begin with a simple Microsoft Access database with a few queries and one form. Our form contains two buttons "male" and "female" that you can use to query the Titanic database.  

### Split the database:  

1. Click `Database Tools` tab.  
2. Click `Access Database` button to pull up the `Database Splitter`  
3. Click `Split Database` button to save the back end to the `data` folder. A `titanic_be.accdb` file should be created.  

### Convert the database:

Next we will need mbtools (I use Ubuntu Linux WSL2):

1. `sudo apt update`  
2. `sudo apt install mdbtools`  

See your table(s) with the following command:  

3. `mdb-tables ./data/titanic_be.accdb`  

Create your `csv` and `sql` table files and `sql` schema file using Python:

4. `python3 transform.py`

### Docker:

1. `docker-compose build`  
2. `docker-compose up -d`  
3. `docker-compose exec db mysql -u root -ppassword123`  
