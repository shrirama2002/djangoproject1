#python should be installed in your system
#if you have anaconda
    1) goto VS code app
    Open the the project folder 
    #select command prompt
    #to create anaconda environment follow below steps
    conda create --name environmentname
    conda activate environmentname
    ex: conda create --name env1
        conda activate env1

    #then install django inside the environment by using below command
        pip install django

    #after installation to run the django server use
        py manage.py runserver

    ###your django server is running now 
    ### follow the link which is generated in output or open it with browser


#if you dont have anaconda
    2) goto VS code app
    Open the the project folder 
    #select command prompt
    #to create python virtual environment follow below steps
        pip install virtualenv
        python -m venv <virtual-environment-name>
    ex: pip install virtualenv
        python -m venv myenv

    # to activate this environment use
        env/Scripts/activate.bat

    #then install django inside the environment by using below command
        pip install django

    #after installation to run the django server use
        py manage.py runserver

    ###your django server is running now 
    ### follow the link which is generated in output or open it with browser

