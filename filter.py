import requests
from pathlib import Path

SOURCE_URL = "https://www.schulnetz-ag.ch/ksba/cindex.php?longurl=2m0MVHQHDWmjafghWBrrRTcDRKHRLZJej0AhKR7Yt24eJ0pdAff8Zk4DZHsn80AA"

# Always keep these
ALWAYS_KEEP = ["I3a"]

# Keywords to exclude
EXCLUDE_KEYWORDS = [
    "Stopp Littering", "Exkursion", "Repetitorium", "Training", "YES", 
    "Sprechstunde", "Tonschiene", "2.1", "Mittelschulmeisterschaften", "Lyrik", "ask!", "Schulsozialarbeit", "Volleyball", "Fussball", "Handball", "Smart",
    "Sommerkonzert", "Konferenz", "Probe", "Freiwillig", "Open Stage", "Abschlussaustellung", "Kulturschiene", "Girls", "spenden", "Meisterschaft", "Orchester",
    "Film", "Wettbewerb", "BiG", "Studienreise", "gespräch", "Konzert", "studien", "Summer Camp", "Shanghai", "Festival", "Kath.", "Merch", "Blaue Lunte", "Matur",
    "Aulatalk", "Twistory", "theater", "finale", "SO", "Versammlung", "Chemielabortag", "Chagall", "Eltern", "schulNetz", "Uselütete", "EMS", "Beachvolley", "MSM",
    "WMS", "Gymnasium",
    "G1a","G1b","G1c","G1d","G1e","G1f","G1g","G1h","G1i","G1j","G1k","G1l","G1m","G1n","G1o","G1p","G1q","G1r","G1s","G1t","G1u","G1v","G1w","G1x","G1y","G1z",
    "G2a","G2b","G2c","G2d","G2e","G2f","G2g","G2h","G2i","G2j","G2k","G2l","G2m","G2n","G2o","G2p","G2q","G2r","G2s","G2t","G2u","G2v","G2w","G2x","G2y","G2z",
    "G3a","G3b","G3c","G3d","G3e","G3f","G3g","G3h","G3i","G3j","G3k","G3l","G3m","G3n","G3o","G3p","G3q","G3r","G3s","G3t","G3u","G3v","G3w","G3x","G3y","G3z",
    "G4a","G4b","G4c","G4d","G4e","G4f","G4g","G4h","G4i","G4j","G4k","G4l","G4m","G4n","G4o","G4p","G4q","G4r","G4s","G4t","G4u","G4v","G4w","G4x","G4y","G4z",
    "I1a","I1b","I2a","I2b","I3b","W1a","W1b","W1c","W2a","W2b","W2c","W3a","W3b","W3c"
]

def keep_event(summary: str) -> bool:
    summary_lower = summary.lower()
    if any(k.lower() in summary_lower for k in ALWAYS_KEEP):
        return True
    if any(k.lower() in summary_lower for k in EXCLUDE_KEYWORDS):
        return False
    return True



def main():
    print("Fetching source calendar...")
    ics_data = requests.get(SOURCE_URL).text

    events = ics_data.split("BEGIN:VEVENT")[1:]  # skip header
    kept_events = []
    skipped_count = 0

    for ev in events:
        block = "BEGIN:VEVENT" + ev
        summary_line = [line for line in block.splitlines() if line.startswith("SUMMARY:")]
        summary = summary_line[0][8:] if summary_line else ""
        if keep_event(summary):
            kept_events.append(block)
        else:
            skipped_count += 1

    Path("docs").mkdir(exist_ok=True)
    with open("docs/filtered.ics", "w", encoding="utf-8") as f:
        f.write("BEGIN:VCALENDAR\n")
        for ev in kept_events:
            f.write(ev + "\n")
        f.write("END:VCALENDAR\n")

    print(f"✅ Total events in source: {len(events)}")
    print(f"✅ Events after filtering: {len(kept_events)}")
    print(f"⚠️ Events skipped: {skipped_count}")
    print("👉 Titles kept:")
    for ev in kept_events[:1000]:
        summary_line = [line for line in ev.splitlines() if line.startswith("SUMMARY:")]
        print("   -", summary_line[0][8:] if summary_line else "<no title>")

if __name__ == "__main__":
    main()
