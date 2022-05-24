import sgqlc.types


subgraph_status_schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
class Account_orderBy(sgqlc.types.Enum):
    __schema__ = subgraph_status_schema
    __choices__ = ('id',)


class ActiveAccount_orderBy(sgqlc.types.Enum):
    __schema__ = subgraph_status_schema
    __choices__ = ('id',)


class BigDecimal(sgqlc.types.Scalar):
    __schema__ = subgraph_status_schema


class BigInt(sgqlc.types.Scalar):
    __schema__ = subgraph_status_schema


Boolean = sgqlc.types.Boolean

class Borrow_orderBy(sgqlc.types.Enum):
    __schema__ = subgraph_status_schema
    __choices__ = ('amount', 'amountUSD', 'asset', 'blockNumber', 'from', 'hash', 'id', 'logIndex', 'market', 'protocol', 'timestamp', 'to')


class Bytes(sgqlc.types.Scalar):
    __schema__ = subgraph_status_schema


class Deposit_orderBy(sgqlc.types.Enum):
    __schema__ = subgraph_status_schema
    __choices__ = ('amount', 'amountUSD', 'asset', 'blockNumber', 'from', 'hash', 'id', 'logIndex', 'market', 'protocol', 'timestamp', 'to')


class Event_orderBy(sgqlc.types.Enum):
    __schema__ = subgraph_status_schema
    __choices__ = ('blockNumber', 'from', 'hash', 'id', 'logIndex', 'protocol', 'timestamp', 'to')


class FinancialsDailySnapshot_orderBy(sgqlc.types.Enum):
    __schema__ = subgraph_status_schema
    __choices__ = ('blockNumber', 'cumulativeBorrowUSD', 'cumulativeDepositUSD', 'cumulativeLiquidateUSD', 'cumulativeProtocolSideRevenueUSD', 'cumulativeSupplySideRevenueUSD', 'cumulativeTotalRevenueUSD', 'dailyBorrowUSD', 'dailyDepositUSD', 'dailyLiquidateUSD', 'dailyProtocolSideRevenueUSD', 'dailySupplySideRevenueUSD', 'dailyTotalRevenueUSD', 'id', 'mintedTokenSupplies', 'protocol', 'protocolControlledValueUSD', 'timestamp', 'totalBorrowBalanceUSD', 'totalDepositBalanceUSD', 'totalValueLockedUSD')


Float = sgqlc.types.Float

ID = sgqlc.types.ID

Int = sgqlc.types.Int

class InterestRateSide(sgqlc.types.Enum):
    __schema__ = subgraph_status_schema
    __choices__ = ('BORROWER', 'LENDER')


class InterestRateType(sgqlc.types.Enum):
    __schema__ = subgraph_status_schema
    __choices__ = ('FIXED_TERM', 'STABLE', 'VARIABLE')


class InterestRate_orderBy(sgqlc.types.Enum):
    __schema__ = subgraph_status_schema
    __choices__ = ('duration', 'id', 'maturityBlock', 'rate', 'side', 'type')


class LendingProtocol_orderBy(sgqlc.types.Enum):
    __schema__ = subgraph_status_schema
    __choices__ = ('cumulativeBorrowUSD', 'cumulativeDepositUSD', 'cumulativeLiquidateUSD', 'cumulativeProtocolSideRevenueUSD', 'cumulativeSupplySideRevenueUSD', 'cumulativeTotalRevenueUSD', 'cumulativeUniqueUsers', 'dailyUsageMetrics', 'financialMetrics', 'hourlyUsageMetrics', 'id', 'lendingType', 'markets', 'methodologyVersion', 'mintedTokenSupplies', 'mintedTokens', 'name', 'network', 'protocolControlledValueUSD', 'riskType', 'schemaVersion', 'slug', 'subgraphVersion', 'totalBorrowBalanceUSD', 'totalDepositBalanceUSD', 'totalValueLockedUSD', 'type')


class LendingType(sgqlc.types.Enum):
    __schema__ = subgraph_status_schema
    __choices__ = ('CDP', 'POOLED')


class Liquidate_orderBy(sgqlc.types.Enum):
    __schema__ = subgraph_status_schema
    __choices__ = ('amount', 'amountUSD', 'asset', 'blockNumber', 'from', 'hash', 'id', 'logIndex', 'market', 'profitUSD', 'protocol', 'timestamp', 'to')


class MarketDailySnapshot_orderBy(sgqlc.types.Enum):
    __schema__ = subgraph_status_schema
    __choices__ = ('blockNumber', 'cumulativeBorrowUSD', 'cumulativeDepositUSD', 'cumulativeLiquidateUSD', 'dailyBorrowUSD', 'dailyDepositUSD', 'dailyLiquidateUSD', 'exchangeRate', 'id', 'inputTokenBalance', 'inputTokenPriceUSD', 'market', 'outputTokenPriceUSD', 'outputTokenSupply', 'protocol', 'rates', 'rewardTokenEmissionsAmount', 'rewardTokenEmissionsUSD', 'timestamp', 'totalBorrowBalanceUSD', 'totalDepositBalanceUSD', 'totalValueLockedUSD')


class MarketHourlySnapshot_orderBy(sgqlc.types.Enum):
    __schema__ = subgraph_status_schema
    __choices__ = ('blockNumber', 'cumulativeBorrowUSD', 'cumulativeDepositUSD', 'cumulativeLiquidateUSD', 'exchangeRate', 'hourlyBorrowUSD', 'hourlyDepositUSD', 'hourlyLiquidateUSD', 'id', 'inputTokenBalance', 'inputTokenPriceUSD', 'market', 'outputTokenPriceUSD', 'outputTokenSupply', 'protocol', 'rates', 'rewardTokenEmissionsAmount', 'rewardTokenEmissionsUSD', 'timestamp', 'totalBorrowBalanceUSD', 'totalDepositBalanceUSD', 'totalValueLockedUSD')


class Market_orderBy(sgqlc.types.Enum):
    __schema__ = subgraph_status_schema
    __choices__ = ('borrows', 'canBorrowFrom', 'canUseAsCollateral', 'createdBlockNumber', 'createdTimestamp', 'cumulativeBorrowUSD', 'cumulativeDepositUSD', 'cumulativeLiquidateUSD', 'dailySnapshots', 'deposits', 'exchangeRate', 'hourlySnapshots', 'id', 'inputToken', 'inputTokenBalance', 'inputTokenPriceUSD', 'isActive', 'liquidates', 'liquidationPenalty', 'liquidationThreshold', 'maximumLTV', 'name', 'outputToken', 'outputTokenPriceUSD', 'outputTokenSupply', 'protocol', 'rates', 'repays', 'rewardTokenEmissionsAmount', 'rewardTokenEmissionsUSD', 'rewardTokens', 'totalBorrowBalanceUSD', 'totalDepositBalanceUSD', 'totalValueLockedUSD', 'withdraws')


class Network(sgqlc.types.Enum):
    __schema__ = subgraph_status_schema
    __choices__ = ('ARBITRUM_ONE', 'AURORA', 'AVALANCHE', 'BSC', 'CELO', 'FANTOM', 'FUSE', 'MAINNET', 'MATIC', 'MOONBEAM', 'MOONRIVER', 'NEAR_MAINNET', 'OPTIMISM', 'XDAI')


class OrderDirection(sgqlc.types.Enum):
    __schema__ = subgraph_status_schema
    __choices__ = ('asc', 'desc')


class ProtocolType(sgqlc.types.Enum):
    __schema__ = subgraph_status_schema
    __choices__ = ('BRIDGE', 'EXCHANGE', 'GENERIC', 'LENDING', 'YIELD')


class Protocol_orderBy(sgqlc.types.Enum):
    __schema__ = subgraph_status_schema
    __choices__ = ('cumulativeProtocolSideRevenueUSD', 'cumulativeSupplySideRevenueUSD', 'cumulativeTotalRevenueUSD', 'cumulativeUniqueUsers', 'dailyUsageMetrics', 'financialMetrics', 'hourlyUsageMetrics', 'id', 'methodologyVersion', 'name', 'network', 'protocolControlledValueUSD', 'schemaVersion', 'slug', 'subgraphVersion', 'totalValueLockedUSD', 'type')


class Repay_orderBy(sgqlc.types.Enum):
    __schema__ = subgraph_status_schema
    __choices__ = ('amount', 'amountUSD', 'asset', 'blockNumber', 'from', 'hash', 'id', 'logIndex', 'market', 'protocol', 'timestamp', 'to')


class RewardTokenType(sgqlc.types.Enum):
    __schema__ = subgraph_status_schema
    __choices__ = ('BORROW', 'DEPOSIT')


class RewardToken_orderBy(sgqlc.types.Enum):
    __schema__ = subgraph_status_schema
    __choices__ = ('id', 'token', 'type')


class RiskType(sgqlc.types.Enum):
    __schema__ = subgraph_status_schema
    __choices__ = ('GLOBAL', 'ISOLATED')


String = sgqlc.types.String

class Token_orderBy(sgqlc.types.Enum):
    __schema__ = subgraph_status_schema
    __choices__ = ('decimals', 'id', 'lastPriceBlockNumber', 'lastPriceUSD', 'name', 'symbol')


class UsageMetricsDailySnapshot_orderBy(sgqlc.types.Enum):
    __schema__ = subgraph_status_schema
    __choices__ = ('blockNumber', 'cumulativeUniqueUsers', 'dailyActiveUsers', 'dailyBorrowCount', 'dailyDepositCount', 'dailyLiquidateCount', 'dailyRepayCount', 'dailyTransactionCount', 'dailyWithdrawCount', 'id', 'protocol', 'timestamp')


class UsageMetricsHourlySnapshot_orderBy(sgqlc.types.Enum):
    __schema__ = subgraph_status_schema
    __choices__ = ('blockNumber', 'cumulativeUniqueUsers', 'hourlyActiveUsers', 'hourlyBorrowCount', 'hourlyDepositCount', 'hourlyLiquidateCount', 'hourlyRepayCount', 'hourlyTransactionCount', 'hourlyWithdrawCount', 'id', 'protocol', 'timestamp')


class Withdraw_orderBy(sgqlc.types.Enum):
    __schema__ = subgraph_status_schema
    __choices__ = ('amount', 'amountUSD', 'asset', 'blockNumber', 'from', 'hash', 'id', 'logIndex', 'market', 'protocol', 'timestamp', 'to')


class _SubgraphErrorPolicy_(sgqlc.types.Enum):
    __schema__ = subgraph_status_schema
    __choices__ = ('allow', 'deny')



########################################################################
# Input Objects
########################################################################
class Account_filter(sgqlc.types.Input):
    __schema__ = subgraph_status_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    _change_block = sgqlc.types.Field('BlockChangedFilter', graphql_name='_change_block')


class ActiveAccount_filter(sgqlc.types.Input):
    __schema__ = subgraph_status_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    _change_block = sgqlc.types.Field('BlockChangedFilter', graphql_name='_change_block')


class BlockChangedFilter(sgqlc.types.Input):
    __schema__ = subgraph_status_schema
    __field_names__ = ('number_gte',)
    number_gte = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number_gte')


class Block_height(sgqlc.types.Input):
    __schema__ = subgraph_status_schema
    __field_names__ = ('hash', 'number', 'number_gte')
    hash = sgqlc.types.Field(Bytes, graphql_name='hash')
    number = sgqlc.types.Field(Int, graphql_name='number')
    number_gte = sgqlc.types.Field(Int, graphql_name='number_gte')


class Borrow_filter(sgqlc.types.Input):
    __schema__ = subgraph_status_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'hash', 'hash_not', 'hash_gt', 'hash_lt', 'hash_gte', 'hash_lte', 'hash_in', 'hash_not_in', 'hash_contains', 'hash_contains_nocase', 'hash_not_contains', 'hash_not_contains_nocase', 'hash_starts_with', 'hash_starts_with_nocase', 'hash_not_starts_with', 'hash_not_starts_with_nocase', 'hash_ends_with', 'hash_ends_with_nocase', 'hash_not_ends_with', 'hash_not_ends_with_nocase', 'log_index', 'log_index_not', 'log_index_gt', 'log_index_lt', 'log_index_gte', 'log_index_lte', 'log_index_in', 'log_index_not_in', 'protocol', 'protocol_not', 'protocol_gt', 'protocol_lt', 'protocol_gte', 'protocol_lte', 'protocol_in', 'protocol_not_in', 'protocol_contains', 'protocol_contains_nocase', 'protocol_not_contains', 'protocol_not_contains_nocase', 'protocol_starts_with', 'protocol_starts_with_nocase', 'protocol_not_starts_with', 'protocol_not_starts_with_nocase', 'protocol_ends_with', 'protocol_ends_with_nocase', 'protocol_not_ends_with', 'protocol_not_ends_with_nocase', 'to', 'to_not', 'to_gt', 'to_lt', 'to_gte', 'to_lte', 'to_in', 'to_not_in', 'to_contains', 'to_contains_nocase', 'to_not_contains', 'to_not_contains_nocase', 'to_starts_with', 'to_starts_with_nocase', 'to_not_starts_with', 'to_not_starts_with_nocase', 'to_ends_with', 'to_ends_with_nocase', 'to_not_ends_with', 'to_not_ends_with_nocase', 'from_', 'from_not', 'from_gt', 'from_lt', 'from_gte', 'from_lte', 'from_in', 'from_not_in', 'from_contains', 'from_contains_nocase', 'from_not_contains', 'from_not_contains_nocase', 'from_starts_with', 'from_starts_with_nocase', 'from_not_starts_with', 'from_not_starts_with_nocase', 'from_ends_with', 'from_ends_with_nocase', 'from_not_ends_with', 'from_not_ends_with_nocase', 'block_number', 'block_number_not', 'block_number_gt', 'block_number_lt', 'block_number_gte', 'block_number_lte', 'block_number_in', 'block_number_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'market', 'market_not', 'market_gt', 'market_lt', 'market_gte', 'market_lte', 'market_in', 'market_not_in', 'market_contains', 'market_contains_nocase', 'market_not_contains', 'market_not_contains_nocase', 'market_starts_with', 'market_starts_with_nocase', 'market_not_starts_with', 'market_not_starts_with_nocase', 'market_ends_with', 'market_ends_with_nocase', 'market_not_ends_with', 'market_not_ends_with_nocase', 'asset', 'asset_not', 'asset_gt', 'asset_lt', 'asset_gte', 'asset_lte', 'asset_in', 'asset_not_in', 'asset_contains', 'asset_contains_nocase', 'asset_not_contains', 'asset_not_contains_nocase', 'asset_starts_with', 'asset_starts_with_nocase', 'asset_not_starts_with', 'asset_not_starts_with_nocase', 'asset_ends_with', 'asset_ends_with_nocase', 'asset_not_ends_with', 'asset_not_ends_with_nocase', 'amount', 'amount_not', 'amount_gt', 'amount_lt', 'amount_gte', 'amount_lte', 'amount_in', 'amount_not_in', 'amount_usd', 'amount_usd_not', 'amount_usd_gt', 'amount_usd_lt', 'amount_usd_gte', 'amount_usd_lte', 'amount_usd_in', 'amount_usd_not_in', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    hash_not = sgqlc.types.Field(String, graphql_name='hash_not')
    hash_gt = sgqlc.types.Field(String, graphql_name='hash_gt')
    hash_lt = sgqlc.types.Field(String, graphql_name='hash_lt')
    hash_gte = sgqlc.types.Field(String, graphql_name='hash_gte')
    hash_lte = sgqlc.types.Field(String, graphql_name='hash_lte')
    hash_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='hash_in')
    hash_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='hash_not_in')
    hash_contains = sgqlc.types.Field(String, graphql_name='hash_contains')
    hash_contains_nocase = sgqlc.types.Field(String, graphql_name='hash_contains_nocase')
    hash_not_contains = sgqlc.types.Field(String, graphql_name='hash_not_contains')
    hash_not_contains_nocase = sgqlc.types.Field(String, graphql_name='hash_not_contains_nocase')
    hash_starts_with = sgqlc.types.Field(String, graphql_name='hash_starts_with')
    hash_starts_with_nocase = sgqlc.types.Field(String, graphql_name='hash_starts_with_nocase')
    hash_not_starts_with = sgqlc.types.Field(String, graphql_name='hash_not_starts_with')
    hash_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='hash_not_starts_with_nocase')
    hash_ends_with = sgqlc.types.Field(String, graphql_name='hash_ends_with')
    hash_ends_with_nocase = sgqlc.types.Field(String, graphql_name='hash_ends_with_nocase')
    hash_not_ends_with = sgqlc.types.Field(String, graphql_name='hash_not_ends_with')
    hash_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='hash_not_ends_with_nocase')
    log_index = sgqlc.types.Field(Int, graphql_name='logIndex')
    log_index_not = sgqlc.types.Field(Int, graphql_name='logIndex_not')
    log_index_gt = sgqlc.types.Field(Int, graphql_name='logIndex_gt')
    log_index_lt = sgqlc.types.Field(Int, graphql_name='logIndex_lt')
    log_index_gte = sgqlc.types.Field(Int, graphql_name='logIndex_gte')
    log_index_lte = sgqlc.types.Field(Int, graphql_name='logIndex_lte')
    log_index_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='logIndex_in')
    log_index_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='logIndex_not_in')
    protocol = sgqlc.types.Field(String, graphql_name='protocol')
    protocol_not = sgqlc.types.Field(String, graphql_name='protocol_not')
    protocol_gt = sgqlc.types.Field(String, graphql_name='protocol_gt')
    protocol_lt = sgqlc.types.Field(String, graphql_name='protocol_lt')
    protocol_gte = sgqlc.types.Field(String, graphql_name='protocol_gte')
    protocol_lte = sgqlc.types.Field(String, graphql_name='protocol_lte')
    protocol_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_in')
    protocol_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_not_in')
    protocol_contains = sgqlc.types.Field(String, graphql_name='protocol_contains')
    protocol_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_contains_nocase')
    protocol_not_contains = sgqlc.types.Field(String, graphql_name='protocol_not_contains')
    protocol_not_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_contains_nocase')
    protocol_starts_with = sgqlc.types.Field(String, graphql_name='protocol_starts_with')
    protocol_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_starts_with_nocase')
    protocol_not_starts_with = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with')
    protocol_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with_nocase')
    protocol_ends_with = sgqlc.types.Field(String, graphql_name='protocol_ends_with')
    protocol_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_ends_with_nocase')
    protocol_not_ends_with = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with')
    protocol_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with_nocase')
    to = sgqlc.types.Field(String, graphql_name='to')
    to_not = sgqlc.types.Field(String, graphql_name='to_not')
    to_gt = sgqlc.types.Field(String, graphql_name='to_gt')
    to_lt = sgqlc.types.Field(String, graphql_name='to_lt')
    to_gte = sgqlc.types.Field(String, graphql_name='to_gte')
    to_lte = sgqlc.types.Field(String, graphql_name='to_lte')
    to_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='to_in')
    to_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='to_not_in')
    to_contains = sgqlc.types.Field(String, graphql_name='to_contains')
    to_contains_nocase = sgqlc.types.Field(String, graphql_name='to_contains_nocase')
    to_not_contains = sgqlc.types.Field(String, graphql_name='to_not_contains')
    to_not_contains_nocase = sgqlc.types.Field(String, graphql_name='to_not_contains_nocase')
    to_starts_with = sgqlc.types.Field(String, graphql_name='to_starts_with')
    to_starts_with_nocase = sgqlc.types.Field(String, graphql_name='to_starts_with_nocase')
    to_not_starts_with = sgqlc.types.Field(String, graphql_name='to_not_starts_with')
    to_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='to_not_starts_with_nocase')
    to_ends_with = sgqlc.types.Field(String, graphql_name='to_ends_with')
    to_ends_with_nocase = sgqlc.types.Field(String, graphql_name='to_ends_with_nocase')
    to_not_ends_with = sgqlc.types.Field(String, graphql_name='to_not_ends_with')
    to_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='to_not_ends_with_nocase')
    from_ = sgqlc.types.Field(String, graphql_name='from')
    from_not = sgqlc.types.Field(String, graphql_name='from_not')
    from_gt = sgqlc.types.Field(String, graphql_name='from_gt')
    from_lt = sgqlc.types.Field(String, graphql_name='from_lt')
    from_gte = sgqlc.types.Field(String, graphql_name='from_gte')
    from_lte = sgqlc.types.Field(String, graphql_name='from_lte')
    from_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='from_in')
    from_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='from_not_in')
    from_contains = sgqlc.types.Field(String, graphql_name='from_contains')
    from_contains_nocase = sgqlc.types.Field(String, graphql_name='from_contains_nocase')
    from_not_contains = sgqlc.types.Field(String, graphql_name='from_not_contains')
    from_not_contains_nocase = sgqlc.types.Field(String, graphql_name='from_not_contains_nocase')
    from_starts_with = sgqlc.types.Field(String, graphql_name='from_starts_with')
    from_starts_with_nocase = sgqlc.types.Field(String, graphql_name='from_starts_with_nocase')
    from_not_starts_with = sgqlc.types.Field(String, graphql_name='from_not_starts_with')
    from_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='from_not_starts_with_nocase')
    from_ends_with = sgqlc.types.Field(String, graphql_name='from_ends_with')
    from_ends_with_nocase = sgqlc.types.Field(String, graphql_name='from_ends_with_nocase')
    from_not_ends_with = sgqlc.types.Field(String, graphql_name='from_not_ends_with')
    from_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='from_not_ends_with_nocase')
    block_number = sgqlc.types.Field(BigInt, graphql_name='blockNumber')
    block_number_not = sgqlc.types.Field(BigInt, graphql_name='blockNumber_not')
    block_number_gt = sgqlc.types.Field(BigInt, graphql_name='blockNumber_gt')
    block_number_lt = sgqlc.types.Field(BigInt, graphql_name='blockNumber_lt')
    block_number_gte = sgqlc.types.Field(BigInt, graphql_name='blockNumber_gte')
    block_number_lte = sgqlc.types.Field(BigInt, graphql_name='blockNumber_lte')
    block_number_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='blockNumber_in')
    block_number_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='blockNumber_not_in')
    timestamp = sgqlc.types.Field(BigInt, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_not_in')
    market = sgqlc.types.Field(String, graphql_name='market')
    market_not = sgqlc.types.Field(String, graphql_name='market_not')
    market_gt = sgqlc.types.Field(String, graphql_name='market_gt')
    market_lt = sgqlc.types.Field(String, graphql_name='market_lt')
    market_gte = sgqlc.types.Field(String, graphql_name='market_gte')
    market_lte = sgqlc.types.Field(String, graphql_name='market_lte')
    market_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='market_in')
    market_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='market_not_in')
    market_contains = sgqlc.types.Field(String, graphql_name='market_contains')
    market_contains_nocase = sgqlc.types.Field(String, graphql_name='market_contains_nocase')
    market_not_contains = sgqlc.types.Field(String, graphql_name='market_not_contains')
    market_not_contains_nocase = sgqlc.types.Field(String, graphql_name='market_not_contains_nocase')
    market_starts_with = sgqlc.types.Field(String, graphql_name='market_starts_with')
    market_starts_with_nocase = sgqlc.types.Field(String, graphql_name='market_starts_with_nocase')
    market_not_starts_with = sgqlc.types.Field(String, graphql_name='market_not_starts_with')
    market_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='market_not_starts_with_nocase')
    market_ends_with = sgqlc.types.Field(String, graphql_name='market_ends_with')
    market_ends_with_nocase = sgqlc.types.Field(String, graphql_name='market_ends_with_nocase')
    market_not_ends_with = sgqlc.types.Field(String, graphql_name='market_not_ends_with')
    market_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='market_not_ends_with_nocase')
    asset = sgqlc.types.Field(String, graphql_name='asset')
    asset_not = sgqlc.types.Field(String, graphql_name='asset_not')
    asset_gt = sgqlc.types.Field(String, graphql_name='asset_gt')
    asset_lt = sgqlc.types.Field(String, graphql_name='asset_lt')
    asset_gte = sgqlc.types.Field(String, graphql_name='asset_gte')
    asset_lte = sgqlc.types.Field(String, graphql_name='asset_lte')
    asset_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='asset_in')
    asset_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='asset_not_in')
    asset_contains = sgqlc.types.Field(String, graphql_name='asset_contains')
    asset_contains_nocase = sgqlc.types.Field(String, graphql_name='asset_contains_nocase')
    asset_not_contains = sgqlc.types.Field(String, graphql_name='asset_not_contains')
    asset_not_contains_nocase = sgqlc.types.Field(String, graphql_name='asset_not_contains_nocase')
    asset_starts_with = sgqlc.types.Field(String, graphql_name='asset_starts_with')
    asset_starts_with_nocase = sgqlc.types.Field(String, graphql_name='asset_starts_with_nocase')
    asset_not_starts_with = sgqlc.types.Field(String, graphql_name='asset_not_starts_with')
    asset_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='asset_not_starts_with_nocase')
    asset_ends_with = sgqlc.types.Field(String, graphql_name='asset_ends_with')
    asset_ends_with_nocase = sgqlc.types.Field(String, graphql_name='asset_ends_with_nocase')
    asset_not_ends_with = sgqlc.types.Field(String, graphql_name='asset_not_ends_with')
    asset_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='asset_not_ends_with_nocase')
    amount = sgqlc.types.Field(BigInt, graphql_name='amount')
    amount_not = sgqlc.types.Field(BigInt, graphql_name='amount_not')
    amount_gt = sgqlc.types.Field(BigInt, graphql_name='amount_gt')
    amount_lt = sgqlc.types.Field(BigInt, graphql_name='amount_lt')
    amount_gte = sgqlc.types.Field(BigInt, graphql_name='amount_gte')
    amount_lte = sgqlc.types.Field(BigInt, graphql_name='amount_lte')
    amount_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='amount_in')
    amount_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='amount_not_in')
    amount_usd = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD')
    amount_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_not')
    amount_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_gt')
    amount_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_lt')
    amount_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_gte')
    amount_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_lte')
    amount_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amountUSD_in')
    amount_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amountUSD_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class Deposit_filter(sgqlc.types.Input):
    __schema__ = subgraph_status_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'hash', 'hash_not', 'hash_gt', 'hash_lt', 'hash_gte', 'hash_lte', 'hash_in', 'hash_not_in', 'hash_contains', 'hash_contains_nocase', 'hash_not_contains', 'hash_not_contains_nocase', 'hash_starts_with', 'hash_starts_with_nocase', 'hash_not_starts_with', 'hash_not_starts_with_nocase', 'hash_ends_with', 'hash_ends_with_nocase', 'hash_not_ends_with', 'hash_not_ends_with_nocase', 'log_index', 'log_index_not', 'log_index_gt', 'log_index_lt', 'log_index_gte', 'log_index_lte', 'log_index_in', 'log_index_not_in', 'protocol', 'protocol_not', 'protocol_gt', 'protocol_lt', 'protocol_gte', 'protocol_lte', 'protocol_in', 'protocol_not_in', 'protocol_contains', 'protocol_contains_nocase', 'protocol_not_contains', 'protocol_not_contains_nocase', 'protocol_starts_with', 'protocol_starts_with_nocase', 'protocol_not_starts_with', 'protocol_not_starts_with_nocase', 'protocol_ends_with', 'protocol_ends_with_nocase', 'protocol_not_ends_with', 'protocol_not_ends_with_nocase', 'to', 'to_not', 'to_gt', 'to_lt', 'to_gte', 'to_lte', 'to_in', 'to_not_in', 'to_contains', 'to_contains_nocase', 'to_not_contains', 'to_not_contains_nocase', 'to_starts_with', 'to_starts_with_nocase', 'to_not_starts_with', 'to_not_starts_with_nocase', 'to_ends_with', 'to_ends_with_nocase', 'to_not_ends_with', 'to_not_ends_with_nocase', 'from_', 'from_not', 'from_gt', 'from_lt', 'from_gte', 'from_lte', 'from_in', 'from_not_in', 'from_contains', 'from_contains_nocase', 'from_not_contains', 'from_not_contains_nocase', 'from_starts_with', 'from_starts_with_nocase', 'from_not_starts_with', 'from_not_starts_with_nocase', 'from_ends_with', 'from_ends_with_nocase', 'from_not_ends_with', 'from_not_ends_with_nocase', 'block_number', 'block_number_not', 'block_number_gt', 'block_number_lt', 'block_number_gte', 'block_number_lte', 'block_number_in', 'block_number_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'market', 'market_not', 'market_gt', 'market_lt', 'market_gte', 'market_lte', 'market_in', 'market_not_in', 'market_contains', 'market_contains_nocase', 'market_not_contains', 'market_not_contains_nocase', 'market_starts_with', 'market_starts_with_nocase', 'market_not_starts_with', 'market_not_starts_with_nocase', 'market_ends_with', 'market_ends_with_nocase', 'market_not_ends_with', 'market_not_ends_with_nocase', 'asset', 'asset_not', 'asset_gt', 'asset_lt', 'asset_gte', 'asset_lte', 'asset_in', 'asset_not_in', 'asset_contains', 'asset_contains_nocase', 'asset_not_contains', 'asset_not_contains_nocase', 'asset_starts_with', 'asset_starts_with_nocase', 'asset_not_starts_with', 'asset_not_starts_with_nocase', 'asset_ends_with', 'asset_ends_with_nocase', 'asset_not_ends_with', 'asset_not_ends_with_nocase', 'amount', 'amount_not', 'amount_gt', 'amount_lt', 'amount_gte', 'amount_lte', 'amount_in', 'amount_not_in', 'amount_usd', 'amount_usd_not', 'amount_usd_gt', 'amount_usd_lt', 'amount_usd_gte', 'amount_usd_lte', 'amount_usd_in', 'amount_usd_not_in', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    hash_not = sgqlc.types.Field(String, graphql_name='hash_not')
    hash_gt = sgqlc.types.Field(String, graphql_name='hash_gt')
    hash_lt = sgqlc.types.Field(String, graphql_name='hash_lt')
    hash_gte = sgqlc.types.Field(String, graphql_name='hash_gte')
    hash_lte = sgqlc.types.Field(String, graphql_name='hash_lte')
    hash_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='hash_in')
    hash_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='hash_not_in')
    hash_contains = sgqlc.types.Field(String, graphql_name='hash_contains')
    hash_contains_nocase = sgqlc.types.Field(String, graphql_name='hash_contains_nocase')
    hash_not_contains = sgqlc.types.Field(String, graphql_name='hash_not_contains')
    hash_not_contains_nocase = sgqlc.types.Field(String, graphql_name='hash_not_contains_nocase')
    hash_starts_with = sgqlc.types.Field(String, graphql_name='hash_starts_with')
    hash_starts_with_nocase = sgqlc.types.Field(String, graphql_name='hash_starts_with_nocase')
    hash_not_starts_with = sgqlc.types.Field(String, graphql_name='hash_not_starts_with')
    hash_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='hash_not_starts_with_nocase')
    hash_ends_with = sgqlc.types.Field(String, graphql_name='hash_ends_with')
    hash_ends_with_nocase = sgqlc.types.Field(String, graphql_name='hash_ends_with_nocase')
    hash_not_ends_with = sgqlc.types.Field(String, graphql_name='hash_not_ends_with')
    hash_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='hash_not_ends_with_nocase')
    log_index = sgqlc.types.Field(Int, graphql_name='logIndex')
    log_index_not = sgqlc.types.Field(Int, graphql_name='logIndex_not')
    log_index_gt = sgqlc.types.Field(Int, graphql_name='logIndex_gt')
    log_index_lt = sgqlc.types.Field(Int, graphql_name='logIndex_lt')
    log_index_gte = sgqlc.types.Field(Int, graphql_name='logIndex_gte')
    log_index_lte = sgqlc.types.Field(Int, graphql_name='logIndex_lte')
    log_index_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='logIndex_in')
    log_index_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='logIndex_not_in')
    protocol = sgqlc.types.Field(String, graphql_name='protocol')
    protocol_not = sgqlc.types.Field(String, graphql_name='protocol_not')
    protocol_gt = sgqlc.types.Field(String, graphql_name='protocol_gt')
    protocol_lt = sgqlc.types.Field(String, graphql_name='protocol_lt')
    protocol_gte = sgqlc.types.Field(String, graphql_name='protocol_gte')
    protocol_lte = sgqlc.types.Field(String, graphql_name='protocol_lte')
    protocol_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_in')
    protocol_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_not_in')
    protocol_contains = sgqlc.types.Field(String, graphql_name='protocol_contains')
    protocol_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_contains_nocase')
    protocol_not_contains = sgqlc.types.Field(String, graphql_name='protocol_not_contains')
    protocol_not_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_contains_nocase')
    protocol_starts_with = sgqlc.types.Field(String, graphql_name='protocol_starts_with')
    protocol_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_starts_with_nocase')
    protocol_not_starts_with = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with')
    protocol_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with_nocase')
    protocol_ends_with = sgqlc.types.Field(String, graphql_name='protocol_ends_with')
    protocol_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_ends_with_nocase')
    protocol_not_ends_with = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with')
    protocol_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with_nocase')
    to = sgqlc.types.Field(String, graphql_name='to')
    to_not = sgqlc.types.Field(String, graphql_name='to_not')
    to_gt = sgqlc.types.Field(String, graphql_name='to_gt')
    to_lt = sgqlc.types.Field(String, graphql_name='to_lt')
    to_gte = sgqlc.types.Field(String, graphql_name='to_gte')
    to_lte = sgqlc.types.Field(String, graphql_name='to_lte')
    to_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='to_in')
    to_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='to_not_in')
    to_contains = sgqlc.types.Field(String, graphql_name='to_contains')
    to_contains_nocase = sgqlc.types.Field(String, graphql_name='to_contains_nocase')
    to_not_contains = sgqlc.types.Field(String, graphql_name='to_not_contains')
    to_not_contains_nocase = sgqlc.types.Field(String, graphql_name='to_not_contains_nocase')
    to_starts_with = sgqlc.types.Field(String, graphql_name='to_starts_with')
    to_starts_with_nocase = sgqlc.types.Field(String, graphql_name='to_starts_with_nocase')
    to_not_starts_with = sgqlc.types.Field(String, graphql_name='to_not_starts_with')
    to_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='to_not_starts_with_nocase')
    to_ends_with = sgqlc.types.Field(String, graphql_name='to_ends_with')
    to_ends_with_nocase = sgqlc.types.Field(String, graphql_name='to_ends_with_nocase')
    to_not_ends_with = sgqlc.types.Field(String, graphql_name='to_not_ends_with')
    to_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='to_not_ends_with_nocase')
    from_ = sgqlc.types.Field(String, graphql_name='from')
    from_not = sgqlc.types.Field(String, graphql_name='from_not')
    from_gt = sgqlc.types.Field(String, graphql_name='from_gt')
    from_lt = sgqlc.types.Field(String, graphql_name='from_lt')
    from_gte = sgqlc.types.Field(String, graphql_name='from_gte')
    from_lte = sgqlc.types.Field(String, graphql_name='from_lte')
    from_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='from_in')
    from_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='from_not_in')
    from_contains = sgqlc.types.Field(String, graphql_name='from_contains')
    from_contains_nocase = sgqlc.types.Field(String, graphql_name='from_contains_nocase')
    from_not_contains = sgqlc.types.Field(String, graphql_name='from_not_contains')
    from_not_contains_nocase = sgqlc.types.Field(String, graphql_name='from_not_contains_nocase')
    from_starts_with = sgqlc.types.Field(String, graphql_name='from_starts_with')
    from_starts_with_nocase = sgqlc.types.Field(String, graphql_name='from_starts_with_nocase')
    from_not_starts_with = sgqlc.types.Field(String, graphql_name='from_not_starts_with')
    from_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='from_not_starts_with_nocase')
    from_ends_with = sgqlc.types.Field(String, graphql_name='from_ends_with')
    from_ends_with_nocase = sgqlc.types.Field(String, graphql_name='from_ends_with_nocase')
    from_not_ends_with = sgqlc.types.Field(String, graphql_name='from_not_ends_with')
    from_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='from_not_ends_with_nocase')
    block_number = sgqlc.types.Field(BigInt, graphql_name='blockNumber')
    block_number_not = sgqlc.types.Field(BigInt, graphql_name='blockNumber_not')
    block_number_gt = sgqlc.types.Field(BigInt, graphql_name='blockNumber_gt')
    block_number_lt = sgqlc.types.Field(BigInt, graphql_name='blockNumber_lt')
    block_number_gte = sgqlc.types.Field(BigInt, graphql_name='blockNumber_gte')
    block_number_lte = sgqlc.types.Field(BigInt, graphql_name='blockNumber_lte')
    block_number_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='blockNumber_in')
    block_number_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='blockNumber_not_in')
    timestamp = sgqlc.types.Field(BigInt, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_not_in')
    market = sgqlc.types.Field(String, graphql_name='market')
    market_not = sgqlc.types.Field(String, graphql_name='market_not')
    market_gt = sgqlc.types.Field(String, graphql_name='market_gt')
    market_lt = sgqlc.types.Field(String, graphql_name='market_lt')
    market_gte = sgqlc.types.Field(String, graphql_name='market_gte')
    market_lte = sgqlc.types.Field(String, graphql_name='market_lte')
    market_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='market_in')
    market_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='market_not_in')
    market_contains = sgqlc.types.Field(String, graphql_name='market_contains')
    market_contains_nocase = sgqlc.types.Field(String, graphql_name='market_contains_nocase')
    market_not_contains = sgqlc.types.Field(String, graphql_name='market_not_contains')
    market_not_contains_nocase = sgqlc.types.Field(String, graphql_name='market_not_contains_nocase')
    market_starts_with = sgqlc.types.Field(String, graphql_name='market_starts_with')
    market_starts_with_nocase = sgqlc.types.Field(String, graphql_name='market_starts_with_nocase')
    market_not_starts_with = sgqlc.types.Field(String, graphql_name='market_not_starts_with')
    market_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='market_not_starts_with_nocase')
    market_ends_with = sgqlc.types.Field(String, graphql_name='market_ends_with')
    market_ends_with_nocase = sgqlc.types.Field(String, graphql_name='market_ends_with_nocase')
    market_not_ends_with = sgqlc.types.Field(String, graphql_name='market_not_ends_with')
    market_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='market_not_ends_with_nocase')
    asset = sgqlc.types.Field(String, graphql_name='asset')
    asset_not = sgqlc.types.Field(String, graphql_name='asset_not')
    asset_gt = sgqlc.types.Field(String, graphql_name='asset_gt')
    asset_lt = sgqlc.types.Field(String, graphql_name='asset_lt')
    asset_gte = sgqlc.types.Field(String, graphql_name='asset_gte')
    asset_lte = sgqlc.types.Field(String, graphql_name='asset_lte')
    asset_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='asset_in')
    asset_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='asset_not_in')
    asset_contains = sgqlc.types.Field(String, graphql_name='asset_contains')
    asset_contains_nocase = sgqlc.types.Field(String, graphql_name='asset_contains_nocase')
    asset_not_contains = sgqlc.types.Field(String, graphql_name='asset_not_contains')
    asset_not_contains_nocase = sgqlc.types.Field(String, graphql_name='asset_not_contains_nocase')
    asset_starts_with = sgqlc.types.Field(String, graphql_name='asset_starts_with')
    asset_starts_with_nocase = sgqlc.types.Field(String, graphql_name='asset_starts_with_nocase')
    asset_not_starts_with = sgqlc.types.Field(String, graphql_name='asset_not_starts_with')
    asset_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='asset_not_starts_with_nocase')
    asset_ends_with = sgqlc.types.Field(String, graphql_name='asset_ends_with')
    asset_ends_with_nocase = sgqlc.types.Field(String, graphql_name='asset_ends_with_nocase')
    asset_not_ends_with = sgqlc.types.Field(String, graphql_name='asset_not_ends_with')
    asset_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='asset_not_ends_with_nocase')
    amount = sgqlc.types.Field(BigInt, graphql_name='amount')
    amount_not = sgqlc.types.Field(BigInt, graphql_name='amount_not')
    amount_gt = sgqlc.types.Field(BigInt, graphql_name='amount_gt')
    amount_lt = sgqlc.types.Field(BigInt, graphql_name='amount_lt')
    amount_gte = sgqlc.types.Field(BigInt, graphql_name='amount_gte')
    amount_lte = sgqlc.types.Field(BigInt, graphql_name='amount_lte')
    amount_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='amount_in')
    amount_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='amount_not_in')
    amount_usd = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD')
    amount_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_not')
    amount_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_gt')
    amount_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_lt')
    amount_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_gte')
    amount_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_lte')
    amount_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amountUSD_in')
    amount_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amountUSD_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class Event_filter(sgqlc.types.Input):
    __schema__ = subgraph_status_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'hash', 'hash_not', 'hash_gt', 'hash_lt', 'hash_gte', 'hash_lte', 'hash_in', 'hash_not_in', 'hash_contains', 'hash_contains_nocase', 'hash_not_contains', 'hash_not_contains_nocase', 'hash_starts_with', 'hash_starts_with_nocase', 'hash_not_starts_with', 'hash_not_starts_with_nocase', 'hash_ends_with', 'hash_ends_with_nocase', 'hash_not_ends_with', 'hash_not_ends_with_nocase', 'log_index', 'log_index_not', 'log_index_gt', 'log_index_lt', 'log_index_gte', 'log_index_lte', 'log_index_in', 'log_index_not_in', 'protocol', 'protocol_not', 'protocol_gt', 'protocol_lt', 'protocol_gte', 'protocol_lte', 'protocol_in', 'protocol_not_in', 'protocol_contains', 'protocol_contains_nocase', 'protocol_not_contains', 'protocol_not_contains_nocase', 'protocol_starts_with', 'protocol_starts_with_nocase', 'protocol_not_starts_with', 'protocol_not_starts_with_nocase', 'protocol_ends_with', 'protocol_ends_with_nocase', 'protocol_not_ends_with', 'protocol_not_ends_with_nocase', 'to', 'to_not', 'to_gt', 'to_lt', 'to_gte', 'to_lte', 'to_in', 'to_not_in', 'to_contains', 'to_contains_nocase', 'to_not_contains', 'to_not_contains_nocase', 'to_starts_with', 'to_starts_with_nocase', 'to_not_starts_with', 'to_not_starts_with_nocase', 'to_ends_with', 'to_ends_with_nocase', 'to_not_ends_with', 'to_not_ends_with_nocase', 'from_', 'from_not', 'from_gt', 'from_lt', 'from_gte', 'from_lte', 'from_in', 'from_not_in', 'from_contains', 'from_contains_nocase', 'from_not_contains', 'from_not_contains_nocase', 'from_starts_with', 'from_starts_with_nocase', 'from_not_starts_with', 'from_not_starts_with_nocase', 'from_ends_with', 'from_ends_with_nocase', 'from_not_ends_with', 'from_not_ends_with_nocase', 'block_number', 'block_number_not', 'block_number_gt', 'block_number_lt', 'block_number_gte', 'block_number_lte', 'block_number_in', 'block_number_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    hash_not = sgqlc.types.Field(String, graphql_name='hash_not')
    hash_gt = sgqlc.types.Field(String, graphql_name='hash_gt')
    hash_lt = sgqlc.types.Field(String, graphql_name='hash_lt')
    hash_gte = sgqlc.types.Field(String, graphql_name='hash_gte')
    hash_lte = sgqlc.types.Field(String, graphql_name='hash_lte')
    hash_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='hash_in')
    hash_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='hash_not_in')
    hash_contains = sgqlc.types.Field(String, graphql_name='hash_contains')
    hash_contains_nocase = sgqlc.types.Field(String, graphql_name='hash_contains_nocase')
    hash_not_contains = sgqlc.types.Field(String, graphql_name='hash_not_contains')
    hash_not_contains_nocase = sgqlc.types.Field(String, graphql_name='hash_not_contains_nocase')
    hash_starts_with = sgqlc.types.Field(String, graphql_name='hash_starts_with')
    hash_starts_with_nocase = sgqlc.types.Field(String, graphql_name='hash_starts_with_nocase')
    hash_not_starts_with = sgqlc.types.Field(String, graphql_name='hash_not_starts_with')
    hash_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='hash_not_starts_with_nocase')
    hash_ends_with = sgqlc.types.Field(String, graphql_name='hash_ends_with')
    hash_ends_with_nocase = sgqlc.types.Field(String, graphql_name='hash_ends_with_nocase')
    hash_not_ends_with = sgqlc.types.Field(String, graphql_name='hash_not_ends_with')
    hash_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='hash_not_ends_with_nocase')
    log_index = sgqlc.types.Field(Int, graphql_name='logIndex')
    log_index_not = sgqlc.types.Field(Int, graphql_name='logIndex_not')
    log_index_gt = sgqlc.types.Field(Int, graphql_name='logIndex_gt')
    log_index_lt = sgqlc.types.Field(Int, graphql_name='logIndex_lt')
    log_index_gte = sgqlc.types.Field(Int, graphql_name='logIndex_gte')
    log_index_lte = sgqlc.types.Field(Int, graphql_name='logIndex_lte')
    log_index_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='logIndex_in')
    log_index_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='logIndex_not_in')
    protocol = sgqlc.types.Field(String, graphql_name='protocol')
    protocol_not = sgqlc.types.Field(String, graphql_name='protocol_not')
    protocol_gt = sgqlc.types.Field(String, graphql_name='protocol_gt')
    protocol_lt = sgqlc.types.Field(String, graphql_name='protocol_lt')
    protocol_gte = sgqlc.types.Field(String, graphql_name='protocol_gte')
    protocol_lte = sgqlc.types.Field(String, graphql_name='protocol_lte')
    protocol_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_in')
    protocol_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_not_in')
    protocol_contains = sgqlc.types.Field(String, graphql_name='protocol_contains')
    protocol_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_contains_nocase')
    protocol_not_contains = sgqlc.types.Field(String, graphql_name='protocol_not_contains')
    protocol_not_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_contains_nocase')
    protocol_starts_with = sgqlc.types.Field(String, graphql_name='protocol_starts_with')
    protocol_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_starts_with_nocase')
    protocol_not_starts_with = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with')
    protocol_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with_nocase')
    protocol_ends_with = sgqlc.types.Field(String, graphql_name='protocol_ends_with')
    protocol_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_ends_with_nocase')
    protocol_not_ends_with = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with')
    protocol_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with_nocase')
    to = sgqlc.types.Field(String, graphql_name='to')
    to_not = sgqlc.types.Field(String, graphql_name='to_not')
    to_gt = sgqlc.types.Field(String, graphql_name='to_gt')
    to_lt = sgqlc.types.Field(String, graphql_name='to_lt')
    to_gte = sgqlc.types.Field(String, graphql_name='to_gte')
    to_lte = sgqlc.types.Field(String, graphql_name='to_lte')
    to_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='to_in')
    to_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='to_not_in')
    to_contains = sgqlc.types.Field(String, graphql_name='to_contains')
    to_contains_nocase = sgqlc.types.Field(String, graphql_name='to_contains_nocase')
    to_not_contains = sgqlc.types.Field(String, graphql_name='to_not_contains')
    to_not_contains_nocase = sgqlc.types.Field(String, graphql_name='to_not_contains_nocase')
    to_starts_with = sgqlc.types.Field(String, graphql_name='to_starts_with')
    to_starts_with_nocase = sgqlc.types.Field(String, graphql_name='to_starts_with_nocase')
    to_not_starts_with = sgqlc.types.Field(String, graphql_name='to_not_starts_with')
    to_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='to_not_starts_with_nocase')
    to_ends_with = sgqlc.types.Field(String, graphql_name='to_ends_with')
    to_ends_with_nocase = sgqlc.types.Field(String, graphql_name='to_ends_with_nocase')
    to_not_ends_with = sgqlc.types.Field(String, graphql_name='to_not_ends_with')
    to_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='to_not_ends_with_nocase')
    from_ = sgqlc.types.Field(String, graphql_name='from')
    from_not = sgqlc.types.Field(String, graphql_name='from_not')
    from_gt = sgqlc.types.Field(String, graphql_name='from_gt')
    from_lt = sgqlc.types.Field(String, graphql_name='from_lt')
    from_gte = sgqlc.types.Field(String, graphql_name='from_gte')
    from_lte = sgqlc.types.Field(String, graphql_name='from_lte')
    from_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='from_in')
    from_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='from_not_in')
    from_contains = sgqlc.types.Field(String, graphql_name='from_contains')
    from_contains_nocase = sgqlc.types.Field(String, graphql_name='from_contains_nocase')
    from_not_contains = sgqlc.types.Field(String, graphql_name='from_not_contains')
    from_not_contains_nocase = sgqlc.types.Field(String, graphql_name='from_not_contains_nocase')
    from_starts_with = sgqlc.types.Field(String, graphql_name='from_starts_with')
    from_starts_with_nocase = sgqlc.types.Field(String, graphql_name='from_starts_with_nocase')
    from_not_starts_with = sgqlc.types.Field(String, graphql_name='from_not_starts_with')
    from_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='from_not_starts_with_nocase')
    from_ends_with = sgqlc.types.Field(String, graphql_name='from_ends_with')
    from_ends_with_nocase = sgqlc.types.Field(String, graphql_name='from_ends_with_nocase')
    from_not_ends_with = sgqlc.types.Field(String, graphql_name='from_not_ends_with')
    from_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='from_not_ends_with_nocase')
    block_number = sgqlc.types.Field(BigInt, graphql_name='blockNumber')
    block_number_not = sgqlc.types.Field(BigInt, graphql_name='blockNumber_not')
    block_number_gt = sgqlc.types.Field(BigInt, graphql_name='blockNumber_gt')
    block_number_lt = sgqlc.types.Field(BigInt, graphql_name='blockNumber_lt')
    block_number_gte = sgqlc.types.Field(BigInt, graphql_name='blockNumber_gte')
    block_number_lte = sgqlc.types.Field(BigInt, graphql_name='blockNumber_lte')
    block_number_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='blockNumber_in')
    block_number_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='blockNumber_not_in')
    timestamp = sgqlc.types.Field(BigInt, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class FinancialsDailySnapshot_filter(sgqlc.types.Input):
    __schema__ = subgraph_status_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'protocol', 'protocol_not', 'protocol_gt', 'protocol_lt', 'protocol_gte', 'protocol_lte', 'protocol_in', 'protocol_not_in', 'protocol_contains', 'protocol_contains_nocase', 'protocol_not_contains', 'protocol_not_contains_nocase', 'protocol_starts_with', 'protocol_starts_with_nocase', 'protocol_not_starts_with', 'protocol_not_starts_with_nocase', 'protocol_ends_with', 'protocol_ends_with_nocase', 'protocol_not_ends_with', 'protocol_not_ends_with_nocase', 'block_number', 'block_number_not', 'block_number_gt', 'block_number_lt', 'block_number_gte', 'block_number_lte', 'block_number_in', 'block_number_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'total_value_locked_usd', 'total_value_locked_usd_not', 'total_value_locked_usd_gt', 'total_value_locked_usd_lt', 'total_value_locked_usd_gte', 'total_value_locked_usd_lte', 'total_value_locked_usd_in', 'total_value_locked_usd_not_in', 'protocol_controlled_value_usd', 'protocol_controlled_value_usd_not', 'protocol_controlled_value_usd_gt', 'protocol_controlled_value_usd_lt', 'protocol_controlled_value_usd_gte', 'protocol_controlled_value_usd_lte', 'protocol_controlled_value_usd_in', 'protocol_controlled_value_usd_not_in', 'minted_token_supplies', 'minted_token_supplies_not', 'minted_token_supplies_contains', 'minted_token_supplies_contains_nocase', 'minted_token_supplies_not_contains', 'minted_token_supplies_not_contains_nocase', 'daily_supply_side_revenue_usd', 'daily_supply_side_revenue_usd_not', 'daily_supply_side_revenue_usd_gt', 'daily_supply_side_revenue_usd_lt', 'daily_supply_side_revenue_usd_gte', 'daily_supply_side_revenue_usd_lte', 'daily_supply_side_revenue_usd_in', 'daily_supply_side_revenue_usd_not_in', 'cumulative_supply_side_revenue_usd', 'cumulative_supply_side_revenue_usd_not', 'cumulative_supply_side_revenue_usd_gt', 'cumulative_supply_side_revenue_usd_lt', 'cumulative_supply_side_revenue_usd_gte', 'cumulative_supply_side_revenue_usd_lte', 'cumulative_supply_side_revenue_usd_in', 'cumulative_supply_side_revenue_usd_not_in', 'daily_protocol_side_revenue_usd', 'daily_protocol_side_revenue_usd_not', 'daily_protocol_side_revenue_usd_gt', 'daily_protocol_side_revenue_usd_lt', 'daily_protocol_side_revenue_usd_gte', 'daily_protocol_side_revenue_usd_lte', 'daily_protocol_side_revenue_usd_in', 'daily_protocol_side_revenue_usd_not_in', 'cumulative_protocol_side_revenue_usd', 'cumulative_protocol_side_revenue_usd_not', 'cumulative_protocol_side_revenue_usd_gt', 'cumulative_protocol_side_revenue_usd_lt', 'cumulative_protocol_side_revenue_usd_gte', 'cumulative_protocol_side_revenue_usd_lte', 'cumulative_protocol_side_revenue_usd_in', 'cumulative_protocol_side_revenue_usd_not_in', 'daily_total_revenue_usd', 'daily_total_revenue_usd_not', 'daily_total_revenue_usd_gt', 'daily_total_revenue_usd_lt', 'daily_total_revenue_usd_gte', 'daily_total_revenue_usd_lte', 'daily_total_revenue_usd_in', 'daily_total_revenue_usd_not_in', 'cumulative_total_revenue_usd', 'cumulative_total_revenue_usd_not', 'cumulative_total_revenue_usd_gt', 'cumulative_total_revenue_usd_lt', 'cumulative_total_revenue_usd_gte', 'cumulative_total_revenue_usd_lte', 'cumulative_total_revenue_usd_in', 'cumulative_total_revenue_usd_not_in', 'total_deposit_balance_usd', 'total_deposit_balance_usd_not', 'total_deposit_balance_usd_gt', 'total_deposit_balance_usd_lt', 'total_deposit_balance_usd_gte', 'total_deposit_balance_usd_lte', 'total_deposit_balance_usd_in', 'total_deposit_balance_usd_not_in', 'daily_deposit_usd', 'daily_deposit_usd_not', 'daily_deposit_usd_gt', 'daily_deposit_usd_lt', 'daily_deposit_usd_gte', 'daily_deposit_usd_lte', 'daily_deposit_usd_in', 'daily_deposit_usd_not_in', 'cumulative_deposit_usd', 'cumulative_deposit_usd_not', 'cumulative_deposit_usd_gt', 'cumulative_deposit_usd_lt', 'cumulative_deposit_usd_gte', 'cumulative_deposit_usd_lte', 'cumulative_deposit_usd_in', 'cumulative_deposit_usd_not_in', 'total_borrow_balance_usd', 'total_borrow_balance_usd_not', 'total_borrow_balance_usd_gt', 'total_borrow_balance_usd_lt', 'total_borrow_balance_usd_gte', 'total_borrow_balance_usd_lte', 'total_borrow_balance_usd_in', 'total_borrow_balance_usd_not_in', 'daily_borrow_usd', 'daily_borrow_usd_not', 'daily_borrow_usd_gt', 'daily_borrow_usd_lt', 'daily_borrow_usd_gte', 'daily_borrow_usd_lte', 'daily_borrow_usd_in', 'daily_borrow_usd_not_in', 'cumulative_borrow_usd', 'cumulative_borrow_usd_not', 'cumulative_borrow_usd_gt', 'cumulative_borrow_usd_lt', 'cumulative_borrow_usd_gte', 'cumulative_borrow_usd_lte', 'cumulative_borrow_usd_in', 'cumulative_borrow_usd_not_in', 'daily_liquidate_usd', 'daily_liquidate_usd_not', 'daily_liquidate_usd_gt', 'daily_liquidate_usd_lt', 'daily_liquidate_usd_gte', 'daily_liquidate_usd_lte', 'daily_liquidate_usd_in', 'daily_liquidate_usd_not_in', 'cumulative_liquidate_usd', 'cumulative_liquidate_usd_not', 'cumulative_liquidate_usd_gt', 'cumulative_liquidate_usd_lt', 'cumulative_liquidate_usd_gte', 'cumulative_liquidate_usd_lte', 'cumulative_liquidate_usd_in', 'cumulative_liquidate_usd_not_in', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    protocol = sgqlc.types.Field(String, graphql_name='protocol')
    protocol_not = sgqlc.types.Field(String, graphql_name='protocol_not')
    protocol_gt = sgqlc.types.Field(String, graphql_name='protocol_gt')
    protocol_lt = sgqlc.types.Field(String, graphql_name='protocol_lt')
    protocol_gte = sgqlc.types.Field(String, graphql_name='protocol_gte')
    protocol_lte = sgqlc.types.Field(String, graphql_name='protocol_lte')
    protocol_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_in')
    protocol_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_not_in')
    protocol_contains = sgqlc.types.Field(String, graphql_name='protocol_contains')
    protocol_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_contains_nocase')
    protocol_not_contains = sgqlc.types.Field(String, graphql_name='protocol_not_contains')
    protocol_not_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_contains_nocase')
    protocol_starts_with = sgqlc.types.Field(String, graphql_name='protocol_starts_with')
    protocol_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_starts_with_nocase')
    protocol_not_starts_with = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with')
    protocol_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with_nocase')
    protocol_ends_with = sgqlc.types.Field(String, graphql_name='protocol_ends_with')
    protocol_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_ends_with_nocase')
    protocol_not_ends_with = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with')
    protocol_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with_nocase')
    block_number = sgqlc.types.Field(BigInt, graphql_name='blockNumber')
    block_number_not = sgqlc.types.Field(BigInt, graphql_name='blockNumber_not')
    block_number_gt = sgqlc.types.Field(BigInt, graphql_name='blockNumber_gt')
    block_number_lt = sgqlc.types.Field(BigInt, graphql_name='blockNumber_lt')
    block_number_gte = sgqlc.types.Field(BigInt, graphql_name='blockNumber_gte')
    block_number_lte = sgqlc.types.Field(BigInt, graphql_name='blockNumber_lte')
    block_number_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='blockNumber_in')
    block_number_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='blockNumber_not_in')
    timestamp = sgqlc.types.Field(BigInt, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_not_in')
    total_value_locked_usd = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD')
    total_value_locked_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_not')
    total_value_locked_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gt')
    total_value_locked_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lt')
    total_value_locked_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gte')
    total_value_locked_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lte')
    total_value_locked_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_in')
    total_value_locked_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_not_in')
    protocol_controlled_value_usd = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD')
    protocol_controlled_value_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD_not')
    protocol_controlled_value_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD_gt')
    protocol_controlled_value_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD_lt')
    protocol_controlled_value_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD_gte')
    protocol_controlled_value_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD_lte')
    protocol_controlled_value_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='protocolControlledValueUSD_in')
    protocol_controlled_value_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='protocolControlledValueUSD_not_in')
    minted_token_supplies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='mintedTokenSupplies')
    minted_token_supplies_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='mintedTokenSupplies_not')
    minted_token_supplies_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='mintedTokenSupplies_contains')
    minted_token_supplies_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='mintedTokenSupplies_contains_nocase')
    minted_token_supplies_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='mintedTokenSupplies_not_contains')
    minted_token_supplies_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='mintedTokenSupplies_not_contains_nocase')
    daily_supply_side_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='dailySupplySideRevenueUSD')
    daily_supply_side_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='dailySupplySideRevenueUSD_not')
    daily_supply_side_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='dailySupplySideRevenueUSD_gt')
    daily_supply_side_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='dailySupplySideRevenueUSD_lt')
    daily_supply_side_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='dailySupplySideRevenueUSD_gte')
    daily_supply_side_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='dailySupplySideRevenueUSD_lte')
    daily_supply_side_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailySupplySideRevenueUSD_in')
    daily_supply_side_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailySupplySideRevenueUSD_not_in')
    cumulative_supply_side_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD')
    cumulative_supply_side_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_not')
    cumulative_supply_side_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_gt')
    cumulative_supply_side_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_lt')
    cumulative_supply_side_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_gte')
    cumulative_supply_side_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_lte')
    cumulative_supply_side_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeSupplySideRevenueUSD_in')
    cumulative_supply_side_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeSupplySideRevenueUSD_not_in')
    daily_protocol_side_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='dailyProtocolSideRevenueUSD')
    daily_protocol_side_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='dailyProtocolSideRevenueUSD_not')
    daily_protocol_side_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='dailyProtocolSideRevenueUSD_gt')
    daily_protocol_side_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='dailyProtocolSideRevenueUSD_lt')
    daily_protocol_side_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='dailyProtocolSideRevenueUSD_gte')
    daily_protocol_side_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='dailyProtocolSideRevenueUSD_lte')
    daily_protocol_side_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyProtocolSideRevenueUSD_in')
    daily_protocol_side_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyProtocolSideRevenueUSD_not_in')
    cumulative_protocol_side_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD')
    cumulative_protocol_side_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_not')
    cumulative_protocol_side_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_gt')
    cumulative_protocol_side_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_lt')
    cumulative_protocol_side_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_gte')
    cumulative_protocol_side_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_lte')
    cumulative_protocol_side_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeProtocolSideRevenueUSD_in')
    cumulative_protocol_side_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeProtocolSideRevenueUSD_not_in')
    daily_total_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='dailyTotalRevenueUSD')
    daily_total_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='dailyTotalRevenueUSD_not')
    daily_total_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='dailyTotalRevenueUSD_gt')
    daily_total_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='dailyTotalRevenueUSD_lt')
    daily_total_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='dailyTotalRevenueUSD_gte')
    daily_total_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='dailyTotalRevenueUSD_lte')
    daily_total_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyTotalRevenueUSD_in')
    daily_total_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyTotalRevenueUSD_not_in')
    cumulative_total_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD')
    cumulative_total_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_not')
    cumulative_total_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_gt')
    cumulative_total_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_lt')
    cumulative_total_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_gte')
    cumulative_total_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_lte')
    cumulative_total_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeTotalRevenueUSD_in')
    cumulative_total_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeTotalRevenueUSD_not_in')
    total_deposit_balance_usd = sgqlc.types.Field(BigDecimal, graphql_name='totalDepositBalanceUSD')
    total_deposit_balance_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='totalDepositBalanceUSD_not')
    total_deposit_balance_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalDepositBalanceUSD_gt')
    total_deposit_balance_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalDepositBalanceUSD_lt')
    total_deposit_balance_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalDepositBalanceUSD_gte')
    total_deposit_balance_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalDepositBalanceUSD_lte')
    total_deposit_balance_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalDepositBalanceUSD_in')
    total_deposit_balance_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalDepositBalanceUSD_not_in')
    daily_deposit_usd = sgqlc.types.Field(BigDecimal, graphql_name='dailyDepositUSD')
    daily_deposit_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='dailyDepositUSD_not')
    daily_deposit_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='dailyDepositUSD_gt')
    daily_deposit_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='dailyDepositUSD_lt')
    daily_deposit_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='dailyDepositUSD_gte')
    daily_deposit_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='dailyDepositUSD_lte')
    daily_deposit_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyDepositUSD_in')
    daily_deposit_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyDepositUSD_not_in')
    cumulative_deposit_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeDepositUSD')
    cumulative_deposit_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeDepositUSD_not')
    cumulative_deposit_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeDepositUSD_gt')
    cumulative_deposit_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeDepositUSD_lt')
    cumulative_deposit_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeDepositUSD_gte')
    cumulative_deposit_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeDepositUSD_lte')
    cumulative_deposit_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeDepositUSD_in')
    cumulative_deposit_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeDepositUSD_not_in')
    total_borrow_balance_usd = sgqlc.types.Field(BigDecimal, graphql_name='totalBorrowBalanceUSD')
    total_borrow_balance_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='totalBorrowBalanceUSD_not')
    total_borrow_balance_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalBorrowBalanceUSD_gt')
    total_borrow_balance_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalBorrowBalanceUSD_lt')
    total_borrow_balance_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalBorrowBalanceUSD_gte')
    total_borrow_balance_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalBorrowBalanceUSD_lte')
    total_borrow_balance_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalBorrowBalanceUSD_in')
    total_borrow_balance_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalBorrowBalanceUSD_not_in')
    daily_borrow_usd = sgqlc.types.Field(BigDecimal, graphql_name='dailyBorrowUSD')
    daily_borrow_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='dailyBorrowUSD_not')
    daily_borrow_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='dailyBorrowUSD_gt')
    daily_borrow_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='dailyBorrowUSD_lt')
    daily_borrow_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='dailyBorrowUSD_gte')
    daily_borrow_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='dailyBorrowUSD_lte')
    daily_borrow_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyBorrowUSD_in')
    daily_borrow_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyBorrowUSD_not_in')
    cumulative_borrow_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeBorrowUSD')
    cumulative_borrow_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeBorrowUSD_not')
    cumulative_borrow_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeBorrowUSD_gt')
    cumulative_borrow_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeBorrowUSD_lt')
    cumulative_borrow_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeBorrowUSD_gte')
    cumulative_borrow_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeBorrowUSD_lte')
    cumulative_borrow_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeBorrowUSD_in')
    cumulative_borrow_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeBorrowUSD_not_in')
    daily_liquidate_usd = sgqlc.types.Field(BigDecimal, graphql_name='dailyLiquidateUSD')
    daily_liquidate_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='dailyLiquidateUSD_not')
    daily_liquidate_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='dailyLiquidateUSD_gt')
    daily_liquidate_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='dailyLiquidateUSD_lt')
    daily_liquidate_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='dailyLiquidateUSD_gte')
    daily_liquidate_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='dailyLiquidateUSD_lte')
    daily_liquidate_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyLiquidateUSD_in')
    daily_liquidate_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyLiquidateUSD_not_in')
    cumulative_liquidate_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeLiquidateUSD')
    cumulative_liquidate_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeLiquidateUSD_not')
    cumulative_liquidate_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeLiquidateUSD_gt')
    cumulative_liquidate_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeLiquidateUSD_lt')
    cumulative_liquidate_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeLiquidateUSD_gte')
    cumulative_liquidate_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeLiquidateUSD_lte')
    cumulative_liquidate_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeLiquidateUSD_in')
    cumulative_liquidate_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeLiquidateUSD_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class InterestRate_filter(sgqlc.types.Input):
    __schema__ = subgraph_status_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'rate', 'rate_not', 'rate_gt', 'rate_lt', 'rate_gte', 'rate_lte', 'rate_in', 'rate_not_in', 'duration', 'duration_not', 'duration_gt', 'duration_lt', 'duration_gte', 'duration_lte', 'duration_in', 'duration_not_in', 'maturity_block', 'maturity_block_not', 'maturity_block_gt', 'maturity_block_lt', 'maturity_block_gte', 'maturity_block_lte', 'maturity_block_in', 'maturity_block_not_in', 'side', 'side_not', 'side_in', 'side_not_in', 'type', 'type_not', 'type_in', 'type_not_in', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    rate = sgqlc.types.Field(BigDecimal, graphql_name='rate')
    rate_not = sgqlc.types.Field(BigDecimal, graphql_name='rate_not')
    rate_gt = sgqlc.types.Field(BigDecimal, graphql_name='rate_gt')
    rate_lt = sgqlc.types.Field(BigDecimal, graphql_name='rate_lt')
    rate_gte = sgqlc.types.Field(BigDecimal, graphql_name='rate_gte')
    rate_lte = sgqlc.types.Field(BigDecimal, graphql_name='rate_lte')
    rate_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rate_in')
    rate_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rate_not_in')
    duration = sgqlc.types.Field(Int, graphql_name='duration')
    duration_not = sgqlc.types.Field(Int, graphql_name='duration_not')
    duration_gt = sgqlc.types.Field(Int, graphql_name='duration_gt')
    duration_lt = sgqlc.types.Field(Int, graphql_name='duration_lt')
    duration_gte = sgqlc.types.Field(Int, graphql_name='duration_gte')
    duration_lte = sgqlc.types.Field(Int, graphql_name='duration_lte')
    duration_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='duration_in')
    duration_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='duration_not_in')
    maturity_block = sgqlc.types.Field(BigInt, graphql_name='maturityBlock')
    maturity_block_not = sgqlc.types.Field(BigInt, graphql_name='maturityBlock_not')
    maturity_block_gt = sgqlc.types.Field(BigInt, graphql_name='maturityBlock_gt')
    maturity_block_lt = sgqlc.types.Field(BigInt, graphql_name='maturityBlock_lt')
    maturity_block_gte = sgqlc.types.Field(BigInt, graphql_name='maturityBlock_gte')
    maturity_block_lte = sgqlc.types.Field(BigInt, graphql_name='maturityBlock_lte')
    maturity_block_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='maturityBlock_in')
    maturity_block_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='maturityBlock_not_in')
    side = sgqlc.types.Field(InterestRateSide, graphql_name='side')
    side_not = sgqlc.types.Field(InterestRateSide, graphql_name='side_not')
    side_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(InterestRateSide)), graphql_name='side_in')
    side_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(InterestRateSide)), graphql_name='side_not_in')
    type = sgqlc.types.Field(InterestRateType, graphql_name='type')
    type_not = sgqlc.types.Field(InterestRateType, graphql_name='type_not')
    type_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(InterestRateType)), graphql_name='type_in')
    type_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(InterestRateType)), graphql_name='type_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class LendingProtocol_filter(sgqlc.types.Input):
    __schema__ = subgraph_status_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'name', 'name_not', 'name_gt', 'name_lt', 'name_gte', 'name_lte', 'name_in', 'name_not_in', 'name_contains', 'name_contains_nocase', 'name_not_contains', 'name_not_contains_nocase', 'name_starts_with', 'name_starts_with_nocase', 'name_not_starts_with', 'name_not_starts_with_nocase', 'name_ends_with', 'name_ends_with_nocase', 'name_not_ends_with', 'name_not_ends_with_nocase', 'slug', 'slug_not', 'slug_gt', 'slug_lt', 'slug_gte', 'slug_lte', 'slug_in', 'slug_not_in', 'slug_contains', 'slug_contains_nocase', 'slug_not_contains', 'slug_not_contains_nocase', 'slug_starts_with', 'slug_starts_with_nocase', 'slug_not_starts_with', 'slug_not_starts_with_nocase', 'slug_ends_with', 'slug_ends_with_nocase', 'slug_not_ends_with', 'slug_not_ends_with_nocase', 'schema_version', 'schema_version_not', 'schema_version_gt', 'schema_version_lt', 'schema_version_gte', 'schema_version_lte', 'schema_version_in', 'schema_version_not_in', 'schema_version_contains', 'schema_version_contains_nocase', 'schema_version_not_contains', 'schema_version_not_contains_nocase', 'schema_version_starts_with', 'schema_version_starts_with_nocase', 'schema_version_not_starts_with', 'schema_version_not_starts_with_nocase', 'schema_version_ends_with', 'schema_version_ends_with_nocase', 'schema_version_not_ends_with', 'schema_version_not_ends_with_nocase', 'subgraph_version', 'subgraph_version_not', 'subgraph_version_gt', 'subgraph_version_lt', 'subgraph_version_gte', 'subgraph_version_lte', 'subgraph_version_in', 'subgraph_version_not_in', 'subgraph_version_contains', 'subgraph_version_contains_nocase', 'subgraph_version_not_contains', 'subgraph_version_not_contains_nocase', 'subgraph_version_starts_with', 'subgraph_version_starts_with_nocase', 'subgraph_version_not_starts_with', 'subgraph_version_not_starts_with_nocase', 'subgraph_version_ends_with', 'subgraph_version_ends_with_nocase', 'subgraph_version_not_ends_with', 'subgraph_version_not_ends_with_nocase', 'methodology_version', 'methodology_version_not', 'methodology_version_gt', 'methodology_version_lt', 'methodology_version_gte', 'methodology_version_lte', 'methodology_version_in', 'methodology_version_not_in', 'methodology_version_contains', 'methodology_version_contains_nocase', 'methodology_version_not_contains', 'methodology_version_not_contains_nocase', 'methodology_version_starts_with', 'methodology_version_starts_with_nocase', 'methodology_version_not_starts_with', 'methodology_version_not_starts_with_nocase', 'methodology_version_ends_with', 'methodology_version_ends_with_nocase', 'methodology_version_not_ends_with', 'methodology_version_not_ends_with_nocase', 'network', 'network_not', 'network_in', 'network_not_in', 'type', 'type_not', 'type_in', 'type_not_in', 'lending_type', 'lending_type_not', 'lending_type_in', 'lending_type_not_in', 'risk_type', 'risk_type_not', 'risk_type_in', 'risk_type_not_in', 'minted_tokens', 'minted_tokens_not', 'minted_tokens_contains', 'minted_tokens_contains_nocase', 'minted_tokens_not_contains', 'minted_tokens_not_contains_nocase', 'cumulative_unique_users', 'cumulative_unique_users_not', 'cumulative_unique_users_gt', 'cumulative_unique_users_lt', 'cumulative_unique_users_gte', 'cumulative_unique_users_lte', 'cumulative_unique_users_in', 'cumulative_unique_users_not_in', 'total_value_locked_usd', 'total_value_locked_usd_not', 'total_value_locked_usd_gt', 'total_value_locked_usd_lt', 'total_value_locked_usd_gte', 'total_value_locked_usd_lte', 'total_value_locked_usd_in', 'total_value_locked_usd_not_in', 'protocol_controlled_value_usd', 'protocol_controlled_value_usd_not', 'protocol_controlled_value_usd_gt', 'protocol_controlled_value_usd_lt', 'protocol_controlled_value_usd_gte', 'protocol_controlled_value_usd_lte', 'protocol_controlled_value_usd_in', 'protocol_controlled_value_usd_not_in', 'cumulative_supply_side_revenue_usd', 'cumulative_supply_side_revenue_usd_not', 'cumulative_supply_side_revenue_usd_gt', 'cumulative_supply_side_revenue_usd_lt', 'cumulative_supply_side_revenue_usd_gte', 'cumulative_supply_side_revenue_usd_lte', 'cumulative_supply_side_revenue_usd_in', 'cumulative_supply_side_revenue_usd_not_in', 'cumulative_protocol_side_revenue_usd', 'cumulative_protocol_side_revenue_usd_not', 'cumulative_protocol_side_revenue_usd_gt', 'cumulative_protocol_side_revenue_usd_lt', 'cumulative_protocol_side_revenue_usd_gte', 'cumulative_protocol_side_revenue_usd_lte', 'cumulative_protocol_side_revenue_usd_in', 'cumulative_protocol_side_revenue_usd_not_in', 'cumulative_total_revenue_usd', 'cumulative_total_revenue_usd_not', 'cumulative_total_revenue_usd_gt', 'cumulative_total_revenue_usd_lt', 'cumulative_total_revenue_usd_gte', 'cumulative_total_revenue_usd_lte', 'cumulative_total_revenue_usd_in', 'cumulative_total_revenue_usd_not_in', 'total_deposit_balance_usd', 'total_deposit_balance_usd_not', 'total_deposit_balance_usd_gt', 'total_deposit_balance_usd_lt', 'total_deposit_balance_usd_gte', 'total_deposit_balance_usd_lte', 'total_deposit_balance_usd_in', 'total_deposit_balance_usd_not_in', 'cumulative_deposit_usd', 'cumulative_deposit_usd_not', 'cumulative_deposit_usd_gt', 'cumulative_deposit_usd_lt', 'cumulative_deposit_usd_gte', 'cumulative_deposit_usd_lte', 'cumulative_deposit_usd_in', 'cumulative_deposit_usd_not_in', 'total_borrow_balance_usd', 'total_borrow_balance_usd_not', 'total_borrow_balance_usd_gt', 'total_borrow_balance_usd_lt', 'total_borrow_balance_usd_gte', 'total_borrow_balance_usd_lte', 'total_borrow_balance_usd_in', 'total_borrow_balance_usd_not_in', 'cumulative_borrow_usd', 'cumulative_borrow_usd_not', 'cumulative_borrow_usd_gt', 'cumulative_borrow_usd_lt', 'cumulative_borrow_usd_gte', 'cumulative_borrow_usd_lte', 'cumulative_borrow_usd_in', 'cumulative_borrow_usd_not_in', 'cumulative_liquidate_usd', 'cumulative_liquidate_usd_not', 'cumulative_liquidate_usd_gt', 'cumulative_liquidate_usd_lt', 'cumulative_liquidate_usd_gte', 'cumulative_liquidate_usd_lte', 'cumulative_liquidate_usd_in', 'cumulative_liquidate_usd_not_in', 'minted_token_supplies', 'minted_token_supplies_not', 'minted_token_supplies_contains', 'minted_token_supplies_contains_nocase', 'minted_token_supplies_not_contains', 'minted_token_supplies_not_contains_nocase', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_not = sgqlc.types.Field(String, graphql_name='name_not')
    name_gt = sgqlc.types.Field(String, graphql_name='name_gt')
    name_lt = sgqlc.types.Field(String, graphql_name='name_lt')
    name_gte = sgqlc.types.Field(String, graphql_name='name_gte')
    name_lte = sgqlc.types.Field(String, graphql_name='name_lte')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='name_in')
    name_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='name_not_in')
    name_contains = sgqlc.types.Field(String, graphql_name='name_contains')
    name_contains_nocase = sgqlc.types.Field(String, graphql_name='name_contains_nocase')
    name_not_contains = sgqlc.types.Field(String, graphql_name='name_not_contains')
    name_not_contains_nocase = sgqlc.types.Field(String, graphql_name='name_not_contains_nocase')
    name_starts_with = sgqlc.types.Field(String, graphql_name='name_starts_with')
    name_starts_with_nocase = sgqlc.types.Field(String, graphql_name='name_starts_with_nocase')
    name_not_starts_with = sgqlc.types.Field(String, graphql_name='name_not_starts_with')
    name_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='name_not_starts_with_nocase')
    name_ends_with = sgqlc.types.Field(String, graphql_name='name_ends_with')
    name_ends_with_nocase = sgqlc.types.Field(String, graphql_name='name_ends_with_nocase')
    name_not_ends_with = sgqlc.types.Field(String, graphql_name='name_not_ends_with')
    name_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='name_not_ends_with_nocase')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    slug_not = sgqlc.types.Field(String, graphql_name='slug_not')
    slug_gt = sgqlc.types.Field(String, graphql_name='slug_gt')
    slug_lt = sgqlc.types.Field(String, graphql_name='slug_lt')
    slug_gte = sgqlc.types.Field(String, graphql_name='slug_gte')
    slug_lte = sgqlc.types.Field(String, graphql_name='slug_lte')
    slug_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='slug_in')
    slug_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='slug_not_in')
    slug_contains = sgqlc.types.Field(String, graphql_name='slug_contains')
    slug_contains_nocase = sgqlc.types.Field(String, graphql_name='slug_contains_nocase')
    slug_not_contains = sgqlc.types.Field(String, graphql_name='slug_not_contains')
    slug_not_contains_nocase = sgqlc.types.Field(String, graphql_name='slug_not_contains_nocase')
    slug_starts_with = sgqlc.types.Field(String, graphql_name='slug_starts_with')
    slug_starts_with_nocase = sgqlc.types.Field(String, graphql_name='slug_starts_with_nocase')
    slug_not_starts_with = sgqlc.types.Field(String, graphql_name='slug_not_starts_with')
    slug_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='slug_not_starts_with_nocase')
    slug_ends_with = sgqlc.types.Field(String, graphql_name='slug_ends_with')
    slug_ends_with_nocase = sgqlc.types.Field(String, graphql_name='slug_ends_with_nocase')
    slug_not_ends_with = sgqlc.types.Field(String, graphql_name='slug_not_ends_with')
    slug_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='slug_not_ends_with_nocase')
    schema_version = sgqlc.types.Field(String, graphql_name='schemaVersion')
    schema_version_not = sgqlc.types.Field(String, graphql_name='schemaVersion_not')
    schema_version_gt = sgqlc.types.Field(String, graphql_name='schemaVersion_gt')
    schema_version_lt = sgqlc.types.Field(String, graphql_name='schemaVersion_lt')
    schema_version_gte = sgqlc.types.Field(String, graphql_name='schemaVersion_gte')
    schema_version_lte = sgqlc.types.Field(String, graphql_name='schemaVersion_lte')
    schema_version_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='schemaVersion_in')
    schema_version_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='schemaVersion_not_in')
    schema_version_contains = sgqlc.types.Field(String, graphql_name='schemaVersion_contains')
    schema_version_contains_nocase = sgqlc.types.Field(String, graphql_name='schemaVersion_contains_nocase')
    schema_version_not_contains = sgqlc.types.Field(String, graphql_name='schemaVersion_not_contains')
    schema_version_not_contains_nocase = sgqlc.types.Field(String, graphql_name='schemaVersion_not_contains_nocase')
    schema_version_starts_with = sgqlc.types.Field(String, graphql_name='schemaVersion_starts_with')
    schema_version_starts_with_nocase = sgqlc.types.Field(String, graphql_name='schemaVersion_starts_with_nocase')
    schema_version_not_starts_with = sgqlc.types.Field(String, graphql_name='schemaVersion_not_starts_with')
    schema_version_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='schemaVersion_not_starts_with_nocase')
    schema_version_ends_with = sgqlc.types.Field(String, graphql_name='schemaVersion_ends_with')
    schema_version_ends_with_nocase = sgqlc.types.Field(String, graphql_name='schemaVersion_ends_with_nocase')
    schema_version_not_ends_with = sgqlc.types.Field(String, graphql_name='schemaVersion_not_ends_with')
    schema_version_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='schemaVersion_not_ends_with_nocase')
    subgraph_version = sgqlc.types.Field(String, graphql_name='subgraphVersion')
    subgraph_version_not = sgqlc.types.Field(String, graphql_name='subgraphVersion_not')
    subgraph_version_gt = sgqlc.types.Field(String, graphql_name='subgraphVersion_gt')
    subgraph_version_lt = sgqlc.types.Field(String, graphql_name='subgraphVersion_lt')
    subgraph_version_gte = sgqlc.types.Field(String, graphql_name='subgraphVersion_gte')
    subgraph_version_lte = sgqlc.types.Field(String, graphql_name='subgraphVersion_lte')
    subgraph_version_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='subgraphVersion_in')
    subgraph_version_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='subgraphVersion_not_in')
    subgraph_version_contains = sgqlc.types.Field(String, graphql_name='subgraphVersion_contains')
    subgraph_version_contains_nocase = sgqlc.types.Field(String, graphql_name='subgraphVersion_contains_nocase')
    subgraph_version_not_contains = sgqlc.types.Field(String, graphql_name='subgraphVersion_not_contains')
    subgraph_version_not_contains_nocase = sgqlc.types.Field(String, graphql_name='subgraphVersion_not_contains_nocase')
    subgraph_version_starts_with = sgqlc.types.Field(String, graphql_name='subgraphVersion_starts_with')
    subgraph_version_starts_with_nocase = sgqlc.types.Field(String, graphql_name='subgraphVersion_starts_with_nocase')
    subgraph_version_not_starts_with = sgqlc.types.Field(String, graphql_name='subgraphVersion_not_starts_with')
    subgraph_version_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='subgraphVersion_not_starts_with_nocase')
    subgraph_version_ends_with = sgqlc.types.Field(String, graphql_name='subgraphVersion_ends_with')
    subgraph_version_ends_with_nocase = sgqlc.types.Field(String, graphql_name='subgraphVersion_ends_with_nocase')
    subgraph_version_not_ends_with = sgqlc.types.Field(String, graphql_name='subgraphVersion_not_ends_with')
    subgraph_version_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='subgraphVersion_not_ends_with_nocase')
    methodology_version = sgqlc.types.Field(String, graphql_name='methodologyVersion')
    methodology_version_not = sgqlc.types.Field(String, graphql_name='methodologyVersion_not')
    methodology_version_gt = sgqlc.types.Field(String, graphql_name='methodologyVersion_gt')
    methodology_version_lt = sgqlc.types.Field(String, graphql_name='methodologyVersion_lt')
    methodology_version_gte = sgqlc.types.Field(String, graphql_name='methodologyVersion_gte')
    methodology_version_lte = sgqlc.types.Field(String, graphql_name='methodologyVersion_lte')
    methodology_version_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='methodologyVersion_in')
    methodology_version_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='methodologyVersion_not_in')
    methodology_version_contains = sgqlc.types.Field(String, graphql_name='methodologyVersion_contains')
    methodology_version_contains_nocase = sgqlc.types.Field(String, graphql_name='methodologyVersion_contains_nocase')
    methodology_version_not_contains = sgqlc.types.Field(String, graphql_name='methodologyVersion_not_contains')
    methodology_version_not_contains_nocase = sgqlc.types.Field(String, graphql_name='methodologyVersion_not_contains_nocase')
    methodology_version_starts_with = sgqlc.types.Field(String, graphql_name='methodologyVersion_starts_with')
    methodology_version_starts_with_nocase = sgqlc.types.Field(String, graphql_name='methodologyVersion_starts_with_nocase')
    methodology_version_not_starts_with = sgqlc.types.Field(String, graphql_name='methodologyVersion_not_starts_with')
    methodology_version_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='methodologyVersion_not_starts_with_nocase')
    methodology_version_ends_with = sgqlc.types.Field(String, graphql_name='methodologyVersion_ends_with')
    methodology_version_ends_with_nocase = sgqlc.types.Field(String, graphql_name='methodologyVersion_ends_with_nocase')
    methodology_version_not_ends_with = sgqlc.types.Field(String, graphql_name='methodologyVersion_not_ends_with')
    methodology_version_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='methodologyVersion_not_ends_with_nocase')
    network = sgqlc.types.Field(Network, graphql_name='network')
    network_not = sgqlc.types.Field(Network, graphql_name='network_not')
    network_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Network)), graphql_name='network_in')
    network_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Network)), graphql_name='network_not_in')
    type = sgqlc.types.Field(ProtocolType, graphql_name='type')
    type_not = sgqlc.types.Field(ProtocolType, graphql_name='type_not')
    type_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ProtocolType)), graphql_name='type_in')
    type_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ProtocolType)), graphql_name='type_not_in')
    lending_type = sgqlc.types.Field(LendingType, graphql_name='lendingType')
    lending_type_not = sgqlc.types.Field(LendingType, graphql_name='lendingType_not')
    lending_type_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(LendingType)), graphql_name='lendingType_in')
    lending_type_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(LendingType)), graphql_name='lendingType_not_in')
    risk_type = sgqlc.types.Field(RiskType, graphql_name='riskType')
    risk_type_not = sgqlc.types.Field(RiskType, graphql_name='riskType_not')
    risk_type_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RiskType)), graphql_name='riskType_in')
    risk_type_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RiskType)), graphql_name='riskType_not_in')
    minted_tokens = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='mintedTokens')
    minted_tokens_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='mintedTokens_not')
    minted_tokens_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='mintedTokens_contains')
    minted_tokens_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='mintedTokens_contains_nocase')
    minted_tokens_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='mintedTokens_not_contains')
    minted_tokens_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='mintedTokens_not_contains_nocase')
    cumulative_unique_users = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers')
    cumulative_unique_users_not = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_not')
    cumulative_unique_users_gt = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_gt')
    cumulative_unique_users_lt = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_lt')
    cumulative_unique_users_gte = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_gte')
    cumulative_unique_users_lte = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_lte')
    cumulative_unique_users_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='cumulativeUniqueUsers_in')
    cumulative_unique_users_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='cumulativeUniqueUsers_not_in')
    total_value_locked_usd = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD')
    total_value_locked_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_not')
    total_value_locked_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gt')
    total_value_locked_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lt')
    total_value_locked_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gte')
    total_value_locked_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lte')
    total_value_locked_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_in')
    total_value_locked_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_not_in')
    protocol_controlled_value_usd = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD')
    protocol_controlled_value_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD_not')
    protocol_controlled_value_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD_gt')
    protocol_controlled_value_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD_lt')
    protocol_controlled_value_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD_gte')
    protocol_controlled_value_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD_lte')
    protocol_controlled_value_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='protocolControlledValueUSD_in')
    protocol_controlled_value_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='protocolControlledValueUSD_not_in')
    cumulative_supply_side_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD')
    cumulative_supply_side_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_not')
    cumulative_supply_side_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_gt')
    cumulative_supply_side_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_lt')
    cumulative_supply_side_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_gte')
    cumulative_supply_side_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_lte')
    cumulative_supply_side_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeSupplySideRevenueUSD_in')
    cumulative_supply_side_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeSupplySideRevenueUSD_not_in')
    cumulative_protocol_side_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD')
    cumulative_protocol_side_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_not')
    cumulative_protocol_side_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_gt')
    cumulative_protocol_side_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_lt')
    cumulative_protocol_side_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_gte')
    cumulative_protocol_side_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_lte')
    cumulative_protocol_side_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeProtocolSideRevenueUSD_in')
    cumulative_protocol_side_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeProtocolSideRevenueUSD_not_in')
    cumulative_total_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD')
    cumulative_total_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_not')
    cumulative_total_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_gt')
    cumulative_total_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_lt')
    cumulative_total_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_gte')
    cumulative_total_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_lte')
    cumulative_total_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeTotalRevenueUSD_in')
    cumulative_total_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeTotalRevenueUSD_not_in')
    total_deposit_balance_usd = sgqlc.types.Field(BigDecimal, graphql_name='totalDepositBalanceUSD')
    total_deposit_balance_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='totalDepositBalanceUSD_not')
    total_deposit_balance_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalDepositBalanceUSD_gt')
    total_deposit_balance_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalDepositBalanceUSD_lt')
    total_deposit_balance_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalDepositBalanceUSD_gte')
    total_deposit_balance_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalDepositBalanceUSD_lte')
    total_deposit_balance_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalDepositBalanceUSD_in')
    total_deposit_balance_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalDepositBalanceUSD_not_in')
    cumulative_deposit_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeDepositUSD')
    cumulative_deposit_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeDepositUSD_not')
    cumulative_deposit_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeDepositUSD_gt')
    cumulative_deposit_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeDepositUSD_lt')
    cumulative_deposit_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeDepositUSD_gte')
    cumulative_deposit_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeDepositUSD_lte')
    cumulative_deposit_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeDepositUSD_in')
    cumulative_deposit_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeDepositUSD_not_in')
    total_borrow_balance_usd = sgqlc.types.Field(BigDecimal, graphql_name='totalBorrowBalanceUSD')
    total_borrow_balance_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='totalBorrowBalanceUSD_not')
    total_borrow_balance_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalBorrowBalanceUSD_gt')
    total_borrow_balance_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalBorrowBalanceUSD_lt')
    total_borrow_balance_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalBorrowBalanceUSD_gte')
    total_borrow_balance_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalBorrowBalanceUSD_lte')
    total_borrow_balance_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalBorrowBalanceUSD_in')
    total_borrow_balance_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalBorrowBalanceUSD_not_in')
    cumulative_borrow_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeBorrowUSD')
    cumulative_borrow_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeBorrowUSD_not')
    cumulative_borrow_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeBorrowUSD_gt')
    cumulative_borrow_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeBorrowUSD_lt')
    cumulative_borrow_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeBorrowUSD_gte')
    cumulative_borrow_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeBorrowUSD_lte')
    cumulative_borrow_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeBorrowUSD_in')
    cumulative_borrow_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeBorrowUSD_not_in')
    cumulative_liquidate_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeLiquidateUSD')
    cumulative_liquidate_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeLiquidateUSD_not')
    cumulative_liquidate_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeLiquidateUSD_gt')
    cumulative_liquidate_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeLiquidateUSD_lt')
    cumulative_liquidate_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeLiquidateUSD_gte')
    cumulative_liquidate_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeLiquidateUSD_lte')
    cumulative_liquidate_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeLiquidateUSD_in')
    cumulative_liquidate_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeLiquidateUSD_not_in')
    minted_token_supplies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='mintedTokenSupplies')
    minted_token_supplies_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='mintedTokenSupplies_not')
    minted_token_supplies_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='mintedTokenSupplies_contains')
    minted_token_supplies_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='mintedTokenSupplies_contains_nocase')
    minted_token_supplies_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='mintedTokenSupplies_not_contains')
    minted_token_supplies_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='mintedTokenSupplies_not_contains_nocase')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class Liquidate_filter(sgqlc.types.Input):
    __schema__ = subgraph_status_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'hash', 'hash_not', 'hash_gt', 'hash_lt', 'hash_gte', 'hash_lte', 'hash_in', 'hash_not_in', 'hash_contains', 'hash_contains_nocase', 'hash_not_contains', 'hash_not_contains_nocase', 'hash_starts_with', 'hash_starts_with_nocase', 'hash_not_starts_with', 'hash_not_starts_with_nocase', 'hash_ends_with', 'hash_ends_with_nocase', 'hash_not_ends_with', 'hash_not_ends_with_nocase', 'log_index', 'log_index_not', 'log_index_gt', 'log_index_lt', 'log_index_gte', 'log_index_lte', 'log_index_in', 'log_index_not_in', 'protocol', 'protocol_not', 'protocol_gt', 'protocol_lt', 'protocol_gte', 'protocol_lte', 'protocol_in', 'protocol_not_in', 'protocol_contains', 'protocol_contains_nocase', 'protocol_not_contains', 'protocol_not_contains_nocase', 'protocol_starts_with', 'protocol_starts_with_nocase', 'protocol_not_starts_with', 'protocol_not_starts_with_nocase', 'protocol_ends_with', 'protocol_ends_with_nocase', 'protocol_not_ends_with', 'protocol_not_ends_with_nocase', 'to', 'to_not', 'to_gt', 'to_lt', 'to_gte', 'to_lte', 'to_in', 'to_not_in', 'to_contains', 'to_contains_nocase', 'to_not_contains', 'to_not_contains_nocase', 'to_starts_with', 'to_starts_with_nocase', 'to_not_starts_with', 'to_not_starts_with_nocase', 'to_ends_with', 'to_ends_with_nocase', 'to_not_ends_with', 'to_not_ends_with_nocase', 'from_', 'from_not', 'from_gt', 'from_lt', 'from_gte', 'from_lte', 'from_in', 'from_not_in', 'from_contains', 'from_contains_nocase', 'from_not_contains', 'from_not_contains_nocase', 'from_starts_with', 'from_starts_with_nocase', 'from_not_starts_with', 'from_not_starts_with_nocase', 'from_ends_with', 'from_ends_with_nocase', 'from_not_ends_with', 'from_not_ends_with_nocase', 'block_number', 'block_number_not', 'block_number_gt', 'block_number_lt', 'block_number_gte', 'block_number_lte', 'block_number_in', 'block_number_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'market', 'market_not', 'market_gt', 'market_lt', 'market_gte', 'market_lte', 'market_in', 'market_not_in', 'market_contains', 'market_contains_nocase', 'market_not_contains', 'market_not_contains_nocase', 'market_starts_with', 'market_starts_with_nocase', 'market_not_starts_with', 'market_not_starts_with_nocase', 'market_ends_with', 'market_ends_with_nocase', 'market_not_ends_with', 'market_not_ends_with_nocase', 'asset', 'asset_not', 'asset_gt', 'asset_lt', 'asset_gte', 'asset_lte', 'asset_in', 'asset_not_in', 'asset_contains', 'asset_contains_nocase', 'asset_not_contains', 'asset_not_contains_nocase', 'asset_starts_with', 'asset_starts_with_nocase', 'asset_not_starts_with', 'asset_not_starts_with_nocase', 'asset_ends_with', 'asset_ends_with_nocase', 'asset_not_ends_with', 'asset_not_ends_with_nocase', 'amount', 'amount_not', 'amount_gt', 'amount_lt', 'amount_gte', 'amount_lte', 'amount_in', 'amount_not_in', 'amount_usd', 'amount_usd_not', 'amount_usd_gt', 'amount_usd_lt', 'amount_usd_gte', 'amount_usd_lte', 'amount_usd_in', 'amount_usd_not_in', 'profit_usd', 'profit_usd_not', 'profit_usd_gt', 'profit_usd_lt', 'profit_usd_gte', 'profit_usd_lte', 'profit_usd_in', 'profit_usd_not_in', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    hash_not = sgqlc.types.Field(String, graphql_name='hash_not')
    hash_gt = sgqlc.types.Field(String, graphql_name='hash_gt')
    hash_lt = sgqlc.types.Field(String, graphql_name='hash_lt')
    hash_gte = sgqlc.types.Field(String, graphql_name='hash_gte')
    hash_lte = sgqlc.types.Field(String, graphql_name='hash_lte')
    hash_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='hash_in')
    hash_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='hash_not_in')
    hash_contains = sgqlc.types.Field(String, graphql_name='hash_contains')
    hash_contains_nocase = sgqlc.types.Field(String, graphql_name='hash_contains_nocase')
    hash_not_contains = sgqlc.types.Field(String, graphql_name='hash_not_contains')
    hash_not_contains_nocase = sgqlc.types.Field(String, graphql_name='hash_not_contains_nocase')
    hash_starts_with = sgqlc.types.Field(String, graphql_name='hash_starts_with')
    hash_starts_with_nocase = sgqlc.types.Field(String, graphql_name='hash_starts_with_nocase')
    hash_not_starts_with = sgqlc.types.Field(String, graphql_name='hash_not_starts_with')
    hash_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='hash_not_starts_with_nocase')
    hash_ends_with = sgqlc.types.Field(String, graphql_name='hash_ends_with')
    hash_ends_with_nocase = sgqlc.types.Field(String, graphql_name='hash_ends_with_nocase')
    hash_not_ends_with = sgqlc.types.Field(String, graphql_name='hash_not_ends_with')
    hash_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='hash_not_ends_with_nocase')
    log_index = sgqlc.types.Field(Int, graphql_name='logIndex')
    log_index_not = sgqlc.types.Field(Int, graphql_name='logIndex_not')
    log_index_gt = sgqlc.types.Field(Int, graphql_name='logIndex_gt')
    log_index_lt = sgqlc.types.Field(Int, graphql_name='logIndex_lt')
    log_index_gte = sgqlc.types.Field(Int, graphql_name='logIndex_gte')
    log_index_lte = sgqlc.types.Field(Int, graphql_name='logIndex_lte')
    log_index_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='logIndex_in')
    log_index_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='logIndex_not_in')
    protocol = sgqlc.types.Field(String, graphql_name='protocol')
    protocol_not = sgqlc.types.Field(String, graphql_name='protocol_not')
    protocol_gt = sgqlc.types.Field(String, graphql_name='protocol_gt')
    protocol_lt = sgqlc.types.Field(String, graphql_name='protocol_lt')
    protocol_gte = sgqlc.types.Field(String, graphql_name='protocol_gte')
    protocol_lte = sgqlc.types.Field(String, graphql_name='protocol_lte')
    protocol_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_in')
    protocol_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_not_in')
    protocol_contains = sgqlc.types.Field(String, graphql_name='protocol_contains')
    protocol_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_contains_nocase')
    protocol_not_contains = sgqlc.types.Field(String, graphql_name='protocol_not_contains')
    protocol_not_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_contains_nocase')
    protocol_starts_with = sgqlc.types.Field(String, graphql_name='protocol_starts_with')
    protocol_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_starts_with_nocase')
    protocol_not_starts_with = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with')
    protocol_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with_nocase')
    protocol_ends_with = sgqlc.types.Field(String, graphql_name='protocol_ends_with')
    protocol_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_ends_with_nocase')
    protocol_not_ends_with = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with')
    protocol_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with_nocase')
    to = sgqlc.types.Field(String, graphql_name='to')
    to_not = sgqlc.types.Field(String, graphql_name='to_not')
    to_gt = sgqlc.types.Field(String, graphql_name='to_gt')
    to_lt = sgqlc.types.Field(String, graphql_name='to_lt')
    to_gte = sgqlc.types.Field(String, graphql_name='to_gte')
    to_lte = sgqlc.types.Field(String, graphql_name='to_lte')
    to_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='to_in')
    to_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='to_not_in')
    to_contains = sgqlc.types.Field(String, graphql_name='to_contains')
    to_contains_nocase = sgqlc.types.Field(String, graphql_name='to_contains_nocase')
    to_not_contains = sgqlc.types.Field(String, graphql_name='to_not_contains')
    to_not_contains_nocase = sgqlc.types.Field(String, graphql_name='to_not_contains_nocase')
    to_starts_with = sgqlc.types.Field(String, graphql_name='to_starts_with')
    to_starts_with_nocase = sgqlc.types.Field(String, graphql_name='to_starts_with_nocase')
    to_not_starts_with = sgqlc.types.Field(String, graphql_name='to_not_starts_with')
    to_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='to_not_starts_with_nocase')
    to_ends_with = sgqlc.types.Field(String, graphql_name='to_ends_with')
    to_ends_with_nocase = sgqlc.types.Field(String, graphql_name='to_ends_with_nocase')
    to_not_ends_with = sgqlc.types.Field(String, graphql_name='to_not_ends_with')
    to_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='to_not_ends_with_nocase')
    from_ = sgqlc.types.Field(String, graphql_name='from')
    from_not = sgqlc.types.Field(String, graphql_name='from_not')
    from_gt = sgqlc.types.Field(String, graphql_name='from_gt')
    from_lt = sgqlc.types.Field(String, graphql_name='from_lt')
    from_gte = sgqlc.types.Field(String, graphql_name='from_gte')
    from_lte = sgqlc.types.Field(String, graphql_name='from_lte')
    from_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='from_in')
    from_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='from_not_in')
    from_contains = sgqlc.types.Field(String, graphql_name='from_contains')
    from_contains_nocase = sgqlc.types.Field(String, graphql_name='from_contains_nocase')
    from_not_contains = sgqlc.types.Field(String, graphql_name='from_not_contains')
    from_not_contains_nocase = sgqlc.types.Field(String, graphql_name='from_not_contains_nocase')
    from_starts_with = sgqlc.types.Field(String, graphql_name='from_starts_with')
    from_starts_with_nocase = sgqlc.types.Field(String, graphql_name='from_starts_with_nocase')
    from_not_starts_with = sgqlc.types.Field(String, graphql_name='from_not_starts_with')
    from_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='from_not_starts_with_nocase')
    from_ends_with = sgqlc.types.Field(String, graphql_name='from_ends_with')
    from_ends_with_nocase = sgqlc.types.Field(String, graphql_name='from_ends_with_nocase')
    from_not_ends_with = sgqlc.types.Field(String, graphql_name='from_not_ends_with')
    from_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='from_not_ends_with_nocase')
    block_number = sgqlc.types.Field(BigInt, graphql_name='blockNumber')
    block_number_not = sgqlc.types.Field(BigInt, graphql_name='blockNumber_not')
    block_number_gt = sgqlc.types.Field(BigInt, graphql_name='blockNumber_gt')
    block_number_lt = sgqlc.types.Field(BigInt, graphql_name='blockNumber_lt')
    block_number_gte = sgqlc.types.Field(BigInt, graphql_name='blockNumber_gte')
    block_number_lte = sgqlc.types.Field(BigInt, graphql_name='blockNumber_lte')
    block_number_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='blockNumber_in')
    block_number_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='blockNumber_not_in')
    timestamp = sgqlc.types.Field(BigInt, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_not_in')
    market = sgqlc.types.Field(String, graphql_name='market')
    market_not = sgqlc.types.Field(String, graphql_name='market_not')
    market_gt = sgqlc.types.Field(String, graphql_name='market_gt')
    market_lt = sgqlc.types.Field(String, graphql_name='market_lt')
    market_gte = sgqlc.types.Field(String, graphql_name='market_gte')
    market_lte = sgqlc.types.Field(String, graphql_name='market_lte')
    market_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='market_in')
    market_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='market_not_in')
    market_contains = sgqlc.types.Field(String, graphql_name='market_contains')
    market_contains_nocase = sgqlc.types.Field(String, graphql_name='market_contains_nocase')
    market_not_contains = sgqlc.types.Field(String, graphql_name='market_not_contains')
    market_not_contains_nocase = sgqlc.types.Field(String, graphql_name='market_not_contains_nocase')
    market_starts_with = sgqlc.types.Field(String, graphql_name='market_starts_with')
    market_starts_with_nocase = sgqlc.types.Field(String, graphql_name='market_starts_with_nocase')
    market_not_starts_with = sgqlc.types.Field(String, graphql_name='market_not_starts_with')
    market_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='market_not_starts_with_nocase')
    market_ends_with = sgqlc.types.Field(String, graphql_name='market_ends_with')
    market_ends_with_nocase = sgqlc.types.Field(String, graphql_name='market_ends_with_nocase')
    market_not_ends_with = sgqlc.types.Field(String, graphql_name='market_not_ends_with')
    market_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='market_not_ends_with_nocase')
    asset = sgqlc.types.Field(String, graphql_name='asset')
    asset_not = sgqlc.types.Field(String, graphql_name='asset_not')
    asset_gt = sgqlc.types.Field(String, graphql_name='asset_gt')
    asset_lt = sgqlc.types.Field(String, graphql_name='asset_lt')
    asset_gte = sgqlc.types.Field(String, graphql_name='asset_gte')
    asset_lte = sgqlc.types.Field(String, graphql_name='asset_lte')
    asset_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='asset_in')
    asset_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='asset_not_in')
    asset_contains = sgqlc.types.Field(String, graphql_name='asset_contains')
    asset_contains_nocase = sgqlc.types.Field(String, graphql_name='asset_contains_nocase')
    asset_not_contains = sgqlc.types.Field(String, graphql_name='asset_not_contains')
    asset_not_contains_nocase = sgqlc.types.Field(String, graphql_name='asset_not_contains_nocase')
    asset_starts_with = sgqlc.types.Field(String, graphql_name='asset_starts_with')
    asset_starts_with_nocase = sgqlc.types.Field(String, graphql_name='asset_starts_with_nocase')
    asset_not_starts_with = sgqlc.types.Field(String, graphql_name='asset_not_starts_with')
    asset_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='asset_not_starts_with_nocase')
    asset_ends_with = sgqlc.types.Field(String, graphql_name='asset_ends_with')
    asset_ends_with_nocase = sgqlc.types.Field(String, graphql_name='asset_ends_with_nocase')
    asset_not_ends_with = sgqlc.types.Field(String, graphql_name='asset_not_ends_with')
    asset_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='asset_not_ends_with_nocase')
    amount = sgqlc.types.Field(BigInt, graphql_name='amount')
    amount_not = sgqlc.types.Field(BigInt, graphql_name='amount_not')
    amount_gt = sgqlc.types.Field(BigInt, graphql_name='amount_gt')
    amount_lt = sgqlc.types.Field(BigInt, graphql_name='amount_lt')
    amount_gte = sgqlc.types.Field(BigInt, graphql_name='amount_gte')
    amount_lte = sgqlc.types.Field(BigInt, graphql_name='amount_lte')
    amount_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='amount_in')
    amount_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='amount_not_in')
    amount_usd = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD')
    amount_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_not')
    amount_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_gt')
    amount_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_lt')
    amount_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_gte')
    amount_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_lte')
    amount_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amountUSD_in')
    amount_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amountUSD_not_in')
    profit_usd = sgqlc.types.Field(BigDecimal, graphql_name='profitUSD')
    profit_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='profitUSD_not')
    profit_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='profitUSD_gt')
    profit_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='profitUSD_lt')
    profit_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='profitUSD_gte')
    profit_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='profitUSD_lte')
    profit_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='profitUSD_in')
    profit_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='profitUSD_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class MarketDailySnapshot_filter(sgqlc.types.Input):
    __schema__ = subgraph_status_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'protocol', 'protocol_not', 'protocol_gt', 'protocol_lt', 'protocol_gte', 'protocol_lte', 'protocol_in', 'protocol_not_in', 'protocol_contains', 'protocol_contains_nocase', 'protocol_not_contains', 'protocol_not_contains_nocase', 'protocol_starts_with', 'protocol_starts_with_nocase', 'protocol_not_starts_with', 'protocol_not_starts_with_nocase', 'protocol_ends_with', 'protocol_ends_with_nocase', 'protocol_not_ends_with', 'protocol_not_ends_with_nocase', 'market', 'market_not', 'market_gt', 'market_lt', 'market_gte', 'market_lte', 'market_in', 'market_not_in', 'market_contains', 'market_contains_nocase', 'market_not_contains', 'market_not_contains_nocase', 'market_starts_with', 'market_starts_with_nocase', 'market_not_starts_with', 'market_not_starts_with_nocase', 'market_ends_with', 'market_ends_with_nocase', 'market_not_ends_with', 'market_not_ends_with_nocase', 'block_number', 'block_number_not', 'block_number_gt', 'block_number_lt', 'block_number_gte', 'block_number_lte', 'block_number_in', 'block_number_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'rates', 'rates_not', 'rates_contains', 'rates_contains_nocase', 'rates_not_contains', 'rates_not_contains_nocase', 'total_value_locked_usd', 'total_value_locked_usd_not', 'total_value_locked_usd_gt', 'total_value_locked_usd_lt', 'total_value_locked_usd_gte', 'total_value_locked_usd_lte', 'total_value_locked_usd_in', 'total_value_locked_usd_not_in', 'total_deposit_balance_usd', 'total_deposit_balance_usd_not', 'total_deposit_balance_usd_gt', 'total_deposit_balance_usd_lt', 'total_deposit_balance_usd_gte', 'total_deposit_balance_usd_lte', 'total_deposit_balance_usd_in', 'total_deposit_balance_usd_not_in', 'daily_deposit_usd', 'daily_deposit_usd_not', 'daily_deposit_usd_gt', 'daily_deposit_usd_lt', 'daily_deposit_usd_gte', 'daily_deposit_usd_lte', 'daily_deposit_usd_in', 'daily_deposit_usd_not_in', 'cumulative_deposit_usd', 'cumulative_deposit_usd_not', 'cumulative_deposit_usd_gt', 'cumulative_deposit_usd_lt', 'cumulative_deposit_usd_gte', 'cumulative_deposit_usd_lte', 'cumulative_deposit_usd_in', 'cumulative_deposit_usd_not_in', 'total_borrow_balance_usd', 'total_borrow_balance_usd_not', 'total_borrow_balance_usd_gt', 'total_borrow_balance_usd_lt', 'total_borrow_balance_usd_gte', 'total_borrow_balance_usd_lte', 'total_borrow_balance_usd_in', 'total_borrow_balance_usd_not_in', 'daily_borrow_usd', 'daily_borrow_usd_not', 'daily_borrow_usd_gt', 'daily_borrow_usd_lt', 'daily_borrow_usd_gte', 'daily_borrow_usd_lte', 'daily_borrow_usd_in', 'daily_borrow_usd_not_in', 'cumulative_borrow_usd', 'cumulative_borrow_usd_not', 'cumulative_borrow_usd_gt', 'cumulative_borrow_usd_lt', 'cumulative_borrow_usd_gte', 'cumulative_borrow_usd_lte', 'cumulative_borrow_usd_in', 'cumulative_borrow_usd_not_in', 'daily_liquidate_usd', 'daily_liquidate_usd_not', 'daily_liquidate_usd_gt', 'daily_liquidate_usd_lt', 'daily_liquidate_usd_gte', 'daily_liquidate_usd_lte', 'daily_liquidate_usd_in', 'daily_liquidate_usd_not_in', 'cumulative_liquidate_usd', 'cumulative_liquidate_usd_not', 'cumulative_liquidate_usd_gt', 'cumulative_liquidate_usd_lt', 'cumulative_liquidate_usd_gte', 'cumulative_liquidate_usd_lte', 'cumulative_liquidate_usd_in', 'cumulative_liquidate_usd_not_in', 'input_token_balance', 'input_token_balance_not', 'input_token_balance_gt', 'input_token_balance_lt', 'input_token_balance_gte', 'input_token_balance_lte', 'input_token_balance_in', 'input_token_balance_not_in', 'input_token_price_usd', 'input_token_price_usd_not', 'input_token_price_usd_gt', 'input_token_price_usd_lt', 'input_token_price_usd_gte', 'input_token_price_usd_lte', 'input_token_price_usd_in', 'input_token_price_usd_not_in', 'output_token_supply', 'output_token_supply_not', 'output_token_supply_gt', 'output_token_supply_lt', 'output_token_supply_gte', 'output_token_supply_lte', 'output_token_supply_in', 'output_token_supply_not_in', 'output_token_price_usd', 'output_token_price_usd_not', 'output_token_price_usd_gt', 'output_token_price_usd_lt', 'output_token_price_usd_gte', 'output_token_price_usd_lte', 'output_token_price_usd_in', 'output_token_price_usd_not_in', 'exchange_rate', 'exchange_rate_not', 'exchange_rate_gt', 'exchange_rate_lt', 'exchange_rate_gte', 'exchange_rate_lte', 'exchange_rate_in', 'exchange_rate_not_in', 'reward_token_emissions_amount', 'reward_token_emissions_amount_not', 'reward_token_emissions_amount_contains', 'reward_token_emissions_amount_contains_nocase', 'reward_token_emissions_amount_not_contains', 'reward_token_emissions_amount_not_contains_nocase', 'reward_token_emissions_usd', 'reward_token_emissions_usd_not', 'reward_token_emissions_usd_contains', 'reward_token_emissions_usd_contains_nocase', 'reward_token_emissions_usd_not_contains', 'reward_token_emissions_usd_not_contains_nocase', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    protocol = sgqlc.types.Field(String, graphql_name='protocol')
    protocol_not = sgqlc.types.Field(String, graphql_name='protocol_not')
    protocol_gt = sgqlc.types.Field(String, graphql_name='protocol_gt')
    protocol_lt = sgqlc.types.Field(String, graphql_name='protocol_lt')
    protocol_gte = sgqlc.types.Field(String, graphql_name='protocol_gte')
    protocol_lte = sgqlc.types.Field(String, graphql_name='protocol_lte')
    protocol_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_in')
    protocol_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_not_in')
    protocol_contains = sgqlc.types.Field(String, graphql_name='protocol_contains')
    protocol_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_contains_nocase')
    protocol_not_contains = sgqlc.types.Field(String, graphql_name='protocol_not_contains')
    protocol_not_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_contains_nocase')
    protocol_starts_with = sgqlc.types.Field(String, graphql_name='protocol_starts_with')
    protocol_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_starts_with_nocase')
    protocol_not_starts_with = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with')
    protocol_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with_nocase')
    protocol_ends_with = sgqlc.types.Field(String, graphql_name='protocol_ends_with')
    protocol_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_ends_with_nocase')
    protocol_not_ends_with = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with')
    protocol_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with_nocase')
    market = sgqlc.types.Field(String, graphql_name='market')
    market_not = sgqlc.types.Field(String, graphql_name='market_not')
    market_gt = sgqlc.types.Field(String, graphql_name='market_gt')
    market_lt = sgqlc.types.Field(String, graphql_name='market_lt')
    market_gte = sgqlc.types.Field(String, graphql_name='market_gte')
    market_lte = sgqlc.types.Field(String, graphql_name='market_lte')
    market_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='market_in')
    market_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='market_not_in')
    market_contains = sgqlc.types.Field(String, graphql_name='market_contains')
    market_contains_nocase = sgqlc.types.Field(String, graphql_name='market_contains_nocase')
    market_not_contains = sgqlc.types.Field(String, graphql_name='market_not_contains')
    market_not_contains_nocase = sgqlc.types.Field(String, graphql_name='market_not_contains_nocase')
    market_starts_with = sgqlc.types.Field(String, graphql_name='market_starts_with')
    market_starts_with_nocase = sgqlc.types.Field(String, graphql_name='market_starts_with_nocase')
    market_not_starts_with = sgqlc.types.Field(String, graphql_name='market_not_starts_with')
    market_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='market_not_starts_with_nocase')
    market_ends_with = sgqlc.types.Field(String, graphql_name='market_ends_with')
    market_ends_with_nocase = sgqlc.types.Field(String, graphql_name='market_ends_with_nocase')
    market_not_ends_with = sgqlc.types.Field(String, graphql_name='market_not_ends_with')
    market_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='market_not_ends_with_nocase')
    block_number = sgqlc.types.Field(BigInt, graphql_name='blockNumber')
    block_number_not = sgqlc.types.Field(BigInt, graphql_name='blockNumber_not')
    block_number_gt = sgqlc.types.Field(BigInt, graphql_name='blockNumber_gt')
    block_number_lt = sgqlc.types.Field(BigInt, graphql_name='blockNumber_lt')
    block_number_gte = sgqlc.types.Field(BigInt, graphql_name='blockNumber_gte')
    block_number_lte = sgqlc.types.Field(BigInt, graphql_name='blockNumber_lte')
    block_number_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='blockNumber_in')
    block_number_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='blockNumber_not_in')
    timestamp = sgqlc.types.Field(BigInt, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_not_in')
    rates = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='rates')
    rates_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='rates_not')
    rates_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='rates_contains')
    rates_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='rates_contains_nocase')
    rates_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='rates_not_contains')
    rates_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='rates_not_contains_nocase')
    total_value_locked_usd = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD')
    total_value_locked_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_not')
    total_value_locked_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gt')
    total_value_locked_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lt')
    total_value_locked_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gte')
    total_value_locked_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lte')
    total_value_locked_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_in')
    total_value_locked_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_not_in')
    total_deposit_balance_usd = sgqlc.types.Field(BigDecimal, graphql_name='totalDepositBalanceUSD')
    total_deposit_balance_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='totalDepositBalanceUSD_not')
    total_deposit_balance_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalDepositBalanceUSD_gt')
    total_deposit_balance_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalDepositBalanceUSD_lt')
    total_deposit_balance_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalDepositBalanceUSD_gte')
    total_deposit_balance_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalDepositBalanceUSD_lte')
    total_deposit_balance_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalDepositBalanceUSD_in')
    total_deposit_balance_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalDepositBalanceUSD_not_in')
    daily_deposit_usd = sgqlc.types.Field(BigDecimal, graphql_name='dailyDepositUSD')
    daily_deposit_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='dailyDepositUSD_not')
    daily_deposit_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='dailyDepositUSD_gt')
    daily_deposit_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='dailyDepositUSD_lt')
    daily_deposit_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='dailyDepositUSD_gte')
    daily_deposit_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='dailyDepositUSD_lte')
    daily_deposit_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyDepositUSD_in')
    daily_deposit_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyDepositUSD_not_in')
    cumulative_deposit_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeDepositUSD')
    cumulative_deposit_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeDepositUSD_not')
    cumulative_deposit_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeDepositUSD_gt')
    cumulative_deposit_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeDepositUSD_lt')
    cumulative_deposit_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeDepositUSD_gte')
    cumulative_deposit_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeDepositUSD_lte')
    cumulative_deposit_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeDepositUSD_in')
    cumulative_deposit_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeDepositUSD_not_in')
    total_borrow_balance_usd = sgqlc.types.Field(BigDecimal, graphql_name='totalBorrowBalanceUSD')
    total_borrow_balance_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='totalBorrowBalanceUSD_not')
    total_borrow_balance_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalBorrowBalanceUSD_gt')
    total_borrow_balance_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalBorrowBalanceUSD_lt')
    total_borrow_balance_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalBorrowBalanceUSD_gte')
    total_borrow_balance_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalBorrowBalanceUSD_lte')
    total_borrow_balance_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalBorrowBalanceUSD_in')
    total_borrow_balance_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalBorrowBalanceUSD_not_in')
    daily_borrow_usd = sgqlc.types.Field(BigDecimal, graphql_name='dailyBorrowUSD')
    daily_borrow_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='dailyBorrowUSD_not')
    daily_borrow_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='dailyBorrowUSD_gt')
    daily_borrow_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='dailyBorrowUSD_lt')
    daily_borrow_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='dailyBorrowUSD_gte')
    daily_borrow_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='dailyBorrowUSD_lte')
    daily_borrow_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyBorrowUSD_in')
    daily_borrow_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyBorrowUSD_not_in')
    cumulative_borrow_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeBorrowUSD')
    cumulative_borrow_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeBorrowUSD_not')
    cumulative_borrow_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeBorrowUSD_gt')
    cumulative_borrow_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeBorrowUSD_lt')
    cumulative_borrow_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeBorrowUSD_gte')
    cumulative_borrow_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeBorrowUSD_lte')
    cumulative_borrow_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeBorrowUSD_in')
    cumulative_borrow_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeBorrowUSD_not_in')
    daily_liquidate_usd = sgqlc.types.Field(BigDecimal, graphql_name='dailyLiquidateUSD')
    daily_liquidate_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='dailyLiquidateUSD_not')
    daily_liquidate_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='dailyLiquidateUSD_gt')
    daily_liquidate_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='dailyLiquidateUSD_lt')
    daily_liquidate_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='dailyLiquidateUSD_gte')
    daily_liquidate_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='dailyLiquidateUSD_lte')
    daily_liquidate_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyLiquidateUSD_in')
    daily_liquidate_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyLiquidateUSD_not_in')
    cumulative_liquidate_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeLiquidateUSD')
    cumulative_liquidate_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeLiquidateUSD_not')
    cumulative_liquidate_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeLiquidateUSD_gt')
    cumulative_liquidate_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeLiquidateUSD_lt')
    cumulative_liquidate_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeLiquidateUSD_gte')
    cumulative_liquidate_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeLiquidateUSD_lte')
    cumulative_liquidate_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeLiquidateUSD_in')
    cumulative_liquidate_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeLiquidateUSD_not_in')
    input_token_balance = sgqlc.types.Field(BigInt, graphql_name='inputTokenBalance')
    input_token_balance_not = sgqlc.types.Field(BigInt, graphql_name='inputTokenBalance_not')
    input_token_balance_gt = sgqlc.types.Field(BigInt, graphql_name='inputTokenBalance_gt')
    input_token_balance_lt = sgqlc.types.Field(BigInt, graphql_name='inputTokenBalance_lt')
    input_token_balance_gte = sgqlc.types.Field(BigInt, graphql_name='inputTokenBalance_gte')
    input_token_balance_lte = sgqlc.types.Field(BigInt, graphql_name='inputTokenBalance_lte')
    input_token_balance_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenBalance_in')
    input_token_balance_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenBalance_not_in')
    input_token_price_usd = sgqlc.types.Field(BigDecimal, graphql_name='inputTokenPriceUSD')
    input_token_price_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='inputTokenPriceUSD_not')
    input_token_price_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='inputTokenPriceUSD_gt')
    input_token_price_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='inputTokenPriceUSD_lt')
    input_token_price_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='inputTokenPriceUSD_gte')
    input_token_price_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='inputTokenPriceUSD_lte')
    input_token_price_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='inputTokenPriceUSD_in')
    input_token_price_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='inputTokenPriceUSD_not_in')
    output_token_supply = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply')
    output_token_supply_not = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply_not')
    output_token_supply_gt = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply_gt')
    output_token_supply_lt = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply_lt')
    output_token_supply_gte = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply_gte')
    output_token_supply_lte = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply_lte')
    output_token_supply_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='outputTokenSupply_in')
    output_token_supply_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='outputTokenSupply_not_in')
    output_token_price_usd = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD')
    output_token_price_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD_not')
    output_token_price_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD_gt')
    output_token_price_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD_lt')
    output_token_price_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD_gte')
    output_token_price_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD_lte')
    output_token_price_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='outputTokenPriceUSD_in')
    output_token_price_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='outputTokenPriceUSD_not_in')
    exchange_rate = sgqlc.types.Field(BigDecimal, graphql_name='exchangeRate')
    exchange_rate_not = sgqlc.types.Field(BigDecimal, graphql_name='exchangeRate_not')
    exchange_rate_gt = sgqlc.types.Field(BigDecimal, graphql_name='exchangeRate_gt')
    exchange_rate_lt = sgqlc.types.Field(BigDecimal, graphql_name='exchangeRate_lt')
    exchange_rate_gte = sgqlc.types.Field(BigDecimal, graphql_name='exchangeRate_gte')
    exchange_rate_lte = sgqlc.types.Field(BigDecimal, graphql_name='exchangeRate_lte')
    exchange_rate_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='exchangeRate_in')
    exchange_rate_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='exchangeRate_not_in')
    reward_token_emissions_amount = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount')
    reward_token_emissions_amount_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount_not')
    reward_token_emissions_amount_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount_contains')
    reward_token_emissions_amount_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount_contains_nocase')
    reward_token_emissions_amount_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount_not_contains')
    reward_token_emissions_amount_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount_not_contains_nocase')
    reward_token_emissions_usd = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD')
    reward_token_emissions_usd_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD_not')
    reward_token_emissions_usd_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD_contains')
    reward_token_emissions_usd_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD_contains_nocase')
    reward_token_emissions_usd_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD_not_contains')
    reward_token_emissions_usd_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD_not_contains_nocase')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class MarketHourlySnapshot_filter(sgqlc.types.Input):
    __schema__ = subgraph_status_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'protocol', 'protocol_not', 'protocol_gt', 'protocol_lt', 'protocol_gte', 'protocol_lte', 'protocol_in', 'protocol_not_in', 'protocol_contains', 'protocol_contains_nocase', 'protocol_not_contains', 'protocol_not_contains_nocase', 'protocol_starts_with', 'protocol_starts_with_nocase', 'protocol_not_starts_with', 'protocol_not_starts_with_nocase', 'protocol_ends_with', 'protocol_ends_with_nocase', 'protocol_not_ends_with', 'protocol_not_ends_with_nocase', 'market', 'market_not', 'market_gt', 'market_lt', 'market_gte', 'market_lte', 'market_in', 'market_not_in', 'market_contains', 'market_contains_nocase', 'market_not_contains', 'market_not_contains_nocase', 'market_starts_with', 'market_starts_with_nocase', 'market_not_starts_with', 'market_not_starts_with_nocase', 'market_ends_with', 'market_ends_with_nocase', 'market_not_ends_with', 'market_not_ends_with_nocase', 'block_number', 'block_number_not', 'block_number_gt', 'block_number_lt', 'block_number_gte', 'block_number_lte', 'block_number_in', 'block_number_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'rates', 'rates_not', 'rates_contains', 'rates_contains_nocase', 'rates_not_contains', 'rates_not_contains_nocase', 'total_value_locked_usd', 'total_value_locked_usd_not', 'total_value_locked_usd_gt', 'total_value_locked_usd_lt', 'total_value_locked_usd_gte', 'total_value_locked_usd_lte', 'total_value_locked_usd_in', 'total_value_locked_usd_not_in', 'total_deposit_balance_usd', 'total_deposit_balance_usd_not', 'total_deposit_balance_usd_gt', 'total_deposit_balance_usd_lt', 'total_deposit_balance_usd_gte', 'total_deposit_balance_usd_lte', 'total_deposit_balance_usd_in', 'total_deposit_balance_usd_not_in', 'hourly_deposit_usd', 'hourly_deposit_usd_not', 'hourly_deposit_usd_gt', 'hourly_deposit_usd_lt', 'hourly_deposit_usd_gte', 'hourly_deposit_usd_lte', 'hourly_deposit_usd_in', 'hourly_deposit_usd_not_in', 'cumulative_deposit_usd', 'cumulative_deposit_usd_not', 'cumulative_deposit_usd_gt', 'cumulative_deposit_usd_lt', 'cumulative_deposit_usd_gte', 'cumulative_deposit_usd_lte', 'cumulative_deposit_usd_in', 'cumulative_deposit_usd_not_in', 'total_borrow_balance_usd', 'total_borrow_balance_usd_not', 'total_borrow_balance_usd_gt', 'total_borrow_balance_usd_lt', 'total_borrow_balance_usd_gte', 'total_borrow_balance_usd_lte', 'total_borrow_balance_usd_in', 'total_borrow_balance_usd_not_in', 'hourly_borrow_usd', 'hourly_borrow_usd_not', 'hourly_borrow_usd_gt', 'hourly_borrow_usd_lt', 'hourly_borrow_usd_gte', 'hourly_borrow_usd_lte', 'hourly_borrow_usd_in', 'hourly_borrow_usd_not_in', 'cumulative_borrow_usd', 'cumulative_borrow_usd_not', 'cumulative_borrow_usd_gt', 'cumulative_borrow_usd_lt', 'cumulative_borrow_usd_gte', 'cumulative_borrow_usd_lte', 'cumulative_borrow_usd_in', 'cumulative_borrow_usd_not_in', 'hourly_liquidate_usd', 'hourly_liquidate_usd_not', 'hourly_liquidate_usd_gt', 'hourly_liquidate_usd_lt', 'hourly_liquidate_usd_gte', 'hourly_liquidate_usd_lte', 'hourly_liquidate_usd_in', 'hourly_liquidate_usd_not_in', 'cumulative_liquidate_usd', 'cumulative_liquidate_usd_not', 'cumulative_liquidate_usd_gt', 'cumulative_liquidate_usd_lt', 'cumulative_liquidate_usd_gte', 'cumulative_liquidate_usd_lte', 'cumulative_liquidate_usd_in', 'cumulative_liquidate_usd_not_in', 'input_token_balance', 'input_token_balance_not', 'input_token_balance_gt', 'input_token_balance_lt', 'input_token_balance_gte', 'input_token_balance_lte', 'input_token_balance_in', 'input_token_balance_not_in', 'input_token_price_usd', 'input_token_price_usd_not', 'input_token_price_usd_gt', 'input_token_price_usd_lt', 'input_token_price_usd_gte', 'input_token_price_usd_lte', 'input_token_price_usd_in', 'input_token_price_usd_not_in', 'output_token_supply', 'output_token_supply_not', 'output_token_supply_gt', 'output_token_supply_lt', 'output_token_supply_gte', 'output_token_supply_lte', 'output_token_supply_in', 'output_token_supply_not_in', 'output_token_price_usd', 'output_token_price_usd_not', 'output_token_price_usd_gt', 'output_token_price_usd_lt', 'output_token_price_usd_gte', 'output_token_price_usd_lte', 'output_token_price_usd_in', 'output_token_price_usd_not_in', 'exchange_rate', 'exchange_rate_not', 'exchange_rate_gt', 'exchange_rate_lt', 'exchange_rate_gte', 'exchange_rate_lte', 'exchange_rate_in', 'exchange_rate_not_in', 'reward_token_emissions_amount', 'reward_token_emissions_amount_not', 'reward_token_emissions_amount_contains', 'reward_token_emissions_amount_contains_nocase', 'reward_token_emissions_amount_not_contains', 'reward_token_emissions_amount_not_contains_nocase', 'reward_token_emissions_usd', 'reward_token_emissions_usd_not', 'reward_token_emissions_usd_contains', 'reward_token_emissions_usd_contains_nocase', 'reward_token_emissions_usd_not_contains', 'reward_token_emissions_usd_not_contains_nocase', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    protocol = sgqlc.types.Field(String, graphql_name='protocol')
    protocol_not = sgqlc.types.Field(String, graphql_name='protocol_not')
    protocol_gt = sgqlc.types.Field(String, graphql_name='protocol_gt')
    protocol_lt = sgqlc.types.Field(String, graphql_name='protocol_lt')
    protocol_gte = sgqlc.types.Field(String, graphql_name='protocol_gte')
    protocol_lte = sgqlc.types.Field(String, graphql_name='protocol_lte')
    protocol_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_in')
    protocol_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_not_in')
    protocol_contains = sgqlc.types.Field(String, graphql_name='protocol_contains')
    protocol_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_contains_nocase')
    protocol_not_contains = sgqlc.types.Field(String, graphql_name='protocol_not_contains')
    protocol_not_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_contains_nocase')
    protocol_starts_with = sgqlc.types.Field(String, graphql_name='protocol_starts_with')
    protocol_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_starts_with_nocase')
    protocol_not_starts_with = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with')
    protocol_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with_nocase')
    protocol_ends_with = sgqlc.types.Field(String, graphql_name='protocol_ends_with')
    protocol_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_ends_with_nocase')
    protocol_not_ends_with = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with')
    protocol_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with_nocase')
    market = sgqlc.types.Field(String, graphql_name='market')
    market_not = sgqlc.types.Field(String, graphql_name='market_not')
    market_gt = sgqlc.types.Field(String, graphql_name='market_gt')
    market_lt = sgqlc.types.Field(String, graphql_name='market_lt')
    market_gte = sgqlc.types.Field(String, graphql_name='market_gte')
    market_lte = sgqlc.types.Field(String, graphql_name='market_lte')
    market_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='market_in')
    market_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='market_not_in')
    market_contains = sgqlc.types.Field(String, graphql_name='market_contains')
    market_contains_nocase = sgqlc.types.Field(String, graphql_name='market_contains_nocase')
    market_not_contains = sgqlc.types.Field(String, graphql_name='market_not_contains')
    market_not_contains_nocase = sgqlc.types.Field(String, graphql_name='market_not_contains_nocase')
    market_starts_with = sgqlc.types.Field(String, graphql_name='market_starts_with')
    market_starts_with_nocase = sgqlc.types.Field(String, graphql_name='market_starts_with_nocase')
    market_not_starts_with = sgqlc.types.Field(String, graphql_name='market_not_starts_with')
    market_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='market_not_starts_with_nocase')
    market_ends_with = sgqlc.types.Field(String, graphql_name='market_ends_with')
    market_ends_with_nocase = sgqlc.types.Field(String, graphql_name='market_ends_with_nocase')
    market_not_ends_with = sgqlc.types.Field(String, graphql_name='market_not_ends_with')
    market_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='market_not_ends_with_nocase')
    block_number = sgqlc.types.Field(BigInt, graphql_name='blockNumber')
    block_number_not = sgqlc.types.Field(BigInt, graphql_name='blockNumber_not')
    block_number_gt = sgqlc.types.Field(BigInt, graphql_name='blockNumber_gt')
    block_number_lt = sgqlc.types.Field(BigInt, graphql_name='blockNumber_lt')
    block_number_gte = sgqlc.types.Field(BigInt, graphql_name='blockNumber_gte')
    block_number_lte = sgqlc.types.Field(BigInt, graphql_name='blockNumber_lte')
    block_number_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='blockNumber_in')
    block_number_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='blockNumber_not_in')
    timestamp = sgqlc.types.Field(BigInt, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_not_in')
    rates = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='rates')
    rates_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='rates_not')
    rates_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='rates_contains')
    rates_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='rates_contains_nocase')
    rates_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='rates_not_contains')
    rates_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='rates_not_contains_nocase')
    total_value_locked_usd = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD')
    total_value_locked_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_not')
    total_value_locked_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gt')
    total_value_locked_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lt')
    total_value_locked_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gte')
    total_value_locked_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lte')
    total_value_locked_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_in')
    total_value_locked_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_not_in')
    total_deposit_balance_usd = sgqlc.types.Field(BigDecimal, graphql_name='totalDepositBalanceUSD')
    total_deposit_balance_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='totalDepositBalanceUSD_not')
    total_deposit_balance_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalDepositBalanceUSD_gt')
    total_deposit_balance_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalDepositBalanceUSD_lt')
    total_deposit_balance_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalDepositBalanceUSD_gte')
    total_deposit_balance_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalDepositBalanceUSD_lte')
    total_deposit_balance_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalDepositBalanceUSD_in')
    total_deposit_balance_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalDepositBalanceUSD_not_in')
    hourly_deposit_usd = sgqlc.types.Field(BigDecimal, graphql_name='hourlyDepositUSD')
    hourly_deposit_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='hourlyDepositUSD_not')
    hourly_deposit_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='hourlyDepositUSD_gt')
    hourly_deposit_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='hourlyDepositUSD_lt')
    hourly_deposit_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='hourlyDepositUSD_gte')
    hourly_deposit_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='hourlyDepositUSD_lte')
    hourly_deposit_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='hourlyDepositUSD_in')
    hourly_deposit_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='hourlyDepositUSD_not_in')
    cumulative_deposit_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeDepositUSD')
    cumulative_deposit_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeDepositUSD_not')
    cumulative_deposit_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeDepositUSD_gt')
    cumulative_deposit_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeDepositUSD_lt')
    cumulative_deposit_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeDepositUSD_gte')
    cumulative_deposit_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeDepositUSD_lte')
    cumulative_deposit_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeDepositUSD_in')
    cumulative_deposit_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeDepositUSD_not_in')
    total_borrow_balance_usd = sgqlc.types.Field(BigDecimal, graphql_name='totalBorrowBalanceUSD')
    total_borrow_balance_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='totalBorrowBalanceUSD_not')
    total_borrow_balance_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalBorrowBalanceUSD_gt')
    total_borrow_balance_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalBorrowBalanceUSD_lt')
    total_borrow_balance_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalBorrowBalanceUSD_gte')
    total_borrow_balance_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalBorrowBalanceUSD_lte')
    total_borrow_balance_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalBorrowBalanceUSD_in')
    total_borrow_balance_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalBorrowBalanceUSD_not_in')
    hourly_borrow_usd = sgqlc.types.Field(BigDecimal, graphql_name='hourlyBorrowUSD')
    hourly_borrow_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='hourlyBorrowUSD_not')
    hourly_borrow_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='hourlyBorrowUSD_gt')
    hourly_borrow_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='hourlyBorrowUSD_lt')
    hourly_borrow_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='hourlyBorrowUSD_gte')
    hourly_borrow_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='hourlyBorrowUSD_lte')
    hourly_borrow_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='hourlyBorrowUSD_in')
    hourly_borrow_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='hourlyBorrowUSD_not_in')
    cumulative_borrow_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeBorrowUSD')
    cumulative_borrow_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeBorrowUSD_not')
    cumulative_borrow_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeBorrowUSD_gt')
    cumulative_borrow_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeBorrowUSD_lt')
    cumulative_borrow_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeBorrowUSD_gte')
    cumulative_borrow_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeBorrowUSD_lte')
    cumulative_borrow_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeBorrowUSD_in')
    cumulative_borrow_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeBorrowUSD_not_in')
    hourly_liquidate_usd = sgqlc.types.Field(BigDecimal, graphql_name='hourlyLiquidateUSD')
    hourly_liquidate_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='hourlyLiquidateUSD_not')
    hourly_liquidate_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='hourlyLiquidateUSD_gt')
    hourly_liquidate_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='hourlyLiquidateUSD_lt')
    hourly_liquidate_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='hourlyLiquidateUSD_gte')
    hourly_liquidate_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='hourlyLiquidateUSD_lte')
    hourly_liquidate_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='hourlyLiquidateUSD_in')
    hourly_liquidate_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='hourlyLiquidateUSD_not_in')
    cumulative_liquidate_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeLiquidateUSD')
    cumulative_liquidate_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeLiquidateUSD_not')
    cumulative_liquidate_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeLiquidateUSD_gt')
    cumulative_liquidate_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeLiquidateUSD_lt')
    cumulative_liquidate_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeLiquidateUSD_gte')
    cumulative_liquidate_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeLiquidateUSD_lte')
    cumulative_liquidate_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeLiquidateUSD_in')
    cumulative_liquidate_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeLiquidateUSD_not_in')
    input_token_balance = sgqlc.types.Field(BigInt, graphql_name='inputTokenBalance')
    input_token_balance_not = sgqlc.types.Field(BigInt, graphql_name='inputTokenBalance_not')
    input_token_balance_gt = sgqlc.types.Field(BigInt, graphql_name='inputTokenBalance_gt')
    input_token_balance_lt = sgqlc.types.Field(BigInt, graphql_name='inputTokenBalance_lt')
    input_token_balance_gte = sgqlc.types.Field(BigInt, graphql_name='inputTokenBalance_gte')
    input_token_balance_lte = sgqlc.types.Field(BigInt, graphql_name='inputTokenBalance_lte')
    input_token_balance_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenBalance_in')
    input_token_balance_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenBalance_not_in')
    input_token_price_usd = sgqlc.types.Field(BigDecimal, graphql_name='inputTokenPriceUSD')
    input_token_price_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='inputTokenPriceUSD_not')
    input_token_price_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='inputTokenPriceUSD_gt')
    input_token_price_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='inputTokenPriceUSD_lt')
    input_token_price_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='inputTokenPriceUSD_gte')
    input_token_price_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='inputTokenPriceUSD_lte')
    input_token_price_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='inputTokenPriceUSD_in')
    input_token_price_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='inputTokenPriceUSD_not_in')
    output_token_supply = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply')
    output_token_supply_not = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply_not')
    output_token_supply_gt = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply_gt')
    output_token_supply_lt = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply_lt')
    output_token_supply_gte = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply_gte')
    output_token_supply_lte = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply_lte')
    output_token_supply_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='outputTokenSupply_in')
    output_token_supply_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='outputTokenSupply_not_in')
    output_token_price_usd = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD')
    output_token_price_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD_not')
    output_token_price_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD_gt')
    output_token_price_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD_lt')
    output_token_price_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD_gte')
    output_token_price_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD_lte')
    output_token_price_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='outputTokenPriceUSD_in')
    output_token_price_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='outputTokenPriceUSD_not_in')
    exchange_rate = sgqlc.types.Field(BigDecimal, graphql_name='exchangeRate')
    exchange_rate_not = sgqlc.types.Field(BigDecimal, graphql_name='exchangeRate_not')
    exchange_rate_gt = sgqlc.types.Field(BigDecimal, graphql_name='exchangeRate_gt')
    exchange_rate_lt = sgqlc.types.Field(BigDecimal, graphql_name='exchangeRate_lt')
    exchange_rate_gte = sgqlc.types.Field(BigDecimal, graphql_name='exchangeRate_gte')
    exchange_rate_lte = sgqlc.types.Field(BigDecimal, graphql_name='exchangeRate_lte')
    exchange_rate_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='exchangeRate_in')
    exchange_rate_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='exchangeRate_not_in')
    reward_token_emissions_amount = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount')
    reward_token_emissions_amount_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount_not')
    reward_token_emissions_amount_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount_contains')
    reward_token_emissions_amount_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount_contains_nocase')
    reward_token_emissions_amount_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount_not_contains')
    reward_token_emissions_amount_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount_not_contains_nocase')
    reward_token_emissions_usd = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD')
    reward_token_emissions_usd_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD_not')
    reward_token_emissions_usd_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD_contains')
    reward_token_emissions_usd_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD_contains_nocase')
    reward_token_emissions_usd_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD_not_contains')
    reward_token_emissions_usd_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD_not_contains_nocase')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class Market_filter(sgqlc.types.Input):
    __schema__ = subgraph_status_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'protocol', 'protocol_not', 'protocol_gt', 'protocol_lt', 'protocol_gte', 'protocol_lte', 'protocol_in', 'protocol_not_in', 'protocol_contains', 'protocol_contains_nocase', 'protocol_not_contains', 'protocol_not_contains_nocase', 'protocol_starts_with', 'protocol_starts_with_nocase', 'protocol_not_starts_with', 'protocol_not_starts_with_nocase', 'protocol_ends_with', 'protocol_ends_with_nocase', 'protocol_not_ends_with', 'protocol_not_ends_with_nocase', 'name', 'name_not', 'name_gt', 'name_lt', 'name_gte', 'name_lte', 'name_in', 'name_not_in', 'name_contains', 'name_contains_nocase', 'name_not_contains', 'name_not_contains_nocase', 'name_starts_with', 'name_starts_with_nocase', 'name_not_starts_with', 'name_not_starts_with_nocase', 'name_ends_with', 'name_ends_with_nocase', 'name_not_ends_with', 'name_not_ends_with_nocase', 'is_active', 'is_active_not', 'is_active_in', 'is_active_not_in', 'can_use_as_collateral', 'can_use_as_collateral_not', 'can_use_as_collateral_in', 'can_use_as_collateral_not_in', 'can_borrow_from', 'can_borrow_from_not', 'can_borrow_from_in', 'can_borrow_from_not_in', 'maximum_ltv', 'maximum_ltv_not', 'maximum_ltv_gt', 'maximum_ltv_lt', 'maximum_ltv_gte', 'maximum_ltv_lte', 'maximum_ltv_in', 'maximum_ltv_not_in', 'liquidation_threshold', 'liquidation_threshold_not', 'liquidation_threshold_gt', 'liquidation_threshold_lt', 'liquidation_threshold_gte', 'liquidation_threshold_lte', 'liquidation_threshold_in', 'liquidation_threshold_not_in', 'liquidation_penalty', 'liquidation_penalty_not', 'liquidation_penalty_gt', 'liquidation_penalty_lt', 'liquidation_penalty_gte', 'liquidation_penalty_lte', 'liquidation_penalty_in', 'liquidation_penalty_not_in', 'input_token', 'input_token_not', 'input_token_gt', 'input_token_lt', 'input_token_gte', 'input_token_lte', 'input_token_in', 'input_token_not_in', 'input_token_contains', 'input_token_contains_nocase', 'input_token_not_contains', 'input_token_not_contains_nocase', 'input_token_starts_with', 'input_token_starts_with_nocase', 'input_token_not_starts_with', 'input_token_not_starts_with_nocase', 'input_token_ends_with', 'input_token_ends_with_nocase', 'input_token_not_ends_with', 'input_token_not_ends_with_nocase', 'output_token', 'output_token_not', 'output_token_gt', 'output_token_lt', 'output_token_gte', 'output_token_lte', 'output_token_in', 'output_token_not_in', 'output_token_contains', 'output_token_contains_nocase', 'output_token_not_contains', 'output_token_not_contains_nocase', 'output_token_starts_with', 'output_token_starts_with_nocase', 'output_token_not_starts_with', 'output_token_not_starts_with_nocase', 'output_token_ends_with', 'output_token_ends_with_nocase', 'output_token_not_ends_with', 'output_token_not_ends_with_nocase', 'reward_tokens', 'reward_tokens_not', 'reward_tokens_contains', 'reward_tokens_contains_nocase', 'reward_tokens_not_contains', 'reward_tokens_not_contains_nocase', 'rates', 'rates_not', 'rates_contains', 'rates_contains_nocase', 'rates_not_contains', 'rates_not_contains_nocase', 'total_value_locked_usd', 'total_value_locked_usd_not', 'total_value_locked_usd_gt', 'total_value_locked_usd_lt', 'total_value_locked_usd_gte', 'total_value_locked_usd_lte', 'total_value_locked_usd_in', 'total_value_locked_usd_not_in', 'total_deposit_balance_usd', 'total_deposit_balance_usd_not', 'total_deposit_balance_usd_gt', 'total_deposit_balance_usd_lt', 'total_deposit_balance_usd_gte', 'total_deposit_balance_usd_lte', 'total_deposit_balance_usd_in', 'total_deposit_balance_usd_not_in', 'cumulative_deposit_usd', 'cumulative_deposit_usd_not', 'cumulative_deposit_usd_gt', 'cumulative_deposit_usd_lt', 'cumulative_deposit_usd_gte', 'cumulative_deposit_usd_lte', 'cumulative_deposit_usd_in', 'cumulative_deposit_usd_not_in', 'total_borrow_balance_usd', 'total_borrow_balance_usd_not', 'total_borrow_balance_usd_gt', 'total_borrow_balance_usd_lt', 'total_borrow_balance_usd_gte', 'total_borrow_balance_usd_lte', 'total_borrow_balance_usd_in', 'total_borrow_balance_usd_not_in', 'cumulative_borrow_usd', 'cumulative_borrow_usd_not', 'cumulative_borrow_usd_gt', 'cumulative_borrow_usd_lt', 'cumulative_borrow_usd_gte', 'cumulative_borrow_usd_lte', 'cumulative_borrow_usd_in', 'cumulative_borrow_usd_not_in', 'cumulative_liquidate_usd', 'cumulative_liquidate_usd_not', 'cumulative_liquidate_usd_gt', 'cumulative_liquidate_usd_lt', 'cumulative_liquidate_usd_gte', 'cumulative_liquidate_usd_lte', 'cumulative_liquidate_usd_in', 'cumulative_liquidate_usd_not_in', 'input_token_balance', 'input_token_balance_not', 'input_token_balance_gt', 'input_token_balance_lt', 'input_token_balance_gte', 'input_token_balance_lte', 'input_token_balance_in', 'input_token_balance_not_in', 'input_token_price_usd', 'input_token_price_usd_not', 'input_token_price_usd_gt', 'input_token_price_usd_lt', 'input_token_price_usd_gte', 'input_token_price_usd_lte', 'input_token_price_usd_in', 'input_token_price_usd_not_in', 'output_token_supply', 'output_token_supply_not', 'output_token_supply_gt', 'output_token_supply_lt', 'output_token_supply_gte', 'output_token_supply_lte', 'output_token_supply_in', 'output_token_supply_not_in', 'output_token_price_usd', 'output_token_price_usd_not', 'output_token_price_usd_gt', 'output_token_price_usd_lt', 'output_token_price_usd_gte', 'output_token_price_usd_lte', 'output_token_price_usd_in', 'output_token_price_usd_not_in', 'exchange_rate', 'exchange_rate_not', 'exchange_rate_gt', 'exchange_rate_lt', 'exchange_rate_gte', 'exchange_rate_lte', 'exchange_rate_in', 'exchange_rate_not_in', 'reward_token_emissions_amount', 'reward_token_emissions_amount_not', 'reward_token_emissions_amount_contains', 'reward_token_emissions_amount_contains_nocase', 'reward_token_emissions_amount_not_contains', 'reward_token_emissions_amount_not_contains_nocase', 'reward_token_emissions_usd', 'reward_token_emissions_usd_not', 'reward_token_emissions_usd_contains', 'reward_token_emissions_usd_contains_nocase', 'reward_token_emissions_usd_not_contains', 'reward_token_emissions_usd_not_contains_nocase', 'created_timestamp', 'created_timestamp_not', 'created_timestamp_gt', 'created_timestamp_lt', 'created_timestamp_gte', 'created_timestamp_lte', 'created_timestamp_in', 'created_timestamp_not_in', 'created_block_number', 'created_block_number_not', 'created_block_number_gt', 'created_block_number_lt', 'created_block_number_gte', 'created_block_number_lte', 'created_block_number_in', 'created_block_number_not_in', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    protocol = sgqlc.types.Field(String, graphql_name='protocol')
    protocol_not = sgqlc.types.Field(String, graphql_name='protocol_not')
    protocol_gt = sgqlc.types.Field(String, graphql_name='protocol_gt')
    protocol_lt = sgqlc.types.Field(String, graphql_name='protocol_lt')
    protocol_gte = sgqlc.types.Field(String, graphql_name='protocol_gte')
    protocol_lte = sgqlc.types.Field(String, graphql_name='protocol_lte')
    protocol_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_in')
    protocol_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_not_in')
    protocol_contains = sgqlc.types.Field(String, graphql_name='protocol_contains')
    protocol_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_contains_nocase')
    protocol_not_contains = sgqlc.types.Field(String, graphql_name='protocol_not_contains')
    protocol_not_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_contains_nocase')
    protocol_starts_with = sgqlc.types.Field(String, graphql_name='protocol_starts_with')
    protocol_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_starts_with_nocase')
    protocol_not_starts_with = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with')
    protocol_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with_nocase')
    protocol_ends_with = sgqlc.types.Field(String, graphql_name='protocol_ends_with')
    protocol_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_ends_with_nocase')
    protocol_not_ends_with = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with')
    protocol_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with_nocase')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_not = sgqlc.types.Field(String, graphql_name='name_not')
    name_gt = sgqlc.types.Field(String, graphql_name='name_gt')
    name_lt = sgqlc.types.Field(String, graphql_name='name_lt')
    name_gte = sgqlc.types.Field(String, graphql_name='name_gte')
    name_lte = sgqlc.types.Field(String, graphql_name='name_lte')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='name_in')
    name_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='name_not_in')
    name_contains = sgqlc.types.Field(String, graphql_name='name_contains')
    name_contains_nocase = sgqlc.types.Field(String, graphql_name='name_contains_nocase')
    name_not_contains = sgqlc.types.Field(String, graphql_name='name_not_contains')
    name_not_contains_nocase = sgqlc.types.Field(String, graphql_name='name_not_contains_nocase')
    name_starts_with = sgqlc.types.Field(String, graphql_name='name_starts_with')
    name_starts_with_nocase = sgqlc.types.Field(String, graphql_name='name_starts_with_nocase')
    name_not_starts_with = sgqlc.types.Field(String, graphql_name='name_not_starts_with')
    name_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='name_not_starts_with_nocase')
    name_ends_with = sgqlc.types.Field(String, graphql_name='name_ends_with')
    name_ends_with_nocase = sgqlc.types.Field(String, graphql_name='name_ends_with_nocase')
    name_not_ends_with = sgqlc.types.Field(String, graphql_name='name_not_ends_with')
    name_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='name_not_ends_with_nocase')
    is_active = sgqlc.types.Field(Boolean, graphql_name='isActive')
    is_active_not = sgqlc.types.Field(Boolean, graphql_name='isActive_not')
    is_active_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='isActive_in')
    is_active_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='isActive_not_in')
    can_use_as_collateral = sgqlc.types.Field(Boolean, graphql_name='canUseAsCollateral')
    can_use_as_collateral_not = sgqlc.types.Field(Boolean, graphql_name='canUseAsCollateral_not')
    can_use_as_collateral_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='canUseAsCollateral_in')
    can_use_as_collateral_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='canUseAsCollateral_not_in')
    can_borrow_from = sgqlc.types.Field(Boolean, graphql_name='canBorrowFrom')
    can_borrow_from_not = sgqlc.types.Field(Boolean, graphql_name='canBorrowFrom_not')
    can_borrow_from_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='canBorrowFrom_in')
    can_borrow_from_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='canBorrowFrom_not_in')
    maximum_ltv = sgqlc.types.Field(BigDecimal, graphql_name='maximumLTV')
    maximum_ltv_not = sgqlc.types.Field(BigDecimal, graphql_name='maximumLTV_not')
    maximum_ltv_gt = sgqlc.types.Field(BigDecimal, graphql_name='maximumLTV_gt')
    maximum_ltv_lt = sgqlc.types.Field(BigDecimal, graphql_name='maximumLTV_lt')
    maximum_ltv_gte = sgqlc.types.Field(BigDecimal, graphql_name='maximumLTV_gte')
    maximum_ltv_lte = sgqlc.types.Field(BigDecimal, graphql_name='maximumLTV_lte')
    maximum_ltv_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='maximumLTV_in')
    maximum_ltv_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='maximumLTV_not_in')
    liquidation_threshold = sgqlc.types.Field(BigDecimal, graphql_name='liquidationThreshold')
    liquidation_threshold_not = sgqlc.types.Field(BigDecimal, graphql_name='liquidationThreshold_not')
    liquidation_threshold_gt = sgqlc.types.Field(BigDecimal, graphql_name='liquidationThreshold_gt')
    liquidation_threshold_lt = sgqlc.types.Field(BigDecimal, graphql_name='liquidationThreshold_lt')
    liquidation_threshold_gte = sgqlc.types.Field(BigDecimal, graphql_name='liquidationThreshold_gte')
    liquidation_threshold_lte = sgqlc.types.Field(BigDecimal, graphql_name='liquidationThreshold_lte')
    liquidation_threshold_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='liquidationThreshold_in')
    liquidation_threshold_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='liquidationThreshold_not_in')
    liquidation_penalty = sgqlc.types.Field(BigDecimal, graphql_name='liquidationPenalty')
    liquidation_penalty_not = sgqlc.types.Field(BigDecimal, graphql_name='liquidationPenalty_not')
    liquidation_penalty_gt = sgqlc.types.Field(BigDecimal, graphql_name='liquidationPenalty_gt')
    liquidation_penalty_lt = sgqlc.types.Field(BigDecimal, graphql_name='liquidationPenalty_lt')
    liquidation_penalty_gte = sgqlc.types.Field(BigDecimal, graphql_name='liquidationPenalty_gte')
    liquidation_penalty_lte = sgqlc.types.Field(BigDecimal, graphql_name='liquidationPenalty_lte')
    liquidation_penalty_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='liquidationPenalty_in')
    liquidation_penalty_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='liquidationPenalty_not_in')
    input_token = sgqlc.types.Field(String, graphql_name='inputToken')
    input_token_not = sgqlc.types.Field(String, graphql_name='inputToken_not')
    input_token_gt = sgqlc.types.Field(String, graphql_name='inputToken_gt')
    input_token_lt = sgqlc.types.Field(String, graphql_name='inputToken_lt')
    input_token_gte = sgqlc.types.Field(String, graphql_name='inputToken_gte')
    input_token_lte = sgqlc.types.Field(String, graphql_name='inputToken_lte')
    input_token_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='inputToken_in')
    input_token_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='inputToken_not_in')
    input_token_contains = sgqlc.types.Field(String, graphql_name='inputToken_contains')
    input_token_contains_nocase = sgqlc.types.Field(String, graphql_name='inputToken_contains_nocase')
    input_token_not_contains = sgqlc.types.Field(String, graphql_name='inputToken_not_contains')
    input_token_not_contains_nocase = sgqlc.types.Field(String, graphql_name='inputToken_not_contains_nocase')
    input_token_starts_with = sgqlc.types.Field(String, graphql_name='inputToken_starts_with')
    input_token_starts_with_nocase = sgqlc.types.Field(String, graphql_name='inputToken_starts_with_nocase')
    input_token_not_starts_with = sgqlc.types.Field(String, graphql_name='inputToken_not_starts_with')
    input_token_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='inputToken_not_starts_with_nocase')
    input_token_ends_with = sgqlc.types.Field(String, graphql_name='inputToken_ends_with')
    input_token_ends_with_nocase = sgqlc.types.Field(String, graphql_name='inputToken_ends_with_nocase')
    input_token_not_ends_with = sgqlc.types.Field(String, graphql_name='inputToken_not_ends_with')
    input_token_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='inputToken_not_ends_with_nocase')
    output_token = sgqlc.types.Field(String, graphql_name='outputToken')
    output_token_not = sgqlc.types.Field(String, graphql_name='outputToken_not')
    output_token_gt = sgqlc.types.Field(String, graphql_name='outputToken_gt')
    output_token_lt = sgqlc.types.Field(String, graphql_name='outputToken_lt')
    output_token_gte = sgqlc.types.Field(String, graphql_name='outputToken_gte')
    output_token_lte = sgqlc.types.Field(String, graphql_name='outputToken_lte')
    output_token_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='outputToken_in')
    output_token_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='outputToken_not_in')
    output_token_contains = sgqlc.types.Field(String, graphql_name='outputToken_contains')
    output_token_contains_nocase = sgqlc.types.Field(String, graphql_name='outputToken_contains_nocase')
    output_token_not_contains = sgqlc.types.Field(String, graphql_name='outputToken_not_contains')
    output_token_not_contains_nocase = sgqlc.types.Field(String, graphql_name='outputToken_not_contains_nocase')
    output_token_starts_with = sgqlc.types.Field(String, graphql_name='outputToken_starts_with')
    output_token_starts_with_nocase = sgqlc.types.Field(String, graphql_name='outputToken_starts_with_nocase')
    output_token_not_starts_with = sgqlc.types.Field(String, graphql_name='outputToken_not_starts_with')
    output_token_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='outputToken_not_starts_with_nocase')
    output_token_ends_with = sgqlc.types.Field(String, graphql_name='outputToken_ends_with')
    output_token_ends_with_nocase = sgqlc.types.Field(String, graphql_name='outputToken_ends_with_nocase')
    output_token_not_ends_with = sgqlc.types.Field(String, graphql_name='outputToken_not_ends_with')
    output_token_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='outputToken_not_ends_with_nocase')
    reward_tokens = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='rewardTokens')
    reward_tokens_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='rewardTokens_not')
    reward_tokens_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='rewardTokens_contains')
    reward_tokens_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='rewardTokens_contains_nocase')
    reward_tokens_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='rewardTokens_not_contains')
    reward_tokens_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='rewardTokens_not_contains_nocase')
    rates = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='rates')
    rates_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='rates_not')
    rates_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='rates_contains')
    rates_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='rates_contains_nocase')
    rates_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='rates_not_contains')
    rates_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='rates_not_contains_nocase')
    total_value_locked_usd = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD')
    total_value_locked_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_not')
    total_value_locked_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gt')
    total_value_locked_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lt')
    total_value_locked_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gte')
    total_value_locked_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lte')
    total_value_locked_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_in')
    total_value_locked_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_not_in')
    total_deposit_balance_usd = sgqlc.types.Field(BigDecimal, graphql_name='totalDepositBalanceUSD')
    total_deposit_balance_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='totalDepositBalanceUSD_not')
    total_deposit_balance_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalDepositBalanceUSD_gt')
    total_deposit_balance_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalDepositBalanceUSD_lt')
    total_deposit_balance_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalDepositBalanceUSD_gte')
    total_deposit_balance_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalDepositBalanceUSD_lte')
    total_deposit_balance_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalDepositBalanceUSD_in')
    total_deposit_balance_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalDepositBalanceUSD_not_in')
    cumulative_deposit_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeDepositUSD')
    cumulative_deposit_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeDepositUSD_not')
    cumulative_deposit_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeDepositUSD_gt')
    cumulative_deposit_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeDepositUSD_lt')
    cumulative_deposit_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeDepositUSD_gte')
    cumulative_deposit_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeDepositUSD_lte')
    cumulative_deposit_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeDepositUSD_in')
    cumulative_deposit_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeDepositUSD_not_in')
    total_borrow_balance_usd = sgqlc.types.Field(BigDecimal, graphql_name='totalBorrowBalanceUSD')
    total_borrow_balance_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='totalBorrowBalanceUSD_not')
    total_borrow_balance_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalBorrowBalanceUSD_gt')
    total_borrow_balance_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalBorrowBalanceUSD_lt')
    total_borrow_balance_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalBorrowBalanceUSD_gte')
    total_borrow_balance_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalBorrowBalanceUSD_lte')
    total_borrow_balance_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalBorrowBalanceUSD_in')
    total_borrow_balance_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalBorrowBalanceUSD_not_in')
    cumulative_borrow_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeBorrowUSD')
    cumulative_borrow_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeBorrowUSD_not')
    cumulative_borrow_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeBorrowUSD_gt')
    cumulative_borrow_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeBorrowUSD_lt')
    cumulative_borrow_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeBorrowUSD_gte')
    cumulative_borrow_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeBorrowUSD_lte')
    cumulative_borrow_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeBorrowUSD_in')
    cumulative_borrow_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeBorrowUSD_not_in')
    cumulative_liquidate_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeLiquidateUSD')
    cumulative_liquidate_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeLiquidateUSD_not')
    cumulative_liquidate_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeLiquidateUSD_gt')
    cumulative_liquidate_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeLiquidateUSD_lt')
    cumulative_liquidate_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeLiquidateUSD_gte')
    cumulative_liquidate_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeLiquidateUSD_lte')
    cumulative_liquidate_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeLiquidateUSD_in')
    cumulative_liquidate_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeLiquidateUSD_not_in')
    input_token_balance = sgqlc.types.Field(BigInt, graphql_name='inputTokenBalance')
    input_token_balance_not = sgqlc.types.Field(BigInt, graphql_name='inputTokenBalance_not')
    input_token_balance_gt = sgqlc.types.Field(BigInt, graphql_name='inputTokenBalance_gt')
    input_token_balance_lt = sgqlc.types.Field(BigInt, graphql_name='inputTokenBalance_lt')
    input_token_balance_gte = sgqlc.types.Field(BigInt, graphql_name='inputTokenBalance_gte')
    input_token_balance_lte = sgqlc.types.Field(BigInt, graphql_name='inputTokenBalance_lte')
    input_token_balance_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenBalance_in')
    input_token_balance_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenBalance_not_in')
    input_token_price_usd = sgqlc.types.Field(BigDecimal, graphql_name='inputTokenPriceUSD')
    input_token_price_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='inputTokenPriceUSD_not')
    input_token_price_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='inputTokenPriceUSD_gt')
    input_token_price_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='inputTokenPriceUSD_lt')
    input_token_price_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='inputTokenPriceUSD_gte')
    input_token_price_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='inputTokenPriceUSD_lte')
    input_token_price_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='inputTokenPriceUSD_in')
    input_token_price_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='inputTokenPriceUSD_not_in')
    output_token_supply = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply')
    output_token_supply_not = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply_not')
    output_token_supply_gt = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply_gt')
    output_token_supply_lt = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply_lt')
    output_token_supply_gte = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply_gte')
    output_token_supply_lte = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply_lte')
    output_token_supply_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='outputTokenSupply_in')
    output_token_supply_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='outputTokenSupply_not_in')
    output_token_price_usd = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD')
    output_token_price_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD_not')
    output_token_price_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD_gt')
    output_token_price_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD_lt')
    output_token_price_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD_gte')
    output_token_price_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD_lte')
    output_token_price_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='outputTokenPriceUSD_in')
    output_token_price_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='outputTokenPriceUSD_not_in')
    exchange_rate = sgqlc.types.Field(BigDecimal, graphql_name='exchangeRate')
    exchange_rate_not = sgqlc.types.Field(BigDecimal, graphql_name='exchangeRate_not')
    exchange_rate_gt = sgqlc.types.Field(BigDecimal, graphql_name='exchangeRate_gt')
    exchange_rate_lt = sgqlc.types.Field(BigDecimal, graphql_name='exchangeRate_lt')
    exchange_rate_gte = sgqlc.types.Field(BigDecimal, graphql_name='exchangeRate_gte')
    exchange_rate_lte = sgqlc.types.Field(BigDecimal, graphql_name='exchangeRate_lte')
    exchange_rate_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='exchangeRate_in')
    exchange_rate_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='exchangeRate_not_in')
    reward_token_emissions_amount = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount')
    reward_token_emissions_amount_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount_not')
    reward_token_emissions_amount_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount_contains')
    reward_token_emissions_amount_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount_contains_nocase')
    reward_token_emissions_amount_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount_not_contains')
    reward_token_emissions_amount_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount_not_contains_nocase')
    reward_token_emissions_usd = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD')
    reward_token_emissions_usd_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD_not')
    reward_token_emissions_usd_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD_contains')
    reward_token_emissions_usd_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD_contains_nocase')
    reward_token_emissions_usd_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD_not_contains')
    reward_token_emissions_usd_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD_not_contains_nocase')
    created_timestamp = sgqlc.types.Field(BigInt, graphql_name='createdTimestamp')
    created_timestamp_not = sgqlc.types.Field(BigInt, graphql_name='createdTimestamp_not')
    created_timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='createdTimestamp_gt')
    created_timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='createdTimestamp_lt')
    created_timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='createdTimestamp_gte')
    created_timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='createdTimestamp_lte')
    created_timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createdTimestamp_in')
    created_timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createdTimestamp_not_in')
    created_block_number = sgqlc.types.Field(BigInt, graphql_name='createdBlockNumber')
    created_block_number_not = sgqlc.types.Field(BigInt, graphql_name='createdBlockNumber_not')
    created_block_number_gt = sgqlc.types.Field(BigInt, graphql_name='createdBlockNumber_gt')
    created_block_number_lt = sgqlc.types.Field(BigInt, graphql_name='createdBlockNumber_lt')
    created_block_number_gte = sgqlc.types.Field(BigInt, graphql_name='createdBlockNumber_gte')
    created_block_number_lte = sgqlc.types.Field(BigInt, graphql_name='createdBlockNumber_lte')
    created_block_number_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createdBlockNumber_in')
    created_block_number_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createdBlockNumber_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class Protocol_filter(sgqlc.types.Input):
    __schema__ = subgraph_status_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'name', 'name_not', 'name_gt', 'name_lt', 'name_gte', 'name_lte', 'name_in', 'name_not_in', 'name_contains', 'name_contains_nocase', 'name_not_contains', 'name_not_contains_nocase', 'name_starts_with', 'name_starts_with_nocase', 'name_not_starts_with', 'name_not_starts_with_nocase', 'name_ends_with', 'name_ends_with_nocase', 'name_not_ends_with', 'name_not_ends_with_nocase', 'slug', 'slug_not', 'slug_gt', 'slug_lt', 'slug_gte', 'slug_lte', 'slug_in', 'slug_not_in', 'slug_contains', 'slug_contains_nocase', 'slug_not_contains', 'slug_not_contains_nocase', 'slug_starts_with', 'slug_starts_with_nocase', 'slug_not_starts_with', 'slug_not_starts_with_nocase', 'slug_ends_with', 'slug_ends_with_nocase', 'slug_not_ends_with', 'slug_not_ends_with_nocase', 'schema_version', 'schema_version_not', 'schema_version_gt', 'schema_version_lt', 'schema_version_gte', 'schema_version_lte', 'schema_version_in', 'schema_version_not_in', 'schema_version_contains', 'schema_version_contains_nocase', 'schema_version_not_contains', 'schema_version_not_contains_nocase', 'schema_version_starts_with', 'schema_version_starts_with_nocase', 'schema_version_not_starts_with', 'schema_version_not_starts_with_nocase', 'schema_version_ends_with', 'schema_version_ends_with_nocase', 'schema_version_not_ends_with', 'schema_version_not_ends_with_nocase', 'subgraph_version', 'subgraph_version_not', 'subgraph_version_gt', 'subgraph_version_lt', 'subgraph_version_gte', 'subgraph_version_lte', 'subgraph_version_in', 'subgraph_version_not_in', 'subgraph_version_contains', 'subgraph_version_contains_nocase', 'subgraph_version_not_contains', 'subgraph_version_not_contains_nocase', 'subgraph_version_starts_with', 'subgraph_version_starts_with_nocase', 'subgraph_version_not_starts_with', 'subgraph_version_not_starts_with_nocase', 'subgraph_version_ends_with', 'subgraph_version_ends_with_nocase', 'subgraph_version_not_ends_with', 'subgraph_version_not_ends_with_nocase', 'methodology_version', 'methodology_version_not', 'methodology_version_gt', 'methodology_version_lt', 'methodology_version_gte', 'methodology_version_lte', 'methodology_version_in', 'methodology_version_not_in', 'methodology_version_contains', 'methodology_version_contains_nocase', 'methodology_version_not_contains', 'methodology_version_not_contains_nocase', 'methodology_version_starts_with', 'methodology_version_starts_with_nocase', 'methodology_version_not_starts_with', 'methodology_version_not_starts_with_nocase', 'methodology_version_ends_with', 'methodology_version_ends_with_nocase', 'methodology_version_not_ends_with', 'methodology_version_not_ends_with_nocase', 'network', 'network_not', 'network_in', 'network_not_in', 'type', 'type_not', 'type_in', 'type_not_in', 'total_value_locked_usd', 'total_value_locked_usd_not', 'total_value_locked_usd_gt', 'total_value_locked_usd_lt', 'total_value_locked_usd_gte', 'total_value_locked_usd_lte', 'total_value_locked_usd_in', 'total_value_locked_usd_not_in', 'protocol_controlled_value_usd', 'protocol_controlled_value_usd_not', 'protocol_controlled_value_usd_gt', 'protocol_controlled_value_usd_lt', 'protocol_controlled_value_usd_gte', 'protocol_controlled_value_usd_lte', 'protocol_controlled_value_usd_in', 'protocol_controlled_value_usd_not_in', 'cumulative_unique_users', 'cumulative_unique_users_not', 'cumulative_unique_users_gt', 'cumulative_unique_users_lt', 'cumulative_unique_users_gte', 'cumulative_unique_users_lte', 'cumulative_unique_users_in', 'cumulative_unique_users_not_in', 'cumulative_supply_side_revenue_usd', 'cumulative_supply_side_revenue_usd_not', 'cumulative_supply_side_revenue_usd_gt', 'cumulative_supply_side_revenue_usd_lt', 'cumulative_supply_side_revenue_usd_gte', 'cumulative_supply_side_revenue_usd_lte', 'cumulative_supply_side_revenue_usd_in', 'cumulative_supply_side_revenue_usd_not_in', 'cumulative_protocol_side_revenue_usd', 'cumulative_protocol_side_revenue_usd_not', 'cumulative_protocol_side_revenue_usd_gt', 'cumulative_protocol_side_revenue_usd_lt', 'cumulative_protocol_side_revenue_usd_gte', 'cumulative_protocol_side_revenue_usd_lte', 'cumulative_protocol_side_revenue_usd_in', 'cumulative_protocol_side_revenue_usd_not_in', 'cumulative_total_revenue_usd', 'cumulative_total_revenue_usd_not', 'cumulative_total_revenue_usd_gt', 'cumulative_total_revenue_usd_lt', 'cumulative_total_revenue_usd_gte', 'cumulative_total_revenue_usd_lte', 'cumulative_total_revenue_usd_in', 'cumulative_total_revenue_usd_not_in', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_not = sgqlc.types.Field(String, graphql_name='name_not')
    name_gt = sgqlc.types.Field(String, graphql_name='name_gt')
    name_lt = sgqlc.types.Field(String, graphql_name='name_lt')
    name_gte = sgqlc.types.Field(String, graphql_name='name_gte')
    name_lte = sgqlc.types.Field(String, graphql_name='name_lte')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='name_in')
    name_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='name_not_in')
    name_contains = sgqlc.types.Field(String, graphql_name='name_contains')
    name_contains_nocase = sgqlc.types.Field(String, graphql_name='name_contains_nocase')
    name_not_contains = sgqlc.types.Field(String, graphql_name='name_not_contains')
    name_not_contains_nocase = sgqlc.types.Field(String, graphql_name='name_not_contains_nocase')
    name_starts_with = sgqlc.types.Field(String, graphql_name='name_starts_with')
    name_starts_with_nocase = sgqlc.types.Field(String, graphql_name='name_starts_with_nocase')
    name_not_starts_with = sgqlc.types.Field(String, graphql_name='name_not_starts_with')
    name_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='name_not_starts_with_nocase')
    name_ends_with = sgqlc.types.Field(String, graphql_name='name_ends_with')
    name_ends_with_nocase = sgqlc.types.Field(String, graphql_name='name_ends_with_nocase')
    name_not_ends_with = sgqlc.types.Field(String, graphql_name='name_not_ends_with')
    name_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='name_not_ends_with_nocase')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    slug_not = sgqlc.types.Field(String, graphql_name='slug_not')
    slug_gt = sgqlc.types.Field(String, graphql_name='slug_gt')
    slug_lt = sgqlc.types.Field(String, graphql_name='slug_lt')
    slug_gte = sgqlc.types.Field(String, graphql_name='slug_gte')
    slug_lte = sgqlc.types.Field(String, graphql_name='slug_lte')
    slug_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='slug_in')
    slug_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='slug_not_in')
    slug_contains = sgqlc.types.Field(String, graphql_name='slug_contains')
    slug_contains_nocase = sgqlc.types.Field(String, graphql_name='slug_contains_nocase')
    slug_not_contains = sgqlc.types.Field(String, graphql_name='slug_not_contains')
    slug_not_contains_nocase = sgqlc.types.Field(String, graphql_name='slug_not_contains_nocase')
    slug_starts_with = sgqlc.types.Field(String, graphql_name='slug_starts_with')
    slug_starts_with_nocase = sgqlc.types.Field(String, graphql_name='slug_starts_with_nocase')
    slug_not_starts_with = sgqlc.types.Field(String, graphql_name='slug_not_starts_with')
    slug_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='slug_not_starts_with_nocase')
    slug_ends_with = sgqlc.types.Field(String, graphql_name='slug_ends_with')
    slug_ends_with_nocase = sgqlc.types.Field(String, graphql_name='slug_ends_with_nocase')
    slug_not_ends_with = sgqlc.types.Field(String, graphql_name='slug_not_ends_with')
    slug_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='slug_not_ends_with_nocase')
    schema_version = sgqlc.types.Field(String, graphql_name='schemaVersion')
    schema_version_not = sgqlc.types.Field(String, graphql_name='schemaVersion_not')
    schema_version_gt = sgqlc.types.Field(String, graphql_name='schemaVersion_gt')
    schema_version_lt = sgqlc.types.Field(String, graphql_name='schemaVersion_lt')
    schema_version_gte = sgqlc.types.Field(String, graphql_name='schemaVersion_gte')
    schema_version_lte = sgqlc.types.Field(String, graphql_name='schemaVersion_lte')
    schema_version_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='schemaVersion_in')
    schema_version_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='schemaVersion_not_in')
    schema_version_contains = sgqlc.types.Field(String, graphql_name='schemaVersion_contains')
    schema_version_contains_nocase = sgqlc.types.Field(String, graphql_name='schemaVersion_contains_nocase')
    schema_version_not_contains = sgqlc.types.Field(String, graphql_name='schemaVersion_not_contains')
    schema_version_not_contains_nocase = sgqlc.types.Field(String, graphql_name='schemaVersion_not_contains_nocase')
    schema_version_starts_with = sgqlc.types.Field(String, graphql_name='schemaVersion_starts_with')
    schema_version_starts_with_nocase = sgqlc.types.Field(String, graphql_name='schemaVersion_starts_with_nocase')
    schema_version_not_starts_with = sgqlc.types.Field(String, graphql_name='schemaVersion_not_starts_with')
    schema_version_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='schemaVersion_not_starts_with_nocase')
    schema_version_ends_with = sgqlc.types.Field(String, graphql_name='schemaVersion_ends_with')
    schema_version_ends_with_nocase = sgqlc.types.Field(String, graphql_name='schemaVersion_ends_with_nocase')
    schema_version_not_ends_with = sgqlc.types.Field(String, graphql_name='schemaVersion_not_ends_with')
    schema_version_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='schemaVersion_not_ends_with_nocase')
    subgraph_version = sgqlc.types.Field(String, graphql_name='subgraphVersion')
    subgraph_version_not = sgqlc.types.Field(String, graphql_name='subgraphVersion_not')
    subgraph_version_gt = sgqlc.types.Field(String, graphql_name='subgraphVersion_gt')
    subgraph_version_lt = sgqlc.types.Field(String, graphql_name='subgraphVersion_lt')
    subgraph_version_gte = sgqlc.types.Field(String, graphql_name='subgraphVersion_gte')
    subgraph_version_lte = sgqlc.types.Field(String, graphql_name='subgraphVersion_lte')
    subgraph_version_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='subgraphVersion_in')
    subgraph_version_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='subgraphVersion_not_in')
    subgraph_version_contains = sgqlc.types.Field(String, graphql_name='subgraphVersion_contains')
    subgraph_version_contains_nocase = sgqlc.types.Field(String, graphql_name='subgraphVersion_contains_nocase')
    subgraph_version_not_contains = sgqlc.types.Field(String, graphql_name='subgraphVersion_not_contains')
    subgraph_version_not_contains_nocase = sgqlc.types.Field(String, graphql_name='subgraphVersion_not_contains_nocase')
    subgraph_version_starts_with = sgqlc.types.Field(String, graphql_name='subgraphVersion_starts_with')
    subgraph_version_starts_with_nocase = sgqlc.types.Field(String, graphql_name='subgraphVersion_starts_with_nocase')
    subgraph_version_not_starts_with = sgqlc.types.Field(String, graphql_name='subgraphVersion_not_starts_with')
    subgraph_version_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='subgraphVersion_not_starts_with_nocase')
    subgraph_version_ends_with = sgqlc.types.Field(String, graphql_name='subgraphVersion_ends_with')
    subgraph_version_ends_with_nocase = sgqlc.types.Field(String, graphql_name='subgraphVersion_ends_with_nocase')
    subgraph_version_not_ends_with = sgqlc.types.Field(String, graphql_name='subgraphVersion_not_ends_with')
    subgraph_version_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='subgraphVersion_not_ends_with_nocase')
    methodology_version = sgqlc.types.Field(String, graphql_name='methodologyVersion')
    methodology_version_not = sgqlc.types.Field(String, graphql_name='methodologyVersion_not')
    methodology_version_gt = sgqlc.types.Field(String, graphql_name='methodologyVersion_gt')
    methodology_version_lt = sgqlc.types.Field(String, graphql_name='methodologyVersion_lt')
    methodology_version_gte = sgqlc.types.Field(String, graphql_name='methodologyVersion_gte')
    methodology_version_lte = sgqlc.types.Field(String, graphql_name='methodologyVersion_lte')
    methodology_version_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='methodologyVersion_in')
    methodology_version_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='methodologyVersion_not_in')
    methodology_version_contains = sgqlc.types.Field(String, graphql_name='methodologyVersion_contains')
    methodology_version_contains_nocase = sgqlc.types.Field(String, graphql_name='methodologyVersion_contains_nocase')
    methodology_version_not_contains = sgqlc.types.Field(String, graphql_name='methodologyVersion_not_contains')
    methodology_version_not_contains_nocase = sgqlc.types.Field(String, graphql_name='methodologyVersion_not_contains_nocase')
    methodology_version_starts_with = sgqlc.types.Field(String, graphql_name='methodologyVersion_starts_with')
    methodology_version_starts_with_nocase = sgqlc.types.Field(String, graphql_name='methodologyVersion_starts_with_nocase')
    methodology_version_not_starts_with = sgqlc.types.Field(String, graphql_name='methodologyVersion_not_starts_with')
    methodology_version_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='methodologyVersion_not_starts_with_nocase')
    methodology_version_ends_with = sgqlc.types.Field(String, graphql_name='methodologyVersion_ends_with')
    methodology_version_ends_with_nocase = sgqlc.types.Field(String, graphql_name='methodologyVersion_ends_with_nocase')
    methodology_version_not_ends_with = sgqlc.types.Field(String, graphql_name='methodologyVersion_not_ends_with')
    methodology_version_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='methodologyVersion_not_ends_with_nocase')
    network = sgqlc.types.Field(Network, graphql_name='network')
    network_not = sgqlc.types.Field(Network, graphql_name='network_not')
    network_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Network)), graphql_name='network_in')
    network_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Network)), graphql_name='network_not_in')
    type = sgqlc.types.Field(ProtocolType, graphql_name='type')
    type_not = sgqlc.types.Field(ProtocolType, graphql_name='type_not')
    type_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ProtocolType)), graphql_name='type_in')
    type_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ProtocolType)), graphql_name='type_not_in')
    total_value_locked_usd = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD')
    total_value_locked_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_not')
    total_value_locked_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gt')
    total_value_locked_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lt')
    total_value_locked_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gte')
    total_value_locked_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lte')
    total_value_locked_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_in')
    total_value_locked_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_not_in')
    protocol_controlled_value_usd = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD')
    protocol_controlled_value_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD_not')
    protocol_controlled_value_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD_gt')
    protocol_controlled_value_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD_lt')
    protocol_controlled_value_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD_gte')
    protocol_controlled_value_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD_lte')
    protocol_controlled_value_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='protocolControlledValueUSD_in')
    protocol_controlled_value_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='protocolControlledValueUSD_not_in')
    cumulative_unique_users = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers')
    cumulative_unique_users_not = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_not')
    cumulative_unique_users_gt = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_gt')
    cumulative_unique_users_lt = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_lt')
    cumulative_unique_users_gte = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_gte')
    cumulative_unique_users_lte = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_lte')
    cumulative_unique_users_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='cumulativeUniqueUsers_in')
    cumulative_unique_users_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='cumulativeUniqueUsers_not_in')
    cumulative_supply_side_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD')
    cumulative_supply_side_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_not')
    cumulative_supply_side_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_gt')
    cumulative_supply_side_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_lt')
    cumulative_supply_side_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_gte')
    cumulative_supply_side_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_lte')
    cumulative_supply_side_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeSupplySideRevenueUSD_in')
    cumulative_supply_side_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeSupplySideRevenueUSD_not_in')
    cumulative_protocol_side_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD')
    cumulative_protocol_side_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_not')
    cumulative_protocol_side_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_gt')
    cumulative_protocol_side_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_lt')
    cumulative_protocol_side_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_gte')
    cumulative_protocol_side_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_lte')
    cumulative_protocol_side_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeProtocolSideRevenueUSD_in')
    cumulative_protocol_side_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeProtocolSideRevenueUSD_not_in')
    cumulative_total_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD')
    cumulative_total_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_not')
    cumulative_total_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_gt')
    cumulative_total_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_lt')
    cumulative_total_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_gte')
    cumulative_total_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_lte')
    cumulative_total_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeTotalRevenueUSD_in')
    cumulative_total_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeTotalRevenueUSD_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class Repay_filter(sgqlc.types.Input):
    __schema__ = subgraph_status_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'hash', 'hash_not', 'hash_gt', 'hash_lt', 'hash_gte', 'hash_lte', 'hash_in', 'hash_not_in', 'hash_contains', 'hash_contains_nocase', 'hash_not_contains', 'hash_not_contains_nocase', 'hash_starts_with', 'hash_starts_with_nocase', 'hash_not_starts_with', 'hash_not_starts_with_nocase', 'hash_ends_with', 'hash_ends_with_nocase', 'hash_not_ends_with', 'hash_not_ends_with_nocase', 'log_index', 'log_index_not', 'log_index_gt', 'log_index_lt', 'log_index_gte', 'log_index_lte', 'log_index_in', 'log_index_not_in', 'protocol', 'protocol_not', 'protocol_gt', 'protocol_lt', 'protocol_gte', 'protocol_lte', 'protocol_in', 'protocol_not_in', 'protocol_contains', 'protocol_contains_nocase', 'protocol_not_contains', 'protocol_not_contains_nocase', 'protocol_starts_with', 'protocol_starts_with_nocase', 'protocol_not_starts_with', 'protocol_not_starts_with_nocase', 'protocol_ends_with', 'protocol_ends_with_nocase', 'protocol_not_ends_with', 'protocol_not_ends_with_nocase', 'to', 'to_not', 'to_gt', 'to_lt', 'to_gte', 'to_lte', 'to_in', 'to_not_in', 'to_contains', 'to_contains_nocase', 'to_not_contains', 'to_not_contains_nocase', 'to_starts_with', 'to_starts_with_nocase', 'to_not_starts_with', 'to_not_starts_with_nocase', 'to_ends_with', 'to_ends_with_nocase', 'to_not_ends_with', 'to_not_ends_with_nocase', 'from_', 'from_not', 'from_gt', 'from_lt', 'from_gte', 'from_lte', 'from_in', 'from_not_in', 'from_contains', 'from_contains_nocase', 'from_not_contains', 'from_not_contains_nocase', 'from_starts_with', 'from_starts_with_nocase', 'from_not_starts_with', 'from_not_starts_with_nocase', 'from_ends_with', 'from_ends_with_nocase', 'from_not_ends_with', 'from_not_ends_with_nocase', 'block_number', 'block_number_not', 'block_number_gt', 'block_number_lt', 'block_number_gte', 'block_number_lte', 'block_number_in', 'block_number_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'market', 'market_not', 'market_gt', 'market_lt', 'market_gte', 'market_lte', 'market_in', 'market_not_in', 'market_contains', 'market_contains_nocase', 'market_not_contains', 'market_not_contains_nocase', 'market_starts_with', 'market_starts_with_nocase', 'market_not_starts_with', 'market_not_starts_with_nocase', 'market_ends_with', 'market_ends_with_nocase', 'market_not_ends_with', 'market_not_ends_with_nocase', 'asset', 'asset_not', 'asset_gt', 'asset_lt', 'asset_gte', 'asset_lte', 'asset_in', 'asset_not_in', 'asset_contains', 'asset_contains_nocase', 'asset_not_contains', 'asset_not_contains_nocase', 'asset_starts_with', 'asset_starts_with_nocase', 'asset_not_starts_with', 'asset_not_starts_with_nocase', 'asset_ends_with', 'asset_ends_with_nocase', 'asset_not_ends_with', 'asset_not_ends_with_nocase', 'amount', 'amount_not', 'amount_gt', 'amount_lt', 'amount_gte', 'amount_lte', 'amount_in', 'amount_not_in', 'amount_usd', 'amount_usd_not', 'amount_usd_gt', 'amount_usd_lt', 'amount_usd_gte', 'amount_usd_lte', 'amount_usd_in', 'amount_usd_not_in', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    hash_not = sgqlc.types.Field(String, graphql_name='hash_not')
    hash_gt = sgqlc.types.Field(String, graphql_name='hash_gt')
    hash_lt = sgqlc.types.Field(String, graphql_name='hash_lt')
    hash_gte = sgqlc.types.Field(String, graphql_name='hash_gte')
    hash_lte = sgqlc.types.Field(String, graphql_name='hash_lte')
    hash_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='hash_in')
    hash_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='hash_not_in')
    hash_contains = sgqlc.types.Field(String, graphql_name='hash_contains')
    hash_contains_nocase = sgqlc.types.Field(String, graphql_name='hash_contains_nocase')
    hash_not_contains = sgqlc.types.Field(String, graphql_name='hash_not_contains')
    hash_not_contains_nocase = sgqlc.types.Field(String, graphql_name='hash_not_contains_nocase')
    hash_starts_with = sgqlc.types.Field(String, graphql_name='hash_starts_with')
    hash_starts_with_nocase = sgqlc.types.Field(String, graphql_name='hash_starts_with_nocase')
    hash_not_starts_with = sgqlc.types.Field(String, graphql_name='hash_not_starts_with')
    hash_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='hash_not_starts_with_nocase')
    hash_ends_with = sgqlc.types.Field(String, graphql_name='hash_ends_with')
    hash_ends_with_nocase = sgqlc.types.Field(String, graphql_name='hash_ends_with_nocase')
    hash_not_ends_with = sgqlc.types.Field(String, graphql_name='hash_not_ends_with')
    hash_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='hash_not_ends_with_nocase')
    log_index = sgqlc.types.Field(Int, graphql_name='logIndex')
    log_index_not = sgqlc.types.Field(Int, graphql_name='logIndex_not')
    log_index_gt = sgqlc.types.Field(Int, graphql_name='logIndex_gt')
    log_index_lt = sgqlc.types.Field(Int, graphql_name='logIndex_lt')
    log_index_gte = sgqlc.types.Field(Int, graphql_name='logIndex_gte')
    log_index_lte = sgqlc.types.Field(Int, graphql_name='logIndex_lte')
    log_index_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='logIndex_in')
    log_index_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='logIndex_not_in')
    protocol = sgqlc.types.Field(String, graphql_name='protocol')
    protocol_not = sgqlc.types.Field(String, graphql_name='protocol_not')
    protocol_gt = sgqlc.types.Field(String, graphql_name='protocol_gt')
    protocol_lt = sgqlc.types.Field(String, graphql_name='protocol_lt')
    protocol_gte = sgqlc.types.Field(String, graphql_name='protocol_gte')
    protocol_lte = sgqlc.types.Field(String, graphql_name='protocol_lte')
    protocol_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_in')
    protocol_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_not_in')
    protocol_contains = sgqlc.types.Field(String, graphql_name='protocol_contains')
    protocol_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_contains_nocase')
    protocol_not_contains = sgqlc.types.Field(String, graphql_name='protocol_not_contains')
    protocol_not_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_contains_nocase')
    protocol_starts_with = sgqlc.types.Field(String, graphql_name='protocol_starts_with')
    protocol_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_starts_with_nocase')
    protocol_not_starts_with = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with')
    protocol_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with_nocase')
    protocol_ends_with = sgqlc.types.Field(String, graphql_name='protocol_ends_with')
    protocol_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_ends_with_nocase')
    protocol_not_ends_with = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with')
    protocol_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with_nocase')
    to = sgqlc.types.Field(String, graphql_name='to')
    to_not = sgqlc.types.Field(String, graphql_name='to_not')
    to_gt = sgqlc.types.Field(String, graphql_name='to_gt')
    to_lt = sgqlc.types.Field(String, graphql_name='to_lt')
    to_gte = sgqlc.types.Field(String, graphql_name='to_gte')
    to_lte = sgqlc.types.Field(String, graphql_name='to_lte')
    to_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='to_in')
    to_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='to_not_in')
    to_contains = sgqlc.types.Field(String, graphql_name='to_contains')
    to_contains_nocase = sgqlc.types.Field(String, graphql_name='to_contains_nocase')
    to_not_contains = sgqlc.types.Field(String, graphql_name='to_not_contains')
    to_not_contains_nocase = sgqlc.types.Field(String, graphql_name='to_not_contains_nocase')
    to_starts_with = sgqlc.types.Field(String, graphql_name='to_starts_with')
    to_starts_with_nocase = sgqlc.types.Field(String, graphql_name='to_starts_with_nocase')
    to_not_starts_with = sgqlc.types.Field(String, graphql_name='to_not_starts_with')
    to_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='to_not_starts_with_nocase')
    to_ends_with = sgqlc.types.Field(String, graphql_name='to_ends_with')
    to_ends_with_nocase = sgqlc.types.Field(String, graphql_name='to_ends_with_nocase')
    to_not_ends_with = sgqlc.types.Field(String, graphql_name='to_not_ends_with')
    to_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='to_not_ends_with_nocase')
    from_ = sgqlc.types.Field(String, graphql_name='from')
    from_not = sgqlc.types.Field(String, graphql_name='from_not')
    from_gt = sgqlc.types.Field(String, graphql_name='from_gt')
    from_lt = sgqlc.types.Field(String, graphql_name='from_lt')
    from_gte = sgqlc.types.Field(String, graphql_name='from_gte')
    from_lte = sgqlc.types.Field(String, graphql_name='from_lte')
    from_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='from_in')
    from_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='from_not_in')
    from_contains = sgqlc.types.Field(String, graphql_name='from_contains')
    from_contains_nocase = sgqlc.types.Field(String, graphql_name='from_contains_nocase')
    from_not_contains = sgqlc.types.Field(String, graphql_name='from_not_contains')
    from_not_contains_nocase = sgqlc.types.Field(String, graphql_name='from_not_contains_nocase')
    from_starts_with = sgqlc.types.Field(String, graphql_name='from_starts_with')
    from_starts_with_nocase = sgqlc.types.Field(String, graphql_name='from_starts_with_nocase')
    from_not_starts_with = sgqlc.types.Field(String, graphql_name='from_not_starts_with')
    from_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='from_not_starts_with_nocase')
    from_ends_with = sgqlc.types.Field(String, graphql_name='from_ends_with')
    from_ends_with_nocase = sgqlc.types.Field(String, graphql_name='from_ends_with_nocase')
    from_not_ends_with = sgqlc.types.Field(String, graphql_name='from_not_ends_with')
    from_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='from_not_ends_with_nocase')
    block_number = sgqlc.types.Field(BigInt, graphql_name='blockNumber')
    block_number_not = sgqlc.types.Field(BigInt, graphql_name='blockNumber_not')
    block_number_gt = sgqlc.types.Field(BigInt, graphql_name='blockNumber_gt')
    block_number_lt = sgqlc.types.Field(BigInt, graphql_name='blockNumber_lt')
    block_number_gte = sgqlc.types.Field(BigInt, graphql_name='blockNumber_gte')
    block_number_lte = sgqlc.types.Field(BigInt, graphql_name='blockNumber_lte')
    block_number_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='blockNumber_in')
    block_number_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='blockNumber_not_in')
    timestamp = sgqlc.types.Field(BigInt, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_not_in')
    market = sgqlc.types.Field(String, graphql_name='market')
    market_not = sgqlc.types.Field(String, graphql_name='market_not')
    market_gt = sgqlc.types.Field(String, graphql_name='market_gt')
    market_lt = sgqlc.types.Field(String, graphql_name='market_lt')
    market_gte = sgqlc.types.Field(String, graphql_name='market_gte')
    market_lte = sgqlc.types.Field(String, graphql_name='market_lte')
    market_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='market_in')
    market_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='market_not_in')
    market_contains = sgqlc.types.Field(String, graphql_name='market_contains')
    market_contains_nocase = sgqlc.types.Field(String, graphql_name='market_contains_nocase')
    market_not_contains = sgqlc.types.Field(String, graphql_name='market_not_contains')
    market_not_contains_nocase = sgqlc.types.Field(String, graphql_name='market_not_contains_nocase')
    market_starts_with = sgqlc.types.Field(String, graphql_name='market_starts_with')
    market_starts_with_nocase = sgqlc.types.Field(String, graphql_name='market_starts_with_nocase')
    market_not_starts_with = sgqlc.types.Field(String, graphql_name='market_not_starts_with')
    market_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='market_not_starts_with_nocase')
    market_ends_with = sgqlc.types.Field(String, graphql_name='market_ends_with')
    market_ends_with_nocase = sgqlc.types.Field(String, graphql_name='market_ends_with_nocase')
    market_not_ends_with = sgqlc.types.Field(String, graphql_name='market_not_ends_with')
    market_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='market_not_ends_with_nocase')
    asset = sgqlc.types.Field(String, graphql_name='asset')
    asset_not = sgqlc.types.Field(String, graphql_name='asset_not')
    asset_gt = sgqlc.types.Field(String, graphql_name='asset_gt')
    asset_lt = sgqlc.types.Field(String, graphql_name='asset_lt')
    asset_gte = sgqlc.types.Field(String, graphql_name='asset_gte')
    asset_lte = sgqlc.types.Field(String, graphql_name='asset_lte')
    asset_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='asset_in')
    asset_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='asset_not_in')
    asset_contains = sgqlc.types.Field(String, graphql_name='asset_contains')
    asset_contains_nocase = sgqlc.types.Field(String, graphql_name='asset_contains_nocase')
    asset_not_contains = sgqlc.types.Field(String, graphql_name='asset_not_contains')
    asset_not_contains_nocase = sgqlc.types.Field(String, graphql_name='asset_not_contains_nocase')
    asset_starts_with = sgqlc.types.Field(String, graphql_name='asset_starts_with')
    asset_starts_with_nocase = sgqlc.types.Field(String, graphql_name='asset_starts_with_nocase')
    asset_not_starts_with = sgqlc.types.Field(String, graphql_name='asset_not_starts_with')
    asset_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='asset_not_starts_with_nocase')
    asset_ends_with = sgqlc.types.Field(String, graphql_name='asset_ends_with')
    asset_ends_with_nocase = sgqlc.types.Field(String, graphql_name='asset_ends_with_nocase')
    asset_not_ends_with = sgqlc.types.Field(String, graphql_name='asset_not_ends_with')
    asset_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='asset_not_ends_with_nocase')
    amount = sgqlc.types.Field(BigInt, graphql_name='amount')
    amount_not = sgqlc.types.Field(BigInt, graphql_name='amount_not')
    amount_gt = sgqlc.types.Field(BigInt, graphql_name='amount_gt')
    amount_lt = sgqlc.types.Field(BigInt, graphql_name='amount_lt')
    amount_gte = sgqlc.types.Field(BigInt, graphql_name='amount_gte')
    amount_lte = sgqlc.types.Field(BigInt, graphql_name='amount_lte')
    amount_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='amount_in')
    amount_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='amount_not_in')
    amount_usd = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD')
    amount_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_not')
    amount_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_gt')
    amount_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_lt')
    amount_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_gte')
    amount_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_lte')
    amount_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amountUSD_in')
    amount_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amountUSD_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class RewardToken_filter(sgqlc.types.Input):
    __schema__ = subgraph_status_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'token', 'token_not', 'token_gt', 'token_lt', 'token_gte', 'token_lte', 'token_in', 'token_not_in', 'token_contains', 'token_contains_nocase', 'token_not_contains', 'token_not_contains_nocase', 'token_starts_with', 'token_starts_with_nocase', 'token_not_starts_with', 'token_not_starts_with_nocase', 'token_ends_with', 'token_ends_with_nocase', 'token_not_ends_with', 'token_not_ends_with_nocase', 'type', 'type_not', 'type_in', 'type_not_in', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    token = sgqlc.types.Field(String, graphql_name='token')
    token_not = sgqlc.types.Field(String, graphql_name='token_not')
    token_gt = sgqlc.types.Field(String, graphql_name='token_gt')
    token_lt = sgqlc.types.Field(String, graphql_name='token_lt')
    token_gte = sgqlc.types.Field(String, graphql_name='token_gte')
    token_lte = sgqlc.types.Field(String, graphql_name='token_lte')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='token_in')
    token_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='token_not_in')
    token_contains = sgqlc.types.Field(String, graphql_name='token_contains')
    token_contains_nocase = sgqlc.types.Field(String, graphql_name='token_contains_nocase')
    token_not_contains = sgqlc.types.Field(String, graphql_name='token_not_contains')
    token_not_contains_nocase = sgqlc.types.Field(String, graphql_name='token_not_contains_nocase')
    token_starts_with = sgqlc.types.Field(String, graphql_name='token_starts_with')
    token_starts_with_nocase = sgqlc.types.Field(String, graphql_name='token_starts_with_nocase')
    token_not_starts_with = sgqlc.types.Field(String, graphql_name='token_not_starts_with')
    token_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='token_not_starts_with_nocase')
    token_ends_with = sgqlc.types.Field(String, graphql_name='token_ends_with')
    token_ends_with_nocase = sgqlc.types.Field(String, graphql_name='token_ends_with_nocase')
    token_not_ends_with = sgqlc.types.Field(String, graphql_name='token_not_ends_with')
    token_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='token_not_ends_with_nocase')
    type = sgqlc.types.Field(RewardTokenType, graphql_name='type')
    type_not = sgqlc.types.Field(RewardTokenType, graphql_name='type_not')
    type_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RewardTokenType)), graphql_name='type_in')
    type_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RewardTokenType)), graphql_name='type_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class Token_filter(sgqlc.types.Input):
    __schema__ = subgraph_status_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'name', 'name_not', 'name_gt', 'name_lt', 'name_gte', 'name_lte', 'name_in', 'name_not_in', 'name_contains', 'name_contains_nocase', 'name_not_contains', 'name_not_contains_nocase', 'name_starts_with', 'name_starts_with_nocase', 'name_not_starts_with', 'name_not_starts_with_nocase', 'name_ends_with', 'name_ends_with_nocase', 'name_not_ends_with', 'name_not_ends_with_nocase', 'symbol', 'symbol_not', 'symbol_gt', 'symbol_lt', 'symbol_gte', 'symbol_lte', 'symbol_in', 'symbol_not_in', 'symbol_contains', 'symbol_contains_nocase', 'symbol_not_contains', 'symbol_not_contains_nocase', 'symbol_starts_with', 'symbol_starts_with_nocase', 'symbol_not_starts_with', 'symbol_not_starts_with_nocase', 'symbol_ends_with', 'symbol_ends_with_nocase', 'symbol_not_ends_with', 'symbol_not_ends_with_nocase', 'decimals', 'decimals_not', 'decimals_gt', 'decimals_lt', 'decimals_gte', 'decimals_lte', 'decimals_in', 'decimals_not_in', 'last_price_usd', 'last_price_usd_not', 'last_price_usd_gt', 'last_price_usd_lt', 'last_price_usd_gte', 'last_price_usd_lte', 'last_price_usd_in', 'last_price_usd_not_in', 'last_price_block_number', 'last_price_block_number_not', 'last_price_block_number_gt', 'last_price_block_number_lt', 'last_price_block_number_gte', 'last_price_block_number_lte', 'last_price_block_number_in', 'last_price_block_number_not_in', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_not = sgqlc.types.Field(String, graphql_name='name_not')
    name_gt = sgqlc.types.Field(String, graphql_name='name_gt')
    name_lt = sgqlc.types.Field(String, graphql_name='name_lt')
    name_gte = sgqlc.types.Field(String, graphql_name='name_gte')
    name_lte = sgqlc.types.Field(String, graphql_name='name_lte')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='name_in')
    name_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='name_not_in')
    name_contains = sgqlc.types.Field(String, graphql_name='name_contains')
    name_contains_nocase = sgqlc.types.Field(String, graphql_name='name_contains_nocase')
    name_not_contains = sgqlc.types.Field(String, graphql_name='name_not_contains')
    name_not_contains_nocase = sgqlc.types.Field(String, graphql_name='name_not_contains_nocase')
    name_starts_with = sgqlc.types.Field(String, graphql_name='name_starts_with')
    name_starts_with_nocase = sgqlc.types.Field(String, graphql_name='name_starts_with_nocase')
    name_not_starts_with = sgqlc.types.Field(String, graphql_name='name_not_starts_with')
    name_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='name_not_starts_with_nocase')
    name_ends_with = sgqlc.types.Field(String, graphql_name='name_ends_with')
    name_ends_with_nocase = sgqlc.types.Field(String, graphql_name='name_ends_with_nocase')
    name_not_ends_with = sgqlc.types.Field(String, graphql_name='name_not_ends_with')
    name_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='name_not_ends_with_nocase')
    symbol = sgqlc.types.Field(String, graphql_name='symbol')
    symbol_not = sgqlc.types.Field(String, graphql_name='symbol_not')
    symbol_gt = sgqlc.types.Field(String, graphql_name='symbol_gt')
    symbol_lt = sgqlc.types.Field(String, graphql_name='symbol_lt')
    symbol_gte = sgqlc.types.Field(String, graphql_name='symbol_gte')
    symbol_lte = sgqlc.types.Field(String, graphql_name='symbol_lte')
    symbol_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='symbol_in')
    symbol_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='symbol_not_in')
    symbol_contains = sgqlc.types.Field(String, graphql_name='symbol_contains')
    symbol_contains_nocase = sgqlc.types.Field(String, graphql_name='symbol_contains_nocase')
    symbol_not_contains = sgqlc.types.Field(String, graphql_name='symbol_not_contains')
    symbol_not_contains_nocase = sgqlc.types.Field(String, graphql_name='symbol_not_contains_nocase')
    symbol_starts_with = sgqlc.types.Field(String, graphql_name='symbol_starts_with')
    symbol_starts_with_nocase = sgqlc.types.Field(String, graphql_name='symbol_starts_with_nocase')
    symbol_not_starts_with = sgqlc.types.Field(String, graphql_name='symbol_not_starts_with')
    symbol_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='symbol_not_starts_with_nocase')
    symbol_ends_with = sgqlc.types.Field(String, graphql_name='symbol_ends_with')
    symbol_ends_with_nocase = sgqlc.types.Field(String, graphql_name='symbol_ends_with_nocase')
    symbol_not_ends_with = sgqlc.types.Field(String, graphql_name='symbol_not_ends_with')
    symbol_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='symbol_not_ends_with_nocase')
    decimals = sgqlc.types.Field(Int, graphql_name='decimals')
    decimals_not = sgqlc.types.Field(Int, graphql_name='decimals_not')
    decimals_gt = sgqlc.types.Field(Int, graphql_name='decimals_gt')
    decimals_lt = sgqlc.types.Field(Int, graphql_name='decimals_lt')
    decimals_gte = sgqlc.types.Field(Int, graphql_name='decimals_gte')
    decimals_lte = sgqlc.types.Field(Int, graphql_name='decimals_lte')
    decimals_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='decimals_in')
    decimals_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='decimals_not_in')
    last_price_usd = sgqlc.types.Field(BigDecimal, graphql_name='lastPriceUSD')
    last_price_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='lastPriceUSD_not')
    last_price_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='lastPriceUSD_gt')
    last_price_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='lastPriceUSD_lt')
    last_price_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='lastPriceUSD_gte')
    last_price_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='lastPriceUSD_lte')
    last_price_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='lastPriceUSD_in')
    last_price_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='lastPriceUSD_not_in')
    last_price_block_number = sgqlc.types.Field(BigInt, graphql_name='lastPriceBlockNumber')
    last_price_block_number_not = sgqlc.types.Field(BigInt, graphql_name='lastPriceBlockNumber_not')
    last_price_block_number_gt = sgqlc.types.Field(BigInt, graphql_name='lastPriceBlockNumber_gt')
    last_price_block_number_lt = sgqlc.types.Field(BigInt, graphql_name='lastPriceBlockNumber_lt')
    last_price_block_number_gte = sgqlc.types.Field(BigInt, graphql_name='lastPriceBlockNumber_gte')
    last_price_block_number_lte = sgqlc.types.Field(BigInt, graphql_name='lastPriceBlockNumber_lte')
    last_price_block_number_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='lastPriceBlockNumber_in')
    last_price_block_number_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='lastPriceBlockNumber_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class UsageMetricsDailySnapshot_filter(sgqlc.types.Input):
    __schema__ = subgraph_status_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'protocol', 'protocol_not', 'protocol_gt', 'protocol_lt', 'protocol_gte', 'protocol_lte', 'protocol_in', 'protocol_not_in', 'protocol_contains', 'protocol_contains_nocase', 'protocol_not_contains', 'protocol_not_contains_nocase', 'protocol_starts_with', 'protocol_starts_with_nocase', 'protocol_not_starts_with', 'protocol_not_starts_with_nocase', 'protocol_ends_with', 'protocol_ends_with_nocase', 'protocol_not_ends_with', 'protocol_not_ends_with_nocase', 'daily_active_users', 'daily_active_users_not', 'daily_active_users_gt', 'daily_active_users_lt', 'daily_active_users_gte', 'daily_active_users_lte', 'daily_active_users_in', 'daily_active_users_not_in', 'cumulative_unique_users', 'cumulative_unique_users_not', 'cumulative_unique_users_gt', 'cumulative_unique_users_lt', 'cumulative_unique_users_gte', 'cumulative_unique_users_lte', 'cumulative_unique_users_in', 'cumulative_unique_users_not_in', 'daily_transaction_count', 'daily_transaction_count_not', 'daily_transaction_count_gt', 'daily_transaction_count_lt', 'daily_transaction_count_gte', 'daily_transaction_count_lte', 'daily_transaction_count_in', 'daily_transaction_count_not_in', 'daily_deposit_count', 'daily_deposit_count_not', 'daily_deposit_count_gt', 'daily_deposit_count_lt', 'daily_deposit_count_gte', 'daily_deposit_count_lte', 'daily_deposit_count_in', 'daily_deposit_count_not_in', 'daily_withdraw_count', 'daily_withdraw_count_not', 'daily_withdraw_count_gt', 'daily_withdraw_count_lt', 'daily_withdraw_count_gte', 'daily_withdraw_count_lte', 'daily_withdraw_count_in', 'daily_withdraw_count_not_in', 'daily_borrow_count', 'daily_borrow_count_not', 'daily_borrow_count_gt', 'daily_borrow_count_lt', 'daily_borrow_count_gte', 'daily_borrow_count_lte', 'daily_borrow_count_in', 'daily_borrow_count_not_in', 'daily_repay_count', 'daily_repay_count_not', 'daily_repay_count_gt', 'daily_repay_count_lt', 'daily_repay_count_gte', 'daily_repay_count_lte', 'daily_repay_count_in', 'daily_repay_count_not_in', 'daily_liquidate_count', 'daily_liquidate_count_not', 'daily_liquidate_count_gt', 'daily_liquidate_count_lt', 'daily_liquidate_count_gte', 'daily_liquidate_count_lte', 'daily_liquidate_count_in', 'daily_liquidate_count_not_in', 'block_number', 'block_number_not', 'block_number_gt', 'block_number_lt', 'block_number_gte', 'block_number_lte', 'block_number_in', 'block_number_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    protocol = sgqlc.types.Field(String, graphql_name='protocol')
    protocol_not = sgqlc.types.Field(String, graphql_name='protocol_not')
    protocol_gt = sgqlc.types.Field(String, graphql_name='protocol_gt')
    protocol_lt = sgqlc.types.Field(String, graphql_name='protocol_lt')
    protocol_gte = sgqlc.types.Field(String, graphql_name='protocol_gte')
    protocol_lte = sgqlc.types.Field(String, graphql_name='protocol_lte')
    protocol_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_in')
    protocol_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_not_in')
    protocol_contains = sgqlc.types.Field(String, graphql_name='protocol_contains')
    protocol_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_contains_nocase')
    protocol_not_contains = sgqlc.types.Field(String, graphql_name='protocol_not_contains')
    protocol_not_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_contains_nocase')
    protocol_starts_with = sgqlc.types.Field(String, graphql_name='protocol_starts_with')
    protocol_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_starts_with_nocase')
    protocol_not_starts_with = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with')
    protocol_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with_nocase')
    protocol_ends_with = sgqlc.types.Field(String, graphql_name='protocol_ends_with')
    protocol_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_ends_with_nocase')
    protocol_not_ends_with = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with')
    protocol_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with_nocase')
    daily_active_users = sgqlc.types.Field(Int, graphql_name='dailyActiveUsers')
    daily_active_users_not = sgqlc.types.Field(Int, graphql_name='dailyActiveUsers_not')
    daily_active_users_gt = sgqlc.types.Field(Int, graphql_name='dailyActiveUsers_gt')
    daily_active_users_lt = sgqlc.types.Field(Int, graphql_name='dailyActiveUsers_lt')
    daily_active_users_gte = sgqlc.types.Field(Int, graphql_name='dailyActiveUsers_gte')
    daily_active_users_lte = sgqlc.types.Field(Int, graphql_name='dailyActiveUsers_lte')
    daily_active_users_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='dailyActiveUsers_in')
    daily_active_users_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='dailyActiveUsers_not_in')
    cumulative_unique_users = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers')
    cumulative_unique_users_not = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_not')
    cumulative_unique_users_gt = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_gt')
    cumulative_unique_users_lt = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_lt')
    cumulative_unique_users_gte = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_gte')
    cumulative_unique_users_lte = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_lte')
    cumulative_unique_users_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='cumulativeUniqueUsers_in')
    cumulative_unique_users_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='cumulativeUniqueUsers_not_in')
    daily_transaction_count = sgqlc.types.Field(Int, graphql_name='dailyTransactionCount')
    daily_transaction_count_not = sgqlc.types.Field(Int, graphql_name='dailyTransactionCount_not')
    daily_transaction_count_gt = sgqlc.types.Field(Int, graphql_name='dailyTransactionCount_gt')
    daily_transaction_count_lt = sgqlc.types.Field(Int, graphql_name='dailyTransactionCount_lt')
    daily_transaction_count_gte = sgqlc.types.Field(Int, graphql_name='dailyTransactionCount_gte')
    daily_transaction_count_lte = sgqlc.types.Field(Int, graphql_name='dailyTransactionCount_lte')
    daily_transaction_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='dailyTransactionCount_in')
    daily_transaction_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='dailyTransactionCount_not_in')
    daily_deposit_count = sgqlc.types.Field(Int, graphql_name='dailyDepositCount')
    daily_deposit_count_not = sgqlc.types.Field(Int, graphql_name='dailyDepositCount_not')
    daily_deposit_count_gt = sgqlc.types.Field(Int, graphql_name='dailyDepositCount_gt')
    daily_deposit_count_lt = sgqlc.types.Field(Int, graphql_name='dailyDepositCount_lt')
    daily_deposit_count_gte = sgqlc.types.Field(Int, graphql_name='dailyDepositCount_gte')
    daily_deposit_count_lte = sgqlc.types.Field(Int, graphql_name='dailyDepositCount_lte')
    daily_deposit_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='dailyDepositCount_in')
    daily_deposit_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='dailyDepositCount_not_in')
    daily_withdraw_count = sgqlc.types.Field(Int, graphql_name='dailyWithdrawCount')
    daily_withdraw_count_not = sgqlc.types.Field(Int, graphql_name='dailyWithdrawCount_not')
    daily_withdraw_count_gt = sgqlc.types.Field(Int, graphql_name='dailyWithdrawCount_gt')
    daily_withdraw_count_lt = sgqlc.types.Field(Int, graphql_name='dailyWithdrawCount_lt')
    daily_withdraw_count_gte = sgqlc.types.Field(Int, graphql_name='dailyWithdrawCount_gte')
    daily_withdraw_count_lte = sgqlc.types.Field(Int, graphql_name='dailyWithdrawCount_lte')
    daily_withdraw_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='dailyWithdrawCount_in')
    daily_withdraw_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='dailyWithdrawCount_not_in')
    daily_borrow_count = sgqlc.types.Field(Int, graphql_name='dailyBorrowCount')
    daily_borrow_count_not = sgqlc.types.Field(Int, graphql_name='dailyBorrowCount_not')
    daily_borrow_count_gt = sgqlc.types.Field(Int, graphql_name='dailyBorrowCount_gt')
    daily_borrow_count_lt = sgqlc.types.Field(Int, graphql_name='dailyBorrowCount_lt')
    daily_borrow_count_gte = sgqlc.types.Field(Int, graphql_name='dailyBorrowCount_gte')
    daily_borrow_count_lte = sgqlc.types.Field(Int, graphql_name='dailyBorrowCount_lte')
    daily_borrow_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='dailyBorrowCount_in')
    daily_borrow_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='dailyBorrowCount_not_in')
    daily_repay_count = sgqlc.types.Field(Int, graphql_name='dailyRepayCount')
    daily_repay_count_not = sgqlc.types.Field(Int, graphql_name='dailyRepayCount_not')
    daily_repay_count_gt = sgqlc.types.Field(Int, graphql_name='dailyRepayCount_gt')
    daily_repay_count_lt = sgqlc.types.Field(Int, graphql_name='dailyRepayCount_lt')
    daily_repay_count_gte = sgqlc.types.Field(Int, graphql_name='dailyRepayCount_gte')
    daily_repay_count_lte = sgqlc.types.Field(Int, graphql_name='dailyRepayCount_lte')
    daily_repay_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='dailyRepayCount_in')
    daily_repay_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='dailyRepayCount_not_in')
    daily_liquidate_count = sgqlc.types.Field(Int, graphql_name='dailyLiquidateCount')
    daily_liquidate_count_not = sgqlc.types.Field(Int, graphql_name='dailyLiquidateCount_not')
    daily_liquidate_count_gt = sgqlc.types.Field(Int, graphql_name='dailyLiquidateCount_gt')
    daily_liquidate_count_lt = sgqlc.types.Field(Int, graphql_name='dailyLiquidateCount_lt')
    daily_liquidate_count_gte = sgqlc.types.Field(Int, graphql_name='dailyLiquidateCount_gte')
    daily_liquidate_count_lte = sgqlc.types.Field(Int, graphql_name='dailyLiquidateCount_lte')
    daily_liquidate_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='dailyLiquidateCount_in')
    daily_liquidate_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='dailyLiquidateCount_not_in')
    block_number = sgqlc.types.Field(BigInt, graphql_name='blockNumber')
    block_number_not = sgqlc.types.Field(BigInt, graphql_name='blockNumber_not')
    block_number_gt = sgqlc.types.Field(BigInt, graphql_name='blockNumber_gt')
    block_number_lt = sgqlc.types.Field(BigInt, graphql_name='blockNumber_lt')
    block_number_gte = sgqlc.types.Field(BigInt, graphql_name='blockNumber_gte')
    block_number_lte = sgqlc.types.Field(BigInt, graphql_name='blockNumber_lte')
    block_number_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='blockNumber_in')
    block_number_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='blockNumber_not_in')
    timestamp = sgqlc.types.Field(BigInt, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class UsageMetricsHourlySnapshot_filter(sgqlc.types.Input):
    __schema__ = subgraph_status_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'protocol', 'protocol_not', 'protocol_gt', 'protocol_lt', 'protocol_gte', 'protocol_lte', 'protocol_in', 'protocol_not_in', 'protocol_contains', 'protocol_contains_nocase', 'protocol_not_contains', 'protocol_not_contains_nocase', 'protocol_starts_with', 'protocol_starts_with_nocase', 'protocol_not_starts_with', 'protocol_not_starts_with_nocase', 'protocol_ends_with', 'protocol_ends_with_nocase', 'protocol_not_ends_with', 'protocol_not_ends_with_nocase', 'hourly_active_users', 'hourly_active_users_not', 'hourly_active_users_gt', 'hourly_active_users_lt', 'hourly_active_users_gte', 'hourly_active_users_lte', 'hourly_active_users_in', 'hourly_active_users_not_in', 'cumulative_unique_users', 'cumulative_unique_users_not', 'cumulative_unique_users_gt', 'cumulative_unique_users_lt', 'cumulative_unique_users_gte', 'cumulative_unique_users_lte', 'cumulative_unique_users_in', 'cumulative_unique_users_not_in', 'hourly_transaction_count', 'hourly_transaction_count_not', 'hourly_transaction_count_gt', 'hourly_transaction_count_lt', 'hourly_transaction_count_gte', 'hourly_transaction_count_lte', 'hourly_transaction_count_in', 'hourly_transaction_count_not_in', 'hourly_deposit_count', 'hourly_deposit_count_not', 'hourly_deposit_count_gt', 'hourly_deposit_count_lt', 'hourly_deposit_count_gte', 'hourly_deposit_count_lte', 'hourly_deposit_count_in', 'hourly_deposit_count_not_in', 'hourly_withdraw_count', 'hourly_withdraw_count_not', 'hourly_withdraw_count_gt', 'hourly_withdraw_count_lt', 'hourly_withdraw_count_gte', 'hourly_withdraw_count_lte', 'hourly_withdraw_count_in', 'hourly_withdraw_count_not_in', 'hourly_borrow_count', 'hourly_borrow_count_not', 'hourly_borrow_count_gt', 'hourly_borrow_count_lt', 'hourly_borrow_count_gte', 'hourly_borrow_count_lte', 'hourly_borrow_count_in', 'hourly_borrow_count_not_in', 'hourly_repay_count', 'hourly_repay_count_not', 'hourly_repay_count_gt', 'hourly_repay_count_lt', 'hourly_repay_count_gte', 'hourly_repay_count_lte', 'hourly_repay_count_in', 'hourly_repay_count_not_in', 'hourly_liquidate_count', 'hourly_liquidate_count_not', 'hourly_liquidate_count_gt', 'hourly_liquidate_count_lt', 'hourly_liquidate_count_gte', 'hourly_liquidate_count_lte', 'hourly_liquidate_count_in', 'hourly_liquidate_count_not_in', 'block_number', 'block_number_not', 'block_number_gt', 'block_number_lt', 'block_number_gte', 'block_number_lte', 'block_number_in', 'block_number_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    protocol = sgqlc.types.Field(String, graphql_name='protocol')
    protocol_not = sgqlc.types.Field(String, graphql_name='protocol_not')
    protocol_gt = sgqlc.types.Field(String, graphql_name='protocol_gt')
    protocol_lt = sgqlc.types.Field(String, graphql_name='protocol_lt')
    protocol_gte = sgqlc.types.Field(String, graphql_name='protocol_gte')
    protocol_lte = sgqlc.types.Field(String, graphql_name='protocol_lte')
    protocol_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_in')
    protocol_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_not_in')
    protocol_contains = sgqlc.types.Field(String, graphql_name='protocol_contains')
    protocol_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_contains_nocase')
    protocol_not_contains = sgqlc.types.Field(String, graphql_name='protocol_not_contains')
    protocol_not_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_contains_nocase')
    protocol_starts_with = sgqlc.types.Field(String, graphql_name='protocol_starts_with')
    protocol_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_starts_with_nocase')
    protocol_not_starts_with = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with')
    protocol_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with_nocase')
    protocol_ends_with = sgqlc.types.Field(String, graphql_name='protocol_ends_with')
    protocol_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_ends_with_nocase')
    protocol_not_ends_with = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with')
    protocol_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with_nocase')
    hourly_active_users = sgqlc.types.Field(Int, graphql_name='hourlyActiveUsers')
    hourly_active_users_not = sgqlc.types.Field(Int, graphql_name='hourlyActiveUsers_not')
    hourly_active_users_gt = sgqlc.types.Field(Int, graphql_name='hourlyActiveUsers_gt')
    hourly_active_users_lt = sgqlc.types.Field(Int, graphql_name='hourlyActiveUsers_lt')
    hourly_active_users_gte = sgqlc.types.Field(Int, graphql_name='hourlyActiveUsers_gte')
    hourly_active_users_lte = sgqlc.types.Field(Int, graphql_name='hourlyActiveUsers_lte')
    hourly_active_users_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='hourlyActiveUsers_in')
    hourly_active_users_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='hourlyActiveUsers_not_in')
    cumulative_unique_users = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers')
    cumulative_unique_users_not = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_not')
    cumulative_unique_users_gt = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_gt')
    cumulative_unique_users_lt = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_lt')
    cumulative_unique_users_gte = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_gte')
    cumulative_unique_users_lte = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_lte')
    cumulative_unique_users_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='cumulativeUniqueUsers_in')
    cumulative_unique_users_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='cumulativeUniqueUsers_not_in')
    hourly_transaction_count = sgqlc.types.Field(Int, graphql_name='hourlyTransactionCount')
    hourly_transaction_count_not = sgqlc.types.Field(Int, graphql_name='hourlyTransactionCount_not')
    hourly_transaction_count_gt = sgqlc.types.Field(Int, graphql_name='hourlyTransactionCount_gt')
    hourly_transaction_count_lt = sgqlc.types.Field(Int, graphql_name='hourlyTransactionCount_lt')
    hourly_transaction_count_gte = sgqlc.types.Field(Int, graphql_name='hourlyTransactionCount_gte')
    hourly_transaction_count_lte = sgqlc.types.Field(Int, graphql_name='hourlyTransactionCount_lte')
    hourly_transaction_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='hourlyTransactionCount_in')
    hourly_transaction_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='hourlyTransactionCount_not_in')
    hourly_deposit_count = sgqlc.types.Field(Int, graphql_name='hourlyDepositCount')
    hourly_deposit_count_not = sgqlc.types.Field(Int, graphql_name='hourlyDepositCount_not')
    hourly_deposit_count_gt = sgqlc.types.Field(Int, graphql_name='hourlyDepositCount_gt')
    hourly_deposit_count_lt = sgqlc.types.Field(Int, graphql_name='hourlyDepositCount_lt')
    hourly_deposit_count_gte = sgqlc.types.Field(Int, graphql_name='hourlyDepositCount_gte')
    hourly_deposit_count_lte = sgqlc.types.Field(Int, graphql_name='hourlyDepositCount_lte')
    hourly_deposit_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='hourlyDepositCount_in')
    hourly_deposit_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='hourlyDepositCount_not_in')
    hourly_withdraw_count = sgqlc.types.Field(Int, graphql_name='hourlyWithdrawCount')
    hourly_withdraw_count_not = sgqlc.types.Field(Int, graphql_name='hourlyWithdrawCount_not')
    hourly_withdraw_count_gt = sgqlc.types.Field(Int, graphql_name='hourlyWithdrawCount_gt')
    hourly_withdraw_count_lt = sgqlc.types.Field(Int, graphql_name='hourlyWithdrawCount_lt')
    hourly_withdraw_count_gte = sgqlc.types.Field(Int, graphql_name='hourlyWithdrawCount_gte')
    hourly_withdraw_count_lte = sgqlc.types.Field(Int, graphql_name='hourlyWithdrawCount_lte')
    hourly_withdraw_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='hourlyWithdrawCount_in')
    hourly_withdraw_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='hourlyWithdrawCount_not_in')
    hourly_borrow_count = sgqlc.types.Field(Int, graphql_name='hourlyBorrowCount')
    hourly_borrow_count_not = sgqlc.types.Field(Int, graphql_name='hourlyBorrowCount_not')
    hourly_borrow_count_gt = sgqlc.types.Field(Int, graphql_name='hourlyBorrowCount_gt')
    hourly_borrow_count_lt = sgqlc.types.Field(Int, graphql_name='hourlyBorrowCount_lt')
    hourly_borrow_count_gte = sgqlc.types.Field(Int, graphql_name='hourlyBorrowCount_gte')
    hourly_borrow_count_lte = sgqlc.types.Field(Int, graphql_name='hourlyBorrowCount_lte')
    hourly_borrow_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='hourlyBorrowCount_in')
    hourly_borrow_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='hourlyBorrowCount_not_in')
    hourly_repay_count = sgqlc.types.Field(Int, graphql_name='hourlyRepayCount')
    hourly_repay_count_not = sgqlc.types.Field(Int, graphql_name='hourlyRepayCount_not')
    hourly_repay_count_gt = sgqlc.types.Field(Int, graphql_name='hourlyRepayCount_gt')
    hourly_repay_count_lt = sgqlc.types.Field(Int, graphql_name='hourlyRepayCount_lt')
    hourly_repay_count_gte = sgqlc.types.Field(Int, graphql_name='hourlyRepayCount_gte')
    hourly_repay_count_lte = sgqlc.types.Field(Int, graphql_name='hourlyRepayCount_lte')
    hourly_repay_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='hourlyRepayCount_in')
    hourly_repay_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='hourlyRepayCount_not_in')
    hourly_liquidate_count = sgqlc.types.Field(Int, graphql_name='hourlyLiquidateCount')
    hourly_liquidate_count_not = sgqlc.types.Field(Int, graphql_name='hourlyLiquidateCount_not')
    hourly_liquidate_count_gt = sgqlc.types.Field(Int, graphql_name='hourlyLiquidateCount_gt')
    hourly_liquidate_count_lt = sgqlc.types.Field(Int, graphql_name='hourlyLiquidateCount_lt')
    hourly_liquidate_count_gte = sgqlc.types.Field(Int, graphql_name='hourlyLiquidateCount_gte')
    hourly_liquidate_count_lte = sgqlc.types.Field(Int, graphql_name='hourlyLiquidateCount_lte')
    hourly_liquidate_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='hourlyLiquidateCount_in')
    hourly_liquidate_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='hourlyLiquidateCount_not_in')
    block_number = sgqlc.types.Field(BigInt, graphql_name='blockNumber')
    block_number_not = sgqlc.types.Field(BigInt, graphql_name='blockNumber_not')
    block_number_gt = sgqlc.types.Field(BigInt, graphql_name='blockNumber_gt')
    block_number_lt = sgqlc.types.Field(BigInt, graphql_name='blockNumber_lt')
    block_number_gte = sgqlc.types.Field(BigInt, graphql_name='blockNumber_gte')
    block_number_lte = sgqlc.types.Field(BigInt, graphql_name='blockNumber_lte')
    block_number_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='blockNumber_in')
    block_number_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='blockNumber_not_in')
    timestamp = sgqlc.types.Field(BigInt, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')


class Withdraw_filter(sgqlc.types.Input):
    __schema__ = subgraph_status_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'hash', 'hash_not', 'hash_gt', 'hash_lt', 'hash_gte', 'hash_lte', 'hash_in', 'hash_not_in', 'hash_contains', 'hash_contains_nocase', 'hash_not_contains', 'hash_not_contains_nocase', 'hash_starts_with', 'hash_starts_with_nocase', 'hash_not_starts_with', 'hash_not_starts_with_nocase', 'hash_ends_with', 'hash_ends_with_nocase', 'hash_not_ends_with', 'hash_not_ends_with_nocase', 'log_index', 'log_index_not', 'log_index_gt', 'log_index_lt', 'log_index_gte', 'log_index_lte', 'log_index_in', 'log_index_not_in', 'protocol', 'protocol_not', 'protocol_gt', 'protocol_lt', 'protocol_gte', 'protocol_lte', 'protocol_in', 'protocol_not_in', 'protocol_contains', 'protocol_contains_nocase', 'protocol_not_contains', 'protocol_not_contains_nocase', 'protocol_starts_with', 'protocol_starts_with_nocase', 'protocol_not_starts_with', 'protocol_not_starts_with_nocase', 'protocol_ends_with', 'protocol_ends_with_nocase', 'protocol_not_ends_with', 'protocol_not_ends_with_nocase', 'to', 'to_not', 'to_gt', 'to_lt', 'to_gte', 'to_lte', 'to_in', 'to_not_in', 'to_contains', 'to_contains_nocase', 'to_not_contains', 'to_not_contains_nocase', 'to_starts_with', 'to_starts_with_nocase', 'to_not_starts_with', 'to_not_starts_with_nocase', 'to_ends_with', 'to_ends_with_nocase', 'to_not_ends_with', 'to_not_ends_with_nocase', 'from_', 'from_not', 'from_gt', 'from_lt', 'from_gte', 'from_lte', 'from_in', 'from_not_in', 'from_contains', 'from_contains_nocase', 'from_not_contains', 'from_not_contains_nocase', 'from_starts_with', 'from_starts_with_nocase', 'from_not_starts_with', 'from_not_starts_with_nocase', 'from_ends_with', 'from_ends_with_nocase', 'from_not_ends_with', 'from_not_ends_with_nocase', 'block_number', 'block_number_not', 'block_number_gt', 'block_number_lt', 'block_number_gte', 'block_number_lte', 'block_number_in', 'block_number_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'market', 'market_not', 'market_gt', 'market_lt', 'market_gte', 'market_lte', 'market_in', 'market_not_in', 'market_contains', 'market_contains_nocase', 'market_not_contains', 'market_not_contains_nocase', 'market_starts_with', 'market_starts_with_nocase', 'market_not_starts_with', 'market_not_starts_with_nocase', 'market_ends_with', 'market_ends_with_nocase', 'market_not_ends_with', 'market_not_ends_with_nocase', 'asset', 'asset_not', 'asset_gt', 'asset_lt', 'asset_gte', 'asset_lte', 'asset_in', 'asset_not_in', 'asset_contains', 'asset_contains_nocase', 'asset_not_contains', 'asset_not_contains_nocase', 'asset_starts_with', 'asset_starts_with_nocase', 'asset_not_starts_with', 'asset_not_starts_with_nocase', 'asset_ends_with', 'asset_ends_with_nocase', 'asset_not_ends_with', 'asset_not_ends_with_nocase', 'amount', 'amount_not', 'amount_gt', 'amount_lt', 'amount_gte', 'amount_lte', 'amount_in', 'amount_not_in', 'amount_usd', 'amount_usd_not', 'amount_usd_gt', 'amount_usd_lt', 'amount_usd_gte', 'amount_usd_lte', 'amount_usd_in', 'amount_usd_not_in', '_change_block')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    hash_not = sgqlc.types.Field(String, graphql_name='hash_not')
    hash_gt = sgqlc.types.Field(String, graphql_name='hash_gt')
    hash_lt = sgqlc.types.Field(String, graphql_name='hash_lt')
    hash_gte = sgqlc.types.Field(String, graphql_name='hash_gte')
    hash_lte = sgqlc.types.Field(String, graphql_name='hash_lte')
    hash_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='hash_in')
    hash_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='hash_not_in')
    hash_contains = sgqlc.types.Field(String, graphql_name='hash_contains')
    hash_contains_nocase = sgqlc.types.Field(String, graphql_name='hash_contains_nocase')
    hash_not_contains = sgqlc.types.Field(String, graphql_name='hash_not_contains')
    hash_not_contains_nocase = sgqlc.types.Field(String, graphql_name='hash_not_contains_nocase')
    hash_starts_with = sgqlc.types.Field(String, graphql_name='hash_starts_with')
    hash_starts_with_nocase = sgqlc.types.Field(String, graphql_name='hash_starts_with_nocase')
    hash_not_starts_with = sgqlc.types.Field(String, graphql_name='hash_not_starts_with')
    hash_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='hash_not_starts_with_nocase')
    hash_ends_with = sgqlc.types.Field(String, graphql_name='hash_ends_with')
    hash_ends_with_nocase = sgqlc.types.Field(String, graphql_name='hash_ends_with_nocase')
    hash_not_ends_with = sgqlc.types.Field(String, graphql_name='hash_not_ends_with')
    hash_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='hash_not_ends_with_nocase')
    log_index = sgqlc.types.Field(Int, graphql_name='logIndex')
    log_index_not = sgqlc.types.Field(Int, graphql_name='logIndex_not')
    log_index_gt = sgqlc.types.Field(Int, graphql_name='logIndex_gt')
    log_index_lt = sgqlc.types.Field(Int, graphql_name='logIndex_lt')
    log_index_gte = sgqlc.types.Field(Int, graphql_name='logIndex_gte')
    log_index_lte = sgqlc.types.Field(Int, graphql_name='logIndex_lte')
    log_index_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='logIndex_in')
    log_index_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='logIndex_not_in')
    protocol = sgqlc.types.Field(String, graphql_name='protocol')
    protocol_not = sgqlc.types.Field(String, graphql_name='protocol_not')
    protocol_gt = sgqlc.types.Field(String, graphql_name='protocol_gt')
    protocol_lt = sgqlc.types.Field(String, graphql_name='protocol_lt')
    protocol_gte = sgqlc.types.Field(String, graphql_name='protocol_gte')
    protocol_lte = sgqlc.types.Field(String, graphql_name='protocol_lte')
    protocol_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_in')
    protocol_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_not_in')
    protocol_contains = sgqlc.types.Field(String, graphql_name='protocol_contains')
    protocol_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_contains_nocase')
    protocol_not_contains = sgqlc.types.Field(String, graphql_name='protocol_not_contains')
    protocol_not_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_contains_nocase')
    protocol_starts_with = sgqlc.types.Field(String, graphql_name='protocol_starts_with')
    protocol_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_starts_with_nocase')
    protocol_not_starts_with = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with')
    protocol_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with_nocase')
    protocol_ends_with = sgqlc.types.Field(String, graphql_name='protocol_ends_with')
    protocol_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_ends_with_nocase')
    protocol_not_ends_with = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with')
    protocol_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with_nocase')
    to = sgqlc.types.Field(String, graphql_name='to')
    to_not = sgqlc.types.Field(String, graphql_name='to_not')
    to_gt = sgqlc.types.Field(String, graphql_name='to_gt')
    to_lt = sgqlc.types.Field(String, graphql_name='to_lt')
    to_gte = sgqlc.types.Field(String, graphql_name='to_gte')
    to_lte = sgqlc.types.Field(String, graphql_name='to_lte')
    to_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='to_in')
    to_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='to_not_in')
    to_contains = sgqlc.types.Field(String, graphql_name='to_contains')
    to_contains_nocase = sgqlc.types.Field(String, graphql_name='to_contains_nocase')
    to_not_contains = sgqlc.types.Field(String, graphql_name='to_not_contains')
    to_not_contains_nocase = sgqlc.types.Field(String, graphql_name='to_not_contains_nocase')
    to_starts_with = sgqlc.types.Field(String, graphql_name='to_starts_with')
    to_starts_with_nocase = sgqlc.types.Field(String, graphql_name='to_starts_with_nocase')
    to_not_starts_with = sgqlc.types.Field(String, graphql_name='to_not_starts_with')
    to_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='to_not_starts_with_nocase')
    to_ends_with = sgqlc.types.Field(String, graphql_name='to_ends_with')
    to_ends_with_nocase = sgqlc.types.Field(String, graphql_name='to_ends_with_nocase')
    to_not_ends_with = sgqlc.types.Field(String, graphql_name='to_not_ends_with')
    to_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='to_not_ends_with_nocase')
    from_ = sgqlc.types.Field(String, graphql_name='from')
    from_not = sgqlc.types.Field(String, graphql_name='from_not')
    from_gt = sgqlc.types.Field(String, graphql_name='from_gt')
    from_lt = sgqlc.types.Field(String, graphql_name='from_lt')
    from_gte = sgqlc.types.Field(String, graphql_name='from_gte')
    from_lte = sgqlc.types.Field(String, graphql_name='from_lte')
    from_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='from_in')
    from_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='from_not_in')
    from_contains = sgqlc.types.Field(String, graphql_name='from_contains')
    from_contains_nocase = sgqlc.types.Field(String, graphql_name='from_contains_nocase')
    from_not_contains = sgqlc.types.Field(String, graphql_name='from_not_contains')
    from_not_contains_nocase = sgqlc.types.Field(String, graphql_name='from_not_contains_nocase')
    from_starts_with = sgqlc.types.Field(String, graphql_name='from_starts_with')
    from_starts_with_nocase = sgqlc.types.Field(String, graphql_name='from_starts_with_nocase')
    from_not_starts_with = sgqlc.types.Field(String, graphql_name='from_not_starts_with')
    from_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='from_not_starts_with_nocase')
    from_ends_with = sgqlc.types.Field(String, graphql_name='from_ends_with')
    from_ends_with_nocase = sgqlc.types.Field(String, graphql_name='from_ends_with_nocase')
    from_not_ends_with = sgqlc.types.Field(String, graphql_name='from_not_ends_with')
    from_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='from_not_ends_with_nocase')
    block_number = sgqlc.types.Field(BigInt, graphql_name='blockNumber')
    block_number_not = sgqlc.types.Field(BigInt, graphql_name='blockNumber_not')
    block_number_gt = sgqlc.types.Field(BigInt, graphql_name='blockNumber_gt')
    block_number_lt = sgqlc.types.Field(BigInt, graphql_name='blockNumber_lt')
    block_number_gte = sgqlc.types.Field(BigInt, graphql_name='blockNumber_gte')
    block_number_lte = sgqlc.types.Field(BigInt, graphql_name='blockNumber_lte')
    block_number_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='blockNumber_in')
    block_number_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='blockNumber_not_in')
    timestamp = sgqlc.types.Field(BigInt, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_not_in')
    market = sgqlc.types.Field(String, graphql_name='market')
    market_not = sgqlc.types.Field(String, graphql_name='market_not')
    market_gt = sgqlc.types.Field(String, graphql_name='market_gt')
    market_lt = sgqlc.types.Field(String, graphql_name='market_lt')
    market_gte = sgqlc.types.Field(String, graphql_name='market_gte')
    market_lte = sgqlc.types.Field(String, graphql_name='market_lte')
    market_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='market_in')
    market_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='market_not_in')
    market_contains = sgqlc.types.Field(String, graphql_name='market_contains')
    market_contains_nocase = sgqlc.types.Field(String, graphql_name='market_contains_nocase')
    market_not_contains = sgqlc.types.Field(String, graphql_name='market_not_contains')
    market_not_contains_nocase = sgqlc.types.Field(String, graphql_name='market_not_contains_nocase')
    market_starts_with = sgqlc.types.Field(String, graphql_name='market_starts_with')
    market_starts_with_nocase = sgqlc.types.Field(String, graphql_name='market_starts_with_nocase')
    market_not_starts_with = sgqlc.types.Field(String, graphql_name='market_not_starts_with')
    market_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='market_not_starts_with_nocase')
    market_ends_with = sgqlc.types.Field(String, graphql_name='market_ends_with')
    market_ends_with_nocase = sgqlc.types.Field(String, graphql_name='market_ends_with_nocase')
    market_not_ends_with = sgqlc.types.Field(String, graphql_name='market_not_ends_with')
    market_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='market_not_ends_with_nocase')
    asset = sgqlc.types.Field(String, graphql_name='asset')
    asset_not = sgqlc.types.Field(String, graphql_name='asset_not')
    asset_gt = sgqlc.types.Field(String, graphql_name='asset_gt')
    asset_lt = sgqlc.types.Field(String, graphql_name='asset_lt')
    asset_gte = sgqlc.types.Field(String, graphql_name='asset_gte')
    asset_lte = sgqlc.types.Field(String, graphql_name='asset_lte')
    asset_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='asset_in')
    asset_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='asset_not_in')
    asset_contains = sgqlc.types.Field(String, graphql_name='asset_contains')
    asset_contains_nocase = sgqlc.types.Field(String, graphql_name='asset_contains_nocase')
    asset_not_contains = sgqlc.types.Field(String, graphql_name='asset_not_contains')
    asset_not_contains_nocase = sgqlc.types.Field(String, graphql_name='asset_not_contains_nocase')
    asset_starts_with = sgqlc.types.Field(String, graphql_name='asset_starts_with')
    asset_starts_with_nocase = sgqlc.types.Field(String, graphql_name='asset_starts_with_nocase')
    asset_not_starts_with = sgqlc.types.Field(String, graphql_name='asset_not_starts_with')
    asset_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='asset_not_starts_with_nocase')
    asset_ends_with = sgqlc.types.Field(String, graphql_name='asset_ends_with')
    asset_ends_with_nocase = sgqlc.types.Field(String, graphql_name='asset_ends_with_nocase')
    asset_not_ends_with = sgqlc.types.Field(String, graphql_name='asset_not_ends_with')
    asset_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='asset_not_ends_with_nocase')
    amount = sgqlc.types.Field(BigInt, graphql_name='amount')
    amount_not = sgqlc.types.Field(BigInt, graphql_name='amount_not')
    amount_gt = sgqlc.types.Field(BigInt, graphql_name='amount_gt')
    amount_lt = sgqlc.types.Field(BigInt, graphql_name='amount_lt')
    amount_gte = sgqlc.types.Field(BigInt, graphql_name='amount_gte')
    amount_lte = sgqlc.types.Field(BigInt, graphql_name='amount_lte')
    amount_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='amount_in')
    amount_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='amount_not_in')
    amount_usd = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD')
    amount_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_not')
    amount_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_gt')
    amount_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_lt')
    amount_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_gte')
    amount_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_lte')
    amount_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amountUSD_in')
    amount_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amountUSD_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')



########################################################################
# Output Objects and Interfaces
########################################################################
class Account(sgqlc.types.Type):
    __schema__ = subgraph_status_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class ActiveAccount(sgqlc.types.Type):
    __schema__ = subgraph_status_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class Event(sgqlc.types.Interface):
    __schema__ = subgraph_status_schema
    __field_names__ = ('id', 'hash', 'log_index', 'protocol', 'to', 'from_', 'block_number', 'timestamp')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    hash = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='hash')
    log_index = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='logIndex')
    protocol = sgqlc.types.Field(sgqlc.types.non_null('LendingProtocol'), graphql_name='protocol')
    to = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='to')
    from_ = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='from')
    block_number = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='blockNumber')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='timestamp')


class FinancialsDailySnapshot(sgqlc.types.Type):
    __schema__ = subgraph_status_schema
    __field_names__ = ('id', 'protocol', 'block_number', 'timestamp', 'total_value_locked_usd', 'protocol_controlled_value_usd', 'minted_token_supplies', 'daily_supply_side_revenue_usd', 'cumulative_supply_side_revenue_usd', 'daily_protocol_side_revenue_usd', 'cumulative_protocol_side_revenue_usd', 'daily_total_revenue_usd', 'cumulative_total_revenue_usd', 'total_deposit_balance_usd', 'daily_deposit_usd', 'cumulative_deposit_usd', 'total_borrow_balance_usd', 'daily_borrow_usd', 'cumulative_borrow_usd', 'daily_liquidate_usd', 'cumulative_liquidate_usd')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    protocol = sgqlc.types.Field(sgqlc.types.non_null('LendingProtocol'), graphql_name='protocol')
    block_number = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='blockNumber')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='timestamp')
    total_value_locked_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalValueLockedUSD')
    protocol_controlled_value_usd = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD')
    minted_token_supplies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='mintedTokenSupplies')
    daily_supply_side_revenue_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='dailySupplySideRevenueUSD')
    cumulative_supply_side_revenue_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeSupplySideRevenueUSD')
    daily_protocol_side_revenue_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='dailyProtocolSideRevenueUSD')
    cumulative_protocol_side_revenue_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeProtocolSideRevenueUSD')
    daily_total_revenue_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='dailyTotalRevenueUSD')
    cumulative_total_revenue_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeTotalRevenueUSD')
    total_deposit_balance_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalDepositBalanceUSD')
    daily_deposit_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='dailyDepositUSD')
    cumulative_deposit_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeDepositUSD')
    total_borrow_balance_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalBorrowBalanceUSD')
    daily_borrow_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='dailyBorrowUSD')
    cumulative_borrow_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeBorrowUSD')
    daily_liquidate_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='dailyLiquidateUSD')
    cumulative_liquidate_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeLiquidateUSD')


class InterestRate(sgqlc.types.Type):
    __schema__ = subgraph_status_schema
    __field_names__ = ('id', 'rate', 'duration', 'maturity_block', 'side', 'type')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    rate = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='rate')
    duration = sgqlc.types.Field(Int, graphql_name='duration')
    maturity_block = sgqlc.types.Field(BigInt, graphql_name='maturityBlock')
    side = sgqlc.types.Field(sgqlc.types.non_null(InterestRateSide), graphql_name='side')
    type = sgqlc.types.Field(sgqlc.types.non_null(InterestRateType), graphql_name='type')


class Market(sgqlc.types.Type):
    __schema__ = subgraph_status_schema
    __field_names__ = ('id', 'protocol', 'name', 'is_active', 'can_use_as_collateral', 'can_borrow_from', 'maximum_ltv', 'liquidation_threshold', 'liquidation_penalty', 'input_token', 'output_token', 'reward_tokens', 'rates', 'total_value_locked_usd', 'total_deposit_balance_usd', 'cumulative_deposit_usd', 'total_borrow_balance_usd', 'cumulative_borrow_usd', 'cumulative_liquidate_usd', 'input_token_balance', 'input_token_price_usd', 'output_token_supply', 'output_token_price_usd', 'exchange_rate', 'reward_token_emissions_amount', 'reward_token_emissions_usd', 'created_timestamp', 'created_block_number', 'daily_snapshots', 'hourly_snapshots', 'deposits', 'withdraws', 'borrows', 'repays', 'liquidates')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    protocol = sgqlc.types.Field(sgqlc.types.non_null('LendingProtocol'), graphql_name='protocol')
    name = sgqlc.types.Field(String, graphql_name='name')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    can_use_as_collateral = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canUseAsCollateral')
    can_borrow_from = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canBorrowFrom')
    maximum_ltv = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='maximumLTV')
    liquidation_threshold = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='liquidationThreshold')
    liquidation_penalty = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='liquidationPenalty')
    input_token = sgqlc.types.Field(sgqlc.types.non_null('Token'), graphql_name='inputToken')
    output_token = sgqlc.types.Field('Token', graphql_name='outputToken')
    reward_tokens = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RewardToken')), graphql_name='rewardTokens', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(RewardToken_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(RewardToken_filter, graphql_name='where', default=None)),
))
    )
    rates = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(InterestRate))), graphql_name='rates', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(InterestRate_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(InterestRate_filter, graphql_name='where', default=None)),
))
    )
    total_value_locked_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalValueLockedUSD')
    total_deposit_balance_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalDepositBalanceUSD')
    cumulative_deposit_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeDepositUSD')
    total_borrow_balance_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalBorrowBalanceUSD')
    cumulative_borrow_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeBorrowUSD')
    cumulative_liquidate_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeLiquidateUSD')
    input_token_balance = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='inputTokenBalance')
    input_token_price_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='inputTokenPriceUSD')
    output_token_supply = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='outputTokenSupply')
    output_token_price_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='outputTokenPriceUSD')
    exchange_rate = sgqlc.types.Field(BigDecimal, graphql_name='exchangeRate')
    reward_token_emissions_amount = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount')
    reward_token_emissions_usd = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD')
    created_timestamp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='createdTimestamp')
    created_block_number = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='createdBlockNumber')
    daily_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MarketDailySnapshot'))), graphql_name='dailySnapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(MarketDailySnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(MarketDailySnapshot_filter, graphql_name='where', default=None)),
))
    )
    hourly_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MarketHourlySnapshot'))), graphql_name='hourlySnapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(MarketHourlySnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(MarketHourlySnapshot_filter, graphql_name='where', default=None)),
))
    )
    deposits = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Deposit'))), graphql_name='deposits', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Deposit_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Deposit_filter, graphql_name='where', default=None)),
))
    )
    withdraws = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Withdraw'))), graphql_name='withdraws', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Withdraw_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Withdraw_filter, graphql_name='where', default=None)),
))
    )
    borrows = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Borrow'))), graphql_name='borrows', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Borrow_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Borrow_filter, graphql_name='where', default=None)),
))
    )
    repays = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Repay'))), graphql_name='repays', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Repay_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Repay_filter, graphql_name='where', default=None)),
))
    )
    liquidates = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Liquidate'))), graphql_name='liquidates', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Liquidate_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Liquidate_filter, graphql_name='where', default=None)),
))
    )


class MarketDailySnapshot(sgqlc.types.Type):
    __schema__ = subgraph_status_schema
    __field_names__ = ('id', 'protocol', 'market', 'block_number', 'timestamp', 'rates', 'total_value_locked_usd', 'total_deposit_balance_usd', 'daily_deposit_usd', 'cumulative_deposit_usd', 'total_borrow_balance_usd', 'daily_borrow_usd', 'cumulative_borrow_usd', 'daily_liquidate_usd', 'cumulative_liquidate_usd', 'input_token_balance', 'input_token_price_usd', 'output_token_supply', 'output_token_price_usd', 'exchange_rate', 'reward_token_emissions_amount', 'reward_token_emissions_usd')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    protocol = sgqlc.types.Field(sgqlc.types.non_null('LendingProtocol'), graphql_name='protocol')
    market = sgqlc.types.Field(sgqlc.types.non_null(Market), graphql_name='market')
    block_number = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='blockNumber')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='timestamp')
    rates = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(InterestRate))), graphql_name='rates', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(InterestRate_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(InterestRate_filter, graphql_name='where', default=None)),
))
    )
    total_value_locked_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalValueLockedUSD')
    total_deposit_balance_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalDepositBalanceUSD')
    daily_deposit_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='dailyDepositUSD')
    cumulative_deposit_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeDepositUSD')
    total_borrow_balance_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalBorrowBalanceUSD')
    daily_borrow_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='dailyBorrowUSD')
    cumulative_borrow_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeBorrowUSD')
    daily_liquidate_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='dailyLiquidateUSD')
    cumulative_liquidate_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeLiquidateUSD')
    input_token_balance = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='inputTokenBalance')
    input_token_price_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='inputTokenPriceUSD')
    output_token_supply = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='outputTokenSupply')
    output_token_price_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='outputTokenPriceUSD')
    exchange_rate = sgqlc.types.Field(BigDecimal, graphql_name='exchangeRate')
    reward_token_emissions_amount = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount')
    reward_token_emissions_usd = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD')


class MarketHourlySnapshot(sgqlc.types.Type):
    __schema__ = subgraph_status_schema
    __field_names__ = ('id', 'protocol', 'market', 'block_number', 'timestamp', 'rates', 'total_value_locked_usd', 'total_deposit_balance_usd', 'hourly_deposit_usd', 'cumulative_deposit_usd', 'total_borrow_balance_usd', 'hourly_borrow_usd', 'cumulative_borrow_usd', 'hourly_liquidate_usd', 'cumulative_liquidate_usd', 'input_token_balance', 'input_token_price_usd', 'output_token_supply', 'output_token_price_usd', 'exchange_rate', 'reward_token_emissions_amount', 'reward_token_emissions_usd')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    protocol = sgqlc.types.Field(sgqlc.types.non_null('LendingProtocol'), graphql_name='protocol')
    market = sgqlc.types.Field(sgqlc.types.non_null(Market), graphql_name='market')
    block_number = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='blockNumber')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='timestamp')
    rates = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(InterestRate))), graphql_name='rates', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(InterestRate_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(InterestRate_filter, graphql_name='where', default=None)),
))
    )
    total_value_locked_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalValueLockedUSD')
    total_deposit_balance_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalDepositBalanceUSD')
    hourly_deposit_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='hourlyDepositUSD')
    cumulative_deposit_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeDepositUSD')
    total_borrow_balance_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalBorrowBalanceUSD')
    hourly_borrow_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='hourlyBorrowUSD')
    cumulative_borrow_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeBorrowUSD')
    hourly_liquidate_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='hourlyLiquidateUSD')
    cumulative_liquidate_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeLiquidateUSD')
    input_token_balance = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='inputTokenBalance')
    input_token_price_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='inputTokenPriceUSD')
    output_token_supply = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='outputTokenSupply')
    output_token_price_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='outputTokenPriceUSD')
    exchange_rate = sgqlc.types.Field(BigDecimal, graphql_name='exchangeRate')
    reward_token_emissions_amount = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount')
    reward_token_emissions_usd = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD')


class Protocol(sgqlc.types.Interface):
    __schema__ = subgraph_status_schema
    __field_names__ = ('id', 'name', 'slug', 'schema_version', 'subgraph_version', 'methodology_version', 'network', 'type', 'total_value_locked_usd', 'protocol_controlled_value_usd', 'cumulative_unique_users', 'cumulative_supply_side_revenue_usd', 'cumulative_protocol_side_revenue_usd', 'cumulative_total_revenue_usd', 'daily_usage_metrics', 'hourly_usage_metrics', 'financial_metrics')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')
    schema_version = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='schemaVersion')
    subgraph_version = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='subgraphVersion')
    methodology_version = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='methodologyVersion')
    network = sgqlc.types.Field(sgqlc.types.non_null(Network), graphql_name='network')
    type = sgqlc.types.Field(sgqlc.types.non_null(ProtocolType), graphql_name='type')
    total_value_locked_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalValueLockedUSD')
    protocol_controlled_value_usd = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD')
    cumulative_unique_users = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='cumulativeUniqueUsers')
    cumulative_supply_side_revenue_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeSupplySideRevenueUSD')
    cumulative_protocol_side_revenue_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeProtocolSideRevenueUSD')
    cumulative_total_revenue_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeTotalRevenueUSD')
    daily_usage_metrics = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UsageMetricsDailySnapshot'))), graphql_name='dailyUsageMetrics', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(UsageMetricsDailySnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(UsageMetricsDailySnapshot_filter, graphql_name='where', default=None)),
))
    )
    hourly_usage_metrics = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UsageMetricsHourlySnapshot'))), graphql_name='hourlyUsageMetrics', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(UsageMetricsHourlySnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(UsageMetricsHourlySnapshot_filter, graphql_name='where', default=None)),
))
    )
    financial_metrics = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FinancialsDailySnapshot))), graphql_name='financialMetrics', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(FinancialsDailySnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(FinancialsDailySnapshot_filter, graphql_name='where', default=None)),
))
    )


class Query(sgqlc.types.Type):
    __schema__ = subgraph_status_schema
    __field_names__ = ('token', 'tokens', 'reward_token', 'reward_tokens', 'interest_rate', 'interest_rates', 'lending_protocol', 'lending_protocols', 'usage_metrics_daily_snapshot', 'usage_metrics_daily_snapshots', 'usage_metrics_hourly_snapshot', 'usage_metrics_hourly_snapshots', 'financials_daily_snapshot', 'financials_daily_snapshots', 'market', 'markets', 'market_daily_snapshot', 'market_daily_snapshots', 'market_hourly_snapshot', 'market_hourly_snapshots', 'deposit', 'deposits', 'withdraw', 'withdraws', 'borrow', 'borrows', 'repay', 'repays', 'liquidate', 'liquidates', 'account', 'accounts', 'active_account', 'active_accounts', 'protocol', 'protocols', 'event', 'events', '_meta')
    token = sgqlc.types.Field('Token', graphql_name='token', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    tokens = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Token'))), graphql_name='tokens', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Token_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Token_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    reward_token = sgqlc.types.Field('RewardToken', graphql_name='rewardToken', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    reward_tokens = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RewardToken'))), graphql_name='rewardTokens', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(RewardToken_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(RewardToken_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    interest_rate = sgqlc.types.Field(InterestRate, graphql_name='interestRate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    interest_rates = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(InterestRate))), graphql_name='interestRates', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(InterestRate_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(InterestRate_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    lending_protocol = sgqlc.types.Field('LendingProtocol', graphql_name='lendingProtocol', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    lending_protocols = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('LendingProtocol'))), graphql_name='lendingProtocols', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(LendingProtocol_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(LendingProtocol_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    usage_metrics_daily_snapshot = sgqlc.types.Field('UsageMetricsDailySnapshot', graphql_name='usageMetricsDailySnapshot', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    usage_metrics_daily_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UsageMetricsDailySnapshot'))), graphql_name='usageMetricsDailySnapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(UsageMetricsDailySnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(UsageMetricsDailySnapshot_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    usage_metrics_hourly_snapshot = sgqlc.types.Field('UsageMetricsHourlySnapshot', graphql_name='usageMetricsHourlySnapshot', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    usage_metrics_hourly_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UsageMetricsHourlySnapshot'))), graphql_name='usageMetricsHourlySnapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(UsageMetricsHourlySnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(UsageMetricsHourlySnapshot_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    financials_daily_snapshot = sgqlc.types.Field(FinancialsDailySnapshot, graphql_name='financialsDailySnapshot', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    financials_daily_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FinancialsDailySnapshot))), graphql_name='financialsDailySnapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(FinancialsDailySnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(FinancialsDailySnapshot_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    market = sgqlc.types.Field(Market, graphql_name='market', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    markets = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Market))), graphql_name='markets', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Market_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Market_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    market_daily_snapshot = sgqlc.types.Field(MarketDailySnapshot, graphql_name='marketDailySnapshot', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    market_daily_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MarketDailySnapshot))), graphql_name='marketDailySnapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(MarketDailySnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(MarketDailySnapshot_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    market_hourly_snapshot = sgqlc.types.Field(MarketHourlySnapshot, graphql_name='marketHourlySnapshot', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    market_hourly_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MarketHourlySnapshot))), graphql_name='marketHourlySnapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(MarketHourlySnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(MarketHourlySnapshot_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    deposit = sgqlc.types.Field('Deposit', graphql_name='deposit', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    deposits = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Deposit'))), graphql_name='deposits', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Deposit_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Deposit_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    withdraw = sgqlc.types.Field('Withdraw', graphql_name='withdraw', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    withdraws = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Withdraw'))), graphql_name='withdraws', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Withdraw_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Withdraw_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    borrow = sgqlc.types.Field('Borrow', graphql_name='borrow', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    borrows = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Borrow'))), graphql_name='borrows', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Borrow_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Borrow_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    repay = sgqlc.types.Field('Repay', graphql_name='repay', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    repays = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Repay'))), graphql_name='repays', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Repay_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Repay_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    liquidate = sgqlc.types.Field('Liquidate', graphql_name='liquidate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    liquidates = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Liquidate'))), graphql_name='liquidates', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Liquidate_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Liquidate_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    account = sgqlc.types.Field(Account, graphql_name='account', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    accounts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Account))), graphql_name='accounts', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Account_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Account_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    active_account = sgqlc.types.Field(ActiveAccount, graphql_name='activeAccount', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    active_accounts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ActiveAccount))), graphql_name='activeAccounts', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(ActiveAccount_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(ActiveAccount_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    protocol = sgqlc.types.Field(Protocol, graphql_name='protocol', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    protocols = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Protocol))), graphql_name='protocols', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Protocol_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Protocol_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    event = sgqlc.types.Field(Event, graphql_name='event', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    events = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Event))), graphql_name='events', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Event_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Event_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    _meta = sgqlc.types.Field('_Meta_', graphql_name='_meta', args=sgqlc.types.ArgDict((
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )


class RewardToken(sgqlc.types.Type):
    __schema__ = subgraph_status_schema
    __field_names__ = ('id', 'token', 'type')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    token = sgqlc.types.Field(sgqlc.types.non_null('Token'), graphql_name='token')
    type = sgqlc.types.Field(sgqlc.types.non_null(RewardTokenType), graphql_name='type')


class Subscription(sgqlc.types.Type):
    __schema__ = subgraph_status_schema
    __field_names__ = ('token', 'tokens', 'reward_token', 'reward_tokens', 'interest_rate', 'interest_rates', 'lending_protocol', 'lending_protocols', 'usage_metrics_daily_snapshot', 'usage_metrics_daily_snapshots', 'usage_metrics_hourly_snapshot', 'usage_metrics_hourly_snapshots', 'financials_daily_snapshot', 'financials_daily_snapshots', 'market', 'markets', 'market_daily_snapshot', 'market_daily_snapshots', 'market_hourly_snapshot', 'market_hourly_snapshots', 'deposit', 'deposits', 'withdraw', 'withdraws', 'borrow', 'borrows', 'repay', 'repays', 'liquidate', 'liquidates', 'account', 'accounts', 'active_account', 'active_accounts', 'protocol', 'protocols', 'event', 'events', '_meta')
    token = sgqlc.types.Field('Token', graphql_name='token', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    tokens = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Token'))), graphql_name='tokens', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Token_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Token_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    reward_token = sgqlc.types.Field(RewardToken, graphql_name='rewardToken', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    reward_tokens = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(RewardToken))), graphql_name='rewardTokens', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(RewardToken_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(RewardToken_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    interest_rate = sgqlc.types.Field(InterestRate, graphql_name='interestRate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    interest_rates = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(InterestRate))), graphql_name='interestRates', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(InterestRate_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(InterestRate_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    lending_protocol = sgqlc.types.Field('LendingProtocol', graphql_name='lendingProtocol', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    lending_protocols = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('LendingProtocol'))), graphql_name='lendingProtocols', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(LendingProtocol_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(LendingProtocol_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    usage_metrics_daily_snapshot = sgqlc.types.Field('UsageMetricsDailySnapshot', graphql_name='usageMetricsDailySnapshot', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    usage_metrics_daily_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UsageMetricsDailySnapshot'))), graphql_name='usageMetricsDailySnapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(UsageMetricsDailySnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(UsageMetricsDailySnapshot_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    usage_metrics_hourly_snapshot = sgqlc.types.Field('UsageMetricsHourlySnapshot', graphql_name='usageMetricsHourlySnapshot', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    usage_metrics_hourly_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UsageMetricsHourlySnapshot'))), graphql_name='usageMetricsHourlySnapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(UsageMetricsHourlySnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(UsageMetricsHourlySnapshot_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    financials_daily_snapshot = sgqlc.types.Field(FinancialsDailySnapshot, graphql_name='financialsDailySnapshot', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    financials_daily_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FinancialsDailySnapshot))), graphql_name='financialsDailySnapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(FinancialsDailySnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(FinancialsDailySnapshot_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    market = sgqlc.types.Field(Market, graphql_name='market', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    markets = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Market))), graphql_name='markets', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Market_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Market_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    market_daily_snapshot = sgqlc.types.Field(MarketDailySnapshot, graphql_name='marketDailySnapshot', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    market_daily_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MarketDailySnapshot))), graphql_name='marketDailySnapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(MarketDailySnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(MarketDailySnapshot_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    market_hourly_snapshot = sgqlc.types.Field(MarketHourlySnapshot, graphql_name='marketHourlySnapshot', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    market_hourly_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MarketHourlySnapshot))), graphql_name='marketHourlySnapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(MarketHourlySnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(MarketHourlySnapshot_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    deposit = sgqlc.types.Field('Deposit', graphql_name='deposit', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    deposits = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Deposit'))), graphql_name='deposits', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Deposit_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Deposit_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    withdraw = sgqlc.types.Field('Withdraw', graphql_name='withdraw', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    withdraws = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Withdraw'))), graphql_name='withdraws', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Withdraw_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Withdraw_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    borrow = sgqlc.types.Field('Borrow', graphql_name='borrow', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    borrows = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Borrow'))), graphql_name='borrows', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Borrow_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Borrow_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    repay = sgqlc.types.Field('Repay', graphql_name='repay', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    repays = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Repay'))), graphql_name='repays', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Repay_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Repay_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    liquidate = sgqlc.types.Field('Liquidate', graphql_name='liquidate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    liquidates = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Liquidate'))), graphql_name='liquidates', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Liquidate_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Liquidate_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    account = sgqlc.types.Field(Account, graphql_name='account', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    accounts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Account))), graphql_name='accounts', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Account_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Account_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    active_account = sgqlc.types.Field(ActiveAccount, graphql_name='activeAccount', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    active_accounts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ActiveAccount))), graphql_name='activeAccounts', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(ActiveAccount_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(ActiveAccount_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    protocol = sgqlc.types.Field(Protocol, graphql_name='protocol', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    protocols = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Protocol))), graphql_name='protocols', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Protocol_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Protocol_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    event = sgqlc.types.Field(Event, graphql_name='event', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    events = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Event))), graphql_name='events', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Event_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Event_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    _meta = sgqlc.types.Field('_Meta_', graphql_name='_meta', args=sgqlc.types.ArgDict((
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )


class Token(sgqlc.types.Type):
    __schema__ = subgraph_status_schema
    __field_names__ = ('id', 'name', 'symbol', 'decimals', 'last_price_usd', 'last_price_block_number')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    symbol = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='symbol')
    decimals = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='decimals')
    last_price_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='lastPriceUSD')
    last_price_block_number = sgqlc.types.Field(BigInt, graphql_name='lastPriceBlockNumber')


class UsageMetricsDailySnapshot(sgqlc.types.Type):
    __schema__ = subgraph_status_schema
    __field_names__ = ('id', 'protocol', 'daily_active_users', 'cumulative_unique_users', 'daily_transaction_count', 'daily_deposit_count', 'daily_withdraw_count', 'daily_borrow_count', 'daily_repay_count', 'daily_liquidate_count', 'block_number', 'timestamp')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    protocol = sgqlc.types.Field(sgqlc.types.non_null('LendingProtocol'), graphql_name='protocol')
    daily_active_users = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='dailyActiveUsers')
    cumulative_unique_users = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='cumulativeUniqueUsers')
    daily_transaction_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='dailyTransactionCount')
    daily_deposit_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='dailyDepositCount')
    daily_withdraw_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='dailyWithdrawCount')
    daily_borrow_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='dailyBorrowCount')
    daily_repay_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='dailyRepayCount')
    daily_liquidate_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='dailyLiquidateCount')
    block_number = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='blockNumber')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='timestamp')


class UsageMetricsHourlySnapshot(sgqlc.types.Type):
    __schema__ = subgraph_status_schema
    __field_names__ = ('id', 'protocol', 'hourly_active_users', 'cumulative_unique_users', 'hourly_transaction_count', 'hourly_deposit_count', 'hourly_withdraw_count', 'hourly_borrow_count', 'hourly_repay_count', 'hourly_liquidate_count', 'block_number', 'timestamp')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    protocol = sgqlc.types.Field(sgqlc.types.non_null('LendingProtocol'), graphql_name='protocol')
    hourly_active_users = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='hourlyActiveUsers')
    cumulative_unique_users = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='cumulativeUniqueUsers')
    hourly_transaction_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='hourlyTransactionCount')
    hourly_deposit_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='hourlyDepositCount')
    hourly_withdraw_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='hourlyWithdrawCount')
    hourly_borrow_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='hourlyBorrowCount')
    hourly_repay_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='hourlyRepayCount')
    hourly_liquidate_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='hourlyLiquidateCount')
    block_number = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='blockNumber')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='timestamp')


class _Block_(sgqlc.types.Type):
    __schema__ = subgraph_status_schema
    __field_names__ = ('hash', 'number')
    hash = sgqlc.types.Field(Bytes, graphql_name='hash')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')

class _Meta_(sgqlc.types.Type):
    __schema__ = subgraph_status_schema
    __field_names__ = ('block', 'deployment', 'has_indexing_errors')
    block = sgqlc.types.Field(sgqlc.types.non_null(_Block_), graphql_name='block')
    deployment = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deployment')
    has_indexing_errors = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasIndexingErrors')

class Borrow(sgqlc.types.Type, Event):
    __schema__ = subgraph_status_schema
    __field_names__ = ('market', 'asset', 'amount', 'amount_usd')
    market = sgqlc.types.Field(sgqlc.types.non_null(Market), graphql_name='market')
    asset = sgqlc.types.Field(sgqlc.types.non_null(Token), graphql_name='asset')
    amount = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='amount')
    amount_usd = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD')


class Deposit(sgqlc.types.Type, Event):
    __schema__ = subgraph_status_schema
    __field_names__ = ('market', 'asset', 'amount', 'amount_usd')
    market = sgqlc.types.Field(sgqlc.types.non_null(Market), graphql_name='market')
    asset = sgqlc.types.Field(sgqlc.types.non_null(Token), graphql_name='asset')
    amount = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='amount')
    amount_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='amountUSD')


class LendingProtocol(sgqlc.types.Type, Protocol):
    __schema__ = subgraph_status_schema
    __field_names__ = ('lending_type', 'risk_type', 'minted_tokens', 'total_deposit_balance_usd', 'cumulative_deposit_usd', 'total_borrow_balance_usd', 'cumulative_borrow_usd', 'cumulative_liquidate_usd', 'minted_token_supplies', 'markets')
    lending_type = sgqlc.types.Field(LendingType, graphql_name='lendingType')
    risk_type = sgqlc.types.Field(RiskType, graphql_name='riskType')
    minted_tokens = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Token)), graphql_name='mintedTokens', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Token_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Token_filter, graphql_name='where', default=None)),
))
    )
    total_deposit_balance_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalDepositBalanceUSD')
    cumulative_deposit_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeDepositUSD')
    total_borrow_balance_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalBorrowBalanceUSD')
    cumulative_borrow_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeBorrowUSD')
    cumulative_liquidate_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeLiquidateUSD')
    minted_token_supplies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='mintedTokenSupplies')
    markets = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Market))), graphql_name='markets', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Market_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Market_filter, graphql_name='where', default=None)),
))
    )


class Liquidate(sgqlc.types.Type, Event):
    __schema__ = subgraph_status_schema
    __field_names__ = ('market', 'asset', 'amount', 'amount_usd', 'profit_usd')
    market = sgqlc.types.Field(sgqlc.types.non_null(Market), graphql_name='market')
    asset = sgqlc.types.Field(sgqlc.types.non_null(Token), graphql_name='asset')
    amount = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='amount')
    amount_usd = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD')
    profit_usd = sgqlc.types.Field(BigDecimal, graphql_name='profitUSD')


class Repay(sgqlc.types.Type, Event):
    __schema__ = subgraph_status_schema
    __field_names__ = ('market', 'asset', 'amount', 'amount_usd')
    market = sgqlc.types.Field(sgqlc.types.non_null(Market), graphql_name='market')
    asset = sgqlc.types.Field(sgqlc.types.non_null(Token), graphql_name='asset')
    amount = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='amount')
    amount_usd = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD')


class Withdraw(sgqlc.types.Type, Event):
    __schema__ = subgraph_status_schema
    __field_names__ = ('market', 'asset', 'amount', 'amount_usd')
    market = sgqlc.types.Field(sgqlc.types.non_null(Market), graphql_name='market')
    asset = sgqlc.types.Field(sgqlc.types.non_null(Token), graphql_name='asset')
    amount = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='amount')
    amount_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='amountUSD')



########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
subgraph_status_schema.query_type = Query
subgraph_status_schema.mutation_type = None
subgraph_status_schema.subscription_type = Subscription

