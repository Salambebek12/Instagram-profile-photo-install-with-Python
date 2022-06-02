# pip install instaloader

def banner():
  print("""
       CODER BY C0L0N3L
       Instagram: @musabdmar
        """)

banner()

import instaloader

ig = instaloader.Instaloader()
dp = input("Instagram Kullanıcı adı: ")

ig.download_profile(dp, profile_pic_only = True)