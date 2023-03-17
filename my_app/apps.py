from h2o_wave import main, app, Q, ui, handle_on  # noqa

from my_app.project import pg_mc
from my_app.page2 import page2  # noqa
from my_app.page3 import page3  # noqa
from my_app.page4 import page4  # noqa


def zone_content():
    return ui.zone('content', zones=[
        # Specify various zones and use the one that is currently
        # needed. Empty zones are ignored.
        ui.zone('horizontal-1', direction=ui.ZoneDirection.ROW),
        ui.zone('horizontal-2', direction=ui.ZoneDirection.ROW),
        ui.zone('vertical-1'),
        ui.zone(
            'grid',
            direction=ui.ZoneDirection.ROW,
            wrap='stretch',
            justify='center'
        )
    ])


custom_theme_purple_dark = ui.theme(
    name='custom-theme-purple-dark',
    primary='#02111d',
    text='#483D8B',
    card='#E6E6FA',
    page='#483d8b'
)

custom_theme_purple_light = ui.theme(
    name='custom-theme-purple-light',
    primary='#1a1a22',
    text='#02111d',
    card='#E6E8FA',
    page='#C9CBE1'
)

desjardins_theme_green_dark = ui.theme(
    name='desjardins-theme-green-dark',
    primary='#065B37',
    text='#292B2F',
    card='#FFFFFF',
    page='#01874E'
)

desjardins_theme_green_dark_pro = ui.theme(
    name='desjardins-theme-green-dark-pro',
    primary='#292B2F',
    text='#065B37',
    card='#FFFBFF',
    page='#F2F2F2'
)

desjardins_theme_green_light = ui.theme(
    name='desjardins-theme-green-light',
    primary='#018654',
    text='#292B2F',
    card='#FFFFFF',
    page='#F2F2F2'
)
imgages = {
    "desjardins": [
        'https://www.desjardins.com/content/dam/images/logos/commun/logo-desjardins-fr.svg',
        'https://www.desjardins.com/ressources/images/d05-logo-ere-numerique2018.svg?resVer=1520861863000'
    ]
}


async def init(q: Q) -> None:
    q.page['meta'] = ui.meta_card(
        box='',
        themes=[
            custom_theme_purple_dark,
            custom_theme_purple_light,
            desjardins_theme_green_dark,
            desjardins_theme_green_light,
            desjardins_theme_green_dark_pro
        ],
        # theme='winter-is-coming',
        theme='desjardins-theme-green-dark-pro',
        layouts=[
            ui.layout(
                breakpoint='xs',
                min_height='100vh',
                zones=[
                    ui.zone(
                        'main', size='1', direction=ui.ZoneDirection.ROW,
                        zones=[
                            ui.zone('sidebar', size='250px'),
                            ui.zone(
                                'body',
                                zones=[
                                    ui.zone('header'),
                                    zone_content()
                                ]
                            ),
                        ]
                    )
                ]
            )
        ])

    q.page['sidebar'] = ui.nav_card(
        box='sidebar', color='primary', title='My App',
        subtitle="Let's conquer the world!",
        value=f'#{q.args["#"]}' if q.args['#'] else '#pg-mc',
        image=imgages['desjardins'][1],
        items=[
            ui.nav_group('Menu', items=[
                ui.nav_item(name='#pg-mc', label='Home'),
                ui.nav_item(name='#page2', label='Charts'),
                ui.nav_item(name='#page3', label='Grid'),
                ui.nav_item(name='#page4', label='Form'),
            ]),
        ])

    q.page['header'] = ui.header_card(
        box='header', title='', subtitle='',
        secondary_items=[ui.textbox(
            name='search', icon='Search',
            width='400px', placeholder='Search...')],
        items=[
            ui.persona(
                title='John Doe', subtitle='Developer', size='xs',
                image='https://images.pexels.com/photos/220453/'
                      'pexels-photo-220453.jpeg?auto=compress&h=750&w=1260'),
        ]
    )

    # If no active hash present, render page1.
    if q.args['#'] is None:
        await pg_mc(q)


@app('/')
async def serve(q: Q):
    # Run only once per client connection.
    if not q.client.initialized:
        q.client.cards = set()
        await init(q)
        q.client.initialized = True

    # Handle routing.
    await handle_on(q)
    await q.page.save()
