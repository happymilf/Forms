from tinydb import TinyDB, Query
from tinydb.table import Table


import enum


class FieldType(enum.Enum):
    EMAIL : str = "email"
    PHONE : str = "phone"
    DATE : str = "date"
    DATETIME : str = "datetime"
    TEXT : str = "text"


class Form:
    def __init__(self, name : str) -> None:
        self.fields : dict = {}
        self.name : str = name

    def set_field(self, field_name : str, field_type : FieldType):
        self.fields[field_name] = field_type.value

    def compile(self) -> dict:
        return { "name" : self.name} | self.fields

    def remove(self, field_name : str):
        if field_name in self.fields.keys():
            self.fields.pop(field_name)
        
    def change_name(self, new_name : str):
        self.name = new_name



class DataBase:
    def __init__(self, db_name : str = "database", tables : list[str] = ["default_table"]):
        self.db_name : str = db_name
        self.db_conn : TinyDB = TinyDB(f'{db_name}.json')
        self.tables : dict[str, Table] = {}
        for i in tables:
            self.tables[i] = self.db_conn.table(i)

    def change_name(self, new_name : str):
        self.db_name = new_name

    def new_table(self, table_name : str):
        if table_name not in self.db_conn.tables():
            self.tables.append(self.db_conn.table(table_name))

    def insert(self, data : Form, table_name : str = "default_table"):
        if table_name in self.tables.keys():
            self.tables[table_name].insert(data.compile())
        

    def search(self, data : dict, table_name : str = "default_table") -> str:
        for i in self.tables[table_name].all():
            if len(i)-1 == len(data):
                tmp : dict = i.copy()
                tmp.pop("name")
                if tmp == data:
                    return i["name"]
        return ""       
        
    def id_search(self, form_id : str, table_name : str = "default_table") -> dict[str, str]:
        if len(self.tables[table_name].all()) > int(form_id):
            return self.tables[table_name].all()[form_id]
        return {}
    def name_search(self, form_name : str, table_name : str = "default_table") -> dict[str, str]:
            for i in self.tables[table_name].all():
                if i["name"] == form_name:
                    return i
            return {}



