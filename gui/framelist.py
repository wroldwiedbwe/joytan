
from gui.qt import *
from gui.bundle import BundleItemUi, BundleUi

class FrameList(QListWidget):

    def __init__(self, mw, parent=None):
        super(FrameList, self).__init__(parent)
        self.mw = mw
        self.fm = mw.fm
        # Store the ID of bundles whicn the UI is rendering
        # Fixme: For now, the ID is just the name of bundle but should be like hash
        self.currentIds = []

    def setNewBundles(self):
        # TODO: Move FM out of the class and make two classes comunicate with each other(?)
        # like Signal & Slot (?)
        # Check newly created bundles in the frame of the FrameManager
        newbds = self.fm.getNewBundles(self.currentIds)

        for bundle in newbds:
            self.setNewId(bundle.name)
            bui, bitem = self.mw.bdfactory.createUi(bundle)
            self.addItem(bui)
            self.setItemWidget(bui, bitem)


    def updateBundles(self):
        # Update the inside of the bundles in the list
        print("Bundle updates")
        for i in range(self.count()):
            bditUi = self.itemWidget(self.item(i))
            bditUi.updateEditors()

    def setNewId(self, id):
        self.currentIds.append(id)

    def getWidgetItem(self, num):
        return self.itemWidget(self.item(num))

    def updateItem(self, Item):
        pass

    def add(self, item, widget):
        pass

    def remove(self):
        pass