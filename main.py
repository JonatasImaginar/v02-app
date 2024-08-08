import os
import pandas as pd
from dotenv import load_dotenv
from modules import config_api_parameters
from modules import get_data_from_api
from modules import DataConn
from modules import load_data_on_redshift

def main():
 
    load_dotenv()
    
    ### Extract
    
    # Load API Parameters
    config_api = {
        'start': config_api_parameters.start,
        'limit': config_api_parameters.limit,
        'key': config_api_parameters.api_key,
        'url': config_api_parameters.url,
        'currency': config_api_parameters.api_currency
    }
    
    # Extract data from API
    data = get_data_from_api(config_api)
    
    
    ### Transform
    
    # Create dataframe columns to structure data
    df_columns = [
        "name",
        "symbol",
        "data_added",
        "last_updated",
        "price",
        "volume_24h"
    ]
    
    # Create dataframe to structure data
    coins_df = pd.DataFrame(data, columns=df_columns)
    
    print("Data structured on dataframe")
    print(coins_df.head())
    
    
    ### Load
    
    # Redshift connection parameters
    user_credentials = {
        'redshift_user': os.getenv('REDSHIFT_USER'),
        'redshift_password': os.getenv('REDSHIFT_PASSWORD'),
        'redshift_host': os.getenv('REDSHIFT_HOST'),
        'redshift_port': os.getenv('REDSHIFT_PORT'),
        'redshift_db': os.getenv('REDSHIFT_DB'),
    }
    
    # Create engine connection
    engine = DataConn(user_credentials)
    
    # Load data on Redshift
    load_data_on_redshift('Coins', coins_df, engine)
    
if __name__ == "__main__":
    main()


