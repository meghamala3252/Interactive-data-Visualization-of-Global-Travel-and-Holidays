from project.app import create_app, socketio
import sys

# Create the application instance
try:
    app = create_app()
except Exception as e:
    import traceback
    traceback.print_exc()
    print("Failed to create app")
    sys.exit(1)

if __name__ == '__main__':
    print("Starting Global Tourism App...")
    print("If you see 'Address already in use', please close other Python windows.")
    print("Access the app at: http://127.0.0.1:5000")
    
    # We use standard Flask run which is more stable for development on Windows
    # SocketIO will still work with async_mode='threading'
    try:
        socketio.run(app, debug=True, port=5000, allow_unsafe_werkzeug=True)
    except OSError as e:
        print(f"Port 5000 is busy. Trying 5001...")
        try:
            socketio.run(app, debug=True, port=5001, allow_unsafe_werkzeug=True)
        except Exception as e2:
            print("CRITICAL ERROR: Could not start server.")
            print(e2)
            input("Press Enter to exit...")
