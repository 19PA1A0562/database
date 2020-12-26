import pytest
from webbot.db.storage import JSONStorage
doc = {"student":{"name":"ram"}}
def test_json(tempdir):
    storage =JSONStorage(tempdir)
    print(storage)
    storage.write(doc)
    assert storage.read() == doc
    storage.close()
