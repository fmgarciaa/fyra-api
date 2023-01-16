#!/bin/sh
echo "What is the App name?"
read app_name
cd fyra
mkdir $app_name
cd $app_name

mkdir migrations
cd migrations
touch __init__.py
cd ..

mkdir models
cd models
touch __init__.py
touch $app_name.py
cd ..

mkdir serializers
cd serializers
touch __init__.py
touch $app_name.py
cd ..

mkdir views
cd views
touch __init__.py
touch $app_name.py
cd ..

touch __init__.py
touch admin.py
touch apps.py
touch permission.py
touch urls.py

echo Done!! happy hacking!!