from enum import Enum

FRAME_OUTPUT_DIR = "StreamAssets/Finishes"

class Hero(Enum):
    hero0 = "Beauty"
    hero1 = "Big Bad Wolf"
    hero2 = "Celestial Tiger"
    hero3 = "Charon"
    hero4 = "Evella"
    hero5 = "Fallen Angel"
    hero6 = "Gepetto"
    hero7 = "Grandmother"
    hero8 = "Gwen"
    hero9 = "Hoard Dragon"
    hero10 = "Jack's Giant"
    hero11 = "Krampus"
    hero12 = "Loki"
    hero13 = "Mad Catter"
    hero14 = "Mask"
    hero15 = "Merlin"
    hero16 = "Mihri, Lion King"
    hero17 = "Mordred"
    hero18 = "Morgan le Fay"
    hero19 = "Mrs. Claus"
    hero20 = "Muerte"
    hero21 = "Pan's Shadow"
    hero22 = "Peter Pants"
    hero23 = "Pied Piper"
    hero24 = "Potion Master"
    hero25 = "Pup, the Magic Dragon"
    hero26 = "Sad Dracula"
    hero27 = "Sir Galahad"
    hero28 = "Skip, the Time Skipper"
    hero29 = "Snow Angel"
    hero30 = "The Cursed King"
    hero31 = "The Fates"
    hero32 = "Trophy Hunter"
    hero33 = "Wonder Waddle"
    hero34 = "Xelhua"

    @classmethod
    def list(cls):
        return list(map(lambda c: str(c.value), cls))
