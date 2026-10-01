import subprocess
import time
import urllib.request
import urllib.parse
import sys

def test_routes():
    print("=" * 60, flush=True)
    print("RUNNING AUTOMATED APPLICATION VERIFICATION", flush=True)
    print("=" * 60, flush=True)
    
    # 1. Start Flask app as a background process
    print("Starting Flask application server on http://127.0.0.1:5000...", flush=True)
    # Redirect standard streams to DEVNULL to avoid hanging on Windows
    process = subprocess.Popen([sys.executable, "app.py"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Give Flask server a few seconds to start (TensorFlow takes a few seconds to load)
    time.sleep(8)
    
    # Check if the process died immediately
    if process.poll() is not None:
        print("Flask app failed to start. Exiting test.", flush=True)
        sys.exit(1)
        
    routes = [
        "",
        "prediction",
        "data-analysis",
        "model-comparison",
        "clustering",
        "ann",
        "ai-concepts",
        "ethics",
        "internship-learning",
        "about"
    ]
    
    success = True
    
    # 2. Test each page (GET)
    for route in routes:
        url = f"http://127.0.0.1:5000/{route}"
        print(f"Testing route: GET {url:<50}", end="", flush=True)
        try:
            # Set a 5-second timeout to prevent hanging indefinitely
            response = urllib.request.urlopen(url, timeout=5)
            code = response.getcode()
            if code == 200:
                print("[ OK ]", flush=True)
            else:
                print(f"[ FAILED (Status: {code}) ]", flush=True)
                success = False
        except Exception as e:
            print(f"[ FAILED (Error: {e}) ]", flush=True)
            success = False

    # 3. Test prediction submission (POST)
    pred_url = "http://127.0.0.1:5000/prediction"
    print(f"Testing route: POST {pred_url:<49}", end="", flush=True)
    
    # Sample diabetic indicators payload
    data = urllib.parse.urlencode({
        'pregnancies': '6',
        'glucose': '148',
        'bloodpressure': '72',
        'skinthickness': '35',
        'insulin': '0',
        'bmi': '33.6',
        'pedigree': '0.627',
        'age': '50'
    }).encode('utf-8')
    
    try:
        req = urllib.request.Request(pred_url, data=data, method="POST")
        response = urllib.request.urlopen(req, timeout=5)
        code = response.getcode()
        html_content = response.read().decode('utf-8')
        
        # Verify status and checking predictions inside response body
        if code == 200:
            checks = [
                "Logistic Regression",
                "K-Nearest Neighbors",
                "Decision Tree",
                "Artificial Neural Network",
                "Model Prediction",
                "Educational Disclaimer:"
            ]
            missing_keywords = [c for c in checks if c not in html_content]
            if not missing_keywords:
                print("[ OK ]", flush=True)
            else:
                print(f"[ FAILED (Missing keywords: {missing_keywords}) ]", flush=True)
                success = False
        else:
            print(f"[ FAILED (Status: {code}) ]", flush=True)
            success = False
            
    except Exception as e:
        print(f"[ FAILED (Error: {e}) ]", flush=True)
        success = False

    # 4. Cleanup background process
    print("Stopping Flask application server...", flush=True)
    process.terminate()
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()
        
    print("=" * 60, flush=True)
    if success:
        print("ALL APP ENDPOINTS AND PREDICTIONS VERIFIED SUCCESSFULLY!", flush=True)
    else:
        print("SOME APPLICATION VERIFICATION TESTS FAILED.", flush=True)
    print("=" * 60, flush=True)
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    test_routes()
