#!/usr/bin/python
# coding=utf-8
import web
import sys
import urllib2
reload(sys)
import json
sys.setdefaultencoding('utf8')
web.config.debug = True


id_redic="https://github.com/login/oauth/authorize?client_id=19f2e6d6a157b86e559e&redirect_uri=http://0.0.0.0:8080/login"

db = web.database(dbn='postgres', user="d0ggy", pw="123", db="webpy_login")
render = web.template.render('templates/')
urls = (
	'/', 'index',
    '/login', 'login',
    '/register','register',
    '/redirect', 'redirect'
)

class index:
    def GET(self):
        return render.index()

def userName(url):
    response = urllib2.Request(url)
    request = urllib2.urlopen(response)
    return request.read()


class login:
    def GET(self):
        i = web.input()
        #print(type(i.code))
        had_code= "https://github.com/login/oauth/access_token?client_id=19f2e6d6a157b86e559e&code="+i.code+"&client_secret=e4cfde3c50cac6a5ef4a0dea81a2a71126860535&redirect_uri=http://192.168.0.128:8080/login"
        #return had_code
        #print(i.code)
        #raise web.seeother(had_code)
        tokenReq = userName(had_code)
        #print tokenReq
        #return tokenReq
        had_token = "https://api.github.com/user?"+tokenReq
        #raise web.seeother(had_token)
        userInfomation = userName(had_token)
        #print type(userInfomation)
        #print userInfomation[2]
        #raise web.seeother(userInfomation)
        #print type(userInfomation)
        #return userInfomation

        params = json.loads(userInfomation)
        return "username = "+params["login"],"email = "+params["email"]

'''
class add:
	def POST(self):
		i = web.input()
		n = db.insert('todo', title=i.title)
		raise web.seeother('/')
'''
app = web.application(urls, globals())
if __name__ == '__main__':
    app.run()