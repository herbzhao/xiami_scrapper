# https://github.com/ultrasonicsoft/angular-python-flask-demo

from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource
# to prevent CORS error - hosting the client and API not on the same origin
from flask_cors import CORS, cross_origin 
from xiami_to_txt import paste_text_from_browser, use_ajax_page

app = Flask(__name__)
api = Api(app)

# resolve CORS issue
CORS(app)

# https://flask-restful.readthedocs.io/en/0.3.5/quickstart.html#argument-parsing


# def abort_if_todo_doesnt_exist(playlist_ID):
#     if todo_id not in parsed_playlist:
#         abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('playlist_ID')
parser.add_argument('playlist_info')
parser.add_argument('special_symbols')

parsed_playlist = {}

# use Playlist ID and ajax pages of Xiami
class Xiami_ID_post(Resource):
    def post(self):
        # clear the items in dictionary when user send a new post request
        parsed_playlist.clear()
        args = parser.parse_args()
        playlist_ID = args['playlist_ID']
        parsed_playlist['result'] = use_ajax_page(playlist_ID)
        return parsed_playlist['result'], 201


# ask user to copy the playlist and identify the speical symbols for parsing
class Xiami_info_post(Resource):
    def post(self):
        parsed_playlist.clear()
        args = parser.parse_args()
        playlist_info = args['playlist_info']
        special_symbols = args['special_symbols']
        parsed_playlist['result'] = paste_text_from_browser(playlist_info=playlist_info, special_symbols=special_symbols)
        return parsed_playlist['result'], 201


class Xiami_get(Resource):
    def get(self):
        print(jsonify(parsed_playlist['result']))
        return jsonify(parsed_playlist['result'])

##
## Actually setup the Api resource routing here
##
# when post, dont care about the ID, when get, use the ID to retrieve
api.add_resource(Xiami_ID_post,'/xiami_ID')
api.add_resource(Xiami_info_post,'/xiami_info')
api.add_resource(Xiami_get,'/xiami_parsed_result')



if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)