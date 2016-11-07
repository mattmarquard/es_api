from flask import Flask
from flask_restful import Resource, Api, reqparse
from es_connect import search_fields, search_latlon

app = Flask(__name__)
api = Api(app)

# class CreateUser(Resource):
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
        try:
            parse = reqparse.RequestParser()
            parse.add_argument('query', type=str, help='Query to search users')
            args = parse.parse_args()
            _query = args['query']
            response = search_fields(_query, ['name'])

            return response

        except Exception as e:

            return {'error': str(e)}


class SearchVenues(Resource):
    def post(self):
        try:
            parse = reqparse.RequestParser()
            parse.add_argument('query', type=str, help='Query to search venues using Event.location_name')
            args = parse.parse_args()
            _query = args['query']
            response = search_fields(_query, ['location_name'], ["events"])

            return response

        except Exception as e:

            return {'error': str(e)}


class SearchEventsByPoint(Resource):
    def post(self):
        try:
            parse = reqparse.RequestParser()
            parse.add_argument('lat', type=int, help='Query to search venues using Event.lat')
            parse.add_argument('lon', type=int, help='Query to search venues using Event.lon')
            args = parse.parse_args()
            lat = args['lat']
            lon = args['lon']
            response = search_latlon(lat, lon)

            return response
        except Exception as e:
            return {'error': str(e)}


class SearchEvents(Resource):
    def post(self):
        try:
            parse = reqparse.RequestParser()
            parse.add_argument('query', type=str, help='Query for event names and descriptions')
            args = parse.parse_args()

            _query = args['query']
            response = search_fields(_query, ['name', 'description'])
            return response
        except Exception as e:
            return {'error': str(e)}


#api.add_resource(CreateUser, '/CreateUser')
api.add_resource(SearchUsers, '/users')
api.add_resource(SearchEvents, '/events')
api.add_resource(SearchVenues, '/venues')
api.add_resource(SearchEventsByPoint, '/point')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
