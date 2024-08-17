
def classFactory(iface):
    from .table_widget_plugin import TableWidgetPlugin
    return TableWidgetPlugin(iface)