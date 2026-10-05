from google import genai
from django.conf import settings

from .tools import get_current_blog, search_blogs


client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


tools = [
    get_current_blog,
    search_blogs,
]


def run_blog_agent(question, blog_id):
    prompt = f"""
You are an AI assistant for a blogging website.

The user is currently viewing blog ID {blog_id}.

You have access to these tools:

1. get_current_blog(blog_id)
   Use this when the user asks about the blog they are currently viewing.

2. search_blogs(query)
   Use this when the user wants to find other blogs.

Rules:

- Use get_current_blog when information about the current blog is required.
- Use search_blogs when the user asks to find or discover other blogs.
- Do not invent information from the database.
- Give clear and simple answers.
- If the requested information cannot be found, say that you could not find it.

Current blog ID:
{blog_id}

User question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
        config={
            "tools": tools
        }
    )

    return response.text