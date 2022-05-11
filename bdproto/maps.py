from clld.web.adapters.geojson import GeoJson, get_lonlat
from clld.web.maps import Map, Layer


class InventoryMap(Map):
    def get_options(self):
        return {"icon_size": 20}

    def get_layers(self):
        yield Layer(
            self.ctx.id,
            self.ctx.name,
            GeoJson(self.ctx).render(self.ctx.language, self.req, dump=False),
        )

    def get_default_options(self):
        return {
            "center": list(reversed(get_lonlat(self.ctx.language) or [0, 0])),
            "zoom": 3,
            "no_popup": True,
            "no_link": True,
            "sidebar": True,
        }


def includeme(config):
    config.register_map("contribution", InventoryMap)
