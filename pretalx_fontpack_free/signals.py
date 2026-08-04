import json
from functools import cache
from pathlib import Path

from django.dispatch import receiver

from pretalx.common.signals import register_fonts

BP = "pretalx_fontpack_free"
CATALOG_PATH = Path(__file__).parent / "fonts.json"


@cache
def load_catalog():
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    for font in catalog.values():
        for value in font.values():
            if isinstance(value, dict):
                for fmt, filename in value.items():
                    value[fmt] = f"{BP}/{filename}"
    return catalog


@receiver(register_fonts, dispatch_uid="fontpack_free_fonts")
def fontpack_free(sender, **kwargs):
    return load_catalog()
