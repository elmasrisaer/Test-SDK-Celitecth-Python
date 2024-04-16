from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "data_limit_in_gb": "dataLimitInGB",
        "start_date": "startDate",
        "end_date": "endDate",
        "network_brand": "networkBrand",
        "start_time": "startTime",
        "end_time": "endTime",
    }
)
class CreatePurchaseRequest(BaseModel):
    """CreatePurchaseRequest

    :param destination: ISO representation of the package's destination
    :type destination: str
    :param data_limit_in_gb: Size of the package in GB. The available options are 1, 2, 3, 5, 8, 20GB
    :type data_limit_in_gb: float
    :param start_date: Start date of the package's validity in the format 'yyyy-MM-dd'. This date can be set to the current day or any day within the next 12 months.
    :type start_date: str
    :param end_date: End date of the package's validity in the format 'yyyy-MM-dd'. End date can be maximum 60 days after Start date.
    :type end_date: str
    :param email: Email address where the purchase confirmation email will be sent (including QR Code & activation steps), defaults to None
    :type email: str, optional
    :param network_brand: Customize the network brand of the issued eSIM. This parameter is accessible to platforms with Diamond tier and requires an alphanumeric string of up to 15 characters, defaults to None
    :type network_brand: str, optional
    :param start_time: Epoch value representing the start time of the package's validity. This timestamp can be set to the current time or any time within the next 12 months., defaults to None
    :type start_time: float, optional
    :param end_time: Epoch value representing the end time of the package's validity. End time can be maximum 60 days after Start time., defaults to None
    :type end_time: float, optional
    """

    def __init__(
        self,
        destination: str,
        data_limit_in_gb: float,
        start_date: str,
        end_date: str,
        email: str = None,
        network_brand: str = None,
        start_time: float = None,
        end_time: float = None,
    ):
        self.destination = destination
        self.data_limit_in_gb = data_limit_in_gb
        self.start_date = start_date
        self.end_date = end_date
        self.email = email
        self.network_brand = network_brand
        self.start_time = start_time
        self.end_time = end_time
