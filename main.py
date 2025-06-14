#!/usr/bin/env python3
"""Entry point script for pixeditor_v2."""

import sys
import os

# Add the current directory to Python path so we can import our modules
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

def main():
    """Run the pixeditor application."""
    from PyQt5 import QtWidgets, QtGui
    
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(QtGui.QPixmap("icons/pixeditor.png")))
    
    from pixeditor import MainWindow
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
