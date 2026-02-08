from project.app import create_app, socketio

app = create_app()

if __name__ == '__main__':
    # Force threading mode for maximum compatibility on Windows
    # Use port 5001 to avoid conflict if 5000 is stuck
    try:
        socketio.run(app, debug=True, port=5001, allow_unsafe_werkzeug=True)
    except OSError as e:
        if "Address already in use" in str(e) or "WinError 10048" in str(e):
             print("Port 5001 is busy, trying 5002...")
             socketio.run(app, debug=True, port=5002, allow_unsafe_werkzeug=True)
        else:
            raise e
