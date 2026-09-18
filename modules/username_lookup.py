import requests
import json
from datetime import datetime

__author__ = "Kuldeep"


class UsernameLookup:
    def __init__(self, username):
        self.username = username.strip()
        self.result = {
            "tool": "ScamHunter",
            "module": "username_lookup",
            "author": "Kuldeep (CEH)",
            "version": "2.0.0",
            "input": self.username,
            "timestamp": str(datetime.now()),
            "found": [],
            "not_found": []
        }

        # Popular platforms with check URLs
        self.platforms = {
            "GitHub": f"https://github.com/{self.username}",
            "Instagram": f"https://www.instagram.com/{self.username}/",
            "Twitter/X": f"https://x.com/{self.username}",
            "Reddit": f"https://www.reddit.com/user/{self.username}",
            "YouTube": f"https://www.youtube.com/@{self.username}",
            "Facebook": f"https://www.facebook.com/{self.username}",
            "Pinterest": f"https://www.pinterest.com/{self.username}/",
            "TikTok": f"https://www.tiktok.com/@{self.username}",
            "Medium": f"https://medium.com/@{self.username}",
            "Dev.to": f"https://dev.to/{self.username}",
            "GitLab": f"https://gitlab.com/{self.username}",
            "Bitbucket": f"https://bitbucket.org/{self.username}/",
            "Keybase": f"https://keybase.io/{self.username}",
            "Steam": f"https://steamcommunity.com/id/{self.username}",
            "Twitch": f"https://www.twitch.tv/{self.username}",
            "SoundCloud": f"https://soundcloud.com/{self.username}",
            "Spotify": f"https://open.spotify.com/user/{self.username}",
            "Patreon": f"https://www.patreon.com/{self.username}",
            "About.me": f"https://about.me/{self.username}",
            "Behance": f"https://www.behance.net/{self.username}",
            "Dribbble": f"https://dribbble.com/{self.username}",
            "Flickr": f"https://www.flickr.com/people/{self.username}",
            "Vimeo": f"https://vimeo.com/{self.username}",
            "WordPress": f"https://{self.username}.wordpress.com",
            "Blogger": f"https://{self.username}.blogspot.com",
            "Replit": f"https://replit.com/@{self.username}",
            "HackerNews": f"https://news.ycombinator.com/user?id={self.username}",
            "ProductHunt": f"https://www.producthunt.com/@{self.username}",
            "Mastodon": f"https://mastodon.social/@{self.username}",
            "Linktree": f"https://linktr.ee/{self.username}",
            "Gravatar": f"https://gravatar.com/{self.username}",
            "Telegram": f"https://t.me/{self.username}"
        }

    def check_platform(self, name, url):
        """Check if username exists on a platform"""
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
            }
            r = requests.get(url, headers=headers, timeout=8, allow_redirects=True)
            if r.status_code == 200:
                return {"platform": name, "url": url, "status": "found"}
        except requests.exceptions.Timeout:
            return {"platform": name, "url": url, "status": "timeout"}
        except Exception:
            pass
        return {"platform": name, "url": url, "status": "not_found"}

    def run(self):
        if not self.username:
            self.result["error"] = "No username provided"
            return self.result

        print(f"  Scanning {len(self.platforms)} platforms...")

        for name, url in self.platforms.items():
            check = self.check_platform(name, url)
            if check["status"] == "found":
                self.result["found"].append({
                    "platform": name,
                    "url": url
                })
                print(f"  [+] Found: {name}")

        self.result["total_found"] = len(self.result["found"])
        self.result["total_checked"] = len(self.platforms)
        return self.result

    def save(self, path=None):
        if not path:
            path = f"report_username_{self.username}.json"

        self.result["_meta"] = {
            "generated_by": "ScamHunter",
            "author": "Kuldeep (CEH)",
            "github": "https://github.com/kuldeepLinux"
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.result, f, indent=2, ensure_ascii=False)
        return path
