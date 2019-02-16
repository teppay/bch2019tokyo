from flask import *
import json
import mongo
import stab
from bson.objectid import ObjectId

app = Flask(__name__)

@app.route("/")
def index():
    title = "index"
    return render_template("index.html", title = title)

"""
@app.route("/", methods=["POST"])
def post():
    data_stab = mongo.get_stab()
    data_stab_keys = data_stab.keys()

    tags_in_table = [
            ['<span class="_id">'         , '</span>'],
            ['<span class="block_hright">', '</span>'],
            ['<span class="block_time">'  , '</span>'],
            ['<span class="from">'        , '</span>'],
            ['<span class="to">'          , '</span>'],
            ['<span class="value">'       , '</span>'],
            ['<span class="from">'        , '</span>'],
            ['<span class="to">'          , '</span>'],
            ['<span class="value">'       , '</span>']]


    display_string = '<div class="table">'
    #for key in data_stab_keys:
    display_string += '<div class="table_row">'
    for i,key in enumerate(data_stab.keys()):
        print(key)
        if key != "txs":
            display_string += tags_in_table[i][0] + str(key) + " : " +str(data_stab[key]) + tags_in_table[i][1]
        else:
            txs = data_stab[key]
            for j in txs:
                for l,k in enumerate(j):
                    display_string += str(k) + str(j.keys)

    display_string += "</div>"
    display_string += "</div>"

    title = "result"
    return render_template("result.html", title = title, display_string = Markup(display_string))
"""

#JSON
@app.route("/", methods=["POST"])
def post():
    json_stab = stab.get_stab()
    data_stab = json.loads(json_stab)
    data_stab_keys = data_stab.keys()

    tags_in_table_open = ['<span class="table_title">', '<span class="table_jornal">', '<span class="table_similarity">', '<span class="table_graph">']
    tags_in_table_close= ['</span>', '</span>', '</span>', '</span>']

    display_string = '<div class="table">'
    for key in data_stab_keys:
        display_string += '<div class="table_row">'
        title           = tags_in_table_open[0] + key               + tags_in_table_close[0]
        journal         = tags_in_table_open[1] + data_stab[key][0] + tags_in_table_close[1]
        similarity      = tags_in_table_open[2] + data_stab[key][1] + tags_in_table_close[2]
        display_string += similarity + title + journal
        display_string += "</div>"
    display_string += "</div>"

    title = "Result"
    return render_template("result.html", title = title, display_string = Markup(display_string))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug = True)