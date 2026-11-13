# تشغيل AP محليًا أولًا

## الخيار 1: Python مباشرة

```bash
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
pip install -r backend/requirements.txt
uvicorn app.main:app --app-dir backend --reload --host 127.0.0.1 --port 8000
```

- API health: http://127.0.0.1:8000/api/health
- Readiness: http://127.0.0.1:8000/api/readiness
- Swagger: http://127.0.0.1:8000/docs

## الخيار 2: Docker Compose

```bash
cp .env.example .env
docker compose up --build
```

الخدمة مربوطة على `127.0.0.1` فقط وليست مكشوفة للشبكة. لا توجد مفاتيح تداول أو تنفيذ أوامر في هذه المرحلة. `LIVE` معطل دائمًا في هذا الهيكل.

## مبدأ التطوير

- Local-first: التطوير والاختبارات على الجهاز، والخادم السحابي خيار نشر لاحق فقط.
- واجهة الويب ثابتة في `web/`، والـ API في `backend/`.
- لا تضع API keys في ملفات المشروع أو Git. ستضاف خزنة أسرار مشفرة ومصادقة قبل أي تكامل تداول.
- لا تستخدم بيانات الواجهة التجريبية لاتخاذ قرارات تداول.
