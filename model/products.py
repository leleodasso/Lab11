from dataclasses import dataclass

import networkx as nx


@dataclass
class Product:
    Product_number:int
    Product_line:str
    Product_type:str
    Product:str
    Product_brand:str
    Product_color:str
    Unit_cost:float
    Unit_price:float

    def __eq__(self, other):
        return self.Product_number == other.Product_number

    def __hash__(self):
        return hash(self.Product_number)