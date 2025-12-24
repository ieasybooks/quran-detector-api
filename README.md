<div align="center">
  <a href="https://pypi.org/project/quran-detector-api" target="_blank"><img src="https://img.shields.io/pypi/v/quran-detector-api?label=PyPI%20Version&color=limegreen" /></a>
  <a href="https://pypi.org/project/quran-detector-api" target="_blank"><img src="https://img.shields.io/pypi/pyversions/quran-detector-api?color=limegreen" /></a>
  <a href="https://pepy.tech/project/quran-detector-api" target="_blank"><img src="https://static.pepy.tech/badge/quran-detector-api" /></a>

  <a href="https://github.com/ieasybooks/quran-detector-api/actions/workflows/kamal-run.yml" target="_blank"><img src="https://github.com/ieasybooks/quran-detector-api/actions/workflows/kamal-run.yml/badge.svg" /></a>
</div>

<div align="center">

  [![ar](https://img.shields.io/badge/lang-ar-brightgreen.svg)](README.md)
  [![en](https://img.shields.io/badge/lang-en-red.svg)](README.en.md)

</div>

<h1 dir="rtl">quran-detector-api</h1>

<p dir="rtl">
خدمة <strong>FastAPI</strong> جاهزة للإنتاج تقوم بتوفير واجهات HTTP لاستخدام مكتبة
<a href="https://github.com/ieasybooks/quran-detector" target="_blank">quran-detector</a>.
</p>

<p dir="rtl">الرابط العام: <a href="https://quran-detector-api.ieasybooks.com/" target="_blank">https://quran-detector-api.ieasybooks.com/</a></p>

<h2 dir="rtl">التوثيق (OpenAPI)</h2>

<ul dir="rtl">
  <li>OpenAPI: <code dir="ltr">/openapi.json</code></li>
  <li>Swagger UI: <code dir="ltr">/docs</code></li>
  <li>ReDoc: <code dir="ltr">/redoc</code></li>
</ul>

<h2 dir="rtl">مميزات الخدمة</h2>

<ul dir="rtl">
  <li>نقطة نهاية لاكتشاف الآيات/المقاطع: <code dir="ltr">POST /v1/detect</code>.</li>
  <li>نقطة نهاية لوسم النص وإرجاعه: <code dir="ltr">POST /v1/annotate</code>.</li>
  <li>نقاط فحص جاهزية وصحة: <code dir="ltr">/v1/healthz</code> و <code dir="ltr">/v1/readyz</code>.</li>
  <li>تحميل محرك الكشف عند الإقلاع (warm startup) لضمان استجابة أسرع.</li>
  <li>حدود واضحة لحجم النص والطلب.</li>
  <li>دعم CORS (اختياري) لاستخدام الخدمة مباشرة من المتصفح.</li>
</ul>

<h2 dir="rtl">متطلبات الاستخدام</h2>

<ul dir="rtl">
  <li>Python بإصدار <strong>3.12</strong> أو أحدث.</li>
  <li>يُفضّل استخدام <code>uv</code> لإدارة الاعتماديات.</li>
  <li>إذا كنت تريد التشغيل محليًا بنفس بيئة المشروع: <code>mise</code> (اختياري).</li>
</ul>

<h2 dir="rtl">التشغيل السريع</h2>

<p dir="rtl">المتطلبات: <code dir="ltr">mise</code> (Python 3.12) و <code dir="ltr">uv</code>.</p>

<pre dir="ltr"><code>cd quran-detector-api
mise trust
mise install
uv sync
uv run quran-detector-api</code></pre>

<p dir="rtl">العنوان الافتراضي: <code dir="ltr">http://127.0.0.1:8000</code></p>

<h2 dir="rtl">الواجهات (API)</h2>

<p dir="rtl">المسار الأساسي: <code dir="ltr">/v1</code></p>

<h3 dir="rtl">Health</h3>

<ul dir="rtl">
  <li><code dir="ltr">GET /v1/healthz</code> → <code dir="ltr">{"status":"ok"}</code> (الخدمة تعمل)</li>
  <li><code dir="ltr">GET /v1/readyz</code> → <code dir="ltr">{"status":"ok"}</code> (المحرك تم تهيئته)</li>
</ul>

<h3 dir="rtl">Detect</h3>

<p dir="rtl"><code dir="ltr">POST /v1/detect</code></p>

<p dir="rtl">نموذج الطلب:</p>

<pre dir="ltr"><code>{
  "text": "string (1..5000 chars)",
  "settings": {
    "find_errors": true,
    "find_missing": true,
    "allowed_error_pct": 0.25,
    "min_match": 3,
    "delimiters": "optional override"
  }
}</code></pre>

<p dir="rtl">نموذج الاستجابة:</p>

<pre dir="ltr"><code>{
  "matches": [
    {
      "surah_name": "الإخلاص",
      "verses": ["قل هو الله احد"],
      "errors": [[]],
      "start_in_text": 0,
      "end_in_text": 4,
      "aya_start": 1,
      "aya_end": 1
    }
  ]
}</code></pre>

<h3 dir="rtl">Annotate</h3>

<p dir="rtl"><code dir="ltr">POST /v1/annotate</code></p>

<p dir="rtl">نموذج الطلب:</p>

<pre dir="ltr"><code>{
  "text": "string (1..5000 chars)",
  "settings": {
    "find_errors": true,
    "find_missing": true,
    "allowed_error_pct": 0.25,
    "min_match": 3,
    "delimiters": "optional override"
  }
}</code></pre>

<p dir="rtl">نموذج الاستجابة:</p>

<pre dir="ltr"><code>{ "annotated_text": "..." }</code></pre>

<h2 dir="rtl">الحدود (Limits)</h2>

<ul dir="rtl">
  <li>أقصى طول نص: <code dir="ltr">5000</code> حرف (مطبق على مستوى API).</li>
  <li>أقصى حجم للطلب: <code dir="ltr">QD_API_MAX_BODY_BYTES</code> (الافتراضي <code dir="ltr">65536</code>).</li>
</ul>

<h2 dir="rtl">الإعدادات (Configuration)</h2>

<p dir="rtl">متغيرات البيئة (اختيارية):</p>

<ul dir="rtl">
  <li><code dir="ltr">QD_API_HOST</code> (default: <code dir="ltr">127.0.0.1</code>)</li>
  <li><code dir="ltr">QD_API_PORT</code> (default: <code dir="ltr">8000</code>)</li>
  <li><code dir="ltr">QD_API_WORKERS</code> (default: <code dir="ltr">1</code>)</li>
  <li><code dir="ltr">QD_API_LOG_LEVEL</code> (default: <code dir="ltr">info</code>)</li>
  <li><code dir="ltr">QD_API_CORS_ORIGINS</code> (default: empty; comma-separated list, or <code dir="ltr">*</code>)</li>
  <li><code dir="ltr">QD_API_ROOT_PATH</code> (default: empty; set behind a proxy path prefix)</li>
  <li><code dir="ltr">QD_API_DOCS_ENABLED</code> (default: <code dir="ltr">true</code>)</li>
  <li><code dir="ltr">QD_API_MAX_TEXT_LENGTH</code> (default/max: <code dir="ltr">5000</code>)</li>
  <li><code dir="ltr">QD_API_MAX_BODY_BYTES</code> (default: <code dir="ltr">65536</code>)</li>
</ul>

<h2 dir="rtl">التطوير</h2>

<h3 dir="rtl">إعادة تشغيل تلقائي (Auto-reload)</h3>

<pre dir="ltr"><code>uv run uvicorn quran_detector_api.main:app --reload</code></pre>

<h2 dir="rtl">التشغيل في الإنتاج (Deployment)</h2>

<h3 dir="rtl">تشغيل Uvicorn بعدة workers</h3>

<pre dir="ltr"><code>uv run uvicorn quran_detector_api.main:app --host 0.0.0.0 --port 8000 --workers 2</code></pre>

<h3 dir="rtl">التشغيل باستخدام Docker</h3>

<p dir="rtl">بناء الصورة:</p>

<pre dir="ltr"><code>docker build -t quran-detector-api .</code></pre>

<p dir="rtl">تشغيل الحاوية:</p>

<pre dir="ltr"><code>docker run --rm -p 8000:8000 quran-detector-api</code></pre>

