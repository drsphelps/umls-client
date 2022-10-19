import requests
from umls_dataclasses.relation import Relation
from umls_dataclasses.source_atom import SourceAtom
from umls_dataclasses.umls_concept import UMLSConcept

from umls_dataclasses.source_atom_cluster import SourceAtomCluster

class UMLSClient():
    def __init__(self, api_key):
        self.base = 'https://uts-ws.nlm.nih.gov/rest'
        self.api_key = api_key

    def _get(self, path, query_params=None, header_params=None):
        query_params = {} if query_params is None else query_params
        header_params = {} if header_params is None else header_params
        query_params['apiKey'] = self.api_key
        response = requests.get(f'{self.base}{path}', params=query_params, headers=header_params)
        return response.json()

    def get_umls_concept(self, cui, version='current'):
        response = self._get(f'/content/{version}/CUI/{cui}')
        response_obj = response['result']
        return UMLSConcept._load(self, response_obj)

    def get_source_atom_cluster(self, ui, source, version='current'):
        response = self._get(f'/content/{version}/source/{source}/{ui}')
        response_obj = response['result']
        return SourceAtomCluster._load(self, response_obj)

    def get_atoms_from_cluster(self, ui, source, version='current'):
        response = self._get(f'/content/{version}/source/{source}/{ui}/atoms')
        response_objs = response['result']
        return [SourceAtom._load(self, response_obj) for response_obj in response_objs]

    def get_tree_from_cluster(self, ui, source, rel_type='ancestors', version='current'):
        response = self._get(f'/content/{version}/source/{source}/{ui}/{rel_type}')
        response_objs = response['result']
        return [SourceAtomCluster._load(self, response_obj) for response_obj in response_objs]

    def get_atom_relations(self, ui, source, version='current'):
        response = self._get(f'/content/{version}/source/{source}/{ui}/relations')
        response_objs = response['result']
        return [Relation._load(self, response_obj) for response_obj in response_objs]
