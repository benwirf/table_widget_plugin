"""
/****************************************************************************************
Copyright:  Ben Wirf
Date:       August 2024
Email:      ben.wirf@gmail.com
****************************************************************************************/
"""

import os

from qgis.PyQt import uic

from qgis.PyQt.QtWidgets import (QDialog, QComboBox, QTableWidgetItem)
from qgis.PyQt.QtGui import (QIcon)

from qgis.core import QgsMapLayerProxyModel
from qgis.gui import QgsFieldComboBox


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'table_widget_plugin_dialog_base.ui'))

class TableWidgetPluginDialog(QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        super(TableWidgetPluginDialog, self).__init__(parent)
        self.setupUi(self)
        self.setMinimumWidth(500)
        #########################################################
        self.name_options = ['Name_1', 'Name_2', 'Name_3', 'Name_4', 'Name_5']
        self.mMapLayerComboBox.setFilters(QgsMapLayerProxyModel.VectorLayer)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(['Field Name', 'Rename To'])
        self.tableWidget.horizontalHeader().setMinimumSectionSize(200)
        
        self.addButton.setText('')
        self.addButton.setIcon(QIcon(":images/themes/default/symbologyAdd.svg"))
        
        self.add_table_row()
        self.addButton.clicked.connect(self.add_table_row)
        self.resetButton.clicked.connect(self.reset_table)
        self.mMapLayerComboBox.layerChanged.connect(self.reset_table)
        
    def reset_table(self):
        self.tableWidget.setRowCount(0)
        self.add_table_row()
        
    def add_table_row(self):
        i = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(i+1)
        fcb = QgsFieldComboBox(self.tableWidget)
        fcb.setLayer(self.mMapLayerComboBox.currentLayer())
        ncb = QComboBox(self.tableWidget)
        ncb.addItems(self.name_options)
        self.tableWidget.setItem(i, 0, QTableWidgetItem())
        self.tableWidget.setItem(i, 1, QTableWidgetItem())
        self.tableWidget.setCellWidget(i, 0, fcb)
        self.tableWidget.setCellWidget(i, 1, ncb)
        self.tableWidget.resizeColumnsToContents()
