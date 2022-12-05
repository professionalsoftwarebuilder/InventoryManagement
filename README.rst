|PyPI badge| |Installs badge| |License badge| |Wheel badge|

Django Inventory
----------------

Free Open Source Inventory and Fixed Assets Control System

Features
--------

* Object oriented approach to asset and inventory management.
* CSV import utility.
* Per asset or per item type photos and information.
* Match suppliers to item types.
* Site wide search capability.
* User defined states (broken, in repairs, etc) for assets.
* An item can be defined as a supply to another item.
* Assign assets to one or more individuals.
* User photos.
* Group assets, inventories or user per locations.
* Purchase request and purchase orders.


License
-------

This project is open sourced under `Apache 2.0 License`_.


Installation
------------

To install **Django Inventory**, simply do:

.. code-block:: bash

    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install django-inventory==1.0rc1
    $ django-inventory.py initialsetup
    $ django-inventory.py runserver

Point your browser to 127.0.0.1:8000 and use the automatically created admin
account.

