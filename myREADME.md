This project (ShortLink) is a Django URL shortening service. You will find information on the project and how to run the code below.

###How to run the service
In order to run the project, navigate to the directory shortlink and type "python manage.py runserver".
A localhost server will start at port 8000. 

###How to use the service

- To shorten a URL, send a POST request to http://localhost:8000/encode. You should send the URL in the POST body as a JSON. For example:\
{\
"url": "http://reaaalllllylooooooong.com/long" \
}
- To decode (or get the original URL from the shortened one), send a GET request with the short URL as a string query parameter to http://localhost:8000/decode. For example:\
http://localhost:8000/decode?url="http://localhost:8000/0"
- You can also be redirected to the original URL if you send a GET request to the short URL. For example, if your long url is "http://loooooooooooooooong.com/" and it was encoded to "http://localhost:8000/12", sending a GET request to http://localhost:8000/12 will redirect you to http://loooooooooooooooong.com/.
###How to run the tests

Type "python manage.py test" from the project's directory (shortlink) in the terminal. 

#### More information

- Project contains two packages: config and shortener. config contains the project's settings. The shortener is for the shortner app. It contains all models, views, routing, tests, and utility for implementing the shortening service.
- The text file long_urls.txt contains long urls for testing. 
- Since the assignment asked to keep the URLs in memory: in case you're performing custom tests on the service, monitor memory usage to avoid memory overload, as the program stores the URLs in memory rather than a DB.

Thank you for taking the time to look at my code and consider my application!

Regards, \
Hadil 