import json
import os

from cerberus import Validator


def validation(payload: dict):
    """
    validate payload against a defined schema
    :param payload: payload to be validated
    :return: None
    """
    with open(os.path.abspath("contact_us_schema.json")) as f:
        schema = json.loads(f.read())

    validator = Validator()
    validator.validate(payload, schema)

    if validator.errors:
        exit(f"Validation failed due to following errors: {validator.errors}")
    else:
        print("Please proceed for further activity")

payload = {
    "FirstName": "foo",
    "LastName": "bar",
    "Email": "foo@bar.com",
    "Message": "This is the test message"

}

validation(payload)