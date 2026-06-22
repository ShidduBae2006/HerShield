[app]

# (str) Title of your application
title = HerShield

# (str) Package name
package.name = hershield

# (str) Package domain (needed for android packaging)
package.domain = org.test
version = 0.1

# (str) Source code directory
source.dir = .

# (list) Source files to include (let it include all python files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# CRITICAL FIX: 'ratelim' added here to fix the geocoder boot crash!
requirements = python3, kivy==2.3.1, kivymd==1.2.0, geocoder, ratelim, plyer, requests, sqlite3, urllib3

# (str) Supported orientations
orientation = portrait

# =============================================================================
# Android specific configurations
# =============================================================================

# (list) Android hardware permissions granted to the app
android.permissions = android.permission.SEND_SMS, android.permission.ACCESS_FINE_LOCATION, android.permission.ACCESS_COARSE_LOCATION, android.permission.INTERNET

# (int) Target Android API (Leave blank or set to 33/34 depending on NDK)
android.api = 33

# (str) The Android arch to build for
android.archs = arm64-v8a

# (str) Bootstrap backend to use for layout initialization
p4a.bootstrap = sdl2
