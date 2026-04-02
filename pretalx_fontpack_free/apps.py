from django.apps import AppConfig
from django.utils.translation import gettext_lazy

from . import __version__


class PluginApp(AppConfig):
    name = "pretalx_fontpack_free"
    verbose_name = "pretalx Fontpack Free"

    class PretalxPluginMeta:
        name = gettext_lazy("pretalx Fontpack Free")
        author = "Tobias Kunze"
        description = gettext_lazy("A collection of free fonts for pretalx")
        visible = False
        version = __version__
        category = "FEATURE"

    def ready(self):
        from . import signals  # noqa: PLC0415, F401
