

line = input("Line: ")
font_size  = input("font size: ")
num_lines = int(input("Number of Lines: "))
x = " "


code = ""

for i in range(num_lines):
    code += (f'<li>{line}</li>'+ '\n\n')

print(code)


# def createhtml(line):
#
#     code = f'''<li>{line}</li>
# <b></b'''
#     return code
#
#
# def createcss(font_size=50):
#
#     start = "li{"
#     end = "}"
#     code = f'font-size: {font_size}'
#
#     x = start + code + end
#     return  x
#
#
#
# print(createcss(font_size))
#
#
#
#
# print(createhtml(line))
# print