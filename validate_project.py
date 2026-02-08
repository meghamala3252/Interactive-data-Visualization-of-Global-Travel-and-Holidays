import os
import sys
import compileall
import traceback
from flask import Flask

print("--- STARTED DIAGNOSTICS ---")

# 1. Check Python Syntax
print("\n[1] Checking Python Syntax...")
try:
    compileall.compile_dir('project', force=True, quiet=1)
    print("[OK] Python syntax check passed.")
except Exception as e:
    print(f"[FAIL] Python syntax error: {e}")

# 2. Check Imports
print("\n[2] Checking Imports...")
try:
    from project.app import create_app
    from project.extensions import db
    from project.models import User, Dashboard
    print("[OK] Core imports successful.")
except Exception as e:
    print(f"[FAIL] Import Error: {e}")
    traceback.print_exc()
    sys.exit(1)

# 3. Check App Initialization
print("\n[3] Checking App Initialization...")
try:
    app = create_app()
    print("[OK] App factory created successfully.")
except Exception as e:
    print(f"[FAIL] App creation failed: {e}")
    traceback.print_exc()
    sys.exit(1)

# 4. Check Database
print("\n[4] Checking Database Connection...")
try:
    with app.app_context():
        db.engine.connect()
        user_count = User.query.count()
        print(f"[OK] Database connected. User count: {user_count}")
except Exception as e:
    print(f"[FAIL] Database error: {e}")
    # Don't exit, might be just a connection issue

# 5. Check Templates
print("\n[5] Checking Templates...")
import jinja2
env = jinja2.Environment()
template_dir = os.path.join('project', 'templates')
for root, dirs, files in os.walk(template_dir):
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    env.parse(f.read())
            except Exception as e:
                print(f"[FAIL] Template Syntax Error in {path}: {e}")

print("\n--- DIAGNOSTICS COMPLETE ---")
