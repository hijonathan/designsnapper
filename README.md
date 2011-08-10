## DesignSnapper Overview

DesignSnapper is a light-weight web app for monitoring changes to web pages over time.

## Technical Specs

Built with Django, Python and Google AppEngine. Uses Compass, Sass and CoffeeScript.

#### Installing ui dependencies (OS X)

- Install Macports.
- Install Ruby (but you should already have it)
- Install Sass and Compass.

        sudo gem install sass
        sudo gem install compass

- Install CoffeeScript dependencies

        sudo port install nodejs
        node -v

        sudo chmod -R g+w /opt/local/
        curl http://npmjs.org/install.sh | sh

        npm install coffee-script
        npm install jitter

That second part is kinda a pain in the butt, but it's a cool little language.

#### How to run the project locally

- Install Python (should already exist).
- Install Google AppEngine SDK http://code.google.com/appengine/downloads.html.
- Clone the repo:

        git clone git@github.com:hijonathan/designsnapper.git

Add the project to your AppEngine launcher or run it from the command line using dev_appserver.py. You'll also need to install Ruby and Compass if you plan to make design changes. Alternatively, you can simply run the Django project from the command line:

        python manage.py runserver [port]
