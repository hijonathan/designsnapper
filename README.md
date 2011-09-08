## DesignSnapper Overview

DesignSnapper is a light-weight web app for monitoring changes to web pages over time.

## Technical Specs

Built with Django and Python. Uses Compass, Sass and CoffeeScript.

#### Installing project dependencies

- Install BeautifulSoup

        easy_install BeautifulSoup

- Install mysql

        easy_install pymysql

OR

        easy_install mysqld

#### Installing ui dependencies (OS X)

- Install Macports.
- Install Ruby (but you should already have it)
- Install Sass and Compass.

        gem install sass
        gem install compass

- Install CoffeeScript dependencies

        sudo port install nodejs
        node -v

        sudo chmod -R g+w /opt/local/
        curl http://npmjs.org/install.sh | sh

        npm install coffee-script
        npm install jitter

That second part is kinda a pain in the butt, but it's a cool little language.

#### How to run the project locally

- Clone the repo:

        git clone git@github.com:hijonathan/designsnapper.git

- Boot the server

        python manage.py runserver [port]

If you're running OS X and have a virtual machine (e.g. Parallels/VMWare) that you'd like to use as well, use this to boot the server instead:

        python manage.py runserver [port]:0.0.0.0