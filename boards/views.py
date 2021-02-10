from datetime import datetime, timedelta

from django.conf import settings
from django.core.cache import cache
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import last_modified

from boards.cache import collection_last_modified_at
from boards.models import Board, BoardBlock, BoardFeed


@last_modified(collection_last_modified_at)
def index(request):

    board = get_object_or_404(Board, slug='collection')

    cached_page = cache.get(f"board_{board.slug}")
    if cached_page and board.refreshed_at and board.refreshed_at <= \
            datetime.utcnow() - timedelta(seconds=settings.BOARD_CACHE_SECONDS):
        return cached_page

    blocks = BoardBlock.objects.filter(board=board)
    feeds = BoardFeed.objects.filter(board=board)
    result = render(request, "board.html", {
        "board": board,
        "blocks": blocks,
        "feeds": feeds,
    })
    cache.set(f"board_{board.slug}", result, settings.BOARD_CACHE_SECONDS)
    return result

