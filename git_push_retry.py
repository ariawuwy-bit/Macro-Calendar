import subprocess
import time
import os
import sys

# Try git push with retry
# Read token from git config or env
token = os.environ.get('GITHUB_TOKEN', '')
if not token:
    # Try to get token from git credential helper
    try:
        result = subprocess.run(['git', 'config', '--get', 'user.token'], 
                                capture_output=True, text=True)
        token = result.stdout.strip()
    except:
        pass

for attempt in range(3):
    print(f"Attempt {attempt+1}/3: git push origin main...")
    try:
        result = subprocess.run(['git', 'push', 'origin', 'main'], 
                               capture_output=True, text=True, timeout=60,
                               env={**os.environ, 'GIT_TERMINAL_PROMPT': '0'})
        if result.returncode == 0:
            print("Push SUCCESS!")
            print(result.stdout)
            sys.exit(0)
        else:
            print(f"Push failed (code {result.returncode})")
            print("STDOUT:", result.stdout[-500:] if len(result.stdout) > 500 else result.stdout)
            print("STDERR:", result.stderr[-500:] if len(result.stderr) > 500 else result.stderr)
    except Exception as e:
        print(f"Exception: {e}")
    
    if attempt < 2:
        wait_time = 10 * (attempt + 1)
        print(f"Waiting {wait_time}s before retry...")
        time.sleep(wait_time)

print("All attempts failed.")
sys.exit(1)
