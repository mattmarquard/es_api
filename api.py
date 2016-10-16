from flask import Flask
import json
from flask_restful import Resource, Api, reqparse
from es_connect import query_es
import testdata

app = Flask(__name__)
api = Api(app)

#class CreateUser(Resource):
#    def post(self):
#        try:
#            parser = reqparse.RequestParser()
#            parser.add_argument('email', type=str, help='Email address to create user')
#            parser.add_argument('password', type=str, help='Password to create user')
#            args = parser.parse_args()
#
#            _userEmail = args['email']
#            _userPassword = args['password']
#
#            return {'Email': args['email'], 'Password': args['password']}
#        except Exception as e:
#            return {'error': str(e)}
#
class SearchUsers(Resource):
    def post(self):
	return testdata.json_user
        #try:
        #    parse = reqparse.RequestParser()
        #    parse.add_argument('query', type=str, help='Query to search users')
        #    args = parse.parse_args()
        #    import pdb; pdb.trace()

        #    _query = args['query']

        #    return {'Query': _query }
        #except Exception as e:
        #    return {'error': str(e)}

class SearchVenues(Resource):
    def post(self):
        unij = testdata.json_venue 
        return json.loads(unij)
        #try:
        #    parse = reqparse.RequestParser()
        #    parse.add_argument('query', type=str, help='Query to search users')
        #    args = parse.parse_args()

        #    _query = args['query']

        #    return {'Query': _query }
        #except Exception as e:
        #    return {'error': str(e)}

class SearchEvents(Resource):
    def post(self):
	return testdata.json_event
        #try:
        #    parse = reqparse.RequestParser()
        #    parse.add_argument('query', type=str, help='Query for event names and descriptions')
        #    args = parse.parse_args()

        #    _query = args['query']
        #    response = query_es(_query)

        #    return {'Result': response }
        #except Exception as e:
        #    return {'error': str(e)}


#api.add_resource(CreateUser, '/CreateUser')
api.add_resource(SearchUsers, '/users')
api.add_resource(SearchEvents, '/events')
api.add_resource(SearchVenues, '/venues')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
