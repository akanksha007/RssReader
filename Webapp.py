"""
This is the python backend processing file. It simply
contains one class Index
"""
import web
import IngiteRSS

urls = (
  '/', 'Index',
)

app = web.application(urls, globals())

render = web.template.render('templates/')
class Index(object):
    def GET(self):
        return render.index([])
    def POST(self):
    	# we take input from the form and parse the xml
    	# and according to the url return the list to the 
    	# interface
    	form = web.input(url='http://feeds.bbci.co.uk/news/rss.xml')
    	url = str(form.url)
    	alist = IngiteRSS.GetRSS(url)
    	return render.index(alist)


if __name__ == "__main__":
    app.run()
