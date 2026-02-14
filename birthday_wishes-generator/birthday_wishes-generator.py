current_year = 2026
recipient_name = input()
year_of_birth = int(input())
sender_name = input()
personalized_message = input()

print(f"""
{recipient_name}, wszystkiego najlepszego z okazji {current_year - year_of_birth} urodzin!
{personalized_message}
{sender_name}
""")