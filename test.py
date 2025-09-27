import os
import datetime

def push_changes():
    # Step 1: Go to your repo folder
    os.chdir(r"C:\Users\User\OneDrive\Documents\GitHub\Log_book.-Digital_Accounting")

    # Step 2: Create a commit message with current date/time
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Step 3: Add all changes
    os.system("git add .")

    # Step 4: Commit with message
    os.system(f'git commit -m "Auto-commit at {now}"')

    # Step 5: Push to GitHub
    os.system("git push origin main")

# Run it
push_changes()