#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["requests", "tqdm"]
# ///
import argparse
import io
import json
import sys
import zipfile
from pathlib import Path
from typing import NamedTuple

import requests
from tqdm import tqdm

API = "https://gwfh.mranftl.com/api/fonts"
CHUNK_SIZE = 64 * 1024
TIMEOUT = 60

PACKAGE_DIR = Path(__file__).resolve().parent.parent / "pretalx_fontpack_free"
FONT_DIR = PACKAGE_DIR / "static" / "pretalx_fontpack_free"
CATALOG_PATH = PACKAGE_DIR / "fonts.json"

FORMATS = {"truetype": "ttf", "woff": "woff", "woff2": "woff2"}
FULL = {
    "regular": "regular",
    "bold": "700",
    "italic": "italic",
    "bolditalic": "700italic",
}
UPRIGHT = {"regular": "regular", "bold": "700"}
UPRIGHT_ALIASES = {"italic": "regular", "bolditalic": "bold"}

CYRILLIC = "Съешь же ещё этих мягких французских булок да выпей чаю."
GREEK = "Ταχίστη αλώπηξ βαφής ψημένη γη, δρασκελίζει υπέρ νωθρού κυνός"
CYRILLIC_GREEK = f"{CYRILLIC}<br>{GREEK}"
ARABIC = "نص حكيم له سر قاطع وذو شأن عظيم مكتوب على ثوب أخضر ومغلف بجلد أزرق"
VIETNAMESE = "Do bạch kim rất quý nên sẽ dùng để lắp vô xương"


class Font(NamedTuple):
    id: str
    name: str
    subsets: tuple
    variants: dict = FULL
    aliases: dict = {}
    sample: str = None


FONTS = [
    Font(
        id="noto-sans",
        name="Noto Sans",
        subsets=(
            "cyrillic",
            "cyrillic-ext",
            "greek",
            "greek-ext",
            "latin",
            "latin-ext",
        ),
        sample=CYRILLIC_GREEK,
    ),
    Font(
        id="noto-sans-jp",
        name="Noto Sans Japanese",
        subsets=("cyrillic", "japanese", "latin", "latin-ext", "vietnamese"),
        variants=UPRIGHT,
        aliases=UPRIGHT_ALIASES,
        sample="あなたに会えて光栄です。",
    ),
    Font(
        id="noto-sans-tc",
        name="Noto Sans Traditional Chinese",
        subsets=("chinese-traditional", "cyrillic", "latin", "latin-ext", "vietnamese"),
        variants=UPRIGHT,
        aliases=UPRIGHT_ALIASES,
        sample="我真歡喜佮你熟似",
    ),
    Font(
        id="noto-sans-sc",
        name="Noto Sans Simplified Chinese",
        subsets=("chinese-simplified", "cyrillic", "latin", "latin-ext", "vietnamese"),
        variants=UPRIGHT,
        aliases=UPRIGHT_ALIASES,
        sample="真是难以置信！",
    ),
    Font(
        id="open-sans",
        name="Open Sans",
        subsets=(
            "cyrillic",
            "cyrillic-ext",
            "greek",
            "greek-ext",
            "latin",
            "latin-ext",
        ),
        sample=CYRILLIC_GREEK,
    ),
    Font(id="roboto", name="Roboto", subsets=("cyrillic", "latin", "latin-ext")),
    Font(
        id="roboto-condensed",
        name="Roboto Condensed",
        subsets=("cyrillic", "latin", "latin-ext"),
    ),
    Font(
        id="noto-serif",
        name="Noto Serif",
        subsets=("cyrillic", "latin", "latin-ext"),
        sample=CYRILLIC,
    ),
    Font(id="fira-sans", name="Fira Sans", subsets=("cyrillic", "latin", "latin-ext")),
    Font(id="lato", name="Lato", subsets=("latin", "latin-ext")),
    Font(
        id="oswald",
        name="Oswald",
        subsets=("cyrillic", "latin", "latin-ext"),
        variants=UPRIGHT,
    ),
    Font(
        id="montserrat", name="Montserrat", subsets=("cyrillic", "latin", "latin-ext")
    ),
    Font(id="vollkorn", name="Vollkorn", subsets=("latin", "latin-ext")),
    Font(id="poppins", name="Poppins", subsets=("latin", "latin-ext")),
    Font(
        id="almarai",
        name="Almarai",
        subsets=("arabic",),
        variants={"regular": "regular", "bold": "800"},
        sample=ARABIC,
    ),
    Font(id="ubuntu", name="Ubuntu", subsets=("cyrillic", "latin", "latin-ext")),
    Font(id="space-mono", name="Space Mono", subsets=("latin", "latin-ext")),
    Font(
        id="tajawal",
        name="Tajawal",
        subsets=("arabic", "latin"),
        variants=UPRIGHT,
        aliases=UPRIGHT_ALIASES,
        sample=ARABIC,
    ),
    Font(
        id="baloo-bhaijaan-2",
        name="Baloo Bhaijaan 2",
        subsets=("arabic", "latin", "latin-ext", "vietnamese"),
        variants=UPRIGHT,
        aliases=UPRIGHT_ALIASES,
        sample=f"{VIETNAMESE}<br>{ARABIC}",
    ),
    Font(
        id="source-sans-3",
        name="Source Sans 3",
        subsets=(
            "cyrillic",
            "cyrillic-ext",
            "greek",
            "greek-ext",
            "latin",
            "latin-ext",
        ),
        sample=CYRILLIC_GREEK,
    ),
    Font(
        id="inter",
        name="Inter",
        subsets=(
            "cyrillic",
            "cyrillic-ext",
            "greek",
            "greek-ext",
            "latin",
            "latin-ext",
        ),
        sample=CYRILLIC_GREEK,
    ),
    Font(
        id="merriweather",
        name="Merriweather",
        subsets=("cyrillic", "cyrillic-ext", "latin", "latin-ext"),
        sample=CYRILLIC,
    ),
    Font(
        id="noto-sans-kr",
        name="Noto Sans Korean",
        subsets=("korean", "latin", "latin-ext"),
        variants=UPRIGHT,
        aliases=UPRIGHT_ALIASES,
        sample="당신을 만나서 영광입니다.",
    ),
    Font(
        id="noto-sans-devanagari",
        name="Noto Sans Devanagari",
        subsets=("devanagari", "latin", "latin-ext"),
        variants=UPRIGHT,
        aliases=UPRIGHT_ALIASES,
        sample="आपसे मिलकर बहुत खुशी हुई।",
    ),
    Font(
        id="noto-sans-hebrew",
        name="Noto Sans Hebrew",
        subsets=("hebrew", "latin", "latin-ext"),
        variants=UPRIGHT,
        aliases=UPRIGHT_ALIASES,
        sample="נעים להכיר אותך.",
    ),
    Font(
        id="raleway",
        name="Raleway",
        subsets=("cyrillic", "cyrillic-ext", "latin", "latin-ext"),
    ),
    Font(
        id="libre-baskerville",
        name="Libre Baskerville",
        subsets=("latin", "latin-ext"),
        variants={"regular": "regular", "bold": "700", "italic": "italic"},
        aliases={"bolditalic": "bold"},
    ),
]


def fetch_metadata(font):
    response = requests.get(
        f"{API}/{font.id}", params={"subsets": ",".join(font.subsets)}, timeout=TIMEOUT
    )
    response.raise_for_status()
    data = response.json()

    missing_subsets = set(font.subsets) - set(data["subsets"])
    if missing_subsets:
        raise ValueError(f"{font.name}: unavailable subsets {sorted(missing_subsets)}")
    available = {variant["id"] for variant in data["variants"]}
    missing_variants = set(font.variants.values()) - available
    if missing_variants:
        raise ValueError(
            f"{font.name}: unavailable variants {sorted(missing_variants)}"
        )
    return data


def build_entry(font, metadata):
    prefix = f"{font.id}-{metadata['version']}-{metadata['storeID']}"
    entry = {
        name: {fmt: f"{prefix}-{variant}.{ext}" for fmt, ext in FORMATS.items()}
        for name, variant in font.variants.items()
    }
    for alias, target in font.aliases.items():
        entry[alias] = entry[target]
    if font.sample:
        entry["sample"] = font.sample
    return entry


def entry_files(entry):
    return {
        file
        for value in entry.values()
        if isinstance(value, dict)
        for file in value.values()
    }


def download(font, files):
    with requests.get(
        f"{API}/{font.id}",
        params={
            "download": "zip",
            "subsets": ",".join(font.subsets),
            "variants": ",".join(font.variants.values()),
            "formats": ",".join(FORMATS.values()),
        },
        timeout=TIMEOUT,
        stream=True,
    ) as response:
        response.raise_for_status()
        archive_data = io.BytesIO()
        # The CJK archives run to tens of megabytes, so show bytes as they arrive.
        with tqdm(
            total=int(response.headers.get("content-length", 0)) or None,
            unit="B",
            unit_scale=True,
            leave=False,
        ) as progress:
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                archive_data.write(chunk)
                progress.update(len(chunk))

    with zipfile.ZipFile(archive_data) as archive:
        missing = files - set(archive.namelist())
        if missing:
            raise ValueError(f"{font.name}: download is missing {sorted(missing)}")
        for name in sorted(files):
            (FONT_DIR / name).write_bytes(archive.read(name))


def update_fonts(*, keep_old=False):
    catalog = {}
    up_to_date = 0
    with tqdm(FONTS, unit="font") as progress:
        for font in progress:
            progress.set_description(font.name)
            entry = build_entry(font, fetch_metadata(font))
            files = entry_files(entry)
            if all((FONT_DIR / name).exists() for name in files):
                up_to_date += 1
            else:
                tqdm.write(f"{font.name}: downloading {len(files)} files")
                download(font, files)
            catalog[font.name] = entry
    print(f"{len(FONTS)} fonts, {up_to_date} already up to date")

    CATALOG_PATH.write_text(
        json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    if not keep_old:
        wanted = {file for entry in catalog.values() for file in entry_files(entry)}
        outdated = sorted(
            path
            for path in FONT_DIR.iterdir()
            if path.suffix.lstrip(".") in FORMATS.values() and path.name not in wanted
        )
        for path in outdated:
            print(f"removing outdated {path.name}")
            path.unlink()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--keep-old",
        action="store_true",
        help="Keep font files that are no longer referenced",
    )
    args = parser.parse_args()

    FONT_DIR.mkdir(parents=True, exist_ok=True)
    try:
        update_fonts(keep_old=args.keep_old)
    except (ValueError, requests.RequestException) as error:
        sys.exit(f"[ERROR] {error}")
