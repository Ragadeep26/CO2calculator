
class Project():
    def __init__(self, project_variant='', structures=[]):
        self.project_variant = project_variant      # string of project variants
        self.structures = structures                # list of structures that belong to project


    def add_structure(self, structure):
        """ Adds a structure to project"""
        self.structures.append(structure)


    def remove_structure(self, structure_to_remove):
        """ Removes a structure from project"""
        for i, structure in enumerate(self.structures):
            if structure.id == structure_to_remove.id:
                self.structures.pop(i)

    def replace_structure(self, structure_to_replace):
        """replaces a structure from project"""
        for i, structure in enumerate(self.structures):
            if structure.id == structure_to_replace.id:
                self.structures[i] = structure_to_replace
 