from nose.tools import *
import re

def assert_response( resp, contains=None, matchs=None, headers=None, \
	status='200' ):
	
	assert status in resp.status,'Expected response %r not in %r'%\
		(status, resp.status)
	if status == '200':
		assert resp.data,'Response is empty.'
	if contains:
		assert contains in resp.data,'Response does not contain %s'%contains
	if matchs:
		reg = re.compile(matchs)
		assert reg.matchs(resp.data), 'Response does not match %r'%matchs
	if headers:
		assert_equal(resp.headers, headers)

