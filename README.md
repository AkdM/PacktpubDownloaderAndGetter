# Packtpub Downloader
----

Packtpub Downloader is a small tool that allows any registered account to automatically download all the ebooks (ps: more options to come).
It will download everything: .pdf, .mobi, .epub and the zip file if any.

![Packpub Downloader screenshot](screenshot.png?raw=true "Screenshot")

## How to use

It is always better to create a virtual environment to isolate Python environments. 

Assuming you already have a working Python environment set up, open up a terminal and refer to [the virtualenv webpage][virtualenv rtd] to set up everything.

**Installing the dependencies**

Now that you have the sourced the environment, run the following to install the dependencies:

`pip install -r requirements.txt`

**Using Packtpub Download(finally)**

The username and password are mandatory:

`python pbdl.py -u myemail@mail.com -p mypassword`

I've set up multiple arguments for you to provide, those can be shown using the following command:

`python pbdl.py --help`

## What for?

Packtpub.com has a free ebook available each day, I didn't want to download my 100+ ebooks I had on my account, so I developed this.

If you feel in the same situation, feel free to use this :)

## Changelog

**v0.3** (October 06, 2016)

* **[FIXED]** Hotfix on UTF-8 encoding

**v0.2** (October 06, 2016)

* **[FIXED]** Some URL weren't downloading
* **[IMPROVED]** CLI is now almost beautiful
* **[IMPROVED]** Speed

**v0.1** (October 06, 2016)

* First version, some things are working.

## Development

Want to contribute? Great! You're welcome to make some pull requests!

## Todos

 - Things

License
----
MIT


**Free Software, Hell Yeah!**

[virtualenv rtd]: <https://virtualenv.pypa.io/en/stable/>