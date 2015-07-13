import web, urllib2, urllib, sys, json
import httplib2


def login(username, password, integratorKey):
	authenticateStr = "<DocuSignCredentials>" \
	                    "<Username>" + username + "</Username>" \
	                    "<Password>" + password + "</Password>" \
	                    "<IntegratorKey>" + integratorKey + "</IntegratorKey>" \
	                    "</DocuSignCredentials>";


	# Step 1 - Login
	url = 'https://demo.docusign.net/restapi/v2/login_information'   
	headers = {'X-DocuSign-Authentication': authenticateStr, 'Accept': 'application/json', 'Content-Type': 'application/json'}
	http = httplib2.Http()
	response, content = http.request(url, 'GET', headers=headers)
	 
	status = response.get('status');
	if (status != '200'): 
	    print("Error calling webservice, status is: %s" % status); sys.exit();
	 
	# get the baseUrl and accountId from the response body
	data = json.loads(content);
	loginInfo = data.get('loginAccounts');
	D = loginInfo[0];
	baseUrl = D['baseUrl'];
	accountId = D['accountId'];
	 
	#--- display results
	#print ("baseUrl = %s\naccountId = %s" % (baseUrl, accountId));  
	return   baseUrl, accountId, authenticateStr