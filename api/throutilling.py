from rest_framework.throttling import UserRateThrottle

class JackRateThrouting(UserRateThrottle):
    scope='jack'