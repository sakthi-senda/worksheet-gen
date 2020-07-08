import webbrowser
import os
path = os.path.dirname(os.path.abspath(__file__))
print("current path " + path)

# fontSize = input("Font??")

f = open('home.html', 'w')

style = open('style.css', 'w')

html_code = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" type="text/css" href="sample_stylesheet.css">
</head>
<body>
    <div class="title">
        My name is Nidhi
    </div>

    <div class="lines">
<ul>
    <li>My name is Sakthi</li>
    <li>My name is Nidhi</li>
</ul>
    </div>

</body>
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
    font-size: 80px;}

.lines{
    font-family: Quicksand;
    padding-top: 20px;
    font-size: 50px;
    opacity: 50%;
}

.title{
    font-family: Quicksand;
    opacity: 100%;
    font-size: 60px;
    text-align: center;

}
"""


            
            


f.write(html_code)
f.close()

style.write(stye_code)
style.close()

# filename = path + "/" + "h.html"
filename = path + "/" + "home.html"
webbrowser.open_new_tab("http://localhost:63343/worksheet-gen/home.html?_ijt=rllnffpfdq8do1g4nss6h2p6da")

# webbrowser.open('https://www.google.com/')