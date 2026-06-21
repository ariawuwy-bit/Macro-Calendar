import subprocess, time, os

# Check if we have network connectivity
print("Testing GitHub connectivity...")
result = subprocess.run(['ping', '-n', '1', 'github.com'], capture_output=True, text=True, timeout=10)
print("Ping result:", result.returncode)

# Try git push with increased timeout via env vars
env = dict(os.environ)
env['GIT_HTTP_LOW_SPEED_LIMIT'] = '0'
env['GIT_HTTP_LOW_SPEED_TIME'] = '300'  # 5 min timeout

print("\nTrying git push with extended timeout...")
for attempt in range(3):
    print(f"\nAttempt {attempt+1}/3...")
    try:
        result = subprocess.run(
            ['git', 'push', 'origin', 'main'],
            capture_output=True, text=True, timeout=120,
            env=env, cwd='D:/WorkbuddyStudio/MacroCalendar'
        )
        if result.returncode == 0:
            print("Push SUCCESS!")
            print(result.stdout[-500:])
            break
        else:
            print(f"Failed (code {result.returncode})")
            print("STDERR:", result.stderr[-300:])
    except Exception as e:
        print(f"Exception: {e}")
    
    if attempt < 2:
        wait = 15 * (attempt + 1)
        print(f"Waiting {wait}s...")
        time.sleep(wait)
else:
    print("\nAll attempts failed. Network may be down.")
    print("Please push manually when network recovers:")
    print("  cd D:/WorkbuddyStudio/MacroCalendar")
    print("  git push origin main")
