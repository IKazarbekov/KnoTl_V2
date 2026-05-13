from app.front import page_builder as pb

def list_chats(chats: list):
    '''
    param chats: lift from tuple from chat_name and chat_id
    '''

    chats_part = [pb.Label(chat_name) for chat_name, chat_id in chats]

    page = pb.create_page(
        [
            pb.Card('Мессенджер',
                [
                    chats_part,
                    pb.UrlCard('Написать по логину','n')
                ], id='m'),
            pb.Card('Написать',
                [
                    pb.UrlCard('Чаты','m'),
                    pb.Form(
                        [
                            pb.Label('Логин'),
                            pb.TextBox('lg')
                        ], is_post_method=True, url='new')
                ], id='n')
        ], False)

    return page
