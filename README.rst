=========================
Django Loose CMS - Search
=========================

A search plugin for Django Loose CMS.

Requirements
------------

Loose CMS Text plugin requires:

* Django version 1.8
* Python 2.6 or 2.7
* django-loose-cms
* django-haystack
* pysolr

Quick Start
-----------

1. Instalation via pip::

    pip install https://github.com/lefterisnik/django-loosecms-search/archive/master.zip

2. Add "loosecms_search" to your INSTALLED_APPS setting after "loosecms" like this::

    INSTALLED_APPS = (
        ...
        'haystack',
        'loosecms_search',
    )
    
3. Run ``python manage.py migrate`` to create the loosecms_search models.

4. Run development server ``python manage.py runserver`` and visit http://127.0.0.1:8000/ to start
   playing with the cms.

Install Sorl Search Engine Backend
----------------------------------

In order to play the plugin you should install the Sorl Search Engine Backend

1. Download and unzip the sorl source package::

    curl -LO https://archive.apache.org/dist/lucene/solr/4.10.2/solr-4.10.2.tgz
    tar xvzf solr-4.10.2.tgz

2. You'll need to revise your schema::

    python manage.py build_solr_schema

   Take the output from that command and place it in ``solr-4.10.2/example/solr/collection1/conf/schema.xml``

3. You'll need to update search index content::

    python manage.py update_index

4. Move to the Sorl folder and start the service::

    cd solr-4.10.2
    cd example
    java -jar start.jar