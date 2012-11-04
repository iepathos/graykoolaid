# -*- coding:utf-8 -*-

def ask():
    form=SQLFORM.factory(
        Field('email',requires=IS_EMAIL()),
        Field('question',requires=IS_NOT_EMPTY()))
    if form.process().accepted:
        if mail.send(to='glen@graykoolaid.com',
                  subject='from %s' % form.vars.email,
                  message = form.vars.question):
            response.flash = 'Thank you'
            response.js = "jQuery('#%s').hide()" % request.cid
        else:
            form.errors.email = "Unable to send the email"
    return dict(form=form)