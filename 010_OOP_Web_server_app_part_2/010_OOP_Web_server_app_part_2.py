# Introduction to Python OOP programing: Practical example part-2
# server library
from http.server import BaseHTTPRequestHandler, HTTPServer
# urlib / Json libs
import urllib.request
import json

hostName = "localhost"
serverPort = 8080
css = """
        h1 {
            color: blue;
            font-family: verdana;
            font-size: 300%;
        }

        p {
            color: black;
            font-family: courier;
            font-size: 160%;
        }
        .container{
            display: flex;
            justify-content: center;
            width: 100%;
        }
        .book-summary{
            width: 80%;
            flex-direction: column;
        }
        .search{
                height: 60px;
                background-color: #607d8b;
        }
        .search-item{
            background-color: #cddc39;
            font-size: 30px;
            display: flex;
            align-items: center;
            padding-left: 8px;
            color: darkblue;
        }
        form {
            display: flex;
            width: 24%;
            justify-content: space-evenly;
            align-items: center;
            height: 100%;
            color: white;
        }
        .summary{
            background-color: lightgray;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .summaryPack{
                width: 80%;
                display: flex;
                flex-direction: column;
                justify-content: center;
                border-bottom: 1px solid black;
        }
"""
HTML = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WeeWStack</title>
    <style>
    {css}
    </style>
</head>
<body>
    <h1>My Book Hunter little application</h1>
    <div class="container">
        <div class="book-summary">
            <div class="search">
                <form action="" method="post">
                    <label for="btitle">Book Title:</label><br>
                    <input type="text" id="fname" name="btitle" value=""><br>
                    <input type="submit" value="Search">
                </form>
            </div>
            <div class="search-item"></div>
            <div class="summary"></div>
        </div>
    </div>
</body>
</html>
"""


class Book():
    def __init__(self, title, authors, description, pageCount):
        self.title = title
        self.authors = authors
        self.description = description
        self.pageCount = pageCount

    def __str__(self):
        return self.title + ' by ' + self.AuthorsSTR()

    @classmethod
    def CreateBook(cls, searchKey):
        data = searchKey["volumeInfo"]
        title = data["title"]
        authors = data["authors"]
        description = data["description"]
        pageCount = data["pageCount"]

        return cls(title, authors, description, pageCount)

    def AuthorsSTR(self):
        return ", ".join(self.authors)


# Initiate the request handler class (Using inheritance)
class myBookServer(BaseHTTPRequestHandler):
    # Static function to convert a certain text format to a dictionary
    @staticmethod
    def stringToDict(FormString):
        DictForm = dict((x.strip(), y.strip())
                        for x, y in (element.split('=')
                                     for element in FormString.split('&')))
        return DictForm
    # Static function to make the API call
    @staticmethod
    def SearchBook(bookname):
        url_title = bookname.replace(" ", "%20")
        url_json = f"https://www.googleapis.com/books/v1/volumes?q=intitle:{url_title}&langRestrict=en&maxResults=40"
        response = urllib.request.urlopen(url_json)
        data = json.loads(response.read().decode())
        return data
    # Method to Update the HTML display

    def UpdateHTML(self, DictForm):
        data = self.SearchBook(DictForm['btitle'])
        for item in data['items']:
            try:
                mybook = Book.CreateBook(item)
                print(mybook)
            except Exception as e:
                print(e)

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        # Get method
        self._set_response()
        self.wfile.write(bytes(HTML, "utf-8"))

    def do_POST(self):
        # Post Method
        content_length = int(self.headers['Content-Length'])
        FormString = self.rfile.read(content_length).decode("utf-8")
        DictForm = self.stringToDict(FormString)
        self.UpdateHTML(DictForm)
        self.do_GET()


# Initiate the Http server object
webServer = HTTPServer((hostName, serverPort), myBookServer)
print(f"Server started http://{hostName}:{serverPort}")

try:
    webServer.serve_forever()
except KeyboardInterrupt:
    pass

webServer.server_close()
print("Server stopped.")
