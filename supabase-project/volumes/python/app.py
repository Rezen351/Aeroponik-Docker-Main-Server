from flask import Flask, jsonify
from supabase import create_client, Client
import os

app = Flask(__name__)

# Supabase client
def get_supabase_client() -> Client:
    url: str = os.environ.get('SUPABASE_URL')
    key: str = os.environ.get('SUPABASE_ANON_KEY')
    supabase : Client = create_client(url, key)
    if not url or not key:
        raise ValueError("SUPABASE_URL and SUPABASE_ANON_KEY must be set")
    return supabase

@app.route('/api/test', methods=['GET'])
def test_supabase():
    try:
        supabase = get_supabase_client()
        response = supabase.table('test').select('id').limit(1).execute()
        return jsonify({"status": "OK", "message": "Supabase API is working", "data": response.data})
    except Exception as e:
        return jsonify({"status": "ERROR", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
