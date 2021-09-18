from flask import Flask, redirect, request, jsonify, json
from countryinfo import CountryInfo

app = Flask(__name__)

@app.route("/")
def main():
    if request.args.get('davlat'):
        query = request.args.get('davlat')
    else:
    	return "<b>Ushbu api davlatlar haqida ma'lumot qidirish uchun!<br>Namuna:<b> <code>https://countryinfouz.herokuapp.com?davlat=Uzbekistan</code> <br><br><i>Developer:</i> <a href='https://t.me/LiderBoY'>Arslonbek</a>"
        
    country = CountryInfo(query)
    info = country.info()
    if info is not None:
        info["google"] = "https://www.google.com/search?q=" + info["name"].replace(" ", "+")
        return jsonify(info)
    else:
        return "Topilmadi!"


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000, use_reloader=True, threaded=True)
