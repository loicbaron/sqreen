import pytest
from werkzeug.exceptions import Forbidden
from project.config.security import check_signature, verify_request_signature

def test_check_signature_ko():
  req_sig = 'a'
  req_body = b'b'
  secret_key = b'c'
  assert check_signature(secret_key, req_sig, req_body) == False

def test_check_signature_ok():
  req_sig = '9d101d2bf630748679226b767d2031634c520390ff0e926afc09bc65a05bfdb2'
  req_body = b'4567'
  secret_key = b'1234'
  assert check_signature(secret_key, req_sig, req_body) == True

def test_verify_request_signature_ok(client, app):
  with app.test_request_context(data='4567', environ_base={'HTTP_X_SQREEN_INTEGRITY': '9d101d2bf630748679226b767d2031634c520390ff0e926afc09bc65a05bfdb2'}):
    @verify_request_signature
    def process_request():
      return True
    assert process_request() == True

def test_verify_request_signature_no_header(client, app):
  with pytest.raises(Forbidden) as excinfo:
    with app.test_request_context(data='a'):
        @verify_request_signature
        def process_request():
          return True
        process_request()

def test_verify_request_signature_not_recognized(client, app):
  with pytest.raises(Forbidden) as excinfo:
    with app.test_request_context(data='a', environ_base={'HTTP_X_SQREEN_INTEGRITY': 'b'}):
        @verify_request_signature
        def process_request():
          return True
        process_request()
