# ##### BEGIN MIT LICENSE BLOCK #####
# MIT License
# 
# Copyright (c) 2018 Insma Software
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ##### END MIT LICENSE BLOCK #####

# ----------------------------------------------------------
# Author: Maciej Klemarczyk (mklemarczyk)
# ----------------------------------------------------------

# ----------------------------------------------
# Define Addon info
# ----------------------------------------------
bl_info = {
    "name": "Architecture Lab",
    "author": "Insma Software - Maciej Klemarczyk (mklemarczyk)",
    "location": "View3D > Add > Mesh > ArchLab",
    "version": (1, 0, 0),
    "blender": (2, 7, 9),
    "description": "Creates rooms, doors, windows, and other architecture objects",
    "wiki_url": "https://github.com/insma/ArchitectureLab/wiki",
    "tracker_url": "https://github.com/insma/ArchitectureLab/issues",
    "category": "Add Mesh"
}


# ----------------------------------------------
# Import modules
# ----------------------------------------------
if "bpy" in locals():
    import importlib
    importlib.reload(archlab_mesh_plane_tool)

    print("archlab: Reloaded multifiles")
else:
    from . import archlab_mesh_plane_tool

    print("archlab: Imported multifiles")

modules = [
    archlab_mesh_plane_tool.ArchLabPlane,
    archlab_mesh_plane_tool.ArchLabPlaneGeneratorPanel
]


# ----------------------------------------------
# Import libraries
# ----------------------------------------------
import bpy

from bpy.props import (
        BoolProperty,
        FloatVectorProperty,
        IntProperty,
        FloatProperty,
        StringProperty,
    )

from bpy.types import (
        AddonPreferences,
        Menu,
        Scene,
        INFO_MT_mesh_add,
        WindowManager,
    )


# ----------------------------------------------------------
# Primitives menu
# ----------------------------------------------------------
class ArchLabMeshPrimitivesAdd(Menu):
    bl_idname = "INFO_MT_archlab_mesh_primitives_add"
    bl_label = "Primitives"

    def draw(self, context):
        self.layout.operator("mesh.archlab_plane", text="Add Plane")

# ----------------------------------------------------------
# ArchLab menu
# ----------------------------------------------------------
class ArchLabMeshCustomMenuAdd(Menu):
    bl_idname = "INFO_MT_archlab_mesh_custom_menu_add"
    bl_label = "ArchLab"

    def draw(self, context):
        self.layout.operator_context = 'INVOKE_REGION_WIN'
        self.layout.menu("INFO_MT_archlab_mesh_primitives_add", text="Primitives", icon="GROUP")

modules.extend([
    ArchLabMeshCustomMenuAdd,
    ArchLabMeshPrimitivesAdd
])

# --------------------------------------------------------------
# Register add mesh menus
# --------------------------------------------------------------
# Define menu
def ArchLabMeshMenu_func(self, context):
    self.layout.menu("INFO_MT_archlab_mesh_custom_menu_add", icon="GROUP")

# --------------------------------------------------------------
# Register all operators and panels
# --------------------------------------------------------------
def register():
    for module_class in modules:
        bpy.utils.register_class(module_class)
    INFO_MT_mesh_add.append(ArchLabMeshMenu_func)

# --------------------------------------------------------------
# Unregister all operators and panels
# --------------------------------------------------------------
def unregister():
    for module_class in modules:
        bpy.utils.unregister_class(module_class)
    INFO_MT_mesh_add.remove(ArchLabMeshMenu_func)

# --------------------------------------------------------------
# Addon registration
# --------------------------------------------------------------
if __name__ == "__main__":
    register()