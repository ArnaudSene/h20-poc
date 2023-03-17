from h2o_wave import main, Q, ui, on  # noqa

from my_app.utils import clear_cards, add_card


@on('#page3')
async def page3(q: Q):
    # When routing, drop all the cards except of the main ones
    # (header, sidebar, meta).
    clear_cards(q)

    for i in range(12):
        add_card(
            q,
            f'item{i}',
            ui.wide_info_card(
                box=ui.box('grid', width='400px'),
                name='',
                title='Tile',
                caption='Lorem ipsum dolor sit amet')
        )
