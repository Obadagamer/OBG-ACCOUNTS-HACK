import discord
import asyncio
import os
import sys
import time
import json
from colorama import Fore, init
from g4f.client import Client

init(autoreset=True)
G, R, C, Y, M, W, B = Fore.GREEN, Fore.RED, Fore.CYAN, Fore.YELLOW, Fore.MAGENTA, Fore.WHITE, Fore.BLUE

client_ai = Client()

# ══════════════════════════════════════════════════════════════
#                   هيكل السيرفر الافتراضي
# ══════════════════════════════════════════════════════════════

DEFAULT_STRUCTURE = {
    "server_name": "OBG SERVER",
    "categories": [
        {
            "name": "🔒 ┃ النظام",
            "text_channels": [
                {"name": "📋┃القوانين",     "topic": "قوانين السيرفر — اقرأ قبل البدء"},
                {"name": "📢┃الإعلانات",    "topic": "إعلانات رسمية فقط"},
                {"name": "🎉┃الترحيب",      "topic": "مرحباً بالأعضاء الجدد"},
                {"name": "👋┃مغادرة",       "topic": "وداعاً للمغادرين"},
                {"name": "🔗┃روابط-مهمة",   "topic": "روابط مهمة للسيرفر"},
            ],
            "voice_channels": []
        },
        {
            "name": "💬 ┃ العام",
            "text_channels": [
                {"name": "💬┃عام",          "topic": "الدردشة العامة"},
                {"name": "🤝┃تعارف",        "topic": "عرّف عن نفسك"},
                {"name": "😂┃ميمز-وصور",    "topic": "ميمز وصور مضحكة"},
                {"name": "🔗┃روابط",        "topic": "مشاركة الروابط"},
                {"name": "🤖┃بوتات",        "topic": "أوامر البوتات هنا"},
            ],
            "voice_channels": [
                {"name": "🔊 عام 1"},
                {"name": "🔊 عام 2"},
                {"name": "🎵 موسيقى"},
                {"name": "🚀 AFK"},
            ]
        },
        {
            "name": "🎮 ┃ الألعاب",
            "text_channels": [
                {"name": "🎮┃عام-الألعاب",  "topic": "نقاشات الألعاب"},
                {"name": "🏆┃مباريات",      "topic": "تنظيم المباريات"},
                {"name": "🔎┃طلب-ضم",       "topic": "ابحث عن فريق"},
                {"name": "📊┃إحصائيات",     "topic": "إحصائيات اللاعبين"},
            ],
            "voice_channels": [
                {"name": "🎮 الألعاب 1"},
                {"name": "🎮 الألعاب 2"},
                {"name": "🏆 المباريات"},
            ]
        },
        {
            "name": "🛠️ ┃ الدعم",
            "text_channels": [
                {"name": "❓┃مساعدة",       "topic": "اطرح أسئلتك"},
                {"name": "🐛┃بلاغات",       "topic": "أبلغ عن المشاكل"},
                {"name": "💡┃اقتراحات",     "topic": "اقتراحاتك لتطوير السيرفر"},
                {"name": "📩┃تذاكر",        "topic": "تواصل مع الإدارة"},
            ],
            "voice_channels": [
                {"name": "📞 الدعم"},
            ]
        },
        {
            "name": "🎵 ┃ الموسيقى",
            "text_channels": [
                {"name": "🎵┃طلبات",        "topic": "اطلب الأغاني"},
                {"name": "📋┃قائمة-تشغيل",  "topic": "قوائم التشغيل"},
            ],
            "voice_channels": [
                {"name": "🎵 الموسيقى 1"},
                {"name": "🎵 الموسيقى 2"},
            ]
        },
        {
            "name": "👑 ┃ الإدارة",
            "text_channels": [
                {"name": "⚙️┃إدارة-عامة",   "topic": "قناة الإدارة"},
                {"name": "📝┃سجل-عقوبات",   "topic": "سجل البانات"},
                {"name": "🔔┃تنبيهات",      "topic": "تنبيهات النظام"},
            ],
            "voice_channels": [
                {"name": "👑 اجتماع الإدارة"},
            ]
        },
    ],
    "roles": [
        {"name": "👑 المالك",       "color": "FFD700", "hoist": True,  "mentionable": True},
        {"name": "🛡️ المدير",       "color": "FF4500", "hoist": True,  "mentionable": True},
        {"name": "⚔️ المشرف",       "color": "FF6347", "hoist": True,  "mentionable": True},
        {"name": "🔨 المودريتور",   "color": "FF8C00", "hoist": True,  "mentionable": True},
        {"name": "💎 VIP",          "color": "1ABC9C", "hoist": True,  "mentionable": True},
        {"name": "🌟 مميز",         "color": "9B59B6", "hoist": True,  "mentionable": False},
        {"name": "🎖️ عضو نشيط",    "color": "3498DB", "hoist": True,  "mentionable": False},
        {"name": "✅ عضو موثق",     "color": "2ECC71", "hoist": False, "mentionable": False},
        {"name": "🆕 عضو جديد",     "color": "95A5A6", "hoist": False, "mentionable": False},
        {"name": "🤖 بوت",          "color": "7289DA", "hoist": True,  "mentionable": False},
    ]
}

# ══════════════════════════════════════════════════════════════
#                   الذكاء الاصطناعي
# ══════════════════════════════════════════════════════════════

def ask_ai(description: str) -> dict:
    prompt = f"""
أنت خبير متخصص في تصميم سيرفرات Discord احترافية.
المستخدم يريد سيرفر بهذا الوصف: "{description}"

أنشئ هيكل سيرفر Discord متكامل واحترافي يناسب هذا الوصف تماماً.
يجب أن يكون الهيكل شاملاً مع كاتكريز كثيرة وقنوات نصية وصوتية وافرة ورتب متدرجة.
استخدم إيموجيز مناسبة لكل عنصر.

أرجع JSON فقط بهذا الشكل الدقيق — بدون أي نص قبله أو بعده:
{{
  "server_name": "اسم مناسب للسيرفر",
  "categories": [
    {{
      "name": "إيموجي ┃ اسم الكاتكري",
      "text_channels": [
        {{"name": "إيموجي┃اسم-القناة", "topic": "وصف القناة"}}
      ],
      "voice_channels": [
        {{"name": "إيموجي اسم الصوتي"}}
      ]
    }}
  ],
  "roles": [
    {{"name": "إيموجي اسم الرتبة", "color": "RRGGBB", "hoist": true, "mentionable": true}}
  ]
}}
"""
    response = client_ai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "أنت خبير Discord servers. أجب بـ JSON نظيف فقط بدون markdown أو نص إضافي."},
            {"role": "user", "content": prompt}
        ]
    )
    raw = response.choices[0].message.content.strip()
    # تنظيف markdown
    if "```" in raw:
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    return json.loads(raw.strip())

# ══════════════════════════════════════════════════════════════
#                   دوال المساعدة — UI
# ══════════════════════════════════════════════════════════════

def draw_banner():
    os.system('clear')
    print(f"""
{C}    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
{C}    ┃ {M} ██████╗ ██████╗  ██████╗     ██████╗ ███╗   ███╗{C}  ┃
{C}    ┃ {M}██╔═══██╗██╔══██╗██╔════╝     ██╔══██╗████╗ ████║{C}  ┃
{C}    ┃ {M}██║   ██║██████╔╝██║  ███╗    ██║  ██║██╔████╔██║{C}  ┃
{C}    ┃ {M}██║   ██║██╔══██╗██║   ██║    ██║  ██║██║╚██╔╝██║{C}  ┃
{C}    ┃ {M}╚██████╔╝██████╔╝╚██████╔╝    ██████╔╝██║ ╚═╝ ██║{C}  ┃
{C}    ┃ {M} ╚═════╝ ╚═════╝  ╚═════╝     ╚═════╝ ╚═╝     ╚═╝{C}  ┃
{C}    ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
{C}    ┃ {W}MODULE: {G}OBG SRV V2.0             {R}BY: {G}OBG STUDIO {C}┃
{C}    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    """)

def section(title):
    print(f"\n  {M}╔{'═'*50}╗")
    print(f"  {M}║  {Y}{title.ljust(48)}{M}║")
    print(f"  {M}╚{'═'*50}╝")

def log_ok(text):
    print(f"  {C}│  {G}✔  {W}{text}")
    time.sleep(0.02)

def log_err(text):
    print(f"  {C}│  {R}✘  {W}{text}")

def progress(cur, total, label):
    bar_len = 28
    filled  = int(bar_len * cur / max(total, 1))
    bar     = '█' * filled + '░' * (bar_len - filled)
    pct     = int(100 * cur / max(total, 1))
    print(f"\r  {C}│  {M}[{G}{bar}{M}] {Y}{pct}%  {W}{label[:28].ljust(28)}", end='', flush=True)

def show_preview(structure):
    cats  = structure.get("categories", [])
    roles = structure.get("roles", [])
    total_txt   = sum(len(c.get("text_channels",  [])) for c in cats)
    total_voice = sum(len(c.get("voice_channels", [])) for c in cats)

    print(f"\n  {C}╔{'═'*50}╗")
    print(f"  {C}║  {Y}📋 معاينة الهيكل{' '*33}{C}║")
    print(f"  {C}╠{'═'*50}╣")
    print(f"  {C}║  {W}اسم السيرفر : {G}{structure.get('server_name','---')[:30].ljust(30)}{C}  ║")
    print(f"  {C}║  {W}كاتكريز    : {Y}{str(len(cats)).ljust(36)}{C}║")
    print(f"  {C}║  {W}نصية       : {Y}{str(total_txt).ljust(36)}{C}║")
    print(f"  {C}║  {W}صوتية      : {Y}{str(total_voice).ljust(36)}{C}║")
    print(f"  {C}║  {W}رتب        : {Y}{str(len(roles)).ljust(36)}{C}║")
    print(f"  {C}╚{'═'*50}╝")

    print(f"\n  {Y}┌─ هيكل الكاتكريز والرومات:")
    for cat in cats:
        print(f"  {Y}│")
        print(f"  {Y}│  {M}📁 {cat['name']}")
        for ch in cat.get("text_channels", []):
            print(f"  {Y}│     {C}💬 {ch['name']}")
        for ch in cat.get("voice_channels", []):
            print(f"  {Y}│     {G}🔊 {ch['name']}")
    print(f"  {Y}│")
    print(f"  {Y}└{'─'*44}")

    print(f"\n  {Y}┌─ الرتب:")
    for r in roles:
        print(f"  {Y}│  {M}🏷️  {r['name']}")
    print(f"  {Y}└{'─'*44}\n")

# ══════════════════════════════════════════════════════════════
#                   تطبيق الهيكل على السيرفر
# ══════════════════════════════════════════════════════════════

async def apply_structure(guild, structure):
    draw_banner()

    # ── حذف القديم ──
    section("الخطوة 1/3 ┃ حذف الهيكل القديم")
    old = list(guild.channels)
    for i, ch in enumerate(old):
        try:
            await ch.delete()
            progress(i+1, len(old), f"حذف: {ch.name}")
        except:
            log_err(f"فشل حذف {ch.name}")
        await asyncio.sleep(0.4)
    print()
    log_ok(f"تم حذف {len(old)} عنصر")

    # ── إنشاء الرتب ──
    section("الخطوة 2/3 ┃ إنشاء الرتب")
    roles = structure.get("roles", [])
    created_roles = 0
    for i, rd in enumerate(roles):
        try:
            hex_c = rd.get("color", "808080").replace("#","")
            await guild.create_role(
                name=rd["name"],
                color=discord.Color(int(hex_c, 16)),
                hoist=rd.get("hoist", False),
                mentionable=rd.get("mentionable", False)
            )
            created_roles += 1
            progress(i+1, len(roles), f"رتبة: {rd['name']}")
        except Exception as e:
            log_err(f"فشل {rd['name']}: {e}")
        await asyncio.sleep(0.5)
    print()
    log_ok(f"تم إنشاء {created_roles} رتبة")

    # ── إنشاء الكاتكريز والرومات ──
    section("الخطوة 3/3 ┃ بناء الكاتكريز والرومات")
    cats = structure.get("categories", [])
    total_txt, total_voice = 0, 0

    for i, cat_data in enumerate(cats):
        try:
            category = await guild.create_category(cat_data["name"])
            progress(i+1, len(cats), f"📁 {cat_data['name']}")
        except Exception as e:
            log_err(f"فشل كاتكري {cat_data['name']}: {e}")
            await asyncio.sleep(0.5)
            continue

        for ch in cat_data.get("text_channels", []):
            try:
                await guild.create_text_channel(
                    name=ch["name"],
                    category=category,
                    topic=ch.get("topic", "")
                )
                total_txt += 1
                progress(i+1, len(cats), f"💬 {ch['name']}")
            except Exception as e:
                log_err(f"فشل {ch['name']}: {e}")
            await asyncio.sleep(0.35)

        for ch in cat_data.get("voice_channels", []):
            try:
                await guild.create_voice_channel(
                    name=ch["name"],
                    category=category
                )
                total_voice += 1
                progress(i+1, len(cats), f"🔊 {ch['name']}")
            except Exception as e:
                log_err(f"فشل {ch['name']}: {e}")
            await asyncio.sleep(0.35)

    print()
    log_ok(f"تم بناء {len(cats)} كاتكري")

    # ── ملخص ──
    srv = structure.get("server_name", guild.name)
    print(f"""
  {G}╔══════════════════════════════════════════════════════╗
  {G}║  {Y}✅  اكتمل التضبيط بنجاح!                          {G}║
  {G}╠══════════════════════════════════════════════════════╣
  {G}║  {C}السيرفر  : {W}{guild.name[:36].ljust(36)}{G}  ║
  {G}║  {C}كاتكريز : {Y}{str(len(cats)).ljust(38)}{G}  ║
  {G}║  {C}نصية    : {Y}{str(total_txt).ljust(38)}{G}  ║
  {G}║  {C}صوتية   : {Y}{str(total_voice).ljust(38)}{G}  ║
  {G}║  {C}رتب     : {Y}{str(created_roles).ljust(38)}{G}  ║
  {G}╚══════════════════════════════════════════════════════╝
    """)
    print(f"  {M}◆  {W}OBG STUDIO — SERVER BUILDER COMPLETE\n")

# ══════════════════════════════════════════════════════════════
#                   البوت الرئيسي
# ══════════════════════════════════════════════════════════════

class OBG_Builder(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        draw_banner()
        print(f"  {G}✔  تم تسجيل الدخول كـ {G}{self.user}\n")
        await self.select_guild()

    async def select_guild(self):
        guilds = list(self.guilds)
        if not guilds:
            print(f"  {R}✘  البوت ليس في أي سيرفر!")
            await self.close()
            return

        print(f"  {C}┌{'─'*52}┐")
        print(f"  {C}│  {Y}{'السيرفرات المتاحة'.ljust(50)}{C}│")
        print(f"  {C}├{'─'*52}┤")
        for i, g in enumerate(guilds):
            line = f"[{i}]  {g.name}  ({g.member_count} عضو)"
            print(f"  {C}│  {Y}{line.ljust(50)}{C}│")
        print(f"  {C}└{'─'*52}┘\n")

        choice = input(f"  {M}╰─❯ {W}اختر رقم السيرفر {C}» {G}").strip()
        try:
            guild = guilds[int(choice)]
        except:
            print(f"  {R}✘  رقم خاطئ")
            await self.select_guild()
            return

        await self.select_mode(guild)

    async def select_mode(self, guild):
        draw_banner()
        print(f"""
  {C}╔══════════════════════════════════════════════════════╗
  {C}║  {Y}السيرفر المختار: {G}{guild.name.ljust(36)}{C}║
  {C}╠══════════════════════════════════════════════════════╣
  {C}║                                                      ║
  {C}║   {M}[1]  {Y}🤖 تعديل بالذكاء الاصطناعي                  {C}║
  {C}║        {W}اوصف السيرفر وسيُبنى تلقائياً               {C}║
  {C}║                                                      ║
  {C}║   {M}[2]  {Y}⚡ تعديل عادي                               {C}║
  {C}║        {W}هيكل احترافي جاهز ومنظم                    {C}║
  {C}║                                                      ║
  {C}║   {R}[0]  {W}رجوع                                        {C}║
  {C}║                                                      ║
  {C}╚══════════════════════════════════════════════════════╝
        """)

        choice = input(f"  {M}╰─❯ {W}اختر الوضع {C}» {G}").strip()

        if choice == "1":
            await self.mode_ai(guild)
        elif choice == "2":
            await self.mode_manual(guild)
        elif choice == "0":
            await self.select_guild()
        else:
            await self.select_mode(guild)

    # ── الوضع الأول: ذكاء اصطناعي ──
    async def mode_ai(self, guild):
        draw_banner()
        print(f"  {M}╔{'═'*50}╗")
        print(f"  {M}║  {Y}🤖 وضع الذكاء الاصطناعي{' '*27}{M}║")
        print(f"  {M}╠{'═'*50}╣")
        print(f"  {M}║  {W}مثال: سيرفر ألعاب عربي مع قسم دعم{' '*14}{M}║")
        print(f"  {M}║  {W}مثال: anime community server{' '*22}{M}║")
        print(f"  {M}╚{'═'*50}╝\n")

        desc = input(f"  {M}╰─❯ {W}اوصف السيرفر {C}» {G}").strip()
        if not desc:
            return await self.mode_ai(guild)

        print(f"\n  {C}┌{'─'*50}┐")
        print(f"  {C}│  {Y}⏳  الذكاء الاصطناعي يبني هيكلك...{' '*14}{C}│")
        print(f"  {C}└{'─'*50}┘")

        try:
            structure = ask_ai(desc)
            print(f"  {G}✔  تم توليد الهيكل: {structure.get('server_name','---')}\n")
        except Exception as e:
            print(f"  {R}✘  فشل الذكاء الاصطناعي: {e}")
            input(f"  {W}اضغط Enter للرجوع...")
            return await self.select_mode(guild)

        show_preview(structure)
        await self.confirm_and_apply(guild, structure)

    # ── الوضع الثاني: هيكل جاهز ──
    async def mode_manual(self, guild):
        draw_banner()
        show_preview(DEFAULT_STRUCTURE)
        await self.confirm_and_apply(guild, DEFAULT_STRUCTURE)

    # ── تأكيد وتطبيق ──
    async def confirm_and_apply(self, guild, structure):
        print(f"  {R}╔{'═'*50}╗")
        print(f"  {R}║  {Y}⚠️  تحذير: سيتم حذف جميع الرومات الحالية!   {R}║")
        print(f"  {R}╚{'═'*50}╝\n")

        confirm = input(f"  {M}╰─❯ {W}اكتب {R}CONFIRM {W}للمتابعة {C}» {G}").strip()
        if confirm != "CONFIRM":
            print(f"  {Y}⚠  تم الإلغاء.")
            await asyncio.sleep(1)
            await self.select_mode(guild)
            return

        await apply_structure(guild, structure)
        print(f"  {C}{'─'*52}")
        print(f"  {Y}⏳  انتظر... جاري الرجوع للأداة")
        print(f"  {C}{'─'*52}")
        await asyncio.sleep(2)
        await self.select_guild()

# ══════════════════════════════════════════════════════════════
#                        التشغيل
# ══════════════════════════════════════════════════════════════

def start():
    draw_banner()
    print(f"    {C}{'─'*52}")
    print(f"    {M}◆  {Y}AUTHENTICATION REQUIRED  {M}◆")
    print(f"    {C}{'─'*52}\n")
    token = input(f"    {M}╰─❯ {W}ENTER BOT TOKEN {C}» {G}").strip()

    intents = discord.Intents.default()
    intents.members = True
    intents.guilds  = True

    client = OBG_Builder(intents=intents)
    try:
        client.run(token)
    except discord.LoginFailure:
        print(f"\n  {R}✘  توكن خاطئ!")
    except Exception as e:
        print(f"\n  {R}✘  خطأ: {e}")

if __name__ == "__main__":
    start()
