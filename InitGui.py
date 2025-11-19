#***************************************************************************
#*    Copyright (C) 2023 
#*    This library is free software
#***************************************************************************
import inspect
import os
import sys
import FreeCAD
import FreeCADGui

class PumpBlowerWBShowCommand:
    def GetResources(self):
        file_path = inspect.getfile(inspect.currentframe())
        module_path=os.path.dirname(file_path)
        return { 
          'Pixmap': os.path.join(module_path, "icons", "pump.svg"),
          'MenuText': "PumpBlowerWB",
          'ToolTip': "Show/Hide PumpBlowerWB"}

    def IsActive(self):
        import PumpLib
        PumpLib
        return True

    def Activated(self):
        try:
          import PumpLib
          PumpLib.main.d.show()
        except Exception as e:
          FreeCAD.Console.PrintError(str(e) + "\n")

    def IsActive(self):
        import PumpLib
        return not FreeCAD.ActiveDocument is None

class PumpBlowerWB(FreeCADGui.Workbench):
    def __init__(self):
        file_path = inspect.getfile(inspect.currentframe())
        module_path=os.path.dirname(file_path)
        self.__class__.Icon = os.path.join(module_path, "icons", "pump.svg")
        self.__class__.MenuText = "PumpBlowerWB"
        self.__class__.ToolTip = "PumpBlowerWB by Pascal"

    def Initialize(self):
        self.commandList = ["PumpBlowerWB_Show"]
        self.appendToolbar("&PumpBlowerWB", self.commandList)
        self.appendMenu("&PumpBlowerWB", self.commandList)

    def Activated(self):
        import PumpLib
        PumpLib
        return

    def Deactivated(self):
        return

    def ContextMenu(self, recipient):
        return

    def GetClassName(self): 
        return "Gui::PythonWorkbench"
FreeCADGui.addWorkbench(PumpBlowerWB())
FreeCADGui.addCommand("PumpBlowerWB_Show", PumpBlowerWBShowCommand())

