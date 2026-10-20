"""Predict ticket priority with simple keyword rules."""


print("HelpDesk AI - Rule-Based Priority Checker")

ticket_text = input("Describe the customer's issue: ").strip()

if ticket_text == "":
    print("A ticket description is required.")
else:
    normalized_text = ticket_text.lower()

    if (
        "production" in normalized_text
        or "server down" in normalized_text
        or "data loss" in normalized_text
        or "security breach" in normalized_text
        or "hacked" in normalized_text
    ):
        priority = "high"
    elif "payment" in normalized_text or "subscription" in normalized_text:
        priority = "medium"
    else:
        priority = "low"

    print(f"Ticket: {ticket_text}")
    print(f"Predicted priority: {priority}")
