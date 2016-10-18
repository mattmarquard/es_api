import json

user_response = { 
#    "_index" : "firebase",
#    "_type" : "user",
#    "_id" : "ghW2JMckiAg3TaHlnJr3Qdnj2L62",
#    "_score" : 1.0,
#    "_source" : {
    "ghW2JMckiAg3TaHlnJr3Qdnj2L62" : {
        "email" : "city@city.com",
        "events" : {
            "-KSKgkenLhdzO-4CKQga" : "true",
            "-KSUXQQY1p0CjDqLpPqn" : "true",
            "-KSV6lGw33Hv7jRwLNmG" : "true",
            "-KTeqiqyQOeuXcTHOWSN" : "true"
        },
        "name" : "city",
        "password" : "city1234",
        "purchase_ids" : {
            "-KTY03yT9ZFzK4mc2pmG" : "true",
            "-KTY2mnmRbcfJBiFLk8S" : "true",
            "-KTesJuBMq0klbMy-56D" : "true"
        },
        "purchases" : {
            "-KSKh1w1jXPNT0VSFyr1" : "true",
            "-KSMm6Rp7UAT2i5KsOvP" : "true",
            "-KSMmHv8QWg5oVkvnpCL" : "true",
            "-KSMmmhP6owoi6pdQXfw" : "true",
            "-KSUXoi-xW0Vlckxdh1U" : "true",
            "-KSUqzuu6YWOF9Nfxbk0" : "true",
            "-KSV-aOIkvWHvJzMMDMv" : "true",
            "-KSV1KLZxbTfhaYCIcqr" : "true",
            "-KSV7ZSog-pY2AZ8C9oh" : "true",
            "-KT7jZGqWNbpRFsBLJw_" : "true",
            "-KTKajnXrG48WZqc7I31" : "true" 
        }
    }
}
venue_response = {
    "_index" : "firebase",
    "_type" : "event",
    "_id" : "-KSV6lGw33Hv7jRwLNmG",
    "_score" : 1.0,  "_source" : {
        "description" : "sdfsdf",
        "duration" : 100000,
        "location_lat" : 40.2047479,
        "location_lon" : 44.51615109999999,
        "location_name" : "DDD Complex",
        "location_place_id" : "ChIJb7hT5za9akARrBspHvRaS1M",
        "name" : "third one",
        "start_date" : 1474786432235,
        "user_id" : "ghW2JMckiAg3TaHlnJr3Qdnj2L62"
    }
}
event_response = {
    "_index" : "firebase",
    "_type" : "event",
    "_id" : "-KSV6lGw33Hv7jRwLNmG",
    "_score" : 1.0,
    "_source" : {
        "description" : "sdfsdf",
        "duration" : 100000,
        "location_lat" : 40.2047479,
        "location_lon" : 44.51615109999999,
        "location_name" : "DDD Complex",
        "location_place_id" : "ChIJb7hT5za9akARrBspHvRaS1M",
        "name" : "third one",
        "start_date" : 1474786432235,
        "user_id" : "ghW2JMckiAg3TaHlnJr3Qdnj2L62"
    }
}

#event_response = event_response.replace(" ", "").replace("\n", "")
#user_response = user_response.replace(" ", "").replace("\n", "")
#venue_response = venue_response.replace("\n", "").replace(" ", "")
json_user = user_response
json_event = event_response
json_venue = venue_response
