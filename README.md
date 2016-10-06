# Packtpub Downloader

Packtpub Downloader is a small tool that allows any registered account to automatically download all the ebooks (ps: more options to come).
It will download everything: .pdf, .mobi, .epub and the zip file if any.

### How to use

#### Using `Virtualenv` *(recommended)*

It is always better to create a virtual environment to isolate Python environments. 

**Installing virtualenv**

Assuming you already have a working Python environment set up, open up a terminal and refer to [the virtualenv webpage][virtualenv rtd] to set up everything.

**Installing the dependencies**

Now that you have the sourced the environment, run the following to install the dependencies:

`pip install -r requirements.txt`

**Using Packtpub Download(finally)**

The username and password are mandatory:

`python pbdl.py -u myemail@mail.com -p mypassword`

I've set up multiple arguments for you to provide, those can be shown using the following command:

`python pbdl.py --help`


### Development

Want to contribute? Great! You're welcome to make some pull requests!

### Todos

 - Things

License
----
MIT


**Free Software, Hell Yeah!**

[virtualenv rtd]: <https://virtualenv.pypa.io/en/stable/>