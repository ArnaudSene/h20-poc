from h2o_wave import main, Q, ui, on  # noqa

from my_app.utils import clear_cards, add_card


@on('#page4')
async def page4(q: Q):
    # When routing, drop all the cards except of the main ones
    # (header, sidebar, meta).
    # Since this page is interactive, we want to update its card
    # instead of recreating it every time, so ignore 'form' card on drop.
    clear_cards(q, ['form'])

    if q.args.step1:
        # Just update the existing card, do not recreate.
        q.page['form'].items = [
            ui.stepper(name='stepper', items=[
                ui.step(label='Step 1'),
                ui.step(label='Step 2'),
                ui.step(label='Step 3'),
            ]),
            ui.textbox(name='textbox2', label='Textbox 1'),
            ui.buttons(justify='end', items=[
                ui.button(name='step2', label='Next', primary=True),
            ])
        ]
    elif q.args.step2:
        # Just update the existing card, do not recreate.
        q.page['form'].items = [
            ui.stepper(name='stepper', items=[
                ui.step(label='Step 1', done=True),
                ui.step(label='Step 2'),
                ui.step(label='Step 3'),
            ]),
            ui.textbox(name='textbox2', label='Textbox 2'),
            ui.buttons(justify='end', items=[
                ui.button(name='step1', label='Cancel'),
                ui.button(name='step3', label='Next', primary=True),
            ])
        ]
    elif q.args.step3:
        # Just update the existing card, do not recreate.
        q.page['form'].items = [
            ui.stepper(name='stepper', items=[
                ui.step(label='Step 1', done=True),
                ui.step(label='Step 2', done=True),
                ui.step(label='Step 3'),
            ]),
            ui.textbox(name='textbox3', label='Textbox 3'),
            ui.buttons(justify='end', items=[
                ui.button(name='step2', label='Cancel'),
                ui.button(name='submit', label='Next', primary=True),
            ])
        ]
    else:
        # If first time on this page, create the card.
        add_card(q, 'form', ui.form_card(box='vertical-1', items=[
            ui.stepper(name='stepper', items=[
                ui.step(label='Step 1'),
                ui.step(label='Step 2'),
                ui.step(label='Step 3'),
            ]),
            ui.textbox(name='textbox1', label='Textbox 1'),
            ui.buttons(justify='end', items=[
                ui.button(name='step2', label='Next', primary=True),
            ]),
        ]))
