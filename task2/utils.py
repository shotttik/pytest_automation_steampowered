
from collections import OrderedDict, namedtuple
import json
import os
import re
from datetime import datetime
RESOURCES_PATH = os.getcwd() + "/Resources/"


# this two functions isn't mine, I found it. I think those functions will help in the future:)
def create_namedtuple_from_dict(obj):
    """converts given list or dict to named tuples, generic alternative to dataclass"""
    if isinstance(obj, dict):
        fields = sorted(obj.keys())
        namedtuple_type = namedtuple(
            typename='TestData',
            field_names=fields,
            rename=True,
        )
        field_value_pairs = OrderedDict(
            (str(field), create_namedtuple_from_dict(obj[field]))
            for field in fields
        )
        try:
            return namedtuple_type(**field_value_pairs)
        except TypeError:
            # Cannot create namedtuple instance so fallback to dict (invalid attribute names)
            return dict(**field_value_pairs)
    elif isinstance(obj, (list, set, tuple, frozenset)):
        return [create_namedtuple_from_dict(item) for item in obj]
    else:
        return obj


def inject_test_data(file):
    """
        Read the content of the JSON file and convert it to a named tuple,
        can be used for injecting test data set to tests, helps in separating test data from the tests
    """
    file = RESOURCES_PATH + file
    with open(file) as f:
        raw_data = json.load(f)
    return create_namedtuple_from_dict(raw_data)


def clean_stats_number(text):
    return int(re.sub("[^0-9]", "", text))


def get_datetime_object(dt: str):
    # string to datetime object , for this example '1 Aug, 2022'
    try:
        dt_obj = datetime.strptime(dt, '%d %b, %Y')
    except:
        dt_obj = None
    return dt_obj


def clean_text(text):
    return re.sub(r"[\n\t]*", "", text)
