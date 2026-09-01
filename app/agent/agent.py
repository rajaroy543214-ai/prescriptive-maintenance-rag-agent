from app.rag.retriever import retrieve


def maintenance_agent(query):
    documents = retrieve(query, n_results=3)

    if not documents:
        return "No relevant maintenance information found."

    context = "\n\n".join(documents)

    # Simple rule-based prescriptive reasoning
    query_lower = query.lower()

    if "overheat" in query_lower or "temperature" in query_lower:
        recommendation = """
Problem: Machine Overheating

Priority: HIGH

Recommended Actions:
1. Stop the machine safely.
2. Check coolant level.
3. Inspect cooling pipes for blockage.
4. Check motor load and ventilation.
5. Inspect the cooling fan.
6. Restart only after temperature returns to normal.

Relevant Manual Information:
""" + context

    else:
        recommendation = """
Problem: """ + query + """

Recommended Actions:
1. Stop the machine safely.
2. Inspect the machine according to the retrieved maintenance manual.
3. Identify the relevant error code and possible cause.
4. Perform the recommended corrective action.
5. Restart the machine and monitor its condition.

Relevant Manual Information:
""" + context

    return recommendation


if __name__ == "__main__":
    query = input("Enter maintenance problem: ")

    result = maintenance_agent(query)

    print("\n=== PRESCRIPTIVE MAINTENANCE RECOMMENDATION ===\n")
    print(result)
