import xml.etree.ElementTree as etree

XML_PATH = "../data/XML_2020_07_07/{filename}.xml"


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
        alim = etree.parse(file_path)
        self._ALIM = alim

    def _load_alim_grp(self):
        file_path = XML_PATH.format(filename = "alim_grp")
        alim_grp = etree.parse(file_path)
        self._ALIM_GRP = alim_grp

    def _load_compo(self):
        file_path = XML_PATH.format(filename = "compo")
        compo = etree.parse(file_path)
        self._COMPO = compo

    def _load_const(self):
        file_path = XML_PATH.format(filename = "const")
        const = etree.parse(file_path)
        self._CONST = const

    def _load_sources(self):
        file_path = XML_PATH.format(filename = "sources")
        sources = etree.parse(file_path)
        self._SOURCES = sources