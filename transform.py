import os
import subprocess

# Set the path to the Microsoft Access database file
access_db = "./data/titanic_be.accdb"
# Get the directory where the Access database file is located
dir = os.path.dirname(access_db)


# Create the schema.sql file for our database
schema_file = open(os.path.join(dir, "schema.sql"), "a")

header_output = """CREATE DATABASE titanic_db;

USE titanic_db;

"""
schema_file.write(header_output)
print("schema.sql file created.")

# Export each table to a CSV file
tables = subprocess.check_output(["mdb-tables", "-1", access_db]).decode().strip().split("\n")
for i, table in enumerate(tables, start=1):
    table_file_path = os.path.join(dir, f"{i:02d}_{table}.csv")
    subprocess.run(["mdb-export", "-I", "sqlite", access_db, table], stdout=open(table_file_path, "w"))
    print(f"{i:02d}_{table}.csv file created successfully!")

# Gather a list of all our csv files
csv_files = [f for f in os.listdir(dir) if f.endswith(".csv")]

# Loop through each CSV file and write the schema to the schema.sql file
for csv in csv_files:
       # Number each file and delete the .csv suffix
       table_name = f"{csv[0:len(csv)-4]}"
       table_file_path = os.path.join(dir, f"{table_name}.sql")
       subprocess.run(["mdb-schema", access_db, "mysql"], stdout=open(table_file_path, "w"))
       print(f"{table_name}.sql file created successfully!")

# Close the schema.sql file
schema_file.close()

# Gather a list of all our sql files
sql_files = [f for f in os.listdir(dir) if f.endswith(".sql") and f[:1].isdigit()]

os.chdir('./data')

# Open the schema file in append
with open("schema.sql", "a") as schema:
    for sql_file, csv_file in zip(sql_files, csv_files):
        with open(sql_file) as f_sql:
            # Write the sql file lines to the schema
            for line in f_sql:
                schema.write(line)
        # Clean up
        print(f"Appended {sql_file} to schema file.")
        os.remove(sql_file)
        with open(csv_file) as f_csv:
            # Write the csv file lines to the schema
            for line in f_csv:
                schema.write(line)
        print(f"Appended {csv_file} to schema file.")
        # Clean up 
        os.remove(csv_file)
