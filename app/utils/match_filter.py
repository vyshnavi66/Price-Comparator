from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def filter_results(query, results):
    threshold = 0.4  # You can tune this
    return [r for r in results if similar(query, r["productName"]) > threshold]
