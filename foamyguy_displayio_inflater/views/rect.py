import displayio
from adafruit_display_shapes.rect import Rect

from foamyguy_displayio_inflater.layout_exceptions import MissingTypeError, IncorrectTypeError, MissingRequiredAttributesError, MissingAttributesError
from foamyguy_displayio_inflater.views.view import View

REQUIRED_ATTRIBUTES = ["x", "y", "height", "width"]


class RectView(View):
    def __init__(self, display, layout_json):
        self.json = layout_json
        if "view_type" not in layout_json:
            raise MissingTypeError
        if layout_json["view_type"] != "Rect":
            raise IncorrectTypeError(
                "view_type '{}' does not match Layout Class 'Rect'".format(layout_json["view_type"])
            )
        self._display = display
        if "attributes" in layout_json:
            _missing_attrs = []
            for attribute in REQUIRED_ATTRIBUTES:
                if attribute not in layout_json['attributes']:
                    _missing_attrs.append(attribute)
            if len(_missing_attrs) > 0:
                raise MissingRequiredAttributesError("Missing required attributes: {}".format(_missing_attrs))

            _outline = 0xFFFFFF
            if "outline" in layout_json["attributes"]:
                _outline = int(layout_json["attributes"]["outline"], 16)

            _fill = 0x000000
            if "fill" in layout_json["attributes"]:
                _fill = int(layout_json["attributes"]["fill"], 16)

            _width = 0
            if "width" in layout_json["attributes"]:
                _width = self.keyword_compiler(layout_json["attributes"]["width"])
            self.width = _width

            _height = 0
            if "height" in layout_json["attributes"]:
                _height = self.keyword_compiler(layout_json["attributes"]["height"])
            self.height = _height

            _stroke = 0
            if "stroke" in layout_json["attributes"]:
                _stroke = self.keyword_compiler(layout_json["attributes"]["stroke"])

            _x = 0
            if "x" in layout_json["attributes"]:
                _x = self.keyword_compiler(layout_json["attributes"]["x"], {"WIDTH":_width, "HEIGHT": _height})

            _y = 0
            if "y" in layout_json["attributes"]:
                _y = self.keyword_compiler(layout_json["attributes"]["y"], {"WIDTH":_width, "HEIGHT": _height})

            self.rect = Rect(_x, _y, _width, _height, fill=_fill, outline=_outline, stroke=_stroke)
            self.view = self.rect
        else:
            raise MissingAttributesError()
