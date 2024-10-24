from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<!doctype html>
<html>
<head>
<title> My Web Server</title>
</head>
<body>
<h1> My Laptop Configuration</h1>
<table >
    <tr>
        <th width="50%">System Config</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>Processor</td>
        <td>13th Gen Intel(R) Core(TM) i5-1335U   1.30 GHz</td>
    </tr>
    <tr>
        <td>Primary Memory</td>
        <td>16.0 GB (15.7 GB usable)</td>
    </tr>
    <tr>
        <td>Seccondary Memory</td>
        <td>512 GB</td>
    </tr>
    <tr>
        <td>OS</td>
        <td>Windows 11 Home Single Language</td>
    </tr>
    <tr>
        <td>Graphic</td>
        <td>Intel® Iris® plus Xe Graphics</td>
    </tr>
</table>
</body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()