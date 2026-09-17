import re
import json
from datetime import datetime
import requests

__author__ = "Kuldeep"


class EmailLookup:
    def __init__(self, email):
        self.email = email.strip().lower()
        self.result = {
            "tool": "ScamHunter",
            "module": "email_lookup",
            "author": "Kuldeep (CEH)",
            "version": "2.0.0",
            "input": self.email,
            "timestamp": str(datetime.now())
        }

    def validate(self):
        """Basic email format check"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, self.email) is not None

    def get_domain(self):
        """Extract domain from email"""
        if "@" in self.email:
            return self.email.split("@")[1]
        return None

    def check_breach(self):
        """Check breaches via Have I Been Pwned API"""
        try:
            url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{self.email}"
            headers = {"User-Agent": "ScamHunter-CEH"}
            r = requests.get(url, headers=headers, timeout=10)
            if r.status_code == 200:
                breaches = r.json()
                return {
                    "breached": True,
                    "count": len(breaches),
                    "breaches": [b.get("Name") for b in breaches]
                }
            elif r.status_code == 404:
                return {"breached": False, "message": "No breaches found"}
            else:
                return {"breached": "unknown", "status": r.status_code}
        except Exception as e:
            return {"breached": "unknown", "error": str(e)}

    def check_disposable(self):
        """Check if email is from disposable provider"""
        disposable_domains = [
            "tempmail.com", "guerrillamail.com", "10minutemail.com",
            "mailinator.com", "throwaway.email", "yopmail.com",
            "trashmail.com", "temp-mail.org", "fakeinbox.com",
            "sharklasers.com", "getnada.com", "dispostable.com"
        ]
        domain = self.get_domain()
        if domain and domain in disposable_domains:
            return {"disposable": True, "domain": domain}
        return {"disposable": False}

    def run(self):
        if not self.validate():
            self.result["error"] = "Invalid email format"
            return self.result

        self.result["valid"] = True
        self.result["domain"] = self.get_domain()
        self.result["disposable"] = self.check_disposable()

        print("  Checking breaches...")
        self.result["breach"] = self.check_breach()

        return self.result

    def save(self, path=None):
        if not path:
            safe = self.email.replace("@", "_at_").replace(".", "_")
            path = f"report_email_{safe}.json"

        self.result["_meta"] = {
            "generated_by": "ScamHunter",
            "author": "Kuldeep (CEH)",
            "github": "https://github.com/kuldeepLinux"
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.result, f, indent=2, ensure_ascii=False)
        return path
