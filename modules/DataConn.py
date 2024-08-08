import sqlalchemy as sa
import pandas as pd


def DataConn(user_credentials):
    
    user = user_credentials.redshift_user
    password = user_credentials.redshift_password
    host = user_credentials.redshift_host
    port = user_credentials.redshift_port
    database = user_credentials.redshift_db
    
    connection_url = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
    
    try:
        engine = sa.create_engine(connection_url)
    except sa.exc.SQLAlchemyError as e:
        print(f"Failed to create connection: {e}")
        
    return engine