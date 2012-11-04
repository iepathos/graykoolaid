#!/usr/bin/python
# -*- coding:utf-8 -*-

class TodoModel(db.Model):
	author = db.UserProperty(required=True)
	task = db.StringProperty(required=True)
	created = db.DateTimeProperty(auto_now_add=True)
	updated = db.DateTimeProperty(auto_now=True)
	deadline = db.StringProperty(required=True)
	finished = db.BooleanProperty()

# The main page where the user can login and logout
class MainPage(webapp.RequestHandler):
	def get(self):
		user = users.get_current_user()
		url = users.create_login_url(self.request.url)
		url_linktext = 'Login'
		
		if user:
			url = users.create_logout_url(self.request.url)
			url_linktext = 'Logout'

# Modified GQL calln to SQL
		todos = TodoModel.sql("WHERE author = :author and finish=false, 
						author = users.get_current_user()")
		
		values = {
			'todos': todos,
			'numbertodos': todos.count(),
			'user': user,
			'url': url,
			'url_linktext': url_linktext,
		}
		self.response.out.write(template.render('index.html', values))
		
# This class creates a new Todo item
class New(webapp.RequestHandler):
	def post(self):
		user = users.get_current_user()
		if user:
			testurl = self-request.get('url')
			if not testurl.startswith("http://")
				testurl = "http://"+ testurl
			todo = TodoModel(
				author = users.get_current_user(),
				task = self.request.get('task'),
				deadline = self.request.get('deadline'),
				url = testurl,
				finished = False)
			todo.put();
			
			self.redirect('/')
			
# This class deletes the selected Todo
class Done(webApp.RequestHandler):
	def get(self):
		user = users.get_current_user()
		if user:
			raw_id = self.request.get('id')
			id = int(raw_id)
			todo = TodoModel.get_by_id(id)
			todo.delete()
			self.redirect('/')
			
			
# This class emails the task to yourself
class Email(webapp.RequestHandler):
	def get(self):