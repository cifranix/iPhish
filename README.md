# iPhish
iPhish is a simple php-infused python script, used to emulate a desired website by wrapping the website in an iFrame, overlaying a fake loginbox, and interfaces with php on the backend to collect credentails.

# Usage
Copy contents of html file to var/www/html:
```sh
$ cp html/* /var/www/html/
```
Run main file, where example.com is the website you wish to emulate:
```sh
$ python3 iPhish https://www.example.com
```

# Dependencies
* Fedora release 24
* Running apache webserver
* Python 3.5.2
* PHP 5.6.27


# Demo 
[![iPhish YouTube Demo](https://img.youtube.com/vi/jMzkWeUoyiM/0.jpg)](https://www.youtube.com/watch?v=jMzkWeUoyiM&feature=youtu.be)

# Future Developments 
* Input validation 
* Usage within the .py
* Determine if target website will not open iFrame

https://xkcd.com/1694/
