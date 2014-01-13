from wtforms import Form, TextField

class TestForm(Form):
	name = TextField('name')