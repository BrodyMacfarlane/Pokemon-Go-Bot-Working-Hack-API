# Credits to Tejado, Milaly, and all the other wonderful developers who worked tirelessly on this project

import logging

class Auth:

    def __init__(self):
        self.log = logging.getLogger(__name__)
        
        self._auth_provider = None
        
        self._login = False
        self._auth_token = None
        
        self._ticket_expire = None
        self._ticket_start = None
        self._ticket_end = None
    
    def get_name(self):
        return self._auth_provider
    
    def is_login(self):
        return self._login
        
    def get_token(self):
        return self._auth_token
        
    def has_ticket(self):
        if self._ticket_expire and self._ticket_start and self._ticket_end:
            return True
        else:
            return False
       
    def set_ticket(self, params):
        self._ticket_expire, self._ticket_start, self._ticket_end = params
    
    def get_ticket(self):
        if self.has_ticket():
            return (self._ticket_expire, self._ticket_start, self._ticket_end)
        else:
            return False