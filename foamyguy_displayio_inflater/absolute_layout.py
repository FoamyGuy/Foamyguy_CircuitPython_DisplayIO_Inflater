import json
import displayio
from foamyguy_displayio_inflater.layout_exceptions import MissingTypeError, IncorrectTypeError, MissingSubViewsError
class AbsoluteLayout:
    def __init__(self, display, layout_json):
        self.layout_json_obj = json.loads(layout_json)
        self._view_type_dict = {}
        self._display = display
        self._sub_views = []
        self._sub_views_id_to_index = {}
        if "view_type" not in self.layout_json_obj:
            raise MissingTypeError
        if self.layout_json_obj["view_type"] != "AbsoluteLayout":
            raise IncorrectTypeError(
                "view_type '{}' does not match Layout Class 'AbsoluteLayout'".format(self.layout_json_obj["view_type"])
            )
        if "sub_views" not in self.layout_json_obj:
            raise MissingSubViewsError

        self.view = self._build_group_from_layout_json()

    def sub_view_by_index(self, index):
        return self._sub_views[index]

    def sub_view_by_id(self, searching_id):
        return self.sub_view_by_index(self._sub_views_id_to_index[searching_id])


    def _build_group_from_layout_json(self):

        _imports_needed_dict = {}
        for view in self.layout_json_obj['sub_views']:
            _imports_needed_dict[view['view_type']] = ""
        #print(_imports_needed_dict)
        for view_type in _imports_needed_dict.keys():
            if view_type == "Line":
                from foamyguy_displayio_inflater.views.line import LineView
                self._view_type_dict[view_type] = LineView
            if view_type == "RoundRect":
                from foamyguy_displayio_inflater.views.roundrect import RoundRectView
                self._view_type_dict[view_type] = RoundRectView
            if view_type == "Rect":
                from foamyguy_displayio_inflater.views.rect import RectView
                self._view_type_dict[view_type] = RectView
            if view_type == "Triangle":
                from foamyguy_displayio_inflater.views.triangle import TriangleView
                self._view_type_dict[view_type] = TriangleView
            if view_type == "SparkLine":
                from foamyguy_displayio_inflater.views.sparkline import SparkLineView
                self._view_type_dict[view_type] = SparkLineView
            if view_type == "Button":
                from foamyguy_displayio_inflater.views.button import ButtonView
                self._view_type_dict[view_type] = ButtonView
            if view_type == "Circle":
                from foamyguy_displayio_inflater.views.circle import CircleView
                self._view_type_dict[view_type] = CircleView
            if view_type == "OnDiskBitmap":
                from foamyguy_displayio_inflater.views.on_disk_bitmap import OnDiskBitmapView
                self._view_type_dict[view_type] = OnDiskBitmapView
            if view_type == "Polygon":
                from foamyguy_displayio_inflater.views.polygon import PolygonView
                self._view_type_dict[view_type] = PolygonView
            if view_type == "Image":
                from foamyguy_displayio_inflater.views.image import ImageView
                self._view_type_dict[view_type] = ImageView
            if view_type == "ProgressBar":
                from foamyguy_displayio_inflater.views.progress_bar import ProgressBarView
                self._view_type_dict[view_type] = ProgressBarView
            if view_type == "Label":
                from foamyguy_displayio_inflater.views.label import LabelView
                self._view_type_dict[view_type] = LabelView
            if view_type == "BitmapLabel":
                from foamyguy_displayio_inflater.views.bitmap_label import LabelView
                self._view_type_dict[view_type] = LabelView

        layout_group = displayio.Group()

        for index, view in enumerate(self.layout_json_obj["sub_views"]):
            if "view_type" not in view:
                raise MissingTypeError("missing view_type on: {}".format(view))
            if "id" in view:
                self._sub_views_id_to_index[view["id"]] = index
            if view["view_type"] != "Button":
                view_layout = self._view_type_dict[view["view_type"]](self._display, view)
                self._sub_views.append(view_layout)
                layout_group.append(view_layout.view)
            if view["view_type"] == "Button":
                button_view = self._view_type_dict[view["view_type"]](self._display, view)
                self._sub_views.append(button_view)
                layout_group.append(button_view.view.group)
        return layout_group
