## Baka model add-ons

[Baka_model](https://github.com/suryakencana/baka_model) is add-ons baka framework built top of pyramid that provides an SQLAlchemy
declarative `Base` alias model.Model and a add method on `request.db`.

# Usage

You can use these as base classes for declarative model definitions, e.g.::

    from base_model.model import Model

    class MyModel(Model):
        """Example model class."""
        
        __tablename__ = 'base.mymodel'

        @classmethod
        def do_first(cls, session):
            instance = session.query(cls).first()

# Register Model

using baka_model, you can apply dependency injection method for model that has been created.

```
    def includeme(config):
        config.register_model('base.MyModel')
        
        
    # in view handler request
    @route('/my.model', renderer='json') 
    def view_mymodel(request):
        MyModel = request.find_model('base.mymodel')
        mymodel = MyModel()
        mymodel.name = 'user model'
        mymodel.address = 'user address'
        mymodel.phone = '0089800-998'
        request.db.add(mymodel)
        
        return {'success': True}
    
```