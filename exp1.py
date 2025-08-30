from http.server import HTTPServer, BaseHTTPRequestHandler

htmlcontent = '''
<!doctype html>
<html>
    <head>
        <title>Loki Sample Web project</title>
    </head>
    <body>
        <font>
            <center><font color="blue" face="arial" size="100">
            <b>List of Protocol in TCP/IP Model</b>
            </font></center>
            <font color="red">
            <h2>
                Application Layer - HTTP, FTP, DNS, Telnet & SSH<br>
                Transport Layer - TCP, & UDP<br>
                Network Layer - IPV6/IPV4<br>
                Link Layer - Ethernet
            </h2>

        </font>
        
    </body>
</html>>'''

class ServerResponse(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(htmlcontent.encode())

print("This is my webserver") 
server_address =('',5000)
httpd = HTTPServer(server_address,ServerResponse)
httpd.serve_forever()