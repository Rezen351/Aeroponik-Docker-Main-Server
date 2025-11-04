from flask import Flask, jsonify, redirect
from supabase import create_client, Client
import os

# --- Konfigurasi Supabase ---
# Ambil dari environment variables (LEBIH BAIK)
SUPABASE_URL = os.environ.get("SUPABASE_URL", "https://studio.almuzky.my.id")
SUPABASE_KEY = os.environ.get("SUPABASE_SERVICE_ROLE_KEY", "GANTI_DENGAN_ANON_KEY_ASLI_ANDA")
BUCKET_NAME = "images" # Ganti jika perlu

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
# ---------------------------

app = Flask(__name__)

# Supabase client
def get_supabase_client() -> Client:
    url: str = os.environ.get('SUPABASE_URL')
    key: str = os.environ.get('SUPABASE_SERVICE_ROLE_KEY')
    supabase : Client = create_client(url, key)
    if not url or not key:
        raise ValueError("SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY must be set")
    return supabase

@app.route('/api/test', methods=['GET'])
def test_supabase():
    try:
        supabase = get_supabase_client()
        response = supabase.table('test').select('id').limit(1).execute()
        return jsonify({"status": "OK", "message": "Supabase API is working", "data": response.data})
    except Exception as e:
        return jsonify({"status": "ERROR", "message": str(e)}), 500

@app.route('/api/buckets', methods=['GET']) 
def list_buckets():
    try:
        supabase_client = get_supabase_client()
        buckets = supabase_client.storage.list_buckets()
        bucket_names = [bucket.name for bucket in buckets]
        return jsonify({"buckets": bucket_names})
    except Exception as e:
        return jsonify({"status": "ERROR", "message": str(e)}), 500

@app.route('/api/latest-image')
def get_latest_image():
    try:
        supabase_client = get_supabase_client()
        # 1. Minta Supabase mengurutkan dan HANYA MENGIRIM 1 FILE TERATAS
        files = supabase_client.storage.from_(BUCKET_NAME).list(
            path="", # Cari di root bucket
            options={
                "limit": 1,
                "offset": 0,
                "sortBy": { "column": "created_at", "order": "desc" }
            }
        )

        if not files:
            return "Bucket kosong atau tidak ditemukan", 404

        # 2. Ambil nama file terbaru (sekarang hanya ada 1 file di list)
        latest_file_name = files[0]['name']

        # 3. Buat Signed URL
        signed_url_response = supabase_client.storage.from_(BUCKET_NAME).create_signed_url(
            path=latest_file_name,
            expires_in=60 # Berlaku 60 detik
        )

        signed_url = signed_url_response['signedURL']

        # 4. Kirim Redirect
        return redirect(signed_url, code=302)

    except Exception as e:
        print(f"Error: {e}")
        return str(e), 500

@app.route('/api/latest-image/<camera>')
def get_latest_image_by_camera(camera):
    try:
        supabase_client = get_supabase_client()
        # 1. List all files and filter by camera prefix
        files = supabase_client.storage.from_(BUCKET_NAME).list(
            path="", # Cari di root bucket
            options={
                "limit": 100,  # Adjust limit as needed
                "offset": 0,
                "sortBy": { "column": "created_at", "order": "desc" }
            }
        )

        if not files:
            return "Bucket kosong atau tidak ditemukan", 404

        # 2. Filter files that start with the camera name
        camera_files = [f for f in files if f['name'].startswith(camera)]

        if not camera_files:
            return f"Tidak ada gambar untuk kamera {camera}", 404

        # 3. Ambil nama file terbaru untuk kamera tersebut
        latest_file_name = camera_files[0]['name']

        # 4. Buat Signed URL
        signed_url_response = supabase_client.storage.from_(BUCKET_NAME).create_signed_url(
            path=latest_file_name,
            expires_in=60 # Berlaku 60 detik
        )

        signed_url = signed_url_response['signedURL']

        # 5. Kirim Redirect
        return redirect(signed_url, code=302)

    except Exception as e:
        print(f"Error: {e}")
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
