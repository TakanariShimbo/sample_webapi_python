# About
This is sample webapi written in python (flask).

# pythonanywhere: https://www.pythonanywhere.com/
1. clone repo at consoles
    ```commandline
    git clone https://github.com/TakanariShimbo/sample_webapi_python.git
    cd sample_webapi_python
    ```
   
2. make virtualenv at consoles
    ```commandline
    mkvirtualenv python3.9_flask_env --python=/usr/bin/python3.9
    deactivate
    ```
   
3. install requirements at consoles
    ```commandline
    workon python3.9_flask_env
    pip install -r requirements.txt
    ```
   
4. start web at web
    Under the Web section click on add new web app.  
    Click Next.  
    Then Select manual configuration then click Next.  
    After that, choose the python version, and click Next.

5. edit wsgi file at files
    ```python
    # +++++++++++ FLASK +++++++++++
    # Flask works like any other WSGI-compatible framework, we just need
    # to import the application.  Often Flask apps are called "app" so we
    # may need to rename it during the import:
    
    import sys
    
    ## The "/home/hmkc1220" below specifies your home
    ## directory -- the rest should be the directory you uploaded your Flask
    ## code to underneath the home directory.  So if you just ran
    ## "git clone git@github.com/myusername/myproject.git"
    ## ...or uploaded files to the directory "myproject", then you should
    ## specify "/home/hmkc1220/myproject"
    
    path = '/home/hmkc1220/sample_webapi_python'
    if path not in sys.path:
        sys.path.append(path)
    
    from index import app as application  # noqa
    
    # NB -- many Flask guides suggest you use a file called run.py; that's
    # not necessary on PythonAnywhere.  And you should make sure your code
    # does *not* invoke the flask development server with app.run(), as it
    # will prevent your wsgi file from working.
    ```
   
6. set virtualenv path at web
    how to check path at consoles
    ```commandline
    workon python3.9_flask_env
    witch python
    ```
   
7. enable Force HTTPS at web

2. Change "project name"
    
# How to create this
0. install python, something virtualenv

1. make and into project_directoy: sample_webapi_python
    ```
    mkdir sample_webapi_python
    cd sample_webapi_python
    ```

2. activate virtualenv
    for exsample conda
    ```
    conda create --name python3.9_sample_webapi_python python=3.9 -y
    conda activate python3.9_sample_webapi_pyhton
    ```
    
3. install librarys
    ```
    pip install Flask
    ```

4. meke and coy&paste main_file: index.py
    ```
    touch index.py
    ```
    copy&paste this rep's index.py
