from boards.models import Board


def board_last_modified_at(request, board_slug):
    board = Board.objects.filter(slug=board_slug).first()
    return board.refreshed_at if board else None


def collection_last_modified_at(request):
    board = Board.objects.filter(slug='collection').first()
    return board.refreshed_at if board else None
