import web
import login
import send

username = "rapheepongghai@gmail.com";
password = "security";
integratorKey = "DEMO-449f6048-de78-4f5b-a375-d35f7f932760";
templateId = "06a8be28-e8a6-4f58-a116-ab20f1c867a8";



urls = (
  '/docusign', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        return render.input_form()

    def POST(self):
        form = web.input(name="Nobody", email="name@email.com", title="Superstar")

        name = "%s" % (form.name)
        email = "%s" % (form.email)
        title = "%s" % (form.title)

        baseUrl, accountId, authenticateStr = login.login(username, password, integratorKey)
        print ("baseUrl = %s\naccountId = %s" % (baseUrl, accountId));  
        envId = send.send(accountId, templateId, email, name, title, baseUrl, authenticateStr)
        print ("Signature request sent!  EnvelopeId is: %s\n" % envId);
     

        return render.index(name = name, email = email, title = title, envId = envId)


# email = "karanghai@gmail.com";
# name = "Karan Ghai";
# title = "Awesomeness";
# baseUrl, accountId, authenticateStr = login.login(username, password, integratorKey)
# print ("baseUrl = %s\naccountId = %s" % (baseUrl, accountId));  
# envId = send.send(accountId, templateId, email, name, title, baseUrl, authenticateStr)
# print ("Signature request sent!  EnvelopeId is: %s\n" % envId);




if __name__ == "__main__":
    app.run()