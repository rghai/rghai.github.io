import web, urllib2, urllib, sys, json
import httplib2

def send(accountId, templateId, email, name, title, baseUrl, authenticateStr):
	#
	# STEP 2 - Create an Envelope with a Recipient and Send...
	#
	 
	#construct the body of the request in JSON format  
	requestBody = "{\"accountId\": \"" + accountId + "\"," + \
	                "\"status\": \"sent\"," + \
	                "\"emailSubject\": \"Attention: Signature required for NDA form\"," + \
	                "\"emailBlurb\": \"NDA form for Bike Room\"," + \
	                "\"templateId\": \"" + templateId + "\"," + \
	                "\"templateRoles\": [{" + \
	                "\"email\": \"" + email + "\"," + \
	                "\"name\": \"" + name + "\"," + \
	                "\"roleName\": \"Receiving Party\"," + \
	                "\"tabs\": {" + \
	                "\"textTabs\": [{" + \
	                "\"tabLabel\": \"TitleText\"," + \
	                "\"value\": \"" + title  + "\"}]}}]}";
	 
	# append "/envelopes" to baseURL and use in the request
	url = baseUrl + "/envelopes";
	headers = {'X-DocuSign-Authentication': authenticateStr, 'Accept': 'application/json'}
	http = httplib2.Http()
	response, content = http.request(url, 'POST', headers=headers, body=requestBody);
	status = response.get('status');
	if (status != '201'): 
	    print("Error calling webservice, status is: %s" % status); sys.exit();
	data = json.loads(content);
	envId = data.get('envelopeId');
	 
	#--- display results
	#print ("Signature request sent!  EnvelopeId is: %s\n" % envId);
	return envId

