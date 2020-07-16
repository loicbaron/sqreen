import pytest
from marshmallow import ValidationError
from project.config.database import must_not_be_blank

def test_verify_request_signature_no_header(client, app):
  with pytest.raises(ValidationError) as excinfo:
    must_not_be_blank(None)
    assert "Data not provided." in str(excinfo.value)
