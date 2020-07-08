import webbrowser
import os
path = os.path.dirname(os.path.abspath(__file__))
print("current path " + path)

# fontSize = input("Font??")

f = open('home.html', 'w')

style = open('style.css', 'w')

line = input("Line: ")
font_size  = input("font size: ")
num_lines = int(input("Number of Lines: "))
x = " "


code = ""
font_code = ""

for i in range(num_lines):
    code += (f'<li>{line}</li>'+ '\n\n')

# test if printing correctly
# print(code)

html_code = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <div class="title"> """ + line + """ </div>

    <div class="lines">
<ul> """ + code + """
</ul>
    </div>

</body>
</html>"""


stye_code = """
@font-face {
font-family: "Quicksand";
src: url(quicksand/Quicksand_Dash.otf) format("opentype");
}
@font-face {
    font-family: Normal;
    src: url(quicksand/Quicksand_Bold.otf) format("opentype");
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
    font-size: """+  font_size +"""px;
    opacity: 50%;
    list-style-type: none;
    
}


.lines li{
    padding-top: 10px;
    padding-bottom: 10px;
    /*removes the bullet points*/
    list-style-type: none;
    margin: 0;
    text-decoration-line: underline;
    text-decoration-opacity: 10%;


}

.title{
    font-family: Quicksand;
    opacity: 100%;
    font-size: 60px;
    text-align: center;
    font-family: Normal;

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