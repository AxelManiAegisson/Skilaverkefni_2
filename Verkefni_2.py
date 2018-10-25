from bottle import *


@route("/")
def index():
    return """
    <h2> Verkefni 2 </h2>
    <a href="/a"> Liður A </a>
    <br></br>
    <a href="/b"> Liður B </a>
    """


@route("/a")
def a():
    return """
        <h2> Verkefni 2.A</h2>
        <a href="/sida/1"> Siða 1 </a> -
        <a href="/sida/2"> Siða 2 </a> -
        <a href="/sida/3"> Siða 3 </a> -
    """

@route("/sida/<id>")
def page(id):
    if id == '1':
        return "Þetta er síða 1<br><a href='/a'>Til baka</a>"
    elif id == '2':
        return "Þetta er síða 2<br><a href='/b'>Til baka</a>"
    elif id == '3':
        return "Þetta er síða 3<br><a href='/c'>Til baka</a>"
    else:
        abort(404, "<h2 style ='color:red'> Þessi síða finnst ekki</h2>")


######################################################################
#Einhver falinn villa hérna sem við fundum ekki
@route("/b")
def b():
    return """
    <h2>Verkefni 2-B</h2>
    <h4>Veldu uppáhaldsbókstafinn þinn</h4>
    <a href="/sida2?fight=1><img src='Myndir/Fighter1.jpg'></a>
    <a href="/sida2?fight=2><img src='Myndir/Fighter2.jpg'></a>
    <a href="/sida2?fight=3><img src='Myndir/Fighter3.jpg'></a>
    <a href="/sida2?fight=4><img src='Myndir/Fighter4.jpg'></a>
    """

@route("/sida2")
def page():
    l = request.query.fight
    if l == '1':
        return "<h3>Þú hefur valið epic boi: </h3> <img src='Myndir/Fighter1.jpg'>"
    l = request.query.fight
    if l == '2':
        return "<h3>Þetta er núðlu boi: </h3> <img src='Myndir/Fighter2.jpg'>"
    l = request.query.fight
    if l == '3':
        return "<h3>Bestur </h3> <img src='Myndir/Fighter3.jpg'>"
    l = request.query.fight
    if l == '4':
        return "<h3>Todd gunward: </h3> <img src='Myndir/Fighter4.jpg'>"


######################################################################

@route('/Myndir/<skra>')
def static(skra):
    return static_file(skra, root='Myndir')

@error(404)
def villa(error):
    return "<h2 style ='color:red> þessi síða fannst ekki</h2> "

run(host="0.0.0.0", port=os.environ.get('PORT'))
