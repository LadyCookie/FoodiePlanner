import xml.etree.ElementTree as etree
import os

XML_PATH = os.path.dirname(__file__) + "/data/XML_2020_07_07/{filename}.xml"


class CliqualAPI:
    #------------#
    # ATTRIBUTES #
    #------------#

    _ALIM = None
    _ALIM_GRP = None
    _COMPO = None
    _CONST = None
    _SOURCES = None


    #-------------#
    # INITIALISER #
    #-------------#

    def __init__(self):
        self._load_all_xml()
        print("...XML loaded.")

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


    #----------#
    # ALIM_GRP #
    #----------#

    #-------#
    # COMPO #
    #-------#

    #-------#
    # CONST #
    #-------#

    # Return a string for the const (element, energy...) with code
    # code should be an integer or a string without spaces
    def get_const(self, const_code):
        print(("Querying consts for const {code}").format(code=const_code))
        prequery = './/CONST[const_code=" {code} "]/const_nom_fr'
        query = prequery.format(code=const_code)
        const = self._CONST.find(query)
        result = None if const is None else const.text
        print(("Found : {result}").format(result=result))
        return result

    #---------#
    # SOURCES #
    #---------#

    # Return a string for the source (paper, study...) with code
    # code should be an integer or a string without spaces
    def get_source(self, source_code):
        print(("Querying sources for source {code}").format(code=source_code))
        prequery = './/SOURCES[source_code=" {code} "]/ref_citation'
        query = prequery.format(code=source_code)
        source = self._SOURCES.find(query)
        result = None if source is None else source.text
        print(("Found : {result}").format(result=result))
        return result