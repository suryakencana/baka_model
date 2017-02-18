## Baka model add-ons

[Baka_model][] is add-ons baka framework built top of pyramid that provides an SQLAlchemy
declarative `Base` alias model.Model and a add method on `request.db`.

# Usage

You can use these as base classes for declarative model definitions, e.g.::

    from base_model.model import Model

    class MyModel(Model):
        """Example model class."""

        @classmethod
        def do_first(cls, session):
            instance = session.query(cls).first()
            
