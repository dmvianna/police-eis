import logging
import yaml
import datetime

from .. import setup_environment
from . import abstract

log = logging.getLogger(__name__)

try:
    _, tables = setup_environment.get_database()
except:
    pass

time_format = "%Y-%m-%d %X"


### Basic Dispatch Features

class DummyFeature(abstract.DispatchFeature):
    def __init__(self, **kwargs):
        abstract.DispatchFeature.__init__(self, **kwargs)
        self.description = ("Dummy feature for testing 2016 schema")
        self.query = ("SELECT "
                      "     dispatch_id, "
                      "     COUNT(event_type_code) AS feature_column "
                      "FROM staging.events_hub "
                      "WHERE event_type_code = 4 "
                      "GROUP BY dispatch_id")
        self.type_of_imputation = "mean"


class RandomFeature(abstract.DispatchFeature):
    def __init__(self, **kwargs):
        abstract.DispatchFeature.__init__(self, **kwargs)
        self.description = ("Random feature for testing")
        self.query = (  "SELECT "
                        "   dispatch_id, "
                        "   random() AS feature_column "
                        "FROM staging.events_hub "
                        "GROUP BY dispatch_id")
        self.type_of_imputation = "mean"
