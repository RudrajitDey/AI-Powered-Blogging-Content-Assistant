from blogs.models import Blog


def get_current_blog(blog_id: int) -> dict:
    try:
        blog = Blog.objects.get(id=blog_id)

        return {
            "success": True,
            "blog_id": blog.id,
            "title": blog.title,
            "category": blog.category.category_name,
            "author": blog.author.username,
            "description": blog.short_description,
            "content": blog.blog_body,
        }

    except Blog.DoesNotExist:
        return {
            "success": False,
            "error": "Blog not found."
        }


def search_blogs(query: str) -> dict:
    blogs = Blog.objects.filter(
        title__icontains=query
    )[:5]

    results = []

    for blog in blogs:
        results.append({
            "id": blog.id,
            "title": blog.title,
            "slug": blog.slug,
            "category": blog.category.category_name,
            "description": blog.short_description,
        })

    return {
        "success": True,
        "results": results,
    }