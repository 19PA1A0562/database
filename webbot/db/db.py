from .table import Table
from .storage import Storage
class DB:
    def __int__(self, storage):
        """initializing a new database with appropriate """
        self._storage = storage
        self.tables={}
    
    def table(self, name):
        """ 
        Get access to a specific named table. 
        Returns a table if it exists.
        create a new table if it dose not exists"""
        if name in self._tables:
            return _tables[name]

        table = Table(name, self._storage)
    def drop(self,name):
        if name in self._tables:
            _tables[name].truncate()
            del _tables[name]
        else:
            raise ValueError(f"no such table {name}")
    def clean(self):
        self._storage.write({})
        self._tables.clear()