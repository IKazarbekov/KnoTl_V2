from abc import ABC, abstractmethod

class PageObject(ABC):
    @abstractmethod
    def get_html(self) -> str:
        pass
    @abstractmethod
    def get_wml(self) -> str:
        pass

class Card(PageObject):
    def __init__(self, title: str, lines: list,  id: str = None, time_reload: int = None):
        """

        :param lines: lists from page objects
        :param title: title in wml, label in html
        :param id: id for went in wml card
        :param time_reload: time auto reload page
        """
        self.lines = lines
        self.title = title
        self.id = id
        self.time_reload = time_reload
    def get_wml(self) -> str:
        card = f'<card title=\"{self.title}\"'
        if not self.id is None:
            card += f' id=\"{self.id}\"'
        card += '>'

        for line in self.lines:
            if isinstance(line, list):
                for obj in line:
                    card += obj.get_wml()
            elif isinstance(line, PageObject):
                card += line.get_wml()
            else:
                raise Exception("Object in argument lines not is list or PageObject.")
            card += '<br/>'

        card += '</card>'
        return card

    def get_html(self) -> str:
        card = f'<h1>{self.title}</h1>'

        for line in self.lines:
            card += "<p>"
            if isinstance(line, list):
                for obj in line:
                    card += obj.get_html()
            elif isinstance(line, PageObject):
                card += line.get_html()
            else:
                raise Exception("Object in argument lines not is list or PageObject.")
            card += "</p>"

        card += '<br/><br/><br/>'
        return card

class Label(PageObject):
    def __init__(self, text: str, size: int = 0, color: str = None):
        """
        demonstrate text
        :param text: text in label
        :param size: 0 - 3 size
        """
        if not 0 <= size <= 3:
            raise ValueError(f"Size in class Label have error value: {size}. It must be in range from 1 to 3.")
        self.text = text
        self.size = size
        self.color = color

    def get_wml(self) -> str:
        if self.color is None:
            return f"<p>{self.text}</p>"
        else:
            return f"<p color=\"{self.color}\">{self.text}</p>"

    def get_html(self) -> str:
        page_obj = str()
        color = self.color
        if not color is None:
            page_obj += f"<font color=\"{color}\">"
        page_obj += f"<span size={self.size * 10 + 10}>{self.text}</span>"
        if not color is None:
            page_obj += "</font>"
        return page_obj

class Url(PageObject):
    def __init__(self,title: str, url: str):
        self.utl = url
        self.title = title

    def get_wml(self) -> str:
        return f"<a href={self.utl}>{self.title}</a>"
    def get_html(self) -> str:
        return f"<a href={self.utl}>{self.title}</a>"

class UrlCard(PageObject):
    def __init__(self,title: str, url: str):
        if url.startswith("#"):
            self.url = url
        else:
            self.url = "#" + url
        self.title = title

    def get_wml(self) -> str:
        return f"<a href={self.url}>{self.title}</a>"
    def get_html(self) -> str:
        return ""

class Content(PageObject):
    """
    PageObject for hidden object if condition
    """
    def __init__(self, page_object: PageObject, is_visible: bool):
        """

        :param page_object: page_object for visible
        :param is_visible: if is False, then page_object will not be visibility
        """
        self.page_object = page_object
        self.is_visible = is_visible

    def get_wml(self) -> str:
        if self.is_visible:
            return self.page_object.get_wml()
        else:
            return ''

    def get_html(self) -> str:
        if self.is_visible:
            return self.page_object.get_wml()
        else:
            return ''

class Image(PageObject):
    def __init__(self, source: str, size: int = None):
        self.source = source
        self.size = size

    def get_wml(self) -> str:
        page_object_img = f"<img src=\"{self.source}\""
        if not self.size is None:
            page_object_img += f"height=\"{self.size}\""
        page_object_img += ">"
        return page_object_img

    def get_html(self) -> str:
        return self.get_wml()

# ----------------------------- FORM SEND ----------------------------------------
class InputPageObject(PageObject):
    """
    should have param: str for send
    """
    def get_wml(self) -> str:
        pass
    def get_html(self) -> str:
        pass
    @abstractmethod
    def get_wml_post_field(self):
        pass

class Form(PageObject):
    def __init__(self, inputs: list[PageObject|list[PageObject]], title: str = '', button_title = 'Отправить', url: str = None):
        """

        :param inputs: list from line or PageObject
            if input is InputPageObject, then use for send to backend server
        :param title:
        :param button_title:
        :param url:
        """
        self.url = url
        self.inputs = inputs
        self.title = title
        self.button_title = button_title
        self.is_post_method = any(isinstance(inp, FileBox) for inp in inputs)

    def get_html(self) -> str:
        form = str()
        form += '<form'
        if not self.url is None:
            form += f' action=\"{self.url}\"'
        if self.is_post_method:
            form += f' method=\"POST\" enctype=\"multipart/form-data\"'
        form += '>'
        for inp in self.inputs:
            form += '<p>'
            if isinstance(inp, list):
                for in_lst_inp in inp:
                    form += in_lst_inp.get_html()
            else:
                form += inp.get_html()
            form += '</p>'
        form += f'<button type="submit">{self.button_title}</button></form>'
        return form
    def get_wml(self) -> str:
        form = str()
        for inp in self.inputs:
            if isinstance(inp, list):
                for in_lst_inp in inp:
                    form += in_lst_inp.get_wml()
            else:
                form += inp.get_wml()
        form += f"<anchor>Отправить<go method=\"get\""
        if not self.url is None:
            form += f" href=\"{self.url}\""
        else:
            form += f" href=\"\""
        form += ">"
        for inp in self.inputs:
            if isinstance(inp, InputPageObject):
                form += f"<postfield name=\"{inp.param}\" value=\"${inp.param}\"/>"
        form += "</go></anchor>"
        return form

class TextBox(InputPageObject):
    """
    TextBox - class denote input text box
        for user input and send form to server
    """
    def __init__(self, param: str, default_value: str = None):
        self.param = param
        self.default_value = default_value
    def get_wml(self) -> str:
        text_box = f"<input type=\"text\" name=\"{self.param}\""
        if not self.default_value is None:
            text_box += f" value=\"{self.default_value}\""
        text_box += "/>"
        return text_box
    def get_html(self) -> str:
        text_box = f"<input type=\"text\" name=\"{self.param}\""
        if not self.default_value is None:
            text_box += f" value=\"{self.default_value}\""
        text_box += f"/>"
        return text_box
    def get_wml_post_field(self):
        return ""

class CheckBox(InputPageObject):
    """
    CheckBox - class denote input check box
        for user input and send form to server
    """
    def __init__(self, param: str):
        self.param = param
    def get_wml(self) -> str:
        return f"<input type=\"text\" name=\"{self.param}\"/><br/>"
    def get_html(self) -> str:
        return f"<input type=\"checkbox\" name=\"{self.param}\">"
    def get_wml_post_field(self):
        return ""

class ConstParam(InputPageObject):
    """
    ConstParam - class denote const param
        and send form to server
    """
    def __init__(self, param: str, value: str):
        self.value = value
        self.param = param
    def get_wml(self) -> str:
        return f"<input type=\"text\" name=\"{self.param}\"/><br/>"
    def get_html(self) -> str:
        return f"<input type=\"hidden\" name=\"{self.param}\" value=\"{self.value}\">"
    def get_wml_post_field(self):
        return ""

class ComboBox(InputPageObject):
    def __init__(self, param: str, selects: dict, default: str = None):
        """

        :param param: param for backend server
        :param selects: dictionary, key - value for server, title - for user
        """
        if len(selects) == 0:
            raise ValueError("Count word in selects is 0")
        for key, value in selects:
            if not isinstance(key, str) or not isinstance(value, str):
                raise TypeError(f"key or value-{key}:{value} is not str")
        self.selects = selects
        self.param = param
        self.default = default

    def get_html(self) -> str:
        page = f"<select name=\"{self.param}\">"
        for value, title in list(self.selects.items()):
            page += f"<option value=\"{value}\""
            if self.default == value:
                page += " selected"
            page += f">{title}</option>"
        page += "</select>"
        return page

    def get_wml(self) -> str:
        page = f"<select name=\"{self.param}\""
        if not self.default is None:
            page += f" value=\"{self.default}\""
        page += ">"
        for value, title in list(self.selects.items()):
            page += f"<option value=\"{value}\">{title}</p>"
        page += "</select>"
        return page

    def get_wml_post_field(self):
        pass

class FileBox(InputPageObject):
    def __init__(self, param):
        self.param = param

    def get_wml(self) -> str:
        return f"<file name=\"{self.param}\">"

    def get_html(self) -> str:
        return f"<input type=\"file\" name=\"{self.param}\">"

    def get_wml_post_field(self):
        pass

def create_page(cards: list, is_wml: bool, default_card: int = None):
    """
    create page from page objects
    :param data: this list of card list of string list of PageObjects
    :param is_wml: is wml page, if False, then html
    :return:
    """
    if not default_card is None:
        move_card = cards.pop(default_card)
        cards.insert(0, move_card)

    page = ''
    if is_wml:
        page += '<?xml version="1.0"?><!DOCTYPE wml PUBLIC "-//WAPFORUM//DTD WML 1.1//EN"><wml>'

    for card in cards:
        if is_wml:
            page += card.get_wml()
        else:
            page += card.get_html()

    if is_wml:
        page += '</wml>'

    return page

if __name__ == "__main__":
    pass