"# PROYECTO-TFG" 

Para ejecutar el proyecto por primera vez, se deben seguir las siguientes instrucciones:

    - Ejecutamos los siguientes comandos: 
        
        docker compose up --build -d
        docker compose exec -ti -u root web bash
        python manage.py makemigrations
        python manage.py migrate
        python manage.py create_data