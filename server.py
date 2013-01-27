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
    engine = create_engine('mysql+mysqldb://'+settings.db_user+':'+settings.db_password+'@'+settings.db_host+'/'+settings.db_name)
    DBSession.configure(bind=engine)
    metadata.bind = engine

    import models

    #Add route here
    config.add_route('army_selection', '/army/selection')
    config.add_route('army_creation', '/army/new', request_method="POST")
    config.add_route('army_edition', '/army/{id}', request_method="GET")
    config.add_route('army_edition_alias', '/army/edition', request_method="GET")
    config.add_route('do_army_edition', '/army/edition/{id}', request_method="POST")

    #Scan for route
    config.scan('controller')

    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
