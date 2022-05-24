import logging
import os
# Operation generates valid queries, which can be printed out and properly indented.
# Bonus point is that it can be used to later interpret the JSON results into native Python objects.
from sgqlc.operation import Operation
from sgqlc.endpoint.http import HTTPEndpoint
from graphql_schemas import lending_schema
from utils.constants import ZERO_ADDRESS
from utils.concurrency import run_concurrency

# Read log level as environment variable (by default INFO)
LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
assert (LOGLEVEL in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']), 'LOGLEVEL is not valid'

# Configure logs format
logging.basicConfig(
    format='%(asctime)s [%(levelname)s] %(message)s',
    level=LOGLEVEL)


class ThegraphService(Exception):
    pass


class StatusEndpointUnavailableException(Exception):
    pass


class LendingMetrics:
    def __init__(self, subgraph_name: str, thegraph_api_url: str = 'https://api.thegraph.com/subgraphs/name/messari/'):
        self.subgraph_name = subgraph_name
        self.thegraph_api_url = thegraph_api_url
        
        self.usage_metrics = None
        self.markets = None
        self.financial_metrics = None
        #self.financials = self.fetch_daily_financials_snapshots()
        #self.usage_metrics = self.fetch_usage_metrics_daily_snapshots()
        #self.markets = self.fetch_markets()

    def call_endpoint(self,operation_definition):
        # Call the endpoint:
        headers = {}
        url = self.thegraph_api_url + self.subgraph_name
        endpoint = HTTPEndpoint(url, headers)

        try:
            subgraph_query_json = endpoint(operation_definition)
        except Exception:
            raise StatusEndpointUnavailableException()
        return subgraph_query_json
        
    def fetch_daily_financials_snapshots(self):
        """
        Get dailyFinancialsSnapshots
        :return: list[dict[json]]
        """
        # Operation module helps to create complex queries and interpret the JSON returned into native Python objects
        operation_definition = Operation(lending_schema.Query)
                
        # Important: we must select explicity which fields we want to request in our Graphql Query
        # In this case we select all possible fields
        omit_fields = ('protocol')
        query_fields = (x for x in lending_schema.FinancialsDailySnapshot.__field_names__ if x not in omit_fields)

        operation_definition.financials_daily_snapshots(first = 1000, order_by='id',order_direction='asc').__fields__(*query_fields)
        
        subgraph_query_json = self.call_endpoint(operation_definition)
        
        subgraph_result = (operation_definition + subgraph_query_json)
        
        if len(subgraph_query_json['data']['financialsDailySnapshots'])<1000:
            return subgraph_result

        while subgraph_query_json['data']['financialsDailySnapshots']:
            last_id = subgraph_result.financials_daily_snapshots[-1].id
            operation_definition = Operation(lending_schema.Query)
            operation_definition.financials_daily_snapshots(first = 1000, order_by='id',order_direction='asc',where={'id_gt':last_id}).__fields__(*query_fields)
            omit_fields = ('protocol')
            subgraph_query_json = self.call_endpoint(operation_definition)
            result = (operation_definition + subgraph_query_json)
            subgraph_result.financials_daily_snapshots.extend(result.financials_daily_snapshots)
        
        # INTERPRET RESULTS INTO NATIVE PYTHON OBJECTS
        # Since we don’t want to cobbler GraphQL fields, we cannot provide nicely named methods.
        # Then we use overloaded methods such as __iadd__, __add__ (`+` symbol), __bytes__(compressed GraphQL
        # representation) and __str__(indented GraphQL representation).
        #
        # A convenience is the `__add__()` (the symbol `+`) to apply the operation to a resulting JSON data,
        # interpreting the results and producing convenient objects
        subgraph_result = (operation_definition + subgraph_query_json)
        return subgraph_result
    
    def fetch_markets(self):
        # Operation module helps to create complex queries and interpret the JSON returned into native Python objects
        operation_definition = Operation(lending_schema.Query)

        query_fields = (str(lending_schema.Market.name),str(lending_schema.Market.total_value_locked_usd)) # str(lending_schema.Market.input_token)
        
        #query_fields = (x for x in lending_schema.Market.__field_names__ if x not in omit_fields)
        operation_definition.markets(first = 1000, order_by='id',order_direction='asc',where={'id_not':ZERO_ADDRESS}).__fields__(*query_fields)
        operation_definition.markets.input_token.__fields__()
        
        subgraph_query_json = self.call_endpoint(operation_definition)
        
        subgraph_result = (operation_definition + subgraph_query_json)
        
        return subgraph_result
    
    def fetch_usage_metrics_daily_snapshots(self):
        # Operation module helps to create complex queries and interpret the JSON returned into native Python objects
        operation_definition = Operation(lending_schema.Query)
        omit_fields = ('protocol')
        query_fields = (x for x in lending_schema.UsageMetricsDailySnapshot.__field_names__ if x not in omit_fields)

        operation_definition.usage_metrics_daily_snapshots(first = 1000, order_by='id',order_direction='asc').__fields__(*query_fields)
        
        subgraph_query_json = self.call_endpoint(operation_definition)
        subgraph_result = (operation_definition + subgraph_query_json)
        
        if len(subgraph_query_json['data']['usageMetricsDailySnapshots'])<1000:
            return subgraph_result

        while subgraph_query_json['data']['usageMetricsDailySnapshots']:
            last_id = subgraph_result.usage_metrics_daily_snapshots[-1].id
            operation_definition = Operation(lending_schema.Query)
            operation_definition.usage_metrics_daily_snapshots(first = 1000, order_by='id',order_direction='asc',where={'id_gt':last_id}).__fields__(*query_fields)
            omit_fields = ('protocol')
            subgraph_query_json = self.call_endpoint(operation_definition)
            result = (operation_definition + subgraph_query_json)
            subgraph_result.usage_metrics_daily_snapshots.extend(result.usage_metrics_daily_snapshots)
        
        # INTERPRET RESULTS INTO NATIVE PYTHON OBJECTS
        # Since we don’t want to cobbler GraphQL fields, we cannot provide nicely named methods.
        # Then we use overloaded methods such as __iadd__, __add__ (`+` symbol), __bytes__(compressed GraphQL
        # representation) and __str__(indented GraphQL representation).
        #
        # A convenience is the `__add__()` (the symbol `+`) to apply the operation to a resulting JSON data,
        # interpreting the results and producing convenient objects
        subgraph_result = (operation_definition + subgraph_query_json)
        
        return subgraph_result
        
    def run_in_parallel(self):
        subgraph_result = run_concurrency([self.fetch_usage_metrics_daily_snapshots, self.fetch_daily_financials_snapshots, self.fetch_markets])
        self.usage_metrics = [item.__dict__['__json_data__'] for item in subgraph_result[0].usage_metrics_daily_snapshots]
        self.financial_metrics = [item.__dict__['__json_data__'] for item in subgraph_result[1].financials_daily_snapshots]
        self.markets = [item.__dict__['__json_data__'] for item in subgraph_result[2].markets]

