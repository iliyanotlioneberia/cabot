from  django.core.paginator import Paginator, Page


class Page2(Page):

    def has_next_2(self):
        return self.number + 1 < self.paginator.num_pages

    def has_next_3(self):
        return self.number + 2 < self.paginator.num_pages

    def has_previous_2(self):
        return self.number > 2

    def has_previous_3(self):
        return self.number > 3

    def has_after_other_pages(self):
        return self.has_before_previous() or self.has_after_next()

    def next_page_number_2(self):
        return self.paginator.validate_number(self.number + 2)

    def next_page_number_3(self):
        return self.paginator.validate_number(self.number + 3)

    def previous_page_number_2(self):
        return self.paginator.validate_number(self.number - 2)

    def previous_page_number_3(self):
        return self.paginator.validate_number(self.number - 3)


class Paginator2(Paginator):
    def _get_page(self, *args, **kwargs):
        """
        Returns an instance of a single page.

        This hook can be used by subclasses to use an alternative to the
        standard :cls:`Page` object.
        """
        return Page2(*args, **kwargs)

