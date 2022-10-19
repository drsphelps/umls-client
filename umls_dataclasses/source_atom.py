from .base_dataclass import BaseDataClass

class SourceAtom(BaseDataClass):
    def __init__(
        self,
        client,
        class_type = None,
        ui = None,
        name = None,
        source_concept = None,
        concept = None,
        obsolete = None,
        suppressible = None,
        root_source = None,
        term_type = None,
        code = None,
        language = None,
        content_view_memberships = None,
    ):
        self.client = client
        self.class_type = class_type,
        self.ui = ui,
        self.name = name,
        self.source_concept = source_concept,
        self.concept = concept,
        self.obsolete = obsolete,
        self.suppressible = suppressible,
        self.root_source = root_source,
        self.term_type = term_type,
        self.code = code,
        self.language = language,
        self.content_view_memberships = content_view_memberships

        self.concept_obj = None

    def initialise(self):
        super().initialise()
        self.concept = self.concept.split('/')[-1] if self.concept is not None else None

    def get_concept(self):
        if self.concept_obj is not None:
            return self.concept_obj
        concept_obj = self.client.get_umls_concept(self.concept)
        self.concept_obj = concept_obj
        return concept_obj
