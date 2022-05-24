from utils.streamlit_utils import build_simple_line_chart, build_pie_chart
from utils.formatting import change_df_types, set_date_columns
from utils.coingecko import get_coin_market_cap
from services.lending import LendingMetrics
from utils.constants import DAI_DECIMALS
import streamlit as st
import pandas as pd


################
## Data Fetch ##
################

def get_lending_metrics():
    lending_metrics = LendingMetrics('makerdao-ethereum')
    lending_metrics.run_in_parallel()
    return lending_metrics


def get_financial_metrics(lending_metrics):
    financial_metrics_df = pd.DataFrame(lending_metrics.financial_metrics)
    financial_metrics_df = set_date_columns(financial_metrics_df)
    financial_metrics_df = change_df_types(financial_metrics_df,['totalValueLockedUSD','totalBorrowBalanceUSD','totalDepositBalanceUSD','dailyProtocolSideRevenueUSD','dailyTotalRevenueUSD','dailyDepositUSD','dailyBorrowUSD','dailyLiquidateUSD'],float)
    return financial_metrics_df

def get_usage_metrics(lending_metrics):
    usage_metrics_df = pd.DataFrame(lending_metrics.usage_metrics)
    usage_metrics_df = set_date_columns(usage_metrics_df)
    usage_metrics_df = change_df_types(usage_metrics_df,['dailyActiveUsers','dailyDepositCount','dailyWithdrawCount','dailyBorrowCount','dailyRepayCount','dailyLiquidateCount'],float)
    return usage_metrics_df

def get_markets(lending_metrics):
    markets_df = pd.json_normalize(lending_metrics.markets)
    markets_df = change_df_types(markets_df,['totalValueLockedUSD'],float)
    return markets_df
    
#################
## Chart build ##
#################

def build_tvl_fig(financial_metrics_df):
    fig = build_simple_line_chart(financial_metrics_df['date'],financial_metrics_df['totalValueLockedUSD'],'tvl','Makerdao TVL','Date','Total Value Locked')
    st.plotly_chart(fig, use_container_width=True)


def build_ratio_fig(financial_metrics_df):
    revenue_df = financial_metrics_df[['date','dailyProtocolSideRevenueUSD','dailyTotalRevenueUSD']]
    mcap_df = get_coin_market_cap('maker')
    revenue_df = revenue_df.merge(mcap_df, how='inner', on='date')
    revenue_df = revenue_df[(revenue_df['dailyProtocolSideRevenueUSD']>0) | (revenue_df['dailyTotalRevenueUSD']>0)]
    
    revenue_df['pe'] = revenue_df['mcap']/revenue_df['dailyProtocolSideRevenueUSD']
    revenue_df['ps'] = revenue_df['mcap']/revenue_df['dailyTotalRevenueUSD']
    #PS_DF = remove_outliers(PS_DF,'pe',.9)
    
    pe_fig = build_simple_line_chart(revenue_df['date'],revenue_df['pe'],'P/E','Makerdao P/E Ratio','Date','P/E Ratio')
    st.plotly_chart(pe_fig, use_container_width=True)
    
    ps_fig = build_simple_line_chart(revenue_df['date'],revenue_df['ps'],'P/S','Makerdao P/S Ratio','Date','P/S Ratio')
    st.plotly_chart(ps_fig, use_container_width=True)


def build_balance_figs(financial_metrics_df):
    borrow_fig = build_simple_line_chart(financial_metrics_df['date'],financial_metrics_df['totalBorrowBalanceUSD'],'Borrows','Makerdao Borrow Balance USD','Date','Total Borrow Balance')
    st.plotly_chart(borrow_fig, use_container_width=True)

    deposit_fig = build_simple_line_chart(financial_metrics_df['date'],financial_metrics_df['totalDepositBalanceUSD'],'Deposits','Makerdao Total Deposit Balance USD','Date','Total Deposit Balance')
    st.plotly_chart(deposit_fig, use_container_width=True)

def build_collat_ratio_fig(financial_metrics_df):
    sub_df = financial_metrics_df[financial_metrics_df['totalDepositBalanceUSD']>0]
    sub_df['collat_ratio'] = sub_df['totalBorrowBalanceUSD']/sub_df['totalDepositBalanceUSD']
    fig = build_simple_line_chart(sub_df['date'],sub_df['collat_ratio'],'ratio','Makerdao Total Collateralization Ratio','Date','Total Collateralization Ratio')
    st.plotly_chart(fig, use_container_width=True)

def build_total_loan_orig_fig(financial_metrics_df):
    fig = build_simple_line_chart(financial_metrics_df['date'],financial_metrics_df['cumulativeBorrowUSD'],'Cumulative Loans','Makerdao Total Loan Origination','Date','Total Loan Origination')
    st.plotly_chart(fig, use_container_width=True)

def build_daily_event_figs(financial_metrics_df):
    deposit_fig = build_simple_line_chart(financial_metrics_df['date'],financial_metrics_df['dailyDepositUSD'],'Deposits','Makerdao Daily Deposits USD','Date','Daily Deposits')
    st.plotly_chart(deposit_fig, use_container_width=True)
    
    borrow_fig = build_simple_line_chart(financial_metrics_df['date'],financial_metrics_df['dailyBorrowUSD'],'Borrows','Makerdao Daily Borrows USD','Date','Daily Borrows')
    st.plotly_chart(borrow_fig, use_container_width=True)

    liquidate_fig = build_simple_line_chart(financial_metrics_df['date'],financial_metrics_df['dailyLiquidateUSD'],'Liquidations','Makerdao Daily Liquidations USD','Date','Daily Liquidations')
    st.plotly_chart(liquidate_fig, use_container_width=True)

def build_daily_counts_figs(usage_metrics_df):
    deposit_fig = build_simple_line_chart(usage_metrics_df['date'],usage_metrics_df['dailyDepositCount'],'# txs','Makerdao Daily Deposit Counts','Date','Daily Deposit Transactions')
    st.plotly_chart(deposit_fig, use_container_width=True)

    withdraw_fig = build_simple_line_chart(usage_metrics_df['date'],usage_metrics_df['dailyWithdrawCount'],'# txs','Makerdao Daily Deposit Counts','Date','Daily Deposit Transactions')
    st.plotly_chart(withdraw_fig, use_container_width=True)

    borrow_fig = build_simple_line_chart(usage_metrics_df['date'],usage_metrics_df['dailyBorrowCount'],'# txs','Makerdao Daily Borrow Counts','Date','Daily Borrow Transactions')
    st.plotly_chart(borrow_fig, use_container_width=True)

    repay_fig = build_simple_line_chart(usage_metrics_df['date'],usage_metrics_df['dailyRepayCount'],'# txs','Makerdao Daily Deposit Counts','Date','Daily Repay Transactions')
    st.plotly_chart(repay_fig, use_container_width=True)

    liquidate_fig = build_simple_line_chart(usage_metrics_df['date'],usage_metrics_df['dailyLiquidateCount'],'# txs','Makerdao Daily Deposit Counts','Date','Daily Liquidation Transactions')
    st.plotly_chart(liquidate_fig, use_container_width=True)    
    

def build_markets_pie_chart(markets):
    top_10 = markets.sort_values(by='totalValueLockedUSD',ascending=False)[:10]
    top_10 = top_10.rename(columns={'totalValueLockedUSD':'Total Valued Locked USD', 'name':'Market'})
    fig = build_pie_chart(top_10,values = 'Total Valued Locked USD',names = 'Market',title = 'Makerdao Top 10 Markets by TVL')
    st.plotly_chart(fig)    

def build_tvl_by_assets_pie_chart(markets):
    assets_df = markets.copy()
    for i,row in assets_df.iterrows():
        if row['inputToken.name']=='Uniswap V2':
            assets_df.loc[i,'inputToken.symbol'] = row['name'].split('-')[0]
    assets_df = assets_df.groupby(['inputToken.id','inputToken.symbol'])['totalValueLockedUSD'].sum().reset_index()
    assets_df = assets_df[assets_df['totalValueLockedUSD']>=1.0]
    assets_df = assets_df.rename(columns={'totalValueLockedUSD':'Total Valued Locked USD', 'inputToken.symbol':'Token'})
    fig = build_pie_chart(assets_df, values = 'Total Valued Locked USD',names = 'Token',title = 'Makerdao TVL by Collateral Token')
    st.plotly_chart(fig,use_container_width=True)

    
#######################
## Protocol Specific ##
#######################

def build_dai_supply_fig(financial_metrics_df):
    financial_metrics_df['mintedTokenSupplies'] = financial_metrics_df['mintedTokenSupplies'].apply(lambda x: float(x[0])/DAI_DECIMALS)
    fig = build_simple_line_chart(financial_metrics_df['date'],financial_metrics_df['mintedTokenSupplies'],'Supply','Total Dai Supply','Date','Total Dai Supply')
    st.plotly_chart(fig, use_container_width=True)    

    

def main():
    lending_metrics = get_lending_metrics()
    financial_metrics = get_financial_metrics(lending_metrics)
    usage_metrics = get_usage_metrics(lending_metrics)
    markets = get_markets(lending_metrics)
    build_tvl_fig(financial_metrics),
    build_ratio_fig(financial_metrics)
    build_balance_figs(financial_metrics)
    build_collat_ratio_fig(financial_metrics)
    build_total_loan_orig_fig(financial_metrics)
    build_daily_event_figs(financial_metrics)
    build_daily_counts_figs(usage_metrics)
    build_dai_supply_fig(financial_metrics)
    build_markets_pie_chart(markets)
    build_tvl_by_assets_pie_chart(markets)

main()

# export PYTHONPATH="${PYTHONPATH}:/my/other/path"
# streamlit run makerdao.py