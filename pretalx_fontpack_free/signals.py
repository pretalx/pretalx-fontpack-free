from django.dispatch import receiver

from pretalx.common.signals import register_fonts

BP = "pretalx_fontpack_free"


def _font(subsets, variants):
    result = {}
    for variant_key, weight_id in variants:
        entry = {}
        for fmt in ("truetype", "woff", "woff2"):
            ext = "ttf" if fmt == "truetype" else fmt
            entry[fmt] = f"{BP}/{subsets}-{weight_id}.{ext}"
        result[variant_key] = entry
    return result


def _font_4(subsets):
    return _font(
        subsets,
        [
            ("regular", "regular"),
            ("bold", "700"),
            ("italic", "italic"),
            ("bolditalic", "700italic"),
        ],
    )


def _font_2(subsets):
    return _font(subsets, [("regular", "regular"), ("bold", "700")])


@receiver(register_fonts, dispatch_uid="fontpack_free_fonts")
def fontpack_free(sender, **kwargs):
    return {
        "Noto Sans": {
            **_font_4("noto-sans-v42-cyrillic_cyrillic-ext_greek_greek-ext_latin_latin-ext"),
            "sample": (
                "\u0421\u044a\u0435\u0448\u044c \u0436\u0435 \u0435\u0449\u0451"
                " \u044d\u0442\u0438\u0445 \u043c\u044f\u0433\u043a\u0438\u0445"
                " \u0444\u0440\u0430\u043d\u0446\u0443\u0437\u0441\u043a\u0438\u0445"
                " \u0431\u0443\u043b\u043e\u043a \u0434\u0430 \u0432\u044b\u043f\u0435\u0439"
                " \u0447\u0430\u044e.<br>"
                "\u03a4\u03b1\u03c7\u03af\u03c3\u03c4\u03b7 \u03b1\u03bb\u03ce\u03c0\u03b7\u03be"
                " \u03b2\u03b1\u03c6\u03ae\u03c2 \u03c8\u03b7\u03bc\u03ad\u03bd\u03b7"
                " \u03b3\u03b7, \u03b4\u03c1\u03b1\u03c3\u03ba\u03b5\u03bb\u03af\u03b6\u03b5\u03b9"
                " \u03c5\u03c0\u03ad\u03c1 \u03bd\u03c9\u03b8\u03c1\u03bf\u03cd"
                " \u03ba\u03c5\u03bd\u03cc\u03c2"
            ),
        },
        "Noto Sans Japanese": {
            **_font_2("noto-sans-jp-v56-cyrillic_japanese_latin_latin-ext_vietnamese"),
            "italic": _font_2("noto-sans-jp-v56-cyrillic_japanese_latin_latin-ext_vietnamese")["regular"],
            "bolditalic": _font_2("noto-sans-jp-v56-cyrillic_japanese_latin_latin-ext_vietnamese")["bold"],
            "sample": "\u3042\u306a\u305f\u306b\u4f1a\u3048\u3066\u5149\u6804\u3067\u3059\u3002",
        },
        "Noto Sans Traditional Chinese": {
            **_font_2("noto-sans-tc-v39-chinese-traditional_cyrillic_latin_latin-ext_vietnamese"),
            "italic": _font_2("noto-sans-tc-v39-chinese-traditional_cyrillic_latin_latin-ext_vietnamese")["regular"],
            "bolditalic": _font_2("noto-sans-tc-v39-chinese-traditional_cyrillic_latin_latin-ext_vietnamese")["bold"],
            "sample": "\u6211\u771f\u6b61\u559c\u4f6e\u4f60\u719f\u4f3c",
        },
        "Noto Sans Simplified Chinese": {
            **_font_2("noto-sans-sc-v40-chinese-simplified_cyrillic_latin_latin-ext_vietnamese"),
            "italic": _font_2("noto-sans-sc-v40-chinese-simplified_cyrillic_latin_latin-ext_vietnamese")["regular"],
            "bolditalic": _font_2("noto-sans-sc-v40-chinese-simplified_cyrillic_latin_latin-ext_vietnamese")["bold"],
            "sample": "\u771f\u662f\u96be\u4ee5\u7f6e\u4fe1\uff01",
        },
        "Open Sans": {
            **_font_4("open-sans-v44-cyrillic_cyrillic-ext_greek_greek-ext_latin_latin-ext"),
            "sample": (
                "\u0421\u044a\u0435\u0448\u044c \u0436\u0435 \u0435\u0449\u0451"
                " \u044d\u0442\u0438\u0445 \u043c\u044f\u0433\u043a\u0438\u0445"
                " \u0444\u0440\u0430\u043d\u0446\u0443\u0437\u0441\u043a\u0438\u0445"
                " \u0431\u0443\u043b\u043e\u043a \u0434\u0430 \u0432\u044b\u043f\u0435\u0439"
                " \u0447\u0430\u044e.<br>"
                "\u03a4\u03b1\u03c7\u03af\u03c3\u03c4\u03b7 \u03b1\u03bb\u03ce\u03c0\u03b7\u03be"
                " \u03b2\u03b1\u03c6\u03ae\u03c2 \u03c8\u03b7\u03bc\u03ad\u03bd\u03b7"
                " \u03b3\u03b7, \u03b4\u03c1\u03b1\u03c3\u03ba\u03b5\u03bb\u03af\u03b6\u03b5\u03b9"
                " \u03c5\u03c0\u03ad\u03c1 \u03bd\u03c9\u03b8\u03c1\u03bf\u03cd"
                " \u03ba\u03c5\u03bd\u03cc\u03c2"
            ),
        },
        "Roboto": _font_4("roboto-v51-cyrillic_latin_latin-ext"),
        "Roboto Condensed": _font_4("roboto-condensed-v31-cyrillic_latin_latin-ext"),
        "Noto Serif": {
            **_font_4("noto-serif-v33-cyrillic_latin_latin-ext"),
            "sample": (
                "\u0421\u044a\u0435\u0448\u044c \u0436\u0435 \u0435\u0449\u0451"
                " \u044d\u0442\u0438\u0445 \u043c\u044f\u0433\u043a\u0438\u0445"
                " \u0444\u0440\u0430\u043d\u0446\u0443\u0437\u0441\u043a\u0438\u0445"
                " \u0431\u0443\u043b\u043e\u043a \u0434\u0430 \u0432\u044b\u043f\u0435\u0439"
                " \u0447\u0430\u044e."
            ),
        },
        "Fira Sans": _font_4("fira-sans-v18-cyrillic_latin_latin-ext"),
        "Lato": _font_4("lato-v25-latin_latin-ext"),
        "Oswald": _font_2("oswald-v57-cyrillic_latin_latin-ext"),
        "Montserrat": _font_4("montserrat-v31-cyrillic_latin_latin-ext"),
        "Vollkorn": _font_4("vollkorn-v30-latin_latin-ext"),
        "Poppins": _font_4("poppins-v24-latin_latin-ext"),
        "Almarai": {
            **_font("almarai-v19-arabic", [("regular", "regular"), ("bold", "800")]),
            "sample": "\u0646\u0635 \u062d\u0643\u064a\u0645 \u0644\u0647 \u0633\u0631 \u0642\u0627\u0637\u0639 \u0648\u0630\u0648 \u0634\u0623\u0646 \u0639\u0638\u064a\u0645 \u0645\u0643\u062a\u0648\u0628 \u0639\u0644\u0649 \u062b\u0648\u0628 \u0623\u062e\u0636\u0631 \u0648\u0645\u063a\u0644\u0641 \u0628\u062c\u0644\u062f \u0623\u0632\u0631\u0642",
        },
        "Ubuntu": _font_4("ubuntu-v21-cyrillic_latin_latin-ext"),
        "Space Mono": _font_4("space-mono-v17-latin_latin-ext"),
        "Tajawal": {
            **_font_2("tajawal-v12-arabic_latin"),
            "italic": _font_2("tajawal-v12-arabic_latin")["regular"],
            "bolditalic": _font_2("tajawal-v12-arabic_latin")["bold"],
            "sample": "\u0646\u0635 \u062d\u0643\u064a\u0645 \u0644\u0647 \u0633\u0631 \u0642\u0627\u0637\u0639 \u0648\u0630\u0648 \u0634\u0623\u0646 \u0639\u0638\u064a\u0645 \u0645\u0643\u062a\u0648\u0628 \u0639\u0644\u0649 \u062b\u0648\u0628 \u0623\u062e\u0636\u0631 \u0648\u0645\u063a\u0644\u0641 \u0628\u062c\u0644\u062f \u0623\u0632\u0631\u0642",
        },
        "Baloo Bhaijaan 2": {
            **_font_2("baloo-bhaijaan-2-v21-arabic_latin_latin-ext_vietnamese"),
            "italic": _font_2("baloo-bhaijaan-2-v21-arabic_latin_latin-ext_vietnamese")["regular"],
            "bolditalic": _font_2("baloo-bhaijaan-2-v21-arabic_latin_latin-ext_vietnamese")["bold"],
            "sample": (
                "Do b\u1ea1ch kim r\u1ea5t qu\u00fd n\u00ean s\u1ebd d\u00f9ng"
                " \u0111\u1ec3 l\u1eafp v\u00f4 x\u01b0\u01a1ng<br>"
                "\u0646\u0635 \u062d\u0643\u064a\u0645 \u0644\u0647 \u0633\u0631"
                " \u0642\u0627\u0637\u0639 \u0648\u0630\u0648 \u0634\u0623\u0646"
                " \u0639\u0638\u064a\u0645 \u0645\u0643\u062a\u0648\u0628 \u0639\u0644\u0649"
                " \u062b\u0648\u0628 \u0623\u062e\u0636\u0631 \u0648\u0645\u063a\u0644\u0641"
                " \u0628\u062c\u0644\u062f \u0623\u0632\u0631\u0642"
            ),
        },
        "Source Sans 3": {
            **_font_4("source-sans-3-v19-cyrillic_cyrillic-ext_greek_greek-ext_latin_latin-ext"),
            "sample": (
                "\u0421\u044a\u0435\u0448\u044c \u0436\u0435 \u0435\u0449\u0451"
                " \u044d\u0442\u0438\u0445 \u043c\u044f\u0433\u043a\u0438\u0445"
                " \u0444\u0440\u0430\u043d\u0446\u0443\u0437\u0441\u043a\u0438\u0445"
                " \u0431\u0443\u043b\u043e\u043a \u0434\u0430 \u0432\u044b\u043f\u0435\u0439"
                " \u0447\u0430\u044e.<br>"
                "\u03a4\u03b1\u03c7\u03af\u03c3\u03c4\u03b7 \u03b1\u03bb\u03ce\u03c0\u03b7\u03be"
                " \u03b2\u03b1\u03c6\u03ae\u03c2 \u03c8\u03b7\u03bc\u03ad\u03bd\u03b7"
                " \u03b3\u03b7, \u03b4\u03c1\u03b1\u03c3\u03ba\u03b5\u03bb\u03af\u03b6\u03b5\u03b9"
                " \u03c5\u03c0\u03ad\u03c1 \u03bd\u03c9\u03b8\u03c1\u03bf\u03cd"
                " \u03ba\u03c5\u03bd\u03cc\u03c2"
            ),
        },
        "Inter": {
            **_font_4("inter-v20-cyrillic_cyrillic-ext_greek_greek-ext_latin_latin-ext"),
            "sample": (
                "\u0421\u044a\u0435\u0448\u044c \u0436\u0435 \u0435\u0449\u0451"
                " \u044d\u0442\u0438\u0445 \u043c\u044f\u0433\u043a\u0438\u0445"
                " \u0444\u0440\u0430\u043d\u0446\u0443\u0437\u0441\u043a\u0438\u0445"
                " \u0431\u0443\u043b\u043e\u043a \u0434\u0430 \u0432\u044b\u043f\u0435\u0439"
                " \u0447\u0430\u044e.<br>"
                "\u03a4\u03b1\u03c7\u03af\u03c3\u03c4\u03b7 \u03b1\u03bb\u03ce\u03c0\u03b7\u03be"
                " \u03b2\u03b1\u03c6\u03ae\u03c2 \u03c8\u03b7\u03bc\u03ad\u03bd\u03b7"
                " \u03b3\u03b7, \u03b4\u03c1\u03b1\u03c3\u03ba\u03b5\u03bb\u03af\u03b6\u03b5\u03b9"
                " \u03c5\u03c0\u03ad\u03c1 \u03bd\u03c9\u03b8\u03c1\u03bf\u03cd"
                " \u03ba\u03c5\u03bd\u03cc\u03c2"
            ),
        },
        "Merriweather": {
            **_font_4("merriweather-v33-cyrillic_cyrillic-ext_latin_latin-ext"),
            "sample": (
                "\u0421\u044a\u0435\u0448\u044c \u0436\u0435 \u0435\u0449\u0451"
                " \u044d\u0442\u0438\u0445 \u043c\u044f\u0433\u043a\u0438\u0445"
                " \u0444\u0440\u0430\u043d\u0446\u0443\u0437\u0441\u043a\u0438\u0445"
                " \u0431\u0443\u043b\u043e\u043a \u0434\u0430 \u0432\u044b\u043f\u0435\u0439"
                " \u0447\u0430\u044e."
            ),
        },
        "Noto Sans Korean": {
            **_font_2("noto-sans-kr-v39-korean_latin_latin-ext"),
            "italic": _font_2("noto-sans-kr-v39-korean_latin_latin-ext")["regular"],
            "bolditalic": _font_2("noto-sans-kr-v39-korean_latin_latin-ext")["bold"],
            "sample": "\ub2f9\uc2e0\uc744 \ub9cc\ub098\uc11c \uc601\uad11\uc785\ub2c8\ub2e4.",
        },
        "Noto Sans Devanagari": {
            **_font_2("noto-sans-devanagari-v30-devanagari_latin_latin-ext"),
            "italic": _font_2("noto-sans-devanagari-v30-devanagari_latin_latin-ext")["regular"],
            "bolditalic": _font_2("noto-sans-devanagari-v30-devanagari_latin_latin-ext")["bold"],
            "sample": "\u0906\u092a\u0938\u0947 \u092e\u093f\u0932\u0915\u0930 \u092c\u0939\u0941\u0924 \u0916\u0941\u0936\u0940 \u0939\u0941\u0908\u0964",
        },
        "Noto Sans Hebrew": {
            **_font_2("noto-sans-hebrew-v50-hebrew_latin_latin-ext"),
            "italic": _font_2("noto-sans-hebrew-v50-hebrew_latin_latin-ext")["regular"],
            "bolditalic": _font_2("noto-sans-hebrew-v50-hebrew_latin_latin-ext")["bold"],
            "sample": "\u05e0\u05e2\u05d9\u05dd \u05dc\u05d4\u05db\u05d9\u05e8 \u05d0\u05d5\u05ea\u05da.",
        },
        "Raleway": _font_4("raleway-v37-cyrillic_cyrillic-ext_latin_latin-ext"),
        "Libre Baskerville": {
            **_font(
                "libre-baskerville-v24-latin_latin-ext",
                [("regular", "regular"), ("bold", "700"), ("italic", "italic")],
            ),
            "bolditalic": _font(
                "libre-baskerville-v24-latin_latin-ext",
                [("bold", "700")],
            )["bold"],
        },
    }
