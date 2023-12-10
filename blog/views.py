from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import BlogPost, BlogCategory, BlogTag


class BlogList(LoginRequiredMixin, ListView):
    model = BlogPost
    paginate_by = 9
    template_name = "blog/blog_list.html"

    def get_queryset(self):
        return super(BlogList, self).get_queryset().filter()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BlogList, self).get_context_data(**kwargs)
        context["blog_categories"] = BlogCategory.objects.all()
        context["blog_tags"] = BlogTag.objects.all()
        context["popular_posts"] = BlogPost.objects.all()[:3]
        return context


class BlogListCategory(ListView):
    model = BlogPost
    paginate_by = 9
    template_name = "blog/blog_list_category.html"

    def get_queryset(self):
        return (
            super(BlogListCategory, self)
            .get_queryset()
            .filter(category__slug=self.kwargs["category"])
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BlogListCategory, self).get_context_data(**kwargs)
        context["selected_category"] = BlogCategory.objects.get(
            slug=self.kwargs["category"]
        )
        context["blog_categories"] = BlogCategory.objects.all()
        context["blog_tags"] = BlogTag.objects.all()
        context["popular_posts"] = BlogPost.objects.all()[:3]
        return context


class BlogListTag(ListView):
    model = BlogPost
    paginate_by = 9
    template_name = "blog/blog_list_tag.html"

    def get_queryset(self):
        return (
            super(BlogListTag, self)
            .get_queryset()
            .filter(tags__slug=self.kwargs["tag"])
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BlogListTag, self).get_context_data(**kwargs)
        context["selected_tag"] = BlogTag.objects.get(slug=self.kwargs["tag"])
        context["blog_categories"] = BlogCategory.objects.all()
        context["blog_tags"] = BlogTag.objects.all()
        context["popular_posts"] = BlogPost.objects.all()[:3]
        return context


class BlogSingle(DetailView):
    model = BlogPost
    template_name = "blog/blog_single.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BlogSingle, self).get_context_data(**kwargs)
        context["blog_categories"] = BlogCategory.objects.all()
        context["blog_tags"] = BlogTag.objects.all()
        context["popular_posts"] = BlogPost.objects.all()[:3]
        # context["related_posts"] = BlogPost.objects.filter(
        #     category=context["object"].category.first()
        # ).exclude(id=context["object"].id)[:3]
        return context


#
# class AboutUs(View):
#     def get(self, request):
#         context = {}
#         context["blog_categories"] = BlogCategory.objects.all()
#         context["blog_tags"] = BlogTag.objects.all()
#         context["popular_posts"] = BlogPost.objects.all()[:3]
#         return render(request, "blog/about_us.html", context)
#
#
# class Contact(View):
#     def get(self, request):
#         context = {}
#         context["blog_categories"] = BlogCategory.objects.all()
#         context["blog_tags"] = BlogTag.objects.all()
#         context["popular_posts"] = BlogPost.objects.all()[:3]
#         return render(request, "blog/contact_us.html", context)
