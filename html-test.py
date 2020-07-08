import webbrowser
import os
path = os.path.dirname(os.path.abspath(__file__))
print("current path " + path)

# fontSize = input("Font??")

f = open('home.html', 'w')

style = open('style.css', 'w')

message = """<html>
<head><link rel="stylesheet" type="text/css" href="style.css"></head>
<body><p>Hello World! Sakthi </p></body>
</html>"""


stye_code = """
@font-face {
font-family: "Quicksand";
src: url(quicksand/Quicksand_Dash.otf) format("opentype");
}

*{
    size: A4;
}

body p{
    font-family: Quicksand;
    color: black;
    font-size: 70px;}"""


            
            


f.write(message)
f.close()

style.write(stye_code)
style.close()

# filename = path + "/" + "h.html"
filename = path + "/" + "home.html"
webbrowser.open_new_tab("http://localhost:63343/worksheet-gen/home.html?_ijt=rllnffpfdq8do1g4nss6h2p6da")

# webbrowser.open('https://www.google.com/')