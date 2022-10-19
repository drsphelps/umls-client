from client import UMLSClient
client = UMLSClient(api_key='5bfdac2d-6406-43f1-8d0c-a8101a0305e4')

sac = client.get_source_atom_cluster('128187005', 'SNOMEDCT_US')
print(f'CONCEPT: {sac.name}, {sac.ui}')

atoms = sac.get_atoms()
for atom in atoms:
    print(f'ATOM: {atom.name}, {atom.ui}')
    concept = atom.get_concept()

relations = sac.get_relations()
for rel in relations:
    print(f'RELATION: {rel.related_from_id} -> {rel.related_id}, {rel.additional_relation_label}: {rel.relation_as_string()}')

ancestors = sac.get_ancestors()
for anc in ancestors:
    print(f'ANCESTOR: {anc.name}')

descendants = sac.get_descendants()
for des in descendants:
    print(f'DESCENDANT: {des.name}')

parents = sac.get_parents()
for par in parents:
    print(f'PARENT: {par.name}')

children = sac.get_children()
for chi in children:
    print(f'CHILDREN: {chi.name}')