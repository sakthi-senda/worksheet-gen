import webbrowser
import os
print("current path " + os.path.dirname(os.path.abspath(__file__)))

f = open('helloworld.html', 'w')

message = """<html>
<head></head>
<body><p>Hello World!</p></body>
</html>"""

f.write(message)
f.close()

