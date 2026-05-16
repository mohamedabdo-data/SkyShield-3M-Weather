import requests
import json

# دالة لجلب بيانات الطقس والمناخ من NASA POWER API
def get_nasa_climate_data(lat, lon):
    """
    هذه الدالة تتصل بمركز بيانات ناسا (NASA POWER) لجلب درجات الحرارة
    والرطوبة لمنطقة معينة (مثل الإسكندرية أو فينيسيا).
    """
    # رابط الـ API الخاص بناسا لمواقع محددة
    url = f"https://power.larc.nasa.gov/api/temporal/daily/point?parameters=T2M,RH2M&community=AG&longitude={lon}&latitude={lat}&start=20230101&end=20230105&format=JSON"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print("✅ تم بنجاح الاتصال ببيانات ناسا!")
            return data
        else:
            print(f"❌ خطأ في الاتصال: {response.status_code}")
            return None
    except Exception as e:
        print(f"⚠️ حدث خطأ غير متوقع: {e}")
        return None

# إحداثيات الإسكندرية (المعرضة لخطر الغرق بسبب ذوبان الجليد)
alex_lat, alex_lon = 31.2001, 29.9187

print(f"--- جاري تحليل البيانات لموقع: الإسكندرية ({alex_lat}, {alex_lon}) ---")
weather_info = get_nasa_climate_data(alex_lat, alex_lon)

if weather_info:
    # عرض جزء من البيانات (درجات الحرارة) للتأكد من العمل
    temps = weather_info['properties']['parameter']['T2M']
    print("نتائج ناسا لدرجات الحرارة في الأيام الأخيرة:")
    print(json.dumps(temps, indent=2))
