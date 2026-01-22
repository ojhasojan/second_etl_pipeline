import os
import pandas as pd
from sqlalchemy import create_engine
import psycopg2
from logger_config import logger

def main():
    logger.info('------'*200)
    logger.info('------'*200)
    logger.info('------'*200)
    logger.info("starting loading all csv file data")
    try:
        data_dir = 'data/'
        all_files = [
            os.path.join(data_dir,f)
            for f in os.listdir(data_dir)
            if f.endswith('.csv')
        ]
    except :
        logger.info("No files found ") 
        return   
        
    logger.info("ACCESSING EACH CSV FILE")
    df_list = []
    for file in all_files:
        try :
            temp_df = pd.read_csv(file)
            print("data loaded successfully from ", file)
            df_list.append(temp_df)    
        except:
            logger.info("error in loading data")    
       
    logger.info("Appending all data into single dataframe")        
    combined_df = pd.concat(df_list, ignore_index = True)   


    # clean data
    logger.info("cleaning process starts")
    logger.info("dropping customer_id and amount where data is missing")
    combined_df.dropna(subset = ['amount','customer_id'],inplace = True) 
            
    logger.info("changing data types of order_date as datetime")
    combined_df['order_date']= pd.to_datetime(combined_df['order_date'])  
            
            
    engine = create_engine("postgresql+psycopg2://demo_user:demo_pass@localhost:5432/weekly_salesdb")
    logger.info("created engine using psycopg2")
            
    combined_df.to_sql("landing_daily_sales", engine, if_exists="replace", index=False)
    logger.info("Data successfully loaded into Postgres table 'landing_daily_sales'.")


if __name__ == "__main__":
    main()
    



