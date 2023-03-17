from h2o_wave import main, Q, ui, on  # noqa

from my_app.utils import clear_cards, add_card


@on('#pg-mc')
async def pg_mc(q: Q):
    # When routing, drop all the cards except of the main ones
    # (header, sidebar, meta).
    clear_cards(q)

    add_card(
        q, 'project',
        ui.tall_info_card(
            box='horizontal-1',
            name='#project',
            title='Project',
            caption='',
            icon='People'
        )
    )

    add_card(
        q, 'Component',
        ui.tall_info_card(
            box='horizontal-2',
            name='#component',
            title='Component',
            caption='',
            icon='ViewInAR'
        )
    )

    add_card(
        q, 'MetaComponent',
        ui.tall_info_card(
            box='horizontal-2',
            name='#meta_component',
            title='MetaComponent',
            caption='',
            icon='ViewAll2'
        )
    )

    add_card(
        q, 'article',
        ui.tall_article_preview_card(
            box=ui.box('vertical-1', height='600px'),
            title='How does magic work',
            image='https://images.pexels.com/photos/624015/pexels-photo-624015.jpeg?auto=compress&cs=tinysrgb&dpr=1&h=750&w=1260',
        content='''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac sodales felis. Duis orci enim, iaculis at augue vel, mattis imperdiet ligula. Sed a placerat lacus, vitae viverra ante. Duis laoreet purus sit amet orci lacinia, non facilisis ipsum venenatis. Duis bibendum malesuada urna. Praesent vehicula tempor volutpat. In sem augue, blandit a tempus sit amet, tristique vehicula nisl. Duis molestie vel nisl a blandit. Nunc mollis ullamcorper elementum.
Donec in erat augue. Nullam mollis ligula nec massa semper, laoreet pellentesque nulla ullamcorper. In ante ex, tristique et mollis id, facilisis non metus. Aliquam neque eros, semper id finibus eu, pellentesque ac magna. Aliquam convallis eros ut erat mollis, sit amet scelerisque ex pretium. Nulla sodales lacus a tellus molestie blandit. Praesent molestie elit viverra, congue purus vel, cursus sem. Donec malesuada libero ut nulla bibendum, in condimentum massa pretium. Aliquam erat volutpat. Interdum et malesuada fames ac ante ipsum primis in faucibus. Integer vel tincidunt purus, congue suscipit neque. Fusce eget lacus nibh. Sed vestibulum neque id erat accumsan, a faucibus leo malesuada. Curabitur varius ligula a velit aliquet tincidunt. Donec vehicula ligula sit amet nunc tempus, non fermentum odio rhoncus.
Vestibulum condimentum consectetur aliquet. Phasellus mollis at nulla vel blandit. Praesent at ligula nulla. Curabitur enim tellus, congue id tempor at, malesuada sed augue. Nulla in justo in libero condimentum euismod. Integer aliquet, velit id convallis maximus, nisl dui porta velit, et pellentesque ligula lorem non nunc. Sed tincidunt purus non elit ultrices egestas quis eu mauris. Sed molestie vulputate enim, a vehicula nibh pulvinar sit amet. Nullam auctor sapien est, et aliquet dui congue ornare. Donec pulvinar scelerisque justo, nec scelerisque velit maximus eget. Ut ac lectus velit. Pellentesque bibendum ex sit amet cursus commodo. Fusce congue metus at elementum ultricies. Suspendisse non rhoncus risus. In hac habitasse platea dictumst.
        '''
        )
    )

#


@on('#project')
async def home(q: Q):
    clear_cards(q)

    add_card(
        q=q,
        name='result_form',
        card=ui.markdown_card(
            box='horizontal-1',
            title='Result form',
            content='Data here'
        )
    )

    add_card(
        q=q,
        name='form',
        card=ui.form_card(
            box='horizontal-2',
            items=[
                ui.textbox(name='project_name', label='Project name', ),
                ui.textbox(name='email_group', label='Email group',
                           placeholder='email_group@desjardins.com'),
                ui.button(name='create_project', label='Create', primary=True),
            ]
        )
    )

    if q.args.create_project:
        # Update existing card content.
        q.page['result_form'].content = \
            f"{q.args.email_group} - {q.args.project_name}"
