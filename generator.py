import os
from datetime import datetime

# بيانات المقال الجديد
article_title = "أحدث المستجدات والنقاشات في مجموعة المبادرة الوطنية للتنمية الاجتماعية"
article_date = datetime.now().strftime("%Y-%m-%d")
filename = f"article_{int(datetime.now().timestamp())}.html"

# 1. إنشاء صفحة المقال الاحترافية
html_content = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{article_title}</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-50 text-gray-800 font-sans">
    <header class="bg-blue-600 text-white shadow-md">
        <div class="container mx-auto px-4 py-4 flex justify-between items-center">
            <h1 class="text-xl font-bold">دليل المقاول الذكي</h1>
            <a href="index.html" class="bg-white text-blue-600 px-4 py-2 rounded-lg font-semibold hover:bg-blue-50 transition">الرئيسية</a>
        </div>
    </header>
    <main class="container mx-auto px-4 py-8 max-w-3xl">
        <article class="bg-white p-6 md:p-8 rounded-xl shadow-sm">
            <span class="text-sm text-blue-600 font-semibold">{article_date}</span>
            <h2 class="text-2xl md:text-3xl font-bold mt-2 mb-4 text-gray-900">{article_title}</h2>
            <hr class="my-4">
            <div class="space-y-4 text-lg leading-relaxed text-gray-700">
                <p>مرحباً بكم متابعينا الأعزاء في تقريرنا الجديد المستوحى من أبرز النقاشات والتفاعلات داخل مجتمعنا الرقمي الضخم (320 ألف عضو).</p>
                <p>نناقش اليوم أهم الفرص والمستجدات التي تم طرحها وكيف يمكن الاستفادة منها عبر آليات العمل الرقمي والتجارة بالعمولة والترويج الذكي.</p>
                <h3 class="text-xl font-bold text-gray-900 mt-6">نقاط رئيسية تم تداولها:</h3>
                <ul class="list-disc list-inside space-y-2">
                    <li>تحليل اتجاهات السوق والمشاريع المصغرة.</li>
                    <li>طرق استثمار الزيارات الكبيرة لتحقيق عائد مادي مستدام.</li>
                    <li>أهمية البناء التلقائي للمحتوى عبر أدوات الويب الحديثة.</li>
                </ul>
            </div>
        </article>
    </main>
    <footer class="bg-gray-800 text-white text-center py-6 mt-12">
        <p>جميع الحقوق محفوظة &copy; 2026 - دليل المقاول الذكي</p>
    </footer>
</body>
</html>
"""

# حفظ ملف المقال
with open(filename, "w", encoding="utf-8") as f:
    f.write(html_content)

# 2. تحديث الصفحة الرئيسية index.html تلقائياً لتتضمن رابط المقال الجديد
index_content = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>دليل المقاول الذكي - الصفحة الرئيسية</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-50 text-gray-800 font-sans">
    <header class="bg-blue-600 text-white shadow-md">
        <div class="container mx-auto px-4 py-4 flex justify-between items-center">
            <h1 class="text-xl font-bold">دليل المقاول الذكي</h1>
            <span class="text-sm bg-blue-700 px-3 py-1 rounded-full">منصة تفاعلية</span>
        </div>
    </header>
    <main class="container mx-auto px-4 py-8 max-w-4xl">
        <section class="mb-8 bg-blue-50 border border-blue-200 p-6 rounded-xl">
            <h2 class="text-2xl font-bold text-blue-900 mb-2">مرحباً بكم في منصة المحتوى التلقائي</h2>
            <p class="text-blue-700">تتم تغطية وتحليل أبرز تفاعلات مجموعة المبادرة الوطنية للتنمية الاجتماعية (320 ألف عضو) ونشرها بشكل آلي.</p>
        </section>
        <h3 class="text-xl font-bold mb-4 text-gray-900">أحدث المقالات المنشورة:</h3>
        <div class="grid gap-4">
            <div class="bg-white p-5 rounded-xl shadow-sm border border-gray-100 hover:shadow-md transition">
                <span class="text-xs text-blue-600 font-semibold">{article_date}</span>
                <h4 class="text-lg font-bold mt-1 text-gray-900">
                    <a href="{filename}" class="hover:text-blue-600 transition">{article_title}</a>
                </h4>
                <p class="text-gray-600 mt-2 text-sm">تقرير شامل حول أحدث النقاشات والفرص الاستثمارية المصغرة المستخرجة من تفاعلات الأعضاء...</p>
                <a href="{filename}" class="inline-block mt-3 text-blue-600 font-semibold text-sm hover:underline">اقرأ المزيد &larr;</a>
            </div>
        </div>
    </main>
    <footer class="bg-gray-800 text-white text-center py-6 mt-12">
        <p>جميع الحقوق محفوظة &copy; 2026 - دليل المقاول الذكي</p>
    </footer>
</body>
</html>
"""

# حفظ ملف index.html المحدث
with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_content)

print("تم توليد المقال وتحديث الصفحة الرئيسية تلقائياً بنجاح!")