# Algotic Economic Data Crawler

این پروژه یک وب‌اسکرپر پایتونی است که داده‌های تقویم اقتصادی را از [algoticlab.com/calendar.html](https://algoticlab.com/calendar.html) با استفاده از Selenium و BeautifulSoup استخراج می‌کند.

## امکانات
- استخراج داده‌های جدول با اهمیت خبر (RED, Orange, Yellow, Holiday)
- خروجی در سه فرمت: CSV، JSON، Markdown
- کاملاً خودکار و آماده برای پایپ‌لاین‌های داده و هوش مصنوعی

## نحوه اجرا (نسخه لوکال)
1. نصب پیش‌نیازها:
    ```
    pip install -r requirements.txt
    ```
2. مطمئن شوید Chrome و ChromeDriver نصب است.
3. اجرای اسکریپت:
    ```
    python algoticEconomicData.py
    ```

## فایل‌های خروجی
- `economic_calendar.csv` : داده‌های جدول به فرمت CSV
- `economic_calendar.json` : داده‌ها به فرمت JSON
- `economic_calendar.md` : داده‌ها به صورت جدول Markdown

## نکات
- اسکریپت به صورت لوکال اجرا می‌شود و قابل تطبیق برای سرور/کلود نیز هست.
- برای خصوصی کردن مخزن، visibility را در گیت‌هاب روی "Private" قرار دهید.
- خروجی نسخه لوکال با نسخه Colab (در صورت نیاز) یکسان خواهد بود.

---

## License
This project is for educational and research purposes. 