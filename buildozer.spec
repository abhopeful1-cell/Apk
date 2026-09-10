[app]
title = Dropper
package.name = dropper
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

# Use Python 3.11 for compatibility with Kivy 2.3.0
# Python 3.14 has API changes that aren't supported yet
requirements = python3.11,kivy==2.3.0

orientation = portrait

fullscreen = 0

android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
