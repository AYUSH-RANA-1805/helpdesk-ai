"""Represent one support ticket using basic Python values."""


ticket_id = 142
customer_name = "Aarav"
support_agent = "Unassigned"
ticket_text = "I paid for Pro but my account still shows the free plan."
category = "unclassified"
priority = "unclassified"
hours_waiting = 2.5
is_resolved = False

print("HelpDesk AI - Ticket Preview")
print(f"Ticket #{ticket_id}")
print(f"Customer: {customer_name}")
print(f"Support agent: {support_agent}")
print(f"Issue: {ticket_text}")
print(f"Category: {category}")
print(f"Priority: {priority}")
print(f"Hours waiting: {hours_waiting}")
print(f"Resolved: {is_resolved}")

print("\nPython types")
print(f"ticket_id: {type(ticket_id)}")
print(f"customer_name: {type(customer_name)}")
print(f"hours_waiting: {type(hours_waiting)}")
print(f"is_resolved: {type(is_resolved)}")
