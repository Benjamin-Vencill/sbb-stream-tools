import math
import matplotlib.pyplot as plt
import numpy as np
import os

from matplotlib import gridspec
from PIL import Image


class FrameCollection:
    """
    A collection of result cards which are rendered into a display Frame.
    """

    def __init__(self, output_dir, max_size=4):
        self.output_dir = output_dir
        self.max_size = max_size
        self.cards = []
        self.load_initial_frames()

    def load_initial_frames(self):
        for i in range(self.max_size):
            self.add_new_result_card("00Empty", "00Empty")
        

    def add_new_result_card(self, hero, placement):

        if os.path.isfile(f"StreamAssets/HeroPortraits/{hero}.png"):
            portrait = np.asarray(Image.open(f"StreamAssets/HeroPortraits/{hero}.png"))
        else:
            portrait = np.asarray(Image.open(f"StreamAssets/HeroPortraits/missingportrait.png"))

        overlay = np.asarray(Image.open(f"StreamAssets/PortraitTokens/{placement}.png"))
        
        x1, y1, x2, y2 = 0, 0, overlay.shape[1], overlay.shape[0]
        card = np.zeros((y2, x2, 4), dtype=np.uint8)
        card[230:, 230:, :] = portrait
        card[y1:y2, x1:x2] = card[y1:y2, x1:x2] * (1 - overlay[:, :, 3:] / 255) + overlay[:, :, :4] * (overlay[:, :, 3:] / 255)
        
        self.cards.append(card)
        if len(self.cards) > self.max_size:
            self.cards.pop(0)

    def plot_collection(self):
        """
        Plot the card collection and save as an image.
        """
        frame = self.cards[0]
        pad = np.zeros((frame.shape[0], 20, frame.shape[2]), dtype=np.uint8)
        for card in self.cards[1:]:
            frame = np.append(frame, pad, axis=1)
            frame = np.append(frame, card, axis=1)

        im = Image.fromarray(frame)
        im.save(f"{self.output_dir}/FrameCollection.png")


if __name__ == "__main__":

    frame_collection = FrameCollection(output_dir="StreamAssets/Finishes", max_size=4)

    while 1:
        response = input("Enter Hero and Placement: ")
        hero, placement = response.split(' ')
        frame_collection.add_new_result_card(hero, placement)
        frame_collection.plot_collection()