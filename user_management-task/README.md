 

#### HOW TO SETUP ON LOCAL Development:

you need to install python =>3.10

#### create new env:

```shell
         # Create the project directory
        mkdir venv
        cd venv
        
        # Create a virtual environment to isolate our package dependencies locally
        python3 -m venv venv
        source env/bin/activate  # On Windows use `env\Scripts\activate`
        
        # Install requirements into the virtual environment
        pip install -r requirements.txt
        python3 manage.py makemigrations
        python3 manage.py migrate
        
        
```
 