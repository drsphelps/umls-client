from .base_dataclass import BaseDataClass

class Relation(BaseDataClass):
    def __init__(
        self,
        ui = None,
        suppressible = None,
        source_ui = None,
        obsolete = None,
        source_originated = None,
        root_source = None,
        group_id = None,        
        attribute_count = None,
        related_from_id = None,
        related_from_id_name = None,
        relation_label = None,
        additional_relation_label = None,
        related_id = None,
        related_id_name = None,
    ):
        self.ui = ui
        self.suppressible = suppressible
        self.source_ui = source_ui
        self.obsolete = obsolete
        self.source_originated = source_originated
        self.root_source = root_source
        self.group_id = group_id
        self.attribute_count = attribute_count
        self.related_from_id = related_from_id
        self.related_from_id_name = related_from_id_name
        self.relation_label = relation_label
        self.additional_relation_label = additional_relation_label
        self.related_id = related_id
        self.related_id_name = related_id_name

    def relation_as_string(self):
        relation_map = {
            'inverse_isa': 'is not a',
            'member_of': 'is a type of',
            'has_finding_site': 'can be found in the'
        }
        if self.additional_relation_label in relation_map:
            return f'{self.related_from_id_name} {relation_map[self.additional_relation_label]} {self.related_id_name}'.lower()
        return ''

    def initialise(self):
        super().initialise()
        self.related_from_id = self.related_from_id.split('/')[-1] if self.related_from_id is not None else None
        self.related_id = self.related_id.split('/')[-1] if self.related_id is not None else None

