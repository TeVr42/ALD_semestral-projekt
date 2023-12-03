from flask import Flask, render_template, request, redirect
from map import Map
from square import Square

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/mapa', methods=["POST"])
def map():
    width = int(request.form['map_width'])
    height = int(request.form['map_height'])
    type = request.form['map_type']
    if width < 0 or height < 0:
        return redirect('/')
    map = Map(width, height, type)
    addresses = map.get_addresses()
    rotations = map.get_rotations()
    return render_template("map.html", height=height, width=width, addresses=addresses, rotations=rotations)

@app.route('/mapa', methods=["GET"])
def map_redirect():
    return redirect('/')

if __name__ == "__main__":
    app.run(port=5000)