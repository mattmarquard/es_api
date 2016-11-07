from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q
from elasticsearch_dsl.query import MultiMatch

def query_es(query=None):

    client = Elasticsearch()

    s = Search(using=client, index="firebase") \
	.filter("term", category="search") \
	.query("match", title="{}".format(query))   \
	.query(~Q("match", description="{}".format(query)))

    s.aggs.bucket('per_tag', 'terms', field='tags') \
	.metric('max_lines', 'max', field='lines')

    response = s.execute()

    for hit in response:
        print(hit.meta.score, hit.title)

    for tag in response.aggregations.per_tag.buckets:
        print(tag.key, tag.max_lines.value)

def search_fields(query, fields=[], dt=[]):
    client = Elasticsearch()
    se = Search(using=client, index="firebase")
    #se = se.params(doc_type=dt)
    if fields > 0:
        q = Q("multi_match", query=query, fields=fields)
    else:
        q = Q("match", query=query)
    se = se.query(q)
    #import pdb; pdb.set_trace()
    response = se.execute()
    response = response.to_dict()['hits']['hits']
    results = {}
    for v in response:
        key = v['_id']
        results[key] = v['_source']
    return results


def search_latlon(lat, lon, dt=[]):
    client = Elasticsearch()
    se = Search(using=client, index="firebase")
    #se = se.params(doc_type=dt)
    q = Q({"bool" : {"must" : {"match_all" : {}}}})
    se = se.query(q)
    se = se.filter("geo_distance",
                   distance="1000km",
                   location="{}, {}".format(lat,lon),)
    response = se.execute()
    response = response.to_dict()['hits']['hits']
    results = {}
    for v in response:
        key = v['_id']
        results[key] = v['_source']
    return results
