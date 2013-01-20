from mongoengine import *
 
class LogModel(Document):
    mod_id = ObjectIdField()
    func_id = ObjectIdField()
    level = StringField(max_length=10)
    time = DateTimeField()
    #ip = StringField()
    detail = DictField()
    #rid = StringField(max_length=50)

    def __unicode__(self):
        return u'%s'%self.detail

    #def __dict__(self):
    #    return {'level':self.level,'time':self.time,'detail':self.detail}
