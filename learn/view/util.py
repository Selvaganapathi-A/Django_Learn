def pager(current_page: int, num_of_pages: int, pages_to_display: int = 5):
    if num_of_pages <= pages_to_display:
        return current_page, tuple(x + 1 for x in range(num_of_pages))

    start, end = 0, num_of_pages
    start_holder, end_holder = 0, 0

    if pages_to_display % 2 == 0:
        end_holder = start_holder = pages_to_display // 2
    else:
        start_holder = (pages_to_display - 1) // 2
        end_holder = start_holder + 1

    start = current_page - start_holder
    end = current_page + end_holder

    if start < 1:
        end = end - start + 1
        start = 1

    if num_of_pages < end:
        start += num_of_pages - end + 1
        end = num_of_pages + 1

    return current_page, tuple(range(start, end))
