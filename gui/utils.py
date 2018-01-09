# Copyright: Damien Elmes <anki@ichi2.net>
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

import os
import sys
from subprocess import call

import gui
from gui.qt import *


isMac = sys.platform.startswith("darwin")
isWin = sys.platform.startswith("win32")
isLin = not isMac and not isWin

# Learned from anki/aqt/profile ... _defaultBase
def defaultBase():
    if isWin:
        loc = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
        assert loc.endswith("/Joytan")
        return loc
    elif isMac:
        return os.path.expanduser("~/Library/Application Support/Joytan")
    else:
        dataDir = os.environ.get(
            "XDG_DATA_HOME", os.path.expanduser("~/.local/share"))
        if not os.path.expanduser(dataDir):
            os.makedirs(dataDir)
        return os.path.join(dataDir, "Joytan")


# Learned from anki/aqt/profile ... _oldFolderLocation
def defaultWorkspace():
    if isMac:
        return os.path.expanduser("~/Joytan")
    elif isWin:
        loc = QStandardPaths.writableLocation(QStandardPaths.HomeLocation)
        return os.path.join(loc, "Joytan")
    else:
        p = os.path.expanduser("~/Joytan")
        if os.path.exists(p):
            return p
        else:
            loc = QStandardPaths.writableLocation(QStandardPaths.HomeLocation)
            return os.path.join(loc, "Joytan")


def defaultMusic():
    loc = QStandardPaths.writableLocation(QStandardPaths.MusicLocation)
    return loc


def defaultDocument():
    loc = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
    return loc


class GetTextDialog(QDialog):

    def __init__(self, parent, question, help=None, edit=None, default="", \
                 title="Anki", minWidth=400):
        QDialog.__init__(self, parent)
        self.setWindowTitle(title)
        self.question = question
        self.help = help
        self.qlabel = QLabel(question)
        self.setMinimumWidth(minWidth)
        v = QVBoxLayout()
        v.addWidget(self.qlabel)
        if not edit:
            edit = QLineEdit()
        self.l = edit
        if default:
            self.l.setText(default)
            self.l.selectAll()
        v.addWidget(self.l)
        buts = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        if help:
            buts |= QDialogButtonBox.Help
        b = QDialogButtonBox(buts)
        v.addWidget(b)
        self.setLayout(v)
        b.button(QDialogButtonBox.Ok).clicked.connect(self.accept)
        b.button(QDialogButtonBox.Cancel).clicked.connect(self.reject)
        if help:
            b.button(QDialogButtonBox.Help).clicked.connect(self.helpRequested)

    def accept(self):
        return QDialog.accept(self)

    def reject(self):
        return QDialog.reject(self)

    def helpRequested(self):
        pass
        #openHelp(self.help)


def getText(prompt, parent=None, help=None, edit=None, default="",
            title="Joytan", geomKey=None, **kwargs):
    if not parent:
        parent = gui.mw.app.activeWindow() or gui.mw
    d = GetTextDialog(parent, prompt, help=help, edit=edit,
                      default=default, title=title, **kwargs)
    d.setWindowModality(Qt.WindowModal)
    if geomKey:
        print("Should restore Geom")
    ret = d.exec_()
    if geomKey and ret:
        print("Should save Geom")
    return (str(d.l.text()), ret)



def getFileToSave(parent, title, filter="*.*", dir=None, suf='jel'):
    opts = QFileDialog.Options()
    opts |= QFileDialog.DontUseNativeDialog
    fd = QFileDialog()

    if os.path.exists(dir):
        fd.setDirectory(dir)
    fd.setOptions(opts)
    fd.setAcceptMode(QFileDialog.AcceptSave)
    fd.setFileMode(QFileDialog.AnyFile)
    fd.setWindowTitle(title)
    fd.setNameFilter(filter)
    fd.setDefaultSuffix(suf)

    fd.exec_()

    try:
        file = fd.selectedFiles()[0]
        assert os.path.isdir(file) is not True
        return file
    except (IndexError, AssertionError, TypeError):
        print("Error: Invalid file is selected.")
        raise


def getFiles(parent, title, filter="*.*", dir=None):
    opts = QFileDialog.Options()
    opts |= QFileDialog.DontUseNativeDialog
    fd = QFileDialog()

    if os.path.exists(dir):
        fd.setDirectory(dir)
    fd.setOptions(opts)
    fd.setFileMode(QFileDialog.ExistingFiles)
    fd.setWindowTitle(title)
    fd.setNameFilter(filter)
    ret = []

    def accept():
        files = fd.selectedFiles()
        for file in files:
            if os.path.isdir(file):
                files.remove(file)
            ret.append(file)
    fd.accepted.connect(accept)
    fd.exec_()
    return ret

def getFile(parent, title, filter="*.*", dir=None):
    opts = QFileDialog.Options()
    opts |= QFileDialog.DontUseNativeDialog
    fd = QFileDialog()

    if os.path.exists(dir):
        fd.setDirectory(dir)
    fd.setOptions(opts)
    fd.setFileMode(QFileDialog.ExistingFile)
    fd.setWindowTitle(title)
    fd.setNameFilter(filter)
    ret = []

    def accept():
        file = str(list(fd.selectedFiles())[0])
        ret.append(file)

    fd.accepted.connect(accept)
    fd.exec_()
    return ret[0]


def path2filename(longpath):
    return os.path.basename(os.path.normpath(longpath))

def path_temp(_temp_dir):
    """
    Returns a path using the given extension that may be used for
    writing out a temporary file.
    """

    from string import ascii_lowercase, digits
    alphanumerics = ascii_lowercase + digits

    from os.path import join
    from random import choice
    from time import time
    return join(
        _temp_dir,
        '%x-%s' % (
            int(time()),
            ''.join(choice(alphanumerics) for i in range(30))
        ),
    )

def showWarning(text, parent=None, help="", title="Joytan"):
    "Show a small warning with an OK button."
    return showInfo(text, parent, help, "warning", title=title)

def showCritical(text, parent=None, help="", title="Joytan"):
    "Show a small critical error with an OK button."
    return showInfo(text, parent, help, "critical", title=title)

def showInfo(text, parent=False, help="", type="info", title="Joytan"):
    "Show a small info window with an OK button."
    if parent is False:
        parent = gui.mw.app.activeWindow() or gui.mw
    if type == "warning":
        icon = QMessageBox.Warning
    elif type == "critical":
        icon = QMessageBox.Critical
    else:
        icon = QMessageBox.Information
    mb = QMessageBox(parent)
    mb.setText(text)
    mb.setIcon(icon)
    mb.setWindowModality(Qt.WindowModal)
    mb.setWindowTitle(title)
    b = mb.addButton(QMessageBox.Ok)
    b.setDefault(True)
    if help:
        b = mb.addButton(QMessageBox.Help)
        b.clicked.connect(lambda: print("Help is under development."))
        b.setAutoDefault(False)
    return mb.exec_()

LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',
    'fil': 'Filipino',
    'he': 'Hebrew'
}

LANGCODES = dict(map(reversed, LANGUAGES.items()))