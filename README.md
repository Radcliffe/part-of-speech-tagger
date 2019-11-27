# Part-of-speech tagger



## Installation

The following instructions are for installing the part-of-speech tagger on an Apache server running Ubuntu 18.04. The steps for your environment may vary.

Install required packages.

     $ sudo apt-get update
     $ sudo apt-get install -y python3 python3-venv \
       libapache2-mod-wsgi-py3 python-dev


Create a virtual environment.

     $ /usr/bin/python3 -m venv venv
     $ source venv/bin/activate
     $ pip 
     $ pip install -r requirements.txt

Download the `averaged_perceptron_tagger` package from the Python
Natural Language Toolkit (NLTK).

     $ python nltk_download.py

Launch the server.

     $ hug -f web/tagger.py

Run the test. If you see "Test passed." then the application is working properly.

     $ python tests/post_test.py


