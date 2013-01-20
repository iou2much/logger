from mongoengine import *
 
class ModuleModel(Document):
    name = StringField(max_length=50)
    sys_id = ObjectIdField()

    def __unicode__(self):
        return u'%s'%self.name
