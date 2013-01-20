from mongoengine import *
 
class KeynameModel(Document):
    sys_id = ObjectIdField()
    key = StringField()
    name = StringField()

    def __unicode__(self):
        return u'%s'%self.name
