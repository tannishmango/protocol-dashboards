
def remove_outliers(df, feature, iqr_size=.5):
    Q1= df[feature].quantile((1-iqr_size)/2)
    Q3 = df[feature].quantile(1-(1-iqr_size)/2)
    IQR = Q3 - Q1
    upper_limit = Q3 + 1.5 * IQR
    lower_limit = Q1 - 1.5 * IQR
    df = df[(df[feature]>lower_limit) & (df[feature]<upper_limit)]
    return df