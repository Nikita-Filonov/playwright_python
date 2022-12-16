from page_factory.component import Component


class ListItem(Component):
    @property
    def type_of(self) -> str:
        return 'list item'
