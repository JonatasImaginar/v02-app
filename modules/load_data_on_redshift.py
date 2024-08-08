import pandas as pd
import sqlalchemy as sa

def load_data_on_redshift(table_name, dataframe, engine_connection):
    
    # Load data on datawarehouse Amazon Redshift
    try:
        dataframe.reset_index(drop=True, inplace=True)
        dataframe.to_sql(
            table_name,
            engine_connection,
            index=False,
            if_exists='append',
        )
        
        print('Data loaded on Amazon Redshift')
        
    except sa.exc.SQLAlchemyError as e:
        print(f"Error occurred while loading the data: {e}")
        
    except Exception as e:
        print(e)
        
    finally:
        # Closing connection
        if hasattr(engine_connection, 'dispose'):
            engine_connection.dispose()
        print('Datawarehouse connection closed successfully')