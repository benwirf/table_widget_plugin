"""
/****************************************************************************************
Copyright:  (C) Ben Wirf
Date:       August 2024
Email:      ben.wirf@gmail.com
****************************************************************************************/
"""

from qgis.core import QgsMapLayerProxyModel
from qgis.PyQt.QtWidgets import QToolBar, QAction
from qgis.PyQt.QtGui import QIcon

from .table_widget_plugin_dialog import TableWidgetPluginDialog


class TableWidgetPlugin:

    def __init__(self, iface):
        self.iface = iface
        self.main_window = self.iface.mainWindow()
        self.dlg = TableWidgetPluginDialog()
        self.toolbar = self.main_window.findChild(QToolBar, 'mPluginToolBar')
        self.action = QAction(QIcon(":images/themes/default/mActionEditTable.svg"), '', self.main_window)
        
    def initGui(self):
        '''This method is where we add the plugin action to the plugin toolbar.
        This is also where we connect any signals and slots
       such as Push Buttons to our class methods which contain our plugin logic.'''
        self.action.setObjectName('mActionTestPlugin')
        self.action.setToolTip('Rename layer fields')
        self.toolbar.addAction(self.action)
        # Show the plugin dialog when the toolbar action is triggered
        self.action.triggered.connect(lambda: self.dlg.show())
        # Connect the accepted signal of the button box (OK button clicked) to a method
        self.dlg.button_box.accepted.connect(self.retrieve_field_names)
        # Close the dialog when the Cancel button is clicked
        self.dlg.button_box.rejected.connect(lambda: self.dlg.close())
    
    def retrieve_field_names(self):
        '''Retrieve the values from the dialog widgets for further processing'''
        field_name_map = {}
        layer = self.dlg.mMapLayerComboBox.currentLayer()
        for i in range(self.dlg.tableWidget.rowCount()):
            field_name = self.dlg.tableWidget.cellWidget(i, 0).currentField()
            new_name = self.dlg.tableWidget.cellWidget(i, 1).currentText()
            field_name_map[field_name] = new_name
        self.iface.messageBar().pushMessage(repr(field_name_map))
            
    def unload(self):
        self.toolbar.removeAction(self.action)
        del self.action

