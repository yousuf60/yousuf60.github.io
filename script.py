def links():
    links = ""
    #         link, title
    for i in [
            ("https://github.com/yousuf60", "github"),
            ("https://linkedin.com/in/yousuf-mahmoud-560037280", "linkedin"),
            ("https://cara.app/yousuf60","Cara.app"),
            ("https://instagram.com/_yousufmh_", "instagram"),
            ("https://pinterest.com/yousuf_mh", "Pinterest"),
                ]:

        links += "<a href=" +i[0]+">" +i[1]+ "</a>\n"
    return links


HEAD = '''

<head>
	<title>Yousuf Mahmoud</title>
	<link rel="stylesheet" href="style/main.css">
    <meta name="viewport" content="width=device-width, inital-scale=1.0">	
</head>

'''
BODY = f'''
<body>

<div id="center-card">

<center>
<img id="profile-img" src="https://avatars.githubusercontent.com/u/64571068">
<h3>Yousuf Mahmoud</h3>
</center>

{links()}

<br>
</div>

</body>

'''
HTML = f'''
<!DOCTYPE html>
<html>
{HEAD}
{BODY}
</html>

'''

with open("index.html", "w") as f:
    f.write(HTML)
    print(HTML)
