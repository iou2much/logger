from mongoengine import *
 
class FuncModel(Document):
    name = StringField(max_length=50)
    mod_id = ObjectIdField()

    def __unicode__(self):
        return u'%s'%self.name
