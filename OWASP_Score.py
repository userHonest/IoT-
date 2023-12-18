Analysis

python
Copy code
# Calculating the total score and average score for the OWASP Top 10 (2021) categories

# Scores given for each category
scores = {
    "A01:2021-Broken Access Control": "N/A",
    "A02:2021-Cryptographic Failures": 3,
    "A03:2021-Injection": 8,
    "A04:2021-Insecure Design": "N/A",
    "A05:2021-Security Misconfiguration": 5,
    "A06:2021-Vulnerable and Outdated Components": 5,
    "A07:2021-Identification and Authentication Failures": 4,
    "A08:2021-Software and Data Integrity Failures": 4,
    "A09:2021-Security Logging and Monitoring Failures": 3,
    "A10:2021-Server-Side Request Forgery (SSRF)": "N/A"
}

# Calculating total and average scores
total_score = sum(score for score in scores.values() if score != "N/A")
applicable_categories = len([score for score in scores.values() if score != "N/A"])
average_score = total_score / applicable_categories

print(total_score, average_score)
