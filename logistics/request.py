from logistics.exception import InvalidRequestError, UnknownStorageError


class Request:
    def __init__(self, request_str, storages):
        res_request = request_str.lower().split(" ")
        if len(res_request) != 7 or not res_request[1].isdigit():
            raise InvalidRequestError

        self.amount = int(res_request[1])
        self.product = str(res_request[2])
        self.departure = str(res_request[4])
        self.destination = str(res_request[6])

        if self.departure not in storages or self.destination not in storages:
            raise UnknownStorageError
