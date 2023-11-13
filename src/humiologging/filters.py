import logging
from .utils import find_my_local_ip, find_my_public_ip


class NetworkContextFilter(logging.Filter):
    public_ip = find_my_public_ip()
    local_ip = find_my_local_ip()

    def filter(self, record):
        record.public_ip = self.public_ip
        record.local_ip = self.local_ip
        return True
