import xml.etree.ElementTree as etree
import os

XML_PATH = os.path.dirname(__file__) + "/data/XML_2020_07_07/{filename}.xml"

class Aliment:
    def __init__(self, name, group, composition):
        self.name = name
        self.group = group
        self.composition = composition

class Group:
    def __init__(self, group, subgroup, subsubgroup):
        self.group = group
        self.subgroup = subgroup
        self.subsubgroup = subsubgroup

class Composition:
    def __init__(self, element, content, trust_code, source, min, max):
        self.element = element
        self.content = content
        self.trust_code = trust_code
        self.source = source
        self.min = min
        self.max = max

class CliqualAPI:
    #------------#
    # ATTRIBUTES #
    #------------#

    _ALIM = None
    _ALIM_GRP = None
    _COMPO = None
    _CONST = None
    _SOURCES = None


    #--------------#
    # INITIALISERS #
    #--------------#

    def __init__(self,
                 load_everything = True,
                 load_alim = False,
                 load_alim_grp = False,
                 load_compo = False,
                 load_const = False,
                 load_sources = False
                 ):
        if(load_everything):
            self._load_all_xml()
        else:
            if(load_alim) : 
                self._load_alim()
            if(load_alim_grp):
                self._load_alim_grp()
            if(load_compo):
                self._load_compo()
            if(load_const):
                self._load_const()
            if(load_sources):
                self._load_sources()

    #--------------#
    # DATA LOADERS #
    #--------------#

    def _load_all_xml(self):
        self._load_alim()
        self._load_alim_grp()
        self._load_compo()
        self._load_const()
        self._load_sources()

    def _load_alim(self):
        file_path = XML_PATH.format(filename = "alim")
        print("...loading xml at " + file_path)
        alim = etree.parse(file_path)
        self._ALIM = alim

    def _load_alim_grp(self):
        file_path = XML_PATH.format(filename = "alim_grp")
        print("...loading xml at " + file_path)
        alim_grp = etree.parse(file_path)
        self._ALIM_GRP = alim_grp

    def _load_compo(self):
        file_path = XML_PATH.format(filename = "compo")
        print("...loading xml at " + file_path)
        compo = etree.parse(file_path)
        self._COMPO = compo

    def _load_const(self):
        file_path = XML_PATH.format(filename = "const")
        print("...loading xml at " + file_path)
        const = etree.parse(file_path)
        self._CONST = const

    def _load_sources(self):
        file_path = XML_PATH.format(filename = "sources")
        print("...loading xml at " + file_path)
        sources = etree.parse(file_path)
        self._SOURCES = sources

    #------#
    # ALIM #
    #------#
    def get_aliment(self, alim_code):
        print(("Querying aliment with code '{code}'").format(code=alim_code))
        prequery = './/ALIM[alim_code="{code}"]'
        query = prequery.format(code = self.format_code(alim_code))
        print(query)
        alim = self._ALIM.find(query)

        name = alim.find('alim_nom_fr').text
        group_code = alim.find('alim_grp_code').text
        subgroup_code = alim.find('alim_ssgrp_code').text
        subsbugroup_code = alim.find('alim_ssssgrp_code').text
        group = self.get_group(group_code, subgroup_code, subsbugroup_code)
        composition = self.get_compo(alim_code)        

        result = Aliment(name, group, composition)
        return result




    #----------#
    # ALIM_GRP #
    #----------#

    # Return a Group from given code
    def get_group(self, group_code, subgroup_code = 0, subsubgroup_code = 0):   
        print(("Querying group with codes '{code1}/{code2}/{code3}'").format(code1=group_code, code2=subgroup_code, code3=subsubgroup_code))
        prequery = './/ALIM_GRP[alim_grp_code="{grp_code}"][alim_ssgrp_code="{subgrp_code}"][alim_ssssgrp_code="{subsubgrp_code}"]'
        query = prequery.format(grp_code = self.format_code(group_code), subgrp_code = self.format_code(subgroup_code), subsubgrp_code = self.format_code(subsubgroup_code))
        print(query)
        grp = self._ALIM_GRP.find(query)

        group = grp.find('alim_grp_nom_fr').text
        subgroup = grp.find('alim_ssgrp_nom_fr').text
        subsubgroup = grp.find('alim_ssssgrp_nom_fr').text

        result = Group(group, subgroup, subsubgroup)
        return result
    
    #-------#
    # COMPO #
    #-------#

    # Return a dict of composition given from alim_code
    def get_compo(self, alim_code):
        print(("Querying composition of aliment '{code}'").format(code=alim_code))
        prequery = './/COMPO[alim_code="{code}"]'
        query = prequery.format(code=self.format_code(alim_code))
        components = self._COMPO.findall(query)

        result = {}
        for component in components:
            const_code = component.find('const_code').text
            element = self.get_const(const_code)

            content_text = component.find('teneur').text
            content = 0.0 if content_text==' - ' else float(content_text)

            source_code = component.find('source_code').text
            source = self.get_source(source_code)
            trust_code = component.find('code_confiance').text
            
            min = component.find('min').text
            max = component.find('max').text

            comp = Composition(element, content, trust_code, source, min, max)
            result[const_code] = comp
            print(("Added {component} to alim composition").format(component=element))
        return result
    
    # Return the composition with given code for given alim_code
    def get_specific_compo(self, alim_code, compo_code):
        print(("Querying composition {compo_code} of aliment '{alim_code}'").format(compo_code=compo_code, alim_code=alim_code))
        prequery = './/COMPO[alim_code="{alim_code}"][const_code="{const_code}"]'
        query = prequery.format(alim_code=self.format_code(alim_code), const_code=self.format_code(compo_code))
        component = self._COMPO.find(query)

        const_code = component.find('const_code').text
        element = self.get_const(const_code)
        
        content_text = component.find('teneur').text
        content = 0.0 if content_text==' - ' else float(content_text)

        source_code = component.find('source_code').text
        source = self.get_source(source_code)
        trust_code = component.find('code_confiance').text
        
        min = component.find('min').text
        max = component.find('max').text

        comp = Composition(element, content, trust_code, source, min, max)
        return comp


    #-------#
    # CONST #
    #-------#

    # Return a string for the const (element, energy...) with code
    def get_const(self, const_code):
        if const_code is None:
            return None
        print(("Querying consts for const '{code}'").format(code=const_code))
        prequery = './/CONST[const_code="{code}"]/const_nom_fr'
        query = prequery.format(code=self.format_code(const_code))
        const = self._CONST.find(query)
        result = None if const is None else const.text
        return result

    #---------#
    # SOURCES #
    #---------#

    # Return a string for the source (paper, study...) with code
    def get_source(self, source_code):
        if source_code is None:
            return None
        print(("Querying sources for source '{code}'").format(code=source_code))
        prequery = './/SOURCES[source_code="{code}"]/ref_citation'
        query = prequery.format(code=self.format_code(source_code))
        source = self._SOURCES.find(query)
        result = None if source is None else source.text
        return result

    #--------------#
    # MISCELLANOUS #
    #--------------#

    # Format an integer or str code to be used within queries
    def format_code(self, code):
        if code is None:
            return None
        integer_code = int(code)
        str_code = str(integer_code)
        result = " " + str_code + " "
        return result