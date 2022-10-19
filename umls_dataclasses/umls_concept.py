from json import load
from .base_dataclass import BaseDataClass

class UMLSConcept(BaseDataClass):
    def __init__(
        self,
        client,
        ui=None,
        name=None,
        class_type=None,
        suppressible=None,
        status=None,
        semantic_types=None,
        atom_count=None,
        cv_member_count=None,
        attribute_count=None,
        relation_count=None,
    ):
        self.client = client
        self.ui = ui
        self.name = name
        self.class_type = class_type
        self.suppressible = suppressible
        self.status = status
        self.semantic_types = semantic_types
        self.atom_count = atom_count
        self.cv_member_count = cv_member_count
        self.attribute_count = attribute_count
        self.relation_count = relation_count
