# -*- coding: utf-8 -*-

from gluon.tools import Mail

# Index
def index():	
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html
    """
    response.flash = "Welcome to Gray Kool Aid, drink me! Everyone is."
    return dict(message=T('Gray Kool Aid is brought to you by Glen Baker - drink the kool aid!'))

# Old Graykoolaid.com
#def oldgray()
#	return dict()

#Blog
def blog():
	redirect(URL('http://graykoolaid.blogspot.com'))
	response.flash="And what would I blog about?"
	return dict()

# About Me
def about():
	return dict()

# Projects
def projects():
	response.flash="Current Project: iamsunmaid.com"
	return dict()

def next():
    return dict()
 
 
# Authentication
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())
  

# Download ?
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request,db)

# Access Services
def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

# return crud... Create, Read, Update, and Delete
@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())


