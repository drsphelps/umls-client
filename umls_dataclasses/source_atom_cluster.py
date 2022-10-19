from .base_dataclass import BaseDataClass

class SourceAtomCluster(BaseDataClass):
    def __init__(
        self,
        client,
        class_type = None,
        ui = None,
        name = None,
        suppressible = None,
        obsolete = None,
        root_source = None,
        atom_count = None,
        c_v_member_count = None,
        subset_memberships = None,
        content_view_memberships = None
    ):
        self.client = client
        self.class_type = class_type,
        self.ui = ui,
        self.name = name,
        self.suppressible = suppressible,
        self.obsolete = obsolete,
        self.root_source = root_source,
        self.atom_count = atom_count,
        self.c_v_member_count = c_v_member_count,
        self.subset_memberships = subset_memberships,
        self.content_view_memberships = content_view_memberships

        self.relation_lst = None
        self.ancestor_lst = None
        self.descendant_lst = None
        self.child_lst = None
        self.parent_lst = None

    def get_atoms(self, count=1):
        if self.atom_count == 0:
            return []
        return self.client.get_atoms_from_cluster(self.ui, self.root_source)[:count]

    def get_relations(self):
        if self.relation_lst is not None:
            return self.relation_lst
        relation_lst = self.client.get_atom_relations(self.ui, self.root_source)
        self.relation_lst = relation_lst
        return relation_lst

    def get_ancestors(self):
        if self.ancestor_lst is not None:
            return self.ancestor_lst
        ancestor_lst = self.client.get_tree_from_cluster(self.ui, self.root_source, rel_type='ancestors')
        self.ancestor_lst = ancestor_lst
        return ancestor_lst
    
    def get_descendants(self):
        if self.descendant_lst is not None:
            return self.descendant_lst
        descendant_lst = self.client.get_tree_from_cluster(self.ui, self.root_source, rel_type='descendants')
        self.descendant_lst = descendant_lst
        return descendant_lst

    def get_parents(self):
        if self.parent_lst is not None:
            return self.parent_lst
        parent_lst = self.client.get_tree_from_cluster(self.ui, self.root_source, rel_type='parents')
        self.parent_lst = parent_lst
        return parent_lst

    def get_children(self):
        if self.child_lst is not None:
            return self.child_lst
        child_lst = self.client.get_tree_from_cluster(self.ui, self.root_source, rel_type='children')
        self.child_lst = child_lst
        return child_lst