#!/usr/bin/python

import SOAPpy, getpass, datetime, array, base64, random, pprint
from types import *
from SOAPpy import Types
soap = SOAPpy.WSDL.Proxy("https://engissues.digium.internal/jira/rpc/soap/jirasoapservice-v2?wsdl")
jirauser='rmeyerriecks@digium.com'
jirapass='tele.phony'

auth = soap.login(jirauser, jirapass)

#user = soap.getUser(auth, 'rmeyerriecks@digium.com')
#print user
#filters = soap.getSavedFilters(auth)
#print filters
issues = soap.getIssuesFromFilterWithLimit(auth, '10956', 0, 20)
sprint = soap.getIssuesFromJqlSearch(auth, "project = DAHDI and fixVersion = \"Sprint 2010-11-11\"", 50)
#print issues
for issue in sprint:
	print issue['key'], issue['assignee'].rpartition('@')[0]
	worklog = soap.getWorklogs(auth, issue['key'])
	date = datetime.date(2010, 11, 11)
	if (worklog != []):
		for work in worklog:
			if ((datetime.date(work['updated'][0],work['updated'][1],work['updated'][2])) > date):
				date = datetime.date(work['updated'][0],work['updated'][1],work['updated'][2])
		print date
#	pprint.pprint(issue)
#	print issue['key'], issue['fixVersions'][0]['name']
