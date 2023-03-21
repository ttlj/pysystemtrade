from sysdata.production.historic_positions_TO_DEPRECATE import contractPositionData
from sysdata.mongodb.mongo_timed_storage_TO_DEPRECATE import mongoListOfEntriesData

POSITION_CONTRACT_COLLECTION = "futures_position_by_contract"


class mongoContractPositionData(contractPositionData, mongoListOfEntriesData):
    """
    Read and write data class to get positions by contract


    """

    @property
    def _collection_name(self):
        return POSITION_CONTRACT_COLLECTION

    @property
    def _data_name(self):
        return "mongoContractPositionData"