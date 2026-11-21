[app]
title = 隐私查询工具
package.name = querytool
package.domain = org.example.querytool
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,json
version = 0.1
main.py.filename = main.py
requirements = python3==3.11,kivy==2.3.0,requests
orientation = portrait
fullscreen = 1
android.permissions = INTERNET
android.archs = arm64-v8a
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.enable_androidx = False
android.usesCleartextTraffic = True
log_level = 2

[buildozer]
android.clean_build = 0
