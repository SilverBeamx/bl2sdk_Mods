import pathlib
from functools import lru_cache
from typing import Dict, List, Sequence, Tuple

import unrealsdk

import imgui
from .. import blimgui
from ..ModMenu import *

IMGUI_SHOW: bool = False


def _toggle() -> None:
    global IMGUI_SHOW
    if IMGUI_SHOW:
        blimgui.close_window()
        IMGUI_SHOW = False
    else:
        blimgui.create_window("Material Editor")
        blimgui.set_draw_callback(instance.draw)
        IMGUI_SHOW = True


class MaterialEditor(SDKMod):
    Name: str = "Material Editor"
    Author: str = "Juso"
    Description: str = "Allows you to edit MaterialInstanceConstant Objects in realtime."
    Version: str = "1.0.0"

    Types: ModTypes = ModTypes.Utility
    Priority: int = ModPriorities.Standard
    SaveEnabledState: EnabledSaveType = EnabledSaveType.NotSaved

    Status: str = "Disabled"

    def __init__(self):
        self.Options: Sequence[Options.Base] = []
        self.Keybinds: Sequence[Keybind] = [Keybind("Open Editor", "F1", OnPress=_toggle)]

        self.input_text_save_modal: str = "Skin"
        self.input_text_search: str = ""
        self.input_text_search_textures: str = ""

        self.current_material_index: int = -1
        self.current_texture_index: int = -1

        self.selected_material: unrealsdk.UObject = None
        self.selected_parent: unrealsdk.UObject = None
        self.select_texture_param: str = ""

        self.texture_backup: unrealsdk.UObject = None
        self.col4_values: Dict[str, Tuple[float, float, float, float]] = {}

        self.path = pathlib.Path()

    def Enable(self) -> None:
        super().Enable()

    def Disable(self) -> None:
        super().Disable()

    def draw(self) -> None:
        # Main Menu Bar
        b_save_modal: bool = False
        if imgui.begin_main_menu_bar():
            if imgui.begin_menu("File"):
                if imgui.menu_item("Save To File", shortcut="Ctrl+S", selected=False, enabled=True)[0]:
                    b_save_modal = True
                imgui.end_menu()
            imgui.end_main_menu_bar()

        # Save Modal Popup
        if b_save_modal:
            imgui.open_popup("Save File")
        if imgui.begin_popup_modal(title="Save File", flags=imgui.WINDOW_ALWAYS_AUTO_RESIZE)[0]:
            self._save_modal()

        # Main Window Search Objects
        self._show_search_window()

        # Settings Window Edit Objects
        self._show_edit_window()

    def _show_search_window(self) -> None:
        imgui.begin("Inventory Editor")

        _, self.input_text_search = imgui.input_text("Search", self.input_text_search, 32)
        material_names, __objs = self.search_skins(self.input_text_search)
        b, self.current_material_index = imgui.listbox("##Materials", self.current_material_index, material_names, 24)
        if b:
            self.selected_material = __objs[self.current_material_index]
            self._get_parent_material()

        imgui.end()

    def _show_edit_window(self) -> None:
        imgui.begin("Edit Material")
        imgui.text(
            f"Editing: "
            f"{None if not self.selected_material else self.selected_material.PathName(self.selected_material)}"
        )
        if not self.selected_parent:
            imgui.end()
            return

        b_texture_modal: bool = False
        if imgui.collapsing_header("Texture Parameters")[0]:
            for param in self._get_texture_parameters(self.selected_parent):
                if imgui.button(param, width=-1):
                    self.select_texture_param = param
                    self.texture_backup = self.selected_material.GetTextureParameterValue(param)[1]
                    b_texture_modal = True

        if b_texture_modal:
            imgui.open_popup("Select Texture")
        if imgui.begin_popup_modal("Select Texture")[0]:
            self._texture_modal()

        if imgui.collapsing_header("Vector Parameters")[0]:
            for param in self._get_vector_parameters(self.selected_parent):
                R, G, B, A = self.col4_values[param]
                b, col = imgui.color_edit4(param, R, G, B, A)
                if b:
                    R, G, B, A = col
                    self.col4_values[param] = col
                    self.selected_material.SetVectorParameterValue(param, (R * 2.55, G * 2.55, B * 2.55, A * 2.55))

        if imgui.collapsing_header("Scalar Parameters")[0]:
            for param in self._get_scalar_parameters(self.selected_parent):
                b, val = imgui.slider_float(param, self.selected_material.GetScalarParameterValue(param)[1], -10, 10)
                if b:
                    self.selected_material.SetScalarParameterValue(param, val)

        imgui.end()

    def _save_modal(self) -> None:
        imgui.text("Save Current Skin to file:")
        _, self.input_text_save_modal = imgui.input_text("File Name", self.input_text_save_modal, 32)
        imgui.text(f"Will be saved as '{(self.path / ('../' + self.input_text_save_modal)).resolve()}.blcm'")
        imgui.text("Saving this file will overwrite any existing file with the same name!")

        if imgui.button("Save"):
            self._save_file(self.path / f"../{self.input_text_save_modal}.blcm")
            self.input_text_save_modal = "Skin"
            imgui.close_current_popup()
        imgui.same_line()
        if imgui.button("Cancel"):
            self.input_text_save_modal = "Skin"
            imgui.close_current_popup()
        imgui.end_popup()

    def _texture_modal(self) -> None:
        imgui.text("Select any material and press 'Select' or 'Cancel'")

        _, self.input_text_search_textures = imgui.input_text("Search##2", self.input_text_search_textures, 32)
        t_names, t_objs = self.search_textures(self.input_text_search_textures)

        b, self.current_texture_index = imgui.listbox("##TextureListBox", self.current_texture_index, t_names, 16)
        if b:
            t2d = t_objs[self.current_texture_index]
            self.selected_material.SetTextureParameterValue(self.select_texture_param, t2d)

        if imgui.button("Select##2"):
            t2d = t_objs[self.current_texture_index]
            self.selected_material.SetTextureParameterValue(self.select_texture_param, t2d)
            imgui.close_current_popup()
        imgui.same_line()
        if imgui.button("Cancel##2"):
            self.selected_material.SetTextureParameterValue(self.select_texture_param, self.texture_backup)
            imgui.close_current_popup()
        imgui.end_popup()

    def _save_file(self, path: pathlib.Path) -> None:
        with open(str(path.absolute()), "w") as fp:
            if not self.selected_material:
                return
            obj_name = self.selected_material.PathName(self.selected_material)

            set_vector = "("
            for param in self.selected_material.VectorParameterValues:
                rgba = param.ParameterValue
                R = rgba.R * 2.55
                G = rgba.G * 2.55
                B = rgba.B * 2.55
                A = rgba.A * 2.55
                set_vector += f"(ParameterName={param.ParameterName},ParameterValue=(R={R},G={G},B={B},A={A})),"
            fp.write(f"set {obj_name} VectorParameterValues {set_vector[:-1]})\n")

            set_texture = "("
            for param in self.selected_material.TextureParameterValues:
                set_texture += f"(ParameterName={param.ParameterName}," \
                               f"ParameterValue=Texture2D'{self.selected_material.PathName(param.ParameterValue)}'),"
            fp.write(f"set {obj_name} TextureParameterValues {set_texture[:-1]})\n")

            set_scalar = "("
            for param in self.selected_material.ScalarParameterValues:
                set_scalar += f"(ParameterName={param.ParameterName},ParameterValue={param.ParameterValue}),"
            fp.write(f"set {obj_name} ScalarParameterValues {set_scalar[:-1]})\n")

    def _get_parent_material(self) -> None:
        p = self.selected_material
        while p.Parent:
            p = p.Parent
        self.selected_parent = p

    @lru_cache(1)
    def _get_texture_parameters(self, mat: unrealsdk.UObject) -> List[str]:
        if not mat:
            return []
        parameters: List[str] = []
        for exp in mat.Expressions:
            if exp and exp.Class == unrealsdk.FindClass("MaterialExpressionTextureSampleParameter2D"):
                parameters.append(exp.ParameterName)
        return sorted(list(set(parameters)))

    @lru_cache(1)
    def _get_vector_parameters(self, mat: unrealsdk.UObject) -> List[str]:
        self.col4_values = {}
        parameters: List[str] = []
        for exp in mat.Expressions:
            if exp and exp.Class == unrealsdk.FindClass("MaterialExpressionVectorParameter"):
                parameters.append(exp.ParameterName)
                self.col4_values[exp.ParameterName] = (1.0, 1.0, 1.0, 1.0)

        return sorted(list(set(parameters)))

    @lru_cache(1)
    def _get_scalar_parameters(self, mat: unrealsdk.UObject) -> List[str]:
        parameters: List[str] = []
        for exp in mat.Expressions:
            if exp and exp.Class == unrealsdk.FindClass("MaterialExpressionScalarParameter"):
                parameters.append(exp.ParameterName)
        return sorted(list(set(parameters)))

    @lru_cache(1)
    def search_skins(self, q: str) -> Tuple[List[str], List[unrealsdk.UObject]]:
        mats = unrealsdk.FindAll("MaterialInstanceConstant")
        names = []
        objs = []
        for m in mats:
            m_name = m.PathName(m)
            if q.lower() in m_name.lower():
                names.append(m_name)
                objs.append(m)

        return names, objs

    @lru_cache(1)
    def search_textures(self, q: str) -> Tuple[List[str], List[unrealsdk.UObject]]:
        mats = unrealsdk.FindAll("Texture2D")
        names = []
        objs = []
        for m in mats:
            m_name = m.PathName(m)
            if q.lower() in m_name.lower():
                names.append(m_name)
                objs.append(m)

        return names, objs


instance = MaterialEditor()
RegisterMod(instance)