from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .agent import run_blog_agent


@require_POST
def blog_chat(request, blog_id):
    question = request.POST.get("question", "").strip()

    if not question:
        return JsonResponse({
            "success": False,
            "error": "Question is required."
        }, status=400)

    try:
        answer = run_blog_agent(
            question=question,
            blog_id=blog_id
        )

        return JsonResponse({
            "success": True,
            "answer": answer
        })

    except Exception as e:
        return JsonResponse({
            "success": False,
            "error": str(e)
        }, status=500)
