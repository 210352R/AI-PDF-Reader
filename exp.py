def format_text(text):
    # Split the text into sections based on '**'
    sections = text.split("**")
    formatted_text = ""

    for idx, section in enumerate(sections):
        # Skip empty sections
        if not section.strip():
            continue

        # Add headers and bullet points for non-empty sections
        if idx % 2 == 1:
            header = f"\n**{section.strip()}**\n"
            formatted_text += header
        else:
            points = section.strip().split("\n")
            for point in points:
                if point.strip():
                    formatted_text += f"- {point.strip()}\n"

    return formatted_text


# Original text
original_text = """
**Question 1**
Explain briefly what a double linked list and a circular linked list is?
Note: Please use diagrams in your explanations

**Double Linked List**
A double linked list is a linear data structure in which each element is connected to the next element and the previous element.
This means that each element has a pointer to the next element and a pointer to the previous element.
This makes it possible to traverse the list in both directions, forwards and backwards.

**Circular Linked List**
A circular linked list is a special type of linked list in which the last element points back to the first element.
This creates a circular loop, which means that the list can be traversed indefinitely.
Circular linked lists are often used to implement queues and stacks.

**Diagrams**
Here are diagrams of a double linked list and a circular linked list:
[Image of a double linked list]
[Image of a circular linked list]
"""

# Format the text
formatted_text = format_text(original_text)

# Print the formatted text
print(formatted_text)
