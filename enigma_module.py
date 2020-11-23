"""An implementation of the Enigma Machine in Python.

This is a toy project intending to implement the Enigma Machine as originally
designed by Arthur Scherbius.
Based on project: https://github.com/ZAdamMac/python-enigma

Modyfication by Adam Jurkiewicz adam(at)abixedukacja.eu - 2020

Apache 2.0 License
"""

default_rotors_catalog = {
    "IC": {
        "wiring": {
            "1": 4,
            "2": 13,
            "3": 20,
            "4": 23,
            "5": 19,
            "6": 9,
            "7": 12,
            "8": 18,
            "9": 21,
            "10": 25,
            "11": 17,
            "12": 14,
            "13": 11,
            "14": 6,
            "15": 5,
            "16": 10,
            "17": 3,
            "18": 1,
            "19": 26,
            "20": 2,
            "21": 16,
            "22": 7,
            "23": 24,
            "24": 15,
            "25": 8,
            "26": 22,
        },
        "notch": "Q",
    },
    "IIC": {
        "wiring": {
            "1": 8,
            "2": 17,
            "3": 26,
            "4": 7,
            "5": 16,
            "6": 10,
            "7": 20,
            "8": 13,
            "9": 15,
            "10": 2,
            "11": 12,
            "12": 14,
            "13": 3,
            "14": 9,
            "15": 6,
            "16": 4,
            "17": 25,
            "18": 1,
            "19": 23,
            "20": 22,
            "21": 5,
            "22": 21,
            "23": 19,
            "24": 18,
            "25": 11,
            "26": 24,
        },
        "notch": "E",
    },
    "IIIC": {
        "wiring": {
            "1": 21,
            "2": 17,
            "3": 14,
            "4": 20,
            "5": 12,
            "6": 19,
            "7": 26,
            "8": 6,
            "9": 13,
            "10": 18,
            "11": 5,
            "12": 8,
            "13": 4,
            "14": 16,
            "15": 24,
            "16": 11,
            "17": 9,
            "18": 2,
            "19": 22,
            "20": 25,
            "21": 7,
            "22": 10,
            "23": 3,
            "24": 23,
            "25": 15,
            "26": 1,
        },
        "notch": "V",
    },
    "IR": {
        "wiring": {
            "1": 10,
            "2": 7,
            "3": 4,
            "4": 17,
            "5": 15,
            "6": 24,
            "7": 21,
            "8": 19,
            "9": 3,
            "10": 1,
            "11": 13,
            "12": 9,
            "13": 6,
            "14": 18,
            "15": 22,
            "16": 20,
            "17": 16,
            "18": 14,
            "19": 5,
            "20": 23,
            "21": 11,
            "22": 2,
            "23": 12,
            "24": 26,
            "25": 25,
            "26": 8,
        },
        "notch": "Q",
    },
    "IIR": {
        "wiring": {
            "1": 14,
            "2": 20,
            "3": 26,
            "4": 16,
            "5": 19,
            "6": 6,
            "7": 2,
            "8": 15,
            "9": 11,
            "10": 13,
            "11": 23,
            "12": 18,
            "13": 3,
            "14": 10,
            "15": 4,
            "16": 9,
            "17": 22,
            "18": 12,
            "19": 1,
            "20": 5,
            "21": 25,
            "22": 21,
            "23": 24,
            "24": 8,
            "25": 7,
            "26": 17,
        },
        "notch": "E",
    },
    "IIIR": {
        "wiring": {
            "1": 10,
            "2": 22,
            "3": 9,
            "4": 21,
            "5": 2,
            "6": 8,
            "7": 20,
            "8": 3,
            "9": 4,
            "10": 25,
            "11": 1,
            "12": 11,
            "13": 5,
            "14": 17,
            "15": 26,
            "16": 16,
            "17": 15,
            "18": 19,
            "19": 7,
            "20": 24,
            "21": 14,
            "22": 18,
            "23": 13,
            "24": 23,
            "25": 6,
            "26": 12,
        },
        "notch": "V",
    },
    "UKW": {
        "wiring": {
            "1": 17,
            "2": 25,
            "3": 8,
            "4": 15,
            "5": 7,
            "6": 14,
            "7": 5,
            "8": 3,
            "9": 22,
            "10": 16,
            "11": 21,
            "12": 26,
            "13": 20,
            "14": 6,
            "15": 4,
            "16": 10,
            "17": 1,
            "18": 24,
            "19": 23,
            "20": 13,
            "21": 11,
            "22": 9,
            "23": 19,
            "24": 18,
            "25": 2,
            "26": 12,
        },
        "notch": "",
    },
    "I-K": {
        "wiring": {
            "1": 16,
            "2": 5,
            "3": 26,
            "4": 21,
            "5": 15,
            "6": 8,
            "7": 24,
            "8": 19,
            "9": 3,
            "10": 22,
            "11": 6,
            "12": 13,
            "13": 20,
            "14": 2,
            "15": 7,
            "16": 12,
            "17": 18,
            "18": 9,
            "19": 14,
            "20": 17,
            "21": 10,
            "22": 23,
            "23": 1,
            "24": 25,
            "25": 4,
            "26": 11,
        },
        "notch": "Q",
    },
    "II-K": {
        "wiring": {
            "1": 26,
            "2": 15,
            "3": 21,
            "4": 5,
            "5": 19,
            "6": 25,
            "7": 4,
            "8": 11,
            "9": 6,
            "10": 23,
            "11": 16,
            "12": 3,
            "13": 9,
            "14": 17,
            "15": 24,
            "16": 8,
            "17": 13,
            "18": 22,
            "19": 2,
            "20": 12,
            "21": 7,
            "22": 14,
            "23": 10,
            "24": 18,
            "25": 1,
            "26": 20,
        },
        "notch": "E",
    },
    "III-K": {
        "wiring": {
            "1": 5,
            "2": 8,
            "3": 18,
            "4": 22,
            "5": 24,
            "6": 7,
            "7": 1,
            "8": 15,
            "9": 2,
            "10": 17,
            "11": 21,
            "12": 19,
            "13": 9,
            "14": 13,
            "15": 26,
            "16": 6,
            "17": 12,
            "18": 25,
            "19": 14,
            "20": 23,
            "21": 11,
            "22": 20,
            "23": 16,
            "24": 4,
            "25": 10,
            "26": 3,
        },
        "notch": "V",
    },
    "UKW-K": {
        "wiring": {
            "1": 9,
            "2": 13,
            "3": 5,
            "4": 20,
            "5": 3,
            "6": 7,
            "7": 6,
            "8": 18,
            "9": 1,
            "10": 25,
            "11": 19,
            "12": 17,
            "13": 2,
            "14": 26,
            "15": 24,
            "16": 23,
            "17": 12,
            "18": 8,
            "19": 11,
            "20": 4,
            "21": 22,
            "22": 21,
            "23": 16,
            "24": 15,
            "25": 10,
            "26": 14,
        },
        "notch": "",
    },
    "I": {
        "wiring": {
            "1": 5,
            "2": 11,
            "3": 13,
            "4": 6,
            "5": 12,
            "6": 7,
            "7": 4,
            "8": 17,
            "9": 22,
            "10": 26,
            "11": 14,
            "12": 20,
            "13": 15,
            "14": 23,
            "15": 25,
            "16": 8,
            "17": 24,
            "18": 21,
            "19": 19,
            "20": 16,
            "21": 1,
            "22": 9,
            "23": 2,
            "24": 18,
            "25": 3,
            "26": 10,
        },
        "notch": "Q",
    },
    "II": {
        "wiring": {
            "1": 1,
            "2": 10,
            "3": 4,
            "4": 11,
            "5": 19,
            "6": 9,
            "7": 18,
            "8": 21,
            "9": 24,
            "10": 2,
            "11": 12,
            "12": 8,
            "13": 23,
            "14": 20,
            "15": 13,
            "16": 3,
            "17": 17,
            "18": 7,
            "19": 26,
            "20": 14,
            "21": 16,
            "22": 25,
            "23": 6,
            "24": 22,
            "25": 15,
            "26": 5,
        },
        "notch": "E",
    },
    "III": {
        "wiring": {
            "1": 2,
            "2": 4,
            "3": 6,
            "4": 8,
            "5": 10,
            "6": 12,
            "7": 3,
            "8": 16,
            "9": 18,
            "10": 20,
            "11": 24,
            "12": 22,
            "13": 26,
            "14": 14,
            "15": 25,
            "16": 5,
            "17": 9,
            "18": 23,
            "19": 7,
            "20": 1,
            "21": 11,
            "22": 13,
            "23": 21,
            "24": 19,
            "25": 17,
            "26": 15,
        },
        "notch": "V",
    },
    "IV": {
        "wiring": {
            "1": 5,
            "2": 19,
            "3": 15,
            "4": 22,
            "5": 16,
            "6": 26,
            "7": 10,
            "8": 1,
            "9": 25,
            "10": 17,
            "11": 21,
            "12": 9,
            "13": 18,
            "14": 8,
            "15": 24,
            "16": 12,
            "17": 14,
            "18": 6,
            "19": 20,
            "20": 7,
            "21": 11,
            "22": 4,
            "23": 3,
            "24": 13,
            "25": 23,
            "26": 2,
        },
        "notch": "J",
    },
    "V": {
        "wiring": {
            "1": 22,
            "2": 26,
            "3": 2,
            "4": 18,
            "5": 7,
            "6": 9,
            "7": 20,
            "8": 25,
            "9": 21,
            "10": 16,
            "11": 19,
            "12": 4,
            "13": 14,
            "14": 8,
            "15": 12,
            "16": 24,
            "17": 1,
            "18": 23,
            "19": 13,
            "20": 10,
            "21": 17,
            "22": 15,
            "23": 6,
            "24": 5,
            "25": 3,
            "26": 11,
        },
        "notch": "Z",
    },
    "VI": {
        "wiring": {
            "1": 10,
            "2": 16,
            "3": 7,
            "4": 22,
            "5": 15,
            "6": 21,
            "7": 13,
            "8": 6,
            "9": 25,
            "10": 17,
            "11": 2,
            "12": 5,
            "13": 14,
            "14": 8,
            "15": 26,
            "16": 18,
            "17": 4,
            "18": 11,
            "19": 1,
            "20": 19,
            "21": 24,
            "22": 12,
            "23": 9,
            "24": 3,
            "25": 20,
            "26": 23,
        },
        "notch": "ZM",
    },
    "VII": {
        "wiring": {
            "1": 14,
            "2": 26,
            "3": 10,
            "4": 8,
            "5": 7,
            "6": 18,
            "7": 3,
            "8": 24,
            "9": 13,
            "10": 25,
            "11": 19,
            "12": 23,
            "13": 2,
            "14": 15,
            "15": 21,
            "16": 6,
            "17": 1,
            "18": 9,
            "19": 22,
            "20": 12,
            "21": 16,
            "22": 5,
            "23": 11,
            "24": 17,
            "25": 4,
            "26": 20,
        },
        "notch": "ZM",
    },
    "VIII": {
        "wiring": {
            "1": 6,
            "2": 11,
            "3": 17,
            "4": 8,
            "5": 20,
            "6": 12,
            "7": 24,
            "8": 15,
            "9": 3,
            "10": 2,
            "11": 10,
            "12": 19,
            "13": 16,
            "14": 4,
            "15": 26,
            "16": 18,
            "17": 1,
            "18": 13,
            "19": 5,
            "20": 23,
            "21": 14,
            "22": 9,
            "23": 21,
            "24": 25,
            "25": 7,
            "26": 22,
        },
        "notch": "ZM",
    },
    "Beta": {
        "wiring": {
            "1": 12,
            "2": 5,
            "3": 25,
            "4": 10,
            "5": 22,
            "6": 3,
            "7": 14,
            "8": 9,
            "9": 24,
            "10": 23,
            "11": 16,
            "12": 2,
            "13": 17,
            "14": 13,
            "15": 4,
            "16": 18,
            "17": 20,
            "18": 1,
            "19": 11,
            "20": 26,
            "21": 7,
            "22": 6,
            "23": 21,
            "24": 8,
            "25": 15,
            "26": 19,
        },
        "notch": "",
        "static": True,
    },
    "Gamma": {
        "wiring": {
            "1": 6,
            "2": 19,
            "3": 15,
            "4": 11,
            "5": 1,
            "6": 14,
            "7": 21,
            "8": 5,
            "9": 18,
            "10": 8,
            "11": 13,
            "12": 2,
            "13": 20,
            "14": 9,
            "15": 25,
            "16": 3,
            "17": 23,
            "18": 12,
            "19": 17,
            "20": 16,
            "21": 26,
            "22": 24,
            "23": 22,
            "24": 7,
            "25": 10,
            "26": 4,
        },
        "notch": "",
        "static": True,
    },
    "Reflector A": {
        "wiring": {
            "1": 5,
            "2": 10,
            "3": 13,
            "4": 26,
            "5": 1,
            "6": 12,
            "7": 25,
            "8": 24,
            "9": 22,
            "10": 2,
            "11": 23,
            "12": 6,
            "13": 3,
            "14": 18,
            "15": 17,
            "16": 21,
            "17": 15,
            "18": 14,
            "19": 20,
            "20": 19,
            "21": 16,
            "22": 9,
            "23": 11,
            "24": 8,
            "25": 7,
            "26": 4,
        },
        "notch": "",
    },
    "Reflector B": {
        "wiring": {
            "1": 25,
            "2": 18,
            "3": 21,
            "4": 8,
            "5": 17,
            "6": 19,
            "7": 12,
            "8": 4,
            "9": 16,
            "10": 24,
            "11": 14,
            "12": 7,
            "13": 15,
            "14": 11,
            "15": 13,
            "16": 9,
            "17": 5,
            "18": 2,
            "19": 6,
            "20": 26,
            "21": 3,
            "22": 23,
            "23": 22,
            "24": 10,
            "25": 1,
            "26": 20,
        },
        "notch": "",
    },
    "Reflector C": {
        "wiring": {
            "1": 6,
            "2": 22,
            "3": 16,
            "4": 10,
            "5": 9,
            "6": 1,
            "7": 15,
            "8": 25,
            "9": 5,
            "10": 4,
            "11": 18,
            "12": 26,
            "13": 24,
            "14": 23,
            "15": 7,
            "16": 3,
            "17": 20,
            "18": 11,
            "19": 21,
            "20": 17,
            "21": 19,
            "22": 2,
            "23": 14,
            "24": 13,
            "25": 8,
            "26": 12,
        },
        "notch": "",
    },
    "Reflector B Thin": {
        "wiring": {
            "1": 5,
            "2": 14,
            "3": 11,
            "4": 17,
            "5": 1,
            "6": 21,
            "7": 25,
            "8": 23,
            "9": 10,
            "10": 9,
            "11": 3,
            "12": 15,
            "13": 16,
            "14": 2,
            "15": 12,
            "16": 13,
            "17": 4,
            "18": 24,
            "19": 26,
            "20": 22,
            "21": 6,
            "22": 20,
            "23": 8,
            "24": 18,
            "25": 7,
            "26": 19,
        },
        "notch": "",
    },
    "Reflector C Thin": {
        "wiring": {
            "1": 18,
            "2": 4,
            "3": 15,
            "4": 2,
            "5": 10,
            "6": 14,
            "7": 20,
            "8": 11,
            "9": 22,
            "10": 5,
            "11": 8,
            "12": 13,
            "13": 12,
            "14": 6,
            "15": 3,
            "16": 23,
            "17": 26,
            "18": 1,
            "19": 24,
            "20": 7,
            "21": 25,
            "22": 9,
            "23": 16,
            "24": 19,
            "25": 21,
            "26": 17,
        },
        "notch": "",
    },
}


class SteckerSettingsInvalid(Exception):
    """Raised if the stecker doesn't like its settings - either a duplicated
    letter was used or a non-letter character was used.
    """


class UndefinedStatorError(Exception):
    """Raised if the stator mode string is not a defined stator type"""


class RotorNotFound(Exception):
    """Raised if the rotor requested is not found in the catalogue"""


class Stecker(object):
    """A class implementation of the stecker. The stecker board was a set of
    junctions which could rewire both the lamps and keys for letters in a
    pairwise fashion. This formed a sort of double-substitution step. The
    stecker board eliminated an entire class of attacks against the machine.

    This stecker provides a method "steck" which performs the substitution.
    """

    def __init__(self, setting):
        """Accepts a string of space-seperated letter pairs denoting stecker
        settings, deduplicates them and grants the object its properties.
        """
        if setting is not None:
            stecker_pairs = setting.upper().split(" ")
            used_characters = []
            valid_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            self.stecker_setting = {}
            for pair in stecker_pairs:
                if (pair[0] in used_characters) or (pair[1] in used_characters):
                    raise SteckerSettingsInvalid
                elif (pair[0] not in valid_chars) or (pair[1] not in valid_chars):
                    raise SteckerSettingsInvalid
                else:
                    self.stecker_setting.update({pair[0]: pair[1]})
                    self.stecker_setting.update({pair[1]: pair[0]})

    def steck(self, char):
        """Accepts a character and parses it through the stecker board."""
        if char.upper() in self.stecker_setting:
            return self.stecker_setting[char]
        else:
            return char  # Un-jumped characters should be returned as is.


class Stator(object):
    """The stator was the first "wheel" of the enigma, which was stationary
    and usually never changed. However, as different machines used different
    variations of the stator, we do have to represent it even if its is
    not stateful. Two stators are provided for - these are the historical
    versions. Use "stat" to actually perform the stator's function, and
    "destat" to do the same in reverse.
    """

    def __init__(self, mode):
        """The stator mode is a string which states which stator to use. As
        currently implemented the options are "civilian" or "military"
        """
        mode = mode.lower()
        if mode == "civilian":
            self.stator_settings = {
                "Q": 1,
                "W": 2,
                "E": 3,
                "R": 4,
                "T": 5,
                "Z": 6,
                "U": 7,
                "I": 8,
                "O": 9,
                "P": 10,
                "A": 11,
                "S": 12,
                "D": 13,
                "F": 14,
                "G": 15,
                "H": 16,
                "J": 17,
                "K": 18,
                "L": 19,
                "Y": 20,
                "X": 21,
                "C": 22,
                "V": 23,
                "B": 24,
                "N": 25,
                "M": 26,
            }
        elif mode == "military":
            self.stator_settings = {
                "A": 1,
                "B": 2,
                "C": 3,
                "D": 4,
                "E": 5,
                "F": 6,
                "G": 7,
                "H": 8,
                "I": 9,
                "J": 10,
                "K": 11,
                "L": 12,
                "M": 13,
                "N": 14,
                "O": 15,
                "P": 16,
                "Q": 17,
                "R": 18,
                "S": 19,
                "T": 20,
                "U": 21,
                "V": 22,
                "W": 23,
                "X": 24,
                "Y": 25,
                "Z": 26,
            }
        else:
            raise UndefinedStatorError

        self.destator = {}
        for key in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            reflected = self.stator_settings[key]
            self.destator.update({reflected: key})

    def stat(self, char):
        char = char.upper()
        return self.stator_settings[char]

    def destat(self, signal):
        return self.destator[signal]


class Rotor(object):
    """This simple class represents a single rotor object. The rotors themselves
    are defined in RotorSettings.json of this package. Select a rotor by provding
    the rotor-type and Ringstellung while initializing.

    It's worth noting the reflector is also treated as a rotor.
    """

    def __init__(self, catalog, rotor_number, ringstellung, ignore_static):
        """Initialize the parameters of this individual rotor.

        :param catalog: A dictionary describing all rotors available.
        :param rotor_number: A rotor descriptor which can be found as a key in catalog
        :param ringstellung: The desired offset letter as a string.
        """
        self.name = rotor_number
        self.step_me = False
        self.static = False
        if rotor_number in catalog:
            description = catalog[rotor_number]
        else:
            raise RotorNotFound
        if ringstellung is None:
            self.ringstellung = "A"
        else:
            self.ringstellung = ringstellung
        ringstellung = alpha_to_num(self.ringstellung.upper())

        # Extremely nasty ringstellung implementation follows.
        # For this to work, ringstellung needs to be a number, rather than an index.

        ringstellunged_to_keys = {}  # Gives the ringstellung offset for entry pins.
        pins_to_ringstellunged = {}  # Gives the ringstellung offset for exit pins.

        pos = ringstellung
        for i in range(1, 27):
            if pos > 26:
                pos -= 26
            ringstellunged_to_keys.update({pos: i})
            pins_to_ringstellunged.update({i: pos})
            pos += 1

        self.notch = []
        for position in description["notch"]:
            self.notch.append(alpha_to_index(position))
        self.wiring = {}
        self.wiring_back = {}

        for shifted_input in ringstellunged_to_keys:
            in_pin = ringstellunged_to_keys[shifted_input]
            out_pin = pins_to_ringstellunged[description["wiring"][str(in_pin)]]
            self.wiring.update({shifted_input: out_pin})
            self.wiring_back.update({out_pin: shifted_input})

        if not ignore_static:
            if (
                "static" in description.keys()
            ):  # Issue 4: Bravo and Gamma rotor need to be static for m4
                if description["static"]:
                    self.static = True
                else:
                    self.static = False


class RotorMechanism(object):
    """This class represents and emulates the entire "moving parts" state of
    the machine. Essentially, this keeps track of the rotors and their
    positions. You can process characters one at a time through this object's
    "process" method. Initial settings are passed with the "set" method.
    """

    def __init__(self, list_rotors, reflector):
        """Expects a list of rotors and a rotor object representing reflector"""
        self.rotors = list_rotors
        for rotor in self.rotors:
            rotor.position = 1
        self.reflector = reflector

    def set(self, rotor_slot, setting):
        """Expects a python-indexed rotor and a character for a setting"""
        self.rotors[rotor_slot].position = alpha_to_index(setting)

    def process(self, bit_in):
        """Expects the pinning code from Stator, and returns an output
        of a similar nature. Also increments the state by adjusting the
        position attribute of each rotor in its set. On each operation
        the position bit is added at both ends."""
        next_bit = bit_in

        self.rotors[0].step_me = True  # The rightmost rotor always steps.
        indexer = -1
        for rotor in self.rotors:
            indexer += 1
            if (
                rotor.position in rotor.notch
            ):  # If a rotor is at its notch, the one on the left steps.
                rotor.step_me = True
                try:
                    self.rotors[indexer + 1].step_me = True
                except IndexError:
                    pass

        for rotor in self.rotors:
            if not rotor.static:  # Edge Case: The M4 B and C rotors do not rotate.
                if rotor.step_me:
                    rotor.step_me = False  # We gonna step now.
                    rotor.position += 1
                    if rotor.position > 25:  # Position is an index, can't exceed 25.
                        rotor.position -= 26

        for rotor in self.rotors:
            entry_face, exit_face = map_faces(rotor)
            entry_pin = entry_face[next_bit]
            exit_pin = rotor.wiring[entry_pin]
            next_bit = exit_face[exit_pin]
        next_bit = self.reflector.wiring[next_bit]
        for rotor in reversed(self.rotors):
            entry_face, exit_face = map_faces(rotor)
            entry_pin = entry_face[next_bit]
            exit_pin = rotor.wiring_back[entry_pin]
            next_bit = exit_face[exit_pin]

        output = next_bit

        return output


class Operator(object):
    """A special preparser that does some preformatting to the feed. This
    includes adjusting the spacing and stripping out characters that can't
    be represented easily in Enigma. This operator is not faithful to
    German practice at the time - it's only a convenience.
    """

    def __init__(self, word_length):
        """word_length is an int that sets the length of "words" in output."""
        self.word_length = word_length

    def format(self, message):
        """Accepts a string as input and does some parsing to it."""
        cased_message = message.upper()
        message_characters = cased_message.replace(" ", "")
        dict_replacement_characters = {
            ".": "X",
            ":": "XX",
            ",": "ZZ",
            "?": "FRAQ",
            "(": "KLAM",
            ")": "KLAM",
            """'""": "X",
        }
        for punct in dict_replacement_characters:
            message_characters = message_characters.replace(
                punct, dict_replacement_characters[punct]
            )

        for character in message_characters:
            if character not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                message_characters = message_characters.replace(character, "")

        m = message_characters
        # This next step adds the spaces which cut the words up.
        message_spaced = " ".join(
            [
                m[i : i + self.word_length]
                for i in range(0, len(message_characters), self.word_length)
            ]
        )
        return message_spaced


class Enigma(object):
    """A magic package that instantiates everything, allowing you to call your
    enigma machine as though it were a machine and operator pair. Allows these
    methods:
    - parse: processes a str message, outputing raw characters. Spacing is
    preserved if operator=False, otherwise it will be changed to word_length.
    If no operator is present, numerals and punctuation are unchanged.
    - set: change various settings. See below.
    """

    def __init__(
        self,
        catalog=default_rotors_catalog,
        stecker="",
        stator="military",
        rotors=[["I", 0], ["II", 0], ["III", 0]],
        reflector="UKW",
        operator=True,
        word_length=5,
        ignore_static_wheels=False,
    ):
        self.stecker = Stecker(setting=str(stecker))
        self.stator = Stator(mode=stator)
        wheels = []
        rotors.reverse()
        for rotor in rotors:
            rotor_req = rotor[0]
            ringstellung = rotor[1]
            rotor_object = Rotor(catalog, rotor_req, ringstellung, ignore_static_wheels)
            wheels.append(rotor_object)
        self.wheel_pack = RotorMechanism(
            wheels,
            reflector=Rotor(
                catalog,
                rotor_number=reflector,
                ringstellung="A",
                ignore_static=ignore_static_wheels,
            ),
        )
        if operator:
            if isinstance(operator, Operator):
                self.operator = operator(word_length)
            else:
                self.operator = Operator(word_length)
        else:
            self.operator = False

    def set_wheels(self, setting):
        """Accepts a string that is the new pack setting, e.g. ABQ"""
        physical_setting = []
        for char in setting:
            physical_setting.append(char.upper())
        physical_setting.reverse()
        for i in range(0, len(physical_setting)):
            self.wheel_pack.set(i, physical_setting[i])

    def set_stecker(self, setting):
        """Accepts a string to be the new stecker board arrangement."""
        self.stecker = Stecker(setting=str(setting))

    # def set_wheelpack(self, list_rotors):
    # self.wheel_pack = RotorMechanism(list_rotors.reverse())

    def parse(self, message="Hello World"):
        if self.operator:
            str_message = self.operator.format(message)
        else:
            str_message = message.upper()

        str_ciphertext = ""
        for character in str_message:
            if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                stecked = self.stecker.steck(character)  # Keystroke - > Stecker
                stated = self.stator.stat(stecked)  # Stecker -> Stator Wheel
                polysubbed = self.wheel_pack.process(
                    stated
                )  # Both ways through wheelpack, wheelpack steps forward.
                destated = self.stator.destat(
                    polysubbed
                )  # Backward through the stator wheel
                lamp = self.stecker.steck(destated)  # Again through stecker
                next_char = lamp
            else:  # Raised if an unformatted message contains special characters
                next_char = character
            str_ciphertext += next_char

        return str_ciphertext


def alpha_to_index(char):
    """Takes a single character and converts it to a number where A=0"""
    translator = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6,
        "H": 7,
        "I": 8,
        "J": 9,
        "K": 10,
        "L": 11,
        "M": 12,
        "N": 13,
        "O": 14,
        "P": 15,
        "Q": 16,
        "R": 17,
        "S": 18,
        "T": 19,
        "U": 20,
        "V": 21,
        "W": 22,
        "X": 23,
        "Y": 24,
        "Z": 25,
    }
    return translator[char.upper()]


def alpha_to_num(char):
    """Takes a single character and converts it to a number where A=1"""
    translator = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9,
        "J": 10,
        "K": 11,
        "L": 12,
        "M": 13,
        "N": 14,
        "O": 15,
        "P": 16,
        "Q": 17,
        "R": 18,
        "S": 19,
        "T": 20,
        "U": 21,
        "V": 22,
        "W": 23,
        "X": 24,
        "Y": 25,
        "Z": 26,
    }
    return translator[char.upper()]


def num_to_alpha(integ):
    """takes a numeral value and spits out the corresponding letter."""
    translator = {
        1: "A",
        2: "B",
        3: "C",
        4: "D",
        5: "E",
        6: "F",
        7: "G",
        8: "H",
        9: "I",
        10: "J",
        11: "K",
        12: "L",
        13: "M",
        14: "N",
        15: "O",
        16: "P",
        17: "Q",
        18: "R",
        19: "S",
        20: "T",
        21: "U",
        22: "V",
        23: "W",
        24: "X",
        25: "Y",
        26: "Z",
    }
    return translator[integ]


def map_faces(rotor):
    """Are you ready for bad entry pinning mapping?"""

    pos = rotor.position + 1  # We need a pin number, rather than an index
    neutral_to_pins = {}
    pins_to_neutral = {}

    for i in range(1, 27):
        if pos > 26:
            pos -= 26
        neutral_to_pins.update({i: pos})
        pins_to_neutral.update({pos: i})  # This is probably not right...
        pos += 1

    return neutral_to_pins, pins_to_neutral
