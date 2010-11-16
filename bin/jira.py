#!/usr/bin/python

import SOAPpy, getpass, datetime, array, base64, random
from SOAPpy import Types
soap = SOAPpy.WSDL.Proxy("https://engissues.digium.internal/jira/rpc/soap/jirasoapservice-v2?wsdl")
jirauser='rmeyerriecks@digium.com'
jirapass='tele.phony'

auth = soap.login(jirauser, jirapass)
#for x in soap.methods.keys():
#	print x
#getworklogs = soap.methods['getWorklogs']
#print getworklogs.inparams
#print getworklogs.inparams[1].name
#print soap.getWorklogs(auth, 'DAHDI-758')

#user = soap.getUser(auth, 'rmeyerriecks@digium.com')
#print user
#filters = soap.getSavedFilters(auth)
#print filters
issues = soap.getIssuesFromFilterWithLimit(auth, '10956', 0, 20)
#print issues
for issue in issues:
	print issue['key'], issue['summary']
