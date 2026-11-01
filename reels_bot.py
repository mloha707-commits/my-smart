import os
import asyncio
import requests
import feedparser
import edge_tts
from moviepy import TextClip, CompositeVideoClip, AudioFileClip, ColorClip

# 1. جلب المفاتيح السرية من متغيرات البيئة (GitHub Secrets)
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# 2. المصادر الرسمية لرصد الأخبار الحصرية (RSS Feeds)
RSS_SOURCES = [
    "https://www.maroc.ma/ar/rss.xml", # البوابة الوطنية للخبر المغربي الرسمي
]

def fetch_exclusive_news():
    """رصد الأخبار الحصرية المتعلقة بالدعم، التمويل والمبادرات"""
    for url in RSS_SOURCES:
        feed = feedparser.parse(url)
        for entry in feed.entries[:5]:
            title = entry.title
            summary = entry.summary if 'summary' in entry else ""
            
            keywords = ["دعم", "تمويل", "مبادرة", "منحة", "برنامج", "مقاولات", "مشروع"]
            if any(kw in title or kw in summary for kw in keywords):
                return title, summary
                
    return "مستجدات برامج الدعم والتمويل", "تابعوا صفحتنا للحصول على أحدث التفاصيل والوثائق الحصرية."

def build_script(title):
    clean_title = title.replace("\n", " ").strip()
    return f"عاجل وحصري: {clean_title}. للتفاصيل الكاملة والخطوات، تجدون الرابط في أول تعليق."

async def generate_reel_video(text_script):
    audio_file = "voice.mp3"
    video_output = "exclusive_reel.mp4"
    
    communicate = edge_tts.Communicate(text_script, "ar-MA-JamalNeural")
    await communicate.save(audio_file)
    
    audio = AudioFileClip(audio_file)
    duration = audio.duration
    
    bg = ColorClip(size=(1080, 1920), color=(15, 23, 42), duration=duration)
    
    watermark = TextClip(
        text="Smart Mokawil | حصري", 
        font_size=38, 
        color='white'
    ).with_opacity(0.7).with_position(('right', 'top')).with_duration(duration)
    
    caption = TextClip(
        text=text_script, 
        font_size=46, 
        color='yellow',
        size=(900, None)
    ).with_position('center').with_duration(duration)
    
    final = CompositeVideoClip([bg, caption, watermark]).with_audio(audio)
    final.write_videofile(video_output, fps=30, codec='libx264', audio_codec='aac')
    return video_output

def send_to_telegram(video_path, caption_text):
    if not TELEGRAM_CHAT_ID:
        print("⚠️ تحذير: لم يتم تحديد Telegram Chat ID، تخطي الإرسال.")
        return
        
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendVideo"
    with open(video_path, 'rb') as video:
        payload = {
            'chat_id': TELEGRAM_CHAT_ID,
            'caption': f"🎬 **ريل جديد جاهز للنشر!**\n\n📝 {caption_text}\n\n👇 قم بتحميله ونشره في صفحتك ومجموعتك الآن!",
            'parse_mode': 'Markdown'
        }
        files = {'video': video}
        r = requests.post(url, data=payload, files=files)
        if r.status_code == 200:
            print("✅ تم إرسال الفيديو بنجاح إلى تيليجرام!")
        else:
            print(f"❌ خطأ الإرسال: {r.text}")

if __name__ == "__main__":
    title, summary = fetch_exclusive_news()
    script_text = build_script(title)
    print(f"📰 الخبر المرصود: {title}")
    
    video_file = asyncio.run(generate_reel_video(script_text))
    send_to_telegram(video_file, script_text)