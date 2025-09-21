# from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render
# import easyocr
# from django.core.files.storage import FileSystemStorage

# # إنشاء قارئ EasyOCR
# reader = easyocr.Reader(['ar', 'en'])  # يقرأ النصوص بالعربية والإنجليزية

# def index(request):
#     if request.method == 'POST' and request.FILES['image']:
#         # رفع الصورة
#         uploaded_file = request.FILES['image']
#         fs = FileSystemStorage()
#         filename = fs.save(uploaded_file.name, uploaded_file)
#         file_url = fs.url(filename)

#         # استخراج النص من الصورة
#         result = reader.readtext(fs.url(filename))

#         # دمج النصوص المستخرجة في نص واحد
#         extracted_text = ' '.join([text[1] for text in result])

#         return render(request, 'result.html', {'text': extracted_text, 'file_url': file_url})

#     return render(request, 'index.html')

# from django.shortcuts import render
# import easyocr
# from django.core.files.storage import FileSystemStorage

# # إنشاء قارئ EasyOCR
# reader = easyocr.Reader(['ar', 'en'])  # يقرأ النصوص بالعربية والإنجليزية

# def index(request):
#     if request.method == 'POST' and request.FILES['image']:
#         # رفع الصورة
#         uploaded_file = request.FILES['image']
#         fs = FileSystemStorage()
#         filename = fs.save(uploaded_file.name, uploaded_file)
#         file_url = fs.url(filename)

#         # المسار الفعلي للملف
#         file_path = fs.path(filename)

#         # استخراج النص من الصورة
#         result = reader.readtext(file_path)

#         # دمج النصوص المستخرجة في نص واحد
#         extracted_text = ' '.join([text[1] for text in result])

#         return render(request, 'result.html', {'text': extracted_text, 'file_url': file_url})

#     return render(request, 'index.html')
# from django.shortcuts import render
# import easyocr
# from django.core.files.storage import FileSystemStorage

# # إنشاء قارئ EasyOCR
# reader = easyocr.Reader(['ar', 'en'])  # يقرأ النصوص بالعربية والإنجليزية

# def index(request):
#     extracted_text = ""
#     file_url = None

#     if request.method == 'POST' and request.FILES.get('image'):
#         uploaded_file = request.FILES['image']
#         fs = FileSystemStorage()
#         filename = fs.save(uploaded_file.name, uploaded_file)

#         file_path = fs.path(filename)  # المسار الفعلي للملف
#         file_url = fs.url(filename)    # رابط لعرض الصورة في HTML

#         try:
#             result = reader.readtext(file_path)
#             extracted_text = ' '.join([text[1] for text in result])
#         except Exception as e:
#             extracted_text = f"حدث خطأ أثناء قراءة الصورة: {e}"

#     return render(request, 'result.html', {'text': extracted_text, 'file_url': file_url})

# from django.shortcuts import render
# import easyocr
# from django.core.files.storage import FileSystemStorage

# # إنشاء قارئ EasyOCR

# reader = easyocr.Reader(['ar', 'en'])  # يقرأ النصوص بالعربية والإنجليزية

# def index(request):
#     extracted_text = ""
#     file_url = None
#     error_message = None  # لإظهار أي خطأ

#     if request.method == 'POST' and request.FILES.get('image'):
#         uploaded_file = request.FILES['image']
#         fs = FileSystemStorage()
#         filename = fs.save(uploaded_file.name, uploaded_file)

#         file_path = fs.path(filename)  # المسار الفعلي للملف
#         file_url = fs.url(filename)    # رابط لعرض الصورة في HTML

#         try:
#             result = reader.readtext(file_path)
#             extracted_text = ' '.join([text[1] for text in result])
#         except Exception as e:
#             error_message = f"حدث خطأ أثناء قراءة الصورة: {e}"

#     return render(request, 'result.html', {
#         'text': extracted_text,
#         'file_url': file_url,
#         'error_message': error_message
#     })

# from django.shortcuts import render
# import easyocr
# from django.core.files.storage import FileSystemStorage

# # إنشاء قارئ EasyOCR
# reader = easyocr.Reader(['ar', 'en'])

# def index(request):
#     if request.method == 'POST' and request.FILES.get('image'):
#         uploaded_file = request.FILES['image']
#         fs = FileSystemStorage()
#         filename = fs.save(uploaded_file.name, uploaded_file)
#         file_path = fs.path(filename)
#         file_url = fs.url(filename)

#         error_message = None
#         extracted_text = ""

#         try:
#             result = reader.readtext(file_path)
#             extracted_text = ' '.join([text[1] for text in result])
#         except Exception as e:
#             error_message = f"حدث خطأ أثناء قراءة الصورة: {e}"

#         return render(request, 'result.html', {
#             'text': extracted_text,
#             'file_url': file_url,
#             'error_message': error_message
#         })

#     # إذا كانت الصفحة مفتوحة لأول مرة أو لم يتم رفع صورة
#     return render(request, 'index.html')

# from django.shortcuts import render
# import easyocr
# from django.core.files.storage import FileSystemStorage
# import os

# # إنشاء قارئ EasyOCR
# reader = easyocr.Reader(['ar', 'en'])  # يقرأ النصوص بالعربية والإنجليزية

# # صيغ الصور المسموح بها
# ALLOWED_EXTENSIONS = ['.png', '.jpg', '.jpeg']

# def index(request):
#     extracted_text = ""
#     file_url = None
#     error_message = None

#     if request.method == 'POST' and request.FILES.get('image'):
#         uploaded_file = request.FILES['image']
#         filename = uploaded_file.name
#         ext = os.path.splitext(filename)[1].lower()

#         # التحقق من الصيغة
#         if ext not in ALLOWED_EXTENSIONS:
#             error_message = "صيغة الملف غير مدعومة. استخدم PNG أو JPG أو JPEG."
#             return render(request, 'result.html', {'text': "", 'file_url': None, 'error_message': error_message})

#         # حفظ الملف
#         fs = FileSystemStorage()
#         saved_filename = fs.save(filename, uploaded_file)
#         file_path = fs.path(saved_filename)
#         file_url = fs.url(saved_filename)

#         # التحقق من أن الملف موجود وحجمه > 0
#         if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
#             error_message = "الملف غير صالح أو تالف."
#             return render(request, 'result.html', {'text': "", 'file_url': None, 'error_message': error_message})

#         # قراءة النصوص
#         try:
#             result = reader.readtext(file_path)
#             if not result:
#                 error_message = "لم يتم العثور على نصوص في الصورة."
#             else:
#                 extracted_text = ' '.join([text[1] for text in result])
#         except Exception as e:
#             error_message = f"حدث خطأ أثناء قراءة الصورة: {e}"

#     # إذا لم يتم رفع أي ملف، عرض صفحة الرفع
#     if request.method != 'POST' or not request.FILES.get('image'):
#         return render(request, 'index.html')

#     return render(request, 'result.html', {
#         'text': extracted_text,
#         'file_url': file_url,
#         'error_message': error_message
#     })
from django.shortcuts import render
import easyocr
from django.core.files.storage import FileSystemStorage
import os
import uuid

# إنشاء قارئ EasyOCR
reader = easyocr.Reader(['ar', 'en'])  # يقرأ النصوص بالعربية والإنجليزية

# صيغ الصور المسموح بها
ALLOWED_EXTENSIONS = ['.png', '.jpg', '.jpeg']

def index(request):
    extracted_text = ""
    file_url = None
    error_message = None

    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_file = request.FILES['image']
        ext = os.path.splitext(uploaded_file.name)[1].lower()

        # التحقق من الصيغة
        if ext not in ALLOWED_EXTENSIONS:
            error_message = "صيغة الملف غير مدعومة. استخدم PNG أو JPG أو JPEG."
            return render(request, 'result.html', {'text': "", 'file_url': None, 'error_message': error_message})

        # توليد اسم ملف آمن وفريد لتجنب مشاكل الأحرف والمسارات الطويلة
        safe_filename = f"{uuid.uuid4().hex}{ext}"

        # حفظ الملف
        fs = FileSystemStorage()
        saved_filename = fs.save(safe_filename, uploaded_file)
        file_path = fs.path(saved_filename)
        file_url = fs.url(saved_filename)

        # التحقق من أن الملف موجود وحجمه > 0
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            error_message = "الملف غير صالح أو تالف."
            return render(request, 'result.html', {'text': "", 'file_url': None, 'error_message': error_message})

        # قراءة النصوص
        try:
            result = reader.readtext(file_path)
            if not result:
                error_message = "لم يتم العثور على نصوص في الصورة."
            else:
                extracted_text = ' '.join([text[1] for text in result])
        except Exception as e:
            error_message = f"حدث خطأ أثناء قراءة الصورة: {e}"

    # إذا لم يتم رفع أي ملف، عرض صفحة رفع الصورة
    if request.method != 'POST' or not request.FILES.get('image'):
        return render(request, 'index.html')

    return render(request, 'result.html', {
        'text': extracted_text,
        'file_url': file_url,
        'error_message': error_message
    })
