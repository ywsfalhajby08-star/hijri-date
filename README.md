# hijri-date

<div dir="rtl">

## بالعربية

أداة Python بسيطة لتحويل التاريخ بين **التقويم الهجري (أم القرى)** و**التقويم الميلادي**، مبنية على مكتبة [hijridate](https://pypi.org/project/hijridate/).

### التثبيت

</div>

```bash
pip install git+https://github.com/ywsfalhajby08-star/hijri-date.git
```

<div dir="rtl">

### الاستخدام من الطرفية

</div>

```bash
hijri-date 2026-11-02          # 22 جمادى الأولى 1448 هـ
hijri-date                     # تاريخ اليوم بالهجري
hijri-date --reverse 1448-05-22  # 2026-11-02
```

<div dir="rtl">

### الاستخدام في Python

</div>

```python
from hijri_date import to_hijri, to_gregorian, today_hijri, format_hijri

to_hijri("2026-11-02")        # (1448, 5, 22)
to_gregorian(1448, 5, 22)     # datetime.date(2026, 11, 2)
today_hijri()                 # (السنة، الشهر، اليوم) لتاريخ اليوم
format_hijri(1448, 5, 22)     # '22 جمادى الأولى 1448 هـ'
```

<div dir="rtl">

### صفحة الويب

الملف `index.html` صفحة عربية مستقلة تعمل مباشرة على GitHub Pages دون أي خادم، وتستخدم تقويم أم القرى المدمج في المتصفح.
لتفعيلها: **Settings ← Pages ← Deploy from a branch ← `main` / `(root)`**.

### الاختبارات

</div>

```bash
pip install -e ".[test]"
python -m pytest
```

<div dir="rtl">

### الرخصة

MIT © ywsfalhajby08-star

</div>

---

## English

A small Python tool to convert dates between the **Hijri (Umm al-Qura)** and **Gregorian** calendars, built on [hijridate](https://pypi.org/project/hijridate/).

### Install

```bash
pip install git+https://github.com/ywsfalhajby08-star/hijri-date.git
```

### Command line

```bash
hijri-date 2026-11-02            # 22 جمادى الأولى 1448 هـ
hijri-date                       # today's Hijri date
hijri-date --reverse 1448-05-22  # 2026-11-02
```

### Python API

| Function | Description |
|---|---|
| `to_hijri(date_or_iso_str)` | Gregorian → Hijri `(year, month, day)` |
| `to_gregorian(year, month, day)` | Hijri → `datetime.date` |
| `today_hijri()` | Today's Hijri `(year, month, day)` |
| `format_hijri(year, month, day)` | Hijri date with the Arabic month name |

Supported range is the Umm al-Qura range of `hijridate`: 1343–1500 AH (1924–2077 CE).

### Web page

`index.html` is a self-contained Arabic page that runs on GitHub Pages with no backend, using the browser's built-in Umm al-Qura calendar (`Intl`). Enable it via **Settings → Pages → Deploy from a branch → `main` / `(root)`**.

### Tests

```bash
pip install -e ".[test]"
python -m pytest
```

### License

MIT © ywsfalhajby08-star
