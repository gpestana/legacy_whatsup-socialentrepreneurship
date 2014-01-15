from app import admin, db
from flask.ext.admin import Admin, BaseView, expose
from flask.ext.admin.contrib.sqla import ModelView
from app.models import Entry, Tag, EntriesTagsAssociation

class MyView(BaseView):
	@expose('/')
	def index(self):
		
		return self.render('index.html')


#admin.add_view(ModelView(Entry, db.session))
#admin.add_view(ModelView(Tag, db.session))
#admin.add_view(ModelView(EntriesTagsAssociation, db.session))

