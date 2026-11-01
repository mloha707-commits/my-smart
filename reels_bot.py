import os
import asyncio
import requests
import feedparser
import edge_tts
from moviepy import TextClip, CompositeVideoClip, AudioFileClip, ColorClip, ImageClip

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

RSS_SOURCES = [
    "https://www.maroc.ma/ar/rss.xml",
]

def fetch_latest_news():
    """جلب أحدث الأخبار وصياغة محتوى غني ومتكامل"""
    for url in RSS_SOURCES:
        feed = feedparser.parse(url)
        for entry in feed.entries[:5]:
            title = entry.title
            summary = entry.summary if 'summary' in entry else ""
            keywords = ["دعم", "تمويل", "مبادرة", "منحة", "برنامج", "مقاولات", "مشروع", "تنمية"]
            if any(kw in title or kw in summary for kw in keywords):
                clean_title = title.replace("\n", " ").strip()
                clean_summary = summary.replace("\n", " ").strip()
                # صياغة احترافية طويلة تضمن فيديو مشوق وواقعي لمدة تتجاوز 25-30 ثانية
                full_script = (
                    f"تطورات ومستجدات هامة. {clean_title}. "
                    f"إليكم التفاصيل الأساسية: {clean_summary}. "
                    f"تابعونا للمزيد من المستجدات والخطوات العملية عبر منصاتنا."
                )
                return title, full_script
                
    return "مستجدات برامج الدعم والتمويل", "تابعوا أحدث التطورات والبرامج الرسمية المخصصة للمواطنين والمقاولين للحصول على الدعم اللازم."

async def generate_professional_reel(script_text):
    audio_file = "voice_over.mp3"
    video_output = "professional_reel.mp4"
    
    print("🎙️ جاري توليد التعليق الصوتي الاحترافي...")
    communicate = edge_tts.Communicate(script_text, "ar-MA-JamalNeural")
    await communicate.save(audio_file)
    
    audio = AudioFileClip(audio_file)
    duration = max(audio.duration, 15) # ضمان مدة كافية ومحترمة للفيديو (15 ثانية على الأقل أو طول الصوت)
    
    print(f"⏱️ مدة الفيديو الكلية ستكون: {duration:.2f} ثانية")
    
    # 1. خلفية ديناميكية داكنة وأنيقة تليق بالمحتوى الإخباري والمالي
    bg = ColorClip(size=(1080, 1920), color=(10, 15, 30), duration=duration)
    
    try:
        # 2. شريط علوي احترافي (Header)
        header = TextClip(
            text="🔴 عاجل وحصري | دليل المقاول الذكي",
            font="Liberation-Sans",
            font_size=45,
            color='#38bdf8',
            size=(980, 120),
            method='caption'
        ).with_position(('center', 250)).with_duration(duration)

        # 3. النص الرئيسي للخبر بتنسيق مريح وواضح للعين
        main_caption = TextClip(
            text=script_text,
            font="Liberation-Sans",
            font_size=52,
            color='white',
            size=(950, 1000),
            method='caption',
            text_align='center'
        ).with_position(('center', 'center')).with_duration(duration)

        # 4. شريط سفلي تفاعلي (Footer / Call to Action)
        footer = TextClip(
            text="👇 تجدون التفاصيل الكاملة في أول تعليق",
            font="Liberation-Sans",
            font_size=42,
            color='#fbbf24',
            size=(980, 100),
            method='caption'
        ).with_position(('center', 1650)).with_duration(duration)

        # دمج الطبقات الاحترافية مع الصوت
        final_video = CompositeVideoClip([bg, header, main_caption, footer]).with_audio(audio)
        
    except Exception as e:
        print(f"⚠️ تنبيه أثناء تركيب الطبقات: {e}. سيتم الاعتماد على التصميم الآمن.")
        fallback_text = TextClip(
            text=script_text,
            font_size=50,
            color='white',
            size=(900, 1000),
            method='caption'
        ).with_position('center').with_duration(duration)
        final_video = CompositeVideoClip([bg, fallback_text]).with_audio(audio)

    print("🎬 جاري تصدير الفيديو الاحترافي برزوليوشن عالي (30 FPS)...")
    final_video.write_videofile(
        video_output, 
        fps=30, 
        codec='libx264', 
        audio_codec='aac',
        preset='medium',
        bitrate='4M'
    )
    return video_output

def send_to_telegram(video_path, caption_text):
    if not TELEGRAM_CHAT_ID:
        print("⚠️ لم يتم ضبط تيليجرام.")
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendVideo"
    with open(video_path, 'rb') as video:
        payload = {
            'chat_id': TELEGRAM_CHAT_ID,
            'caption': f"🎬 **ريل احترافي جديد!**\n\n{caption_text}",
            'parse_mode': 'Markdown'
        }
        files = {'video': video}
        requests.post(url, data=payload, files=files)
        print("✅ تم الإرسال إلى تيليجرام بنجاح!")

if __name__ == "__main__":
    title, script_text = fetch_latest_news()
    print(f"📰 الخبر المختار: {title}")
    
    video_file = asyncio.run(generate_professional_reel(script_text))
    send_to_telegram(video_file, script_text)