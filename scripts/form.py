
import csv
import sys

from functools import partial
from PyQt5.QtWidgets import QApplication, QComboBox, QDialog, QFormLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

from data import Hero, FRAME_OUTPUT_DIR
from frame_collection import FrameCollection

def onSubmit(*args):
    """
    Submit the form.
    """

class Form(QDialog):
    def __init__(self, csv_filename: str, parent=None) -> None:
        super(Form, self).__init__(parent=None)

        self.csv_filename = csv_filename
        self.csv_delimeter = ","

        self.mainVerticalLayout = QVBoxLayout()
        self.entryFormLayout = QFormLayout()

        self.heroComboBox = QComboBox()
        self.heroComboBox.addItems(Hero.list())

        self.placementComboBox = QComboBox()
        self.placementComboBox.addItems([str(i) for i in range(1, 9)])

        self.mmrGainTextBox = QLineEdit()
        self.rankGainLineEdit = QLineEdit()

        self.entryFormLayout.addRow("Hero:", self.heroComboBox)
        self.entryFormLayout.addRow("Placement:", self.placementComboBox)
        self.entryFormLayout.addRow("MMR Gain:", self.mmrGainTextBox)
        self.entryFormLayout.addRow("New Rank:", self.rankGainLineEdit)

        self.submitButton = QPushButton("Submit")
        self.submitButton.clicked.connect(self.onSubmit)

        self.mainVerticalLayout.addLayout(self.entryFormLayout)
        self.mainVerticalLayout.addWidget(self.submitButton)

        self.setLayout(self.mainVerticalLayout)
        self.setWindowTitle("Storybook Brawl Results")

    def onSubmit(self) -> None:
        currentHeroSelection = self.heroComboBox.currentText()
        currentPlacementSelection = self.placementComboBox.currentText()
        currentMMRGainSelection = self.mmrGainTextBox.text()
        currentRankSelection = self.rankGainLineEdit.text()

        print(f"New Entry:\n\tHero: {currentHeroSelection}\n\tPlacement: {currentPlacementSelection}\n\tMMR Gain: {currentMMRGainSelection}\n\tNew Rank: {currentRankSelection}")
        
        heroSubmission = "".join(c for c in currentHeroSelection if c not in " '.,").lower()
        placementSubmission = int(currentPlacementSelection)
        mmrSubmission = int(currentMMRGainSelection)
        rankSubmission = int(currentRankSelection)

        self.storeCSVEntry(heroSubmission, placementSubmission, mmrSubmission, rankSubmission)
        self.displayMatchHistory()

    def storeCSVEntry(self, hero: str, placement: int, mmr: int, rank: int) -> None:
        """
        Append the submission to the CSV file.
        """
        with open(self.csv_filename, "a") as f:
            csv_writer = csv.writer(f, delimiter=self.csv_delimeter)
            csv_writer.writerow([hero, placement, mmr, rank])

    def displayMatchHistory(self) -> None:
        """
        Use the CSV database to display the most recent match history.
        """
        self.frameCollection = FrameCollection(FRAME_OUTPUT_DIR)
        with open(self.csv_filename, "r") as f:
            match_history = f.readlines()[-4:]

        for entry in match_history:
            hero, placement, mmr, rank = entry.split(self.csv_delimeter)
            self.frameCollection.add_new_result_card(hero, placement)
        self.frameCollection.plot_collection()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    form = Form("storybook_match_data.csv")
    form.show()
    app.exec_()