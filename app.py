from flask import Flask, redirect, request, jsonify, json, render_template
from countryinfo import CountryInfo

app = Flask(__name__)

@app.route("/")
def main():
    if request.args.get('davlat'):
        query = request.args.get('davlat')
    else:
      return """
<!DOCTYPE html>
<html>

<head>
    <title>CountryInfo UZ</title>
    <link rel="icon" href="https://www.elitetourism.com/images/languange_icon.png">
</head>

<body>
    <script type="text/javascript">
        function myFunction() {
            /* Get the text field */
            var copyText = document.getElementById("myInput");

            /* Select the text field */
            copyText.select();
            copyText.setSelectionRange(0, 99999); /* For mobile devices */

            /* Copy the text inside the text field */
            navigator.clipboard.writeText(copyText.value);

            /* Alert the copied text */
            alert("Nusxalandi: " + copyText.value);
        }
    </script>
    <style type="text/css">
        article {
            background: linear-gradient( to right, hsl(98 100% 62%), hsl(204 100% 59%));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
        }
        
        h1 {
            font-size: 10vmin;
            line-height: 1.1;
        }
        
        body {
            background: hsl(204 100% 5%);
            min-block-size: 100%;
            min-inline-size: 100%;
            box-sizing: border-box;
            display: grid;
            place-content: center;
            font-family: system-ui;
            font-size: min(200%, 5vmin);
        }
        
        h1,
        p,
        b,
        body {
            margin: 0;
        }
        
        p,
        b,
        b {
            font-family: "Dank Mono", ui-monospace, monospace;
        }
        
        html {
            block-size: 100%;
            inline-size: 100%;
        }
    </style>
    <article>
        <h1>CountryInfo UZ</h1><br>
        <p>Ushbu API davlatlar haqida ma'lumot qidiradi va ma'lumotni JSON formatda qaytaradi.</p><br>
        <b>Namuna: https://lidey.pythonanywhere.com?davlat=Uzbekistan</b>
    </article>
</body>

</html>
    """
    try:
        country = CountryInfo(query)
        info = country.info()
        if info is not None:
            info["google"] = "https://www.google.com/search?q=" + info["name"].replace(" ", "+")
            return jsonify(info)
        else:
            return "Topilmadi!"
    except Exception as ex:
        return f"<h1>Xatolik!</h1><br>Topilmadi: <h5><b>{ex}</b></h5>"


if __name__ == '__main__':
    app.run(debug=True)
