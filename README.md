<div align="center">

```
 ██████╗ ██████╗  ██████╗     ███████╗██████╗ ██╗   ██╗
██╔═══██╗██╔══██╗██╔════╝     ██╔════╝██╔══██╗██║   ██║
██║   ██║██████╔╝██║  ███╗    ███████╗██████╔╝██║   ██║
██║   ██║██╔══██╗██║   ██║    ╚════██║██╔══██╗╚██╗ ██╔╝
╚██████╔╝██████╔╝╚██████╔╝    ███████║██║  ██║ ╚████╔╝
 ╚═════╝ ╚═════╝  ╚═════╝     ╚══════╝╚═╝  ╚═╝  ╚═══╝
```

**SRV V2.0** — by **OBG STUDIO**

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Discord](https://img.shields.io/badge/Discord-Bot-5865F2?style=for-the-badge&logo=discord)
![AI](https://img.shields.io/badge/AI-GPT--4-ff6b6b?style=for-the-badge&logo=openai)
![Platform](https://img.shields.io/badge/Platform-Termux-black?style=for-the-badge&logo=android)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

## 🇸🇦 عربي

### 📌 ما هي الأداة؟

**OBG SRV** أداة تيرمنال متطورة لبناء وتضبيط سيرفرات Discord بالكامل، تعمل بطريقتين:

- 🤖 **وضع الذكاء الاصطناعي** — اوصف سيرفرك وسيُبنى تلقائياً بكاتكريز ورومات ورتب مخصصة
- ⚡ **الوضع العادي** — هيكل احترافي جاهز ومنظم بالكامل بضغطة واحدة

---

### 🚀 المميزات

| الميزة | الوصف |
|--------|-------|
| 🤖 **AI Setup** | بناء السيرفر تلقائياً بناءً على وصفك عبر GPT-4 |
| ⚡ **Quick Setup** | هيكل احترافي جاهز — كاتكريز + رومات + رتب |
| 🔄 **Multi-Server** | يعمل على عدة سيرفرات دون إعادة التشغيل |
| 🎨 **واجهة ملونة** | شاشة Terminal احترافية مع شريط تقدم |
| 📋 **معاينة** | مشاهدة الهيكل كاملاً قبل التطبيق |
| 🛡️ **تأكيد مزدوج** | حماية من الحذف الخاطئ |

---

### ⚡ التثبيت والتشغيل

> افتح **Termux** وانسخ الأوامر بالترتيب:

```bash
pkg update && pkg upgrade -y
```
```bash
pkg install python git -y
```
```bash
pip install discord.py colorama g4f
```
```bash
git clone https://github.com/Obadagamer/OBG-SETUP-AI-SERVER.git
```
```bash
cd OBG-SETUP-AI-SERVER
```
```bash
python 135.py
```

---

### 🎮 طريقة الاستخدام

**الخطوة 1 — أدخل التوكن**
```
╰─❯ ENTER BOT TOKEN »
```

**الخطوة 2 — اختر السيرفر**
```
┌────────────────────────────────────────────────────┐
│  [0]  My Server  (150 عضو)                         │
│  [1]  Gaming Hub  (300 عضو)                        │
└────────────────────────────────────────────────────┘
```

**الخطوة 3 — اختر الوضع**
```
╔══════════════════════════════════════════════════════╗
║   [1]  🤖 تعديل بالذكاء الاصطناعي                  ║
║        اوصف السيرفر وسيُبنى تلقائياً               ║
║                                                      ║
║   [2]  ⚡ تعديل عادي                               ║
║        هيكل احترافي جاهز ومنظم                    ║
╚══════════════════════════════════════════════════════╝
```

**الوضع 🤖 AI — مثال:**
```
╰─❯ اوصف السيرفر » سيرفر ألعاب عربي مع قسم دعم وموسيقى
⏳  الذكاء الاصطناعي يبني هيكلك...
✔  تم توليد الهيكل: سيرفر الألعاب العربي
```

**الخطوة 4 — معاينة ثم تأكيد**
```
╰─❯ اكتب CONFIRM للمتابعة »
```

---

### 🔑 كيف أحصل على توكن البوت؟ (من الصفر)

**الخطوة 1 — افتح بوابة المطورين**
- اذهب إلى [discord.com/developers/applications](https://discord.com/developers/applications)
- سجّل الدخول بحسابك على Discord

**الخطوة 2 — أنشئ تطبيقاً جديداً**
- اضغط على زر **New Application** في الزاوية اليمنى العليا
- اكتب اسم البوت ثم اضغط **Create**

**الخطوة 3 — اذهب إلى قسم البوت**
- من القائمة اليسرى اضغط على **Bot**
- اضغط **Add Bot** ثم أكّد بـ **Yes, do it!**

**الخطوة 4 — فعّل الصلاحيات**
- تحت قسم **Privileged Gateway Intents** فعّل الثلاثة:
  - ✅ `PRESENCE INTENT`
  - ✅ `SERVER MEMBERS INTENT`
  - ✅ `MESSAGE CONTENT INTENT`
- اضغط **Save Changes**

**الخطوة 5 — انسخ التوكن**
- اضغط **Reset Token** ثم أكّد
- اضغط **Copy** وانسخ التوكن

**الخطوة 6 — أضف البوت للسيرفر**
- من القائمة اليسرى اضغط **OAuth2**
- اضغط على **OAuth2 URL Generator**
- انزل للأسفل وستجد قسم **Scopes** — ضع ✅ على **bot**
- بعدها سيظهر قسم **Bot Permissions** تحته — اختر الصلاحيات اللي تريدها
- انزل للأسفل وانسخ الرابط الظاهر في **Generated URL**
- افتح الرابط في المتصفح واختر السيرفر اللي تبي تضيف البوت فيه
- اضغط **Authorize** وأكمل التحقق

**الخطوة 7 — شغّل الأداة**
- الصق التوكن عند مطالبة الأداة به

> ⚠️ **تحذير:** لا تشارك توكن البوت مع أحد أبداً ولا ترفعه على GitHub

---

### 📋 المتطلبات

| المكتبة | الإصدار | الوظيفة |
|---------|---------|---------|
| `discord.py` | آخر إصدار | التواصل مع Discord API |
| `colorama` | آخر إصدار | الألوان في Terminal |
| `g4f` | آخر إصدار | الذكاء الاصطناعي GPT-4 |
| `python` | 3.8+ | لغة البرمجة |

---

---

## 🌐 English

### 📌 What is this tool?

**OBG SRV** is an advanced terminal tool for building and configuring Discord servers completely, operating in two modes:

- 🤖 **AI Mode** — Describe your server and it gets built automatically with custom categories, channels, and roles
- ⚡ **Quick Mode** — A ready-made professional structure built with one confirmation

---

### 🚀 Features

| Feature | Description |
|---------|-------------|
| 🤖 **AI Setup** | Auto-build server structure using GPT-4 based on your description |
| ⚡ **Quick Setup** | Professional ready-made structure — categories + channels + roles |
| 🔄 **Multi-Server** | Works on multiple servers without restarting |
| 🎨 **Colored UI** | Professional terminal interface with progress bar |
| 📋 **Preview** | View the full structure before applying |
| 🛡️ **Double Confirm** | Protection against accidental deletion |

---

### ⚡ Installation & Launch

> Open **Termux** and run these commands in order:

```bash
pkg update && pkg upgrade -y
```
```bash
pkg install python git -y
```
```bash
pip install discord.py colorama g4f
```
```bash
git clone https://github.com/Obadagamer/OBG-SETUP-AI-SERVER.git
```
```bash
cd OBG-SETUP-AI-SERVER
```
```bash
python 135.py
```

---

### 🔑 How to get your Bot Token? (Step by Step)

**Step 1 — Open the Developer Portal**
- Go to [discord.com/developers/applications](https://discord.com/developers/applications)
- Log in with your Discord account

**Step 2 — Create a New Application**
- Click **New Application** in the top right corner
- Enter a name for your bot and click **Create**

**Step 3 — Go to the Bot Section**
- Click **Bot** from the left sidebar
- Click **Add Bot** then confirm with **Yes, do it!**

**Step 4 — Enable Privileged Intents**
- Under **Privileged Gateway Intents**, enable all three:
  - ✅ `PRESENCE INTENT`
  - ✅ `SERVER MEMBERS INTENT`
  - ✅ `MESSAGE CONTENT INTENT`
- Click **Save Changes**

**Step 5 — Copy the Token**
- Click **Reset Token** and confirm
- Click **Copy** to copy your bot token

**Step 6 — Add the Bot to your Server**
- From the left sidebar click **OAuth2**
- Click **OAuth2 URL Generator**
- Scroll down to the **Scopes** section — check ✅ **bot**
- A new section **Bot Permissions** will appear below — select the permissions you need
- Scroll down and copy the link shown in **Generated URL**
- Open the link in your browser and choose the server you want to add the bot to
- Click **Authorize** and complete the verification

**Step 7 — Run the Tool**
- Paste the token when the tool prompts you for it

> ⚠️ **Warning:** Never share your bot token with anyone or upload it to GitHub

---

### 📋 Requirements

| Library | Version | Purpose |
|---------|---------|---------|
| `discord.py` | Latest | Discord API communication |
| `colorama` | Latest | Terminal colors |
| `g4f` | Latest | GPT-4 AI integration |
| `python` | 3.8+ | Programming language |

---

<div align="center">

---

### 📲 تواصل معنا | Connect with us

[![TikTok](https://img.shields.io/badge/TikTok-@om0g0-ff0050?style=for-the-badge&logo=tiktok)](https://www.tiktok.com/@om0g0)
[![YouTube](https://img.shields.io/badge/YouTube-@obadagameing-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@obadagameing)
[![Discord](https://img.shields.io/badge/Discord-Server-5865F2?style=for-the-badge&logo=discord)](https://discord.gg/sxUGzPtv)

---

**© 2025 OBG STUDIO — All Rights Reserved**

*Made with ❤️ by OBG STUDIO*

</div>

