from mongoengine import *
 
class SystemModel(Document):
    #id  = ObjectIdField()
    name = StringField(max_length=50)
    desc = StringField(max_length=150)

    #def __id__(self):
    #    return u'%s'%self.id
    def __unicode__(self):
        return u'%s'%self.name
