class ReqIFDataTypeDefinitionString:
    def __init__(self, identifier: str):
        self.identifier = identifier


class ReqIFDataTypeDefinitionEnumeration:
    def __init__(self, identifier: str, values_map):
        self.identifier = identifier
        self.values_map = values_map
