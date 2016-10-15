from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q

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
