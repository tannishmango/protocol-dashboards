from datetime import datetime
from utils.constants import SECONDS_IN_DAY

def change_df_types(df, columns_to_change, type):
    for col in columns_to_change:
        df[col] = df[col].astype(type)
    return df

def set_date_columns(df):
    df['date'] = df['id'].apply(lambda x: datetime.utcfromtimestamp(int(x) * SECONDS_IN_DAY))
    return df