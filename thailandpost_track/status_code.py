"""
A libraly that provides a python interface to Thailand Post API
"""


class StatusCode:
    ALL = 'all'
    PRELOAD = '101'
    ACCEPTED_BY_AGENT = '102'
    COLLECTION = '103'
    IN_TRANSIT = '201'
    PERFORM_CUSTOMS_CLEARANCE = '202'
    RETURN_TO_SENDER = '203'
    ARRIVAL_AT_OUTWARD_OFFICE = '204'
    ARRIVAL_AT_INWARD_OFFICE = '205'
    ARRIVAL_AT_POST_OFFICE = '206'
    PREPARE_TRANSIT = '207'
    ITEM_OUT_FOR_PHYSICAL_DELIVERY = '301'
    ITEM_ARRIVAL_AT_COLLECTION_POINT = '302'
    UNSUCCESSFUL = '401'
    FINAL_DELIVERY = '501'
