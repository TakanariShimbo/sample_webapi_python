# About
This is sample webapi written in python.

# pythonanywhere
1. clone repo
    ```commandline
    git clone https://github.com/TakanariShimbo/sample_webapi_python.git
    cd sample_webapi_python
    ```
   
2. make virtualenv
    ```commandline
    mkvirtualenv python3.9_flask_env --python=/usr/bin/python3.9
    deactivate
    ```
   
3. install requirements
    ```commandline
    workon python3.9_flask_env
    pip install -r requirements.txt
    ```
   
4. start web  
    Under the Web section click on add new web app.  
    Click Next.  
    Then Select manual configuration then click Next.  
    After that, choose the python version, and click Next.

5. edit wsgi file
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
   
6. set virtualenv path  
    how to check path
    ```commandline
    workon python3.9_flask_env
    witch python
    ```
   
7. enable Force HTTPS