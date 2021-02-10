from boards.models import Board


def collection_last_modified_at(request):
    board = Board.objects.filter(slug='collection').first()
    return board.refreshed_at if board else None
