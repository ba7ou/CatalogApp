# Udacity Fullstack Nanodegree Project 3 - Catalog App

This app create, update and delete items in various predefined categories.

## Setup

This app uses

- [Flask](http://flask.pocoo.org)
- [SQLAlchemy](http://www.sqlalchemy.org)
- [Bootstrap 3](http://getbootstrap.com/)

These dependencies must be installed before you can run the app. The easiest way to do so is by using [pip](https://pypi.python.org/pypi/pip). Simply run the following commands:

  ```pip install Flask

	```pip install SQLAlchemy

The app uses Google and Facebook for authentication as the next step you have to obtain a client id and client secret, you can use the following documentation:
- https://developers.google.com/identity/sign-in/web/devconsole-project
- https://developers.facebook.com/docs/apps/register



Next you have to create the database. Run

	python database_setup.py

## Run the app

To start the app simply run

	python application.py

## What's included
```
catalog/
├── static
|   └── styles.css
├── templates
|   ├── catalog.html
|   ├── category.html
|   ├── deleteItem.html
|   ├── editItem.html
|   ├── header.html
|   ├── item.html
|   ├── login.html
|   ├── main.html
|   ├── newItem.html
|   └── publiccatalog.html
├── application.py
├── client_secrets.json
├── database_setup.py
├── fb_client_secrets.json
├── lotofitems.py
└── readme.md
```

## Remarks
- You can run python lotofitems.py to populate the database with examples
- The app offers two JSON endpoints:
	- /catalog/categories.json
	- /catalog/<category_name>/items.json
- The app is not optimized for small devices (smartphones etc.)

## Creators

**NAUTIN Nicolas**

- <https://twitter.com/Batou__>
- <https://github.com/ba7ou>

**Udacity**


## Copyright and license

Code and documentation copyright 2011-2015 Twitter, Inc. Code released under [the MIT license]
