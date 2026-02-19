"""Regular expression basics."""

import re


def main() -> None:
    text = "Contact support@example.com or admin@test.org by 2026-02-19."

    emails = re.findall(r"[\w.-]+@[\w.-]+", text)
    date_match = re.search(r"\d{4}-\d{2}-\d{2}", text)
    masked = re.sub(r"[\w.-]+@[\w.-]+", "[email-hidden]", text)

    print("Emails:", emails)
    print("Date found:", date_match.group(0) if date_match else "None")
    print("Masked text:", masked)


if __name__ == "__main__":
    main()
