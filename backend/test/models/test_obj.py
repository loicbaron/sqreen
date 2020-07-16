import json
from project.models.obj import Obj

def test_obj_constructor():
  obj = Obj(1, 'a')
  assert isinstance(obj, Obj)
  assert obj.id == 1
  assert obj.attribute == 'a'

def test_obj_fromBlob():
  obj = Obj.fromBlob({'id': 1, 'attribute': 'a'})
  assert isinstance(obj, Obj)
  assert obj.id == 1
  assert obj.attribute == 'a'

def test_obj_fromBlob_id_none():
  obj = Obj.fromBlob({'attribute': 'a'})
  assert isinstance(obj, Obj)
  assert obj.id == None
  assert obj.attribute == 'a'

def test_obj_toJSON():
  json_obj = Obj(1, 'a').toJSON()
  assert isinstance(json_obj, str)
  assert json.loads(json_obj)['id'] == 1
  assert json.loads(json_obj)['attribute'] == 'a'

def test_obj_str():
  obj = Obj(1, 'a')
  assert "{}".format(obj) == "id:{}, attribute:{}".format(obj.id, obj.attribute)

def test_obj_repr():
  obj = Obj(1, 'a')
  assert repr(obj) == "Object(id: {}, attribute:{})".format(obj.id, obj.attribute)