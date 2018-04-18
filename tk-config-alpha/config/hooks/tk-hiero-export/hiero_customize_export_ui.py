# Copyright (c) 2018 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import sgtk
from sgtk.platform.qt import QtGui

HookBaseClass = sgtk.get_hook_baseclass()


#class HieroCustomizeExportUI(HookBaseClass):
#    """
#    This class defines methods that can be used to customize the UI of the various
#    Shotgun-related exporters. Each processor has its own set of create/get/set
#    methods, allowing for customizable UI elements for each type of export.
#    """
#    # For detailed documentation of the methods available for this hook, see
#    # the documentation at http://developer.shotgunsoftware.com/tk-hiero-export/
#    pass

    
class HieroCustomizeExportUI(HookBaseClass):
    def create_shot_processor_widget(self, parent_widget):
        widget = QtGui.QGroupBox("Crater Properties", parent_widget)
        widget.setLayout(QtGui.QFormLayout())
        return widget

    def get_shot_processor_ui_properties(self):
        return [
            dict(
                label="Create Cut:",
                name="custom_create_cut_bool_property",
                value=True,
                tooltip="Create a Cut and CutItems in Shotgun...",
            ),
            dict(
                label="Transcode:",
                name="custom_transcode_bool_property",
                value=True,
                tooltip="Transcode and update shots",
            ),
        ]

    def set_shot_processor_ui_properties(self, widget, properties):
        layout = widget.layout()
        for label, prop in properties.iteritems():
            layout.addRow(label, prop)
            
            
            
            
    # transcode wiget =======================================================   
    def create_transcode_exporter_widget(self, parent_widget):
        widget = QtGui.QGroupBox("Crater Properties", parent_widget)
        widget.setLayout(QtGui.QFormLayout())
        return widget

    def get_transcode_exporter_ui_properties(self):
        return [
            dict(
                label="Custom two:",
                name="custom_two",
                value=True,
                tooltip="Custom two tooltip",
            )
        ]

    def set_transcode_exporter_ui_properties(self, widget, properties):
        layout = widget.layout()
        for label, prop in properties.iteritems():
            layout.addRow(label, prop)

            
            
            
    # audio exporter wiget =======================================================           
    def create_audio_exporter_widget(self, parent_widget):
        widget = QtGui.QGroupBox("Crater Properties", parent_widget)
        widget.setLayout(QtGui.QFormLayout())
        return widget

    def get_audio_exporter_ui_properties(self):
        return [
            dict(
                label="Custom three:",
                name="custom_three",
                value=True,
                tooltip="Custom three tooltip",
            )
        ]

    def set_audio_exporter_ui_properties(self, widget, properties):
        layout = widget.layout()
        for label, prop in properties.iteritems():
            layout.addRow(label, prop)
            



    # nuke shot exporter wiget =======================================================   
    def create_nuke_shot_exporter_widget(self, parent_widget):
        widget = QtGui.QGroupBox("Crater Properties", parent_widget)
        widget.setLayout(QtGui.QFormLayout())
        return widget

    def get_nuke_shot_exporter_ui_properties(self):
        return [
            dict(
                label="Custom four:",
                name="custom_four",
                value=True,
                tooltip="Custom four tooltip",
            )
        ]

    def set_nuke_shot_exporter_ui_properties(self, widget, properties):
        layout = widget.layout()
        for label, prop in properties.iteritems():
            layout.addRow(label, prop)