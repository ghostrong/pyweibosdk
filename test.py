#!/usr/bin/env python

from weiboapi import apiclient
api = apiclient.APIClient()

print 'My token is:', api.access_token
limit = api.rate_limit()
print limit['remaining_ip_hits']

# get data from public_timeline
# http://open.weibo.com/wiki/2/statuses/public_timeline
r = api.call("statuses/public_timeline", count=10)
print r.keys()
print 'Got statuses: ', len(r['statuses'])
