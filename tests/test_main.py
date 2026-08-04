import pytest
from django.contrib.staticfiles import finders

from pretalx.common.fonts import get_fonts


def test_plugin_importable():
    import pretalx_fontpack_free  # noqa: F401, PLC0415


@pytest.mark.django_db
def test_signal_returns_fonts(event):
    fonts = get_fonts(event)

    assert "Noto Sans" in fonts
    assert "Roboto" in fonts
    assert "regular" in fonts["Noto Sans"]
    assert "woff2" in fonts["Noto Sans"]["regular"]


@pytest.mark.django_db
def test_all_fonts_have_regular_variant(event):
    fonts = get_fonts(event)

    for name, data in fonts.items():
        assert "regular" in data, f"{name} is missing regular variant"
        for fmt in ("truetype", "woff2"):
            assert fmt in data["regular"], f"{name} regular is missing {fmt}"


@pytest.mark.django_db
def test_all_font_files_exist(event):
    for name, data in get_fonts(event).items():
        for variant, formats in data.items():
            if not isinstance(formats, dict):
                continue
            for fmt, path in formats.items():
                assert finders.find(path), f"{name} {variant} {fmt}: {path} is missing"


@pytest.mark.django_db
def test_fonts_with_samples(event):
    fonts = get_fonts(event)

    fonts_with_samples = {name for name, data in fonts.items() if "sample" in data}
    assert "Noto Sans" in fonts_with_samples
    assert "Almarai" in fonts_with_samples
