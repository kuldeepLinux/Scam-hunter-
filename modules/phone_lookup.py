import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import json
from datetime import datetime

__author__ = "Kuldeep"

class PhoneLookup:
    def __init__(self, number, region="IN"):
        self.raw = number
        self.region = region
        self.result = {
            "tool": "ScamHunter",
            "author": "Kuldeep (CEH)",
            "version": "1.0.0",
            "input": number,
            "timestamp": str(datetime.now())
        }

    def run(self):
        try:
            parsed = phonenumbers.parse(self.raw, self.region)
            if not phonenumbers.is_valid_number(parsed):
                self.result["error"] = "Invalid number"
                return self.result
            self.result.update({
                "valid": True,
                "country": geocoder.description_for_number(parsed, "en"),
                "carrier": carrier.name_for_number(parsed, "en"),
                "timezones": list(timezone.time_zones_for_number(parsed)),
                "type": self._type(parsed),
            })
        except Exception as e:
            self.result["error"] = str(e)
        return self.result

    def _type(self, parsed):
        t = phonenumbers.number_type(parsed)
        mapping = {0:"Fixed Line",1:"Mobile",2:"Fixed/Mobile",3:"Toll Free",
                   4:"Premium",5:"Shared Cost",6:"VoIP",7:"Personal",8:"Pager",
                   9:"Universal",10:"Voicemail"}
        return mapping.get(t, "Unknown")

    def save(self, path="report.json"):
        self.result["_meta"] = {
            "generated_by": "ScamHunter",
            "author": "Kuldeep (CEH)",
            "github": "https://github.com/kuldeepLinux"
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.result, f, indent=2, ensure_ascii=False)
        return path
