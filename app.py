from flask import Flask, render_template, jsonify
import subprocess, json, os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scan/<path:repo_path>')
def run_scan(repo_path):
    cmd = f'python securepipe.py --repo {repo_path}'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return jsonify({
        'stdout': result.stdout,
        'stderr': result.stderr,
        'returncode': result.returncode
    })

# @app.route('/reports')
# def reports():
#     reports_dir = 'reports'
#     files = os.listdir(reports_dir) if os.path.exists(reports_dir) else []
#     return jsonify({'reports': files})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
