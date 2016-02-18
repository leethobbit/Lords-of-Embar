from webapp2 import WSGIApplication


wsgi = WSGIApplication([], debug=True, config={
    'template_path': 'app/html'
})
