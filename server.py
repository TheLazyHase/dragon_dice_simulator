from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

if __name__ == '__main__':
    config = Configurator()

    #SQLAlchemy stuff
    from models import (
        DBSession,
        metadata
    )

    from sqlalchemy import create_engine
    import settings
    engine = create_engine('mysql+mysqldb://'+settings.user+':'+settings.db_password+'@'+settings.db_localhost+'/'+settings.db_name)
    DBSession.configure(bind=engine)
    metadata.bind = engine

    #Add route here
    config.add_route('army_creation', '/army/creation')

    #Scan for route
    config.scan('controller')

    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
