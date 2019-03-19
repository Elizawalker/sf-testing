# sf-testing
Automate everyday testing tasks because I'm lazy

How to retain session ID of a previous webdriver instance.  This is needed as a work-around for multi-factor authentication.

Before executing tests run following command 
Terminal (mac):
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --no-first-run --no-default-browser-check --user-data-dir=$(mktemp -d -t 'chrome-remote_data_dir')

PowerShell (Windows):
C:\"Program Files (x86)"\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --no-first-run --no-default-browser-check --user-data-dir=$(mktemp -d -t 'chrome-remote_data_dir')
